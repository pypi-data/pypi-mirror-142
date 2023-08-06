# flake8: noqa

import concurrent.futures
import csv
import json
import os
import pathlib
import shutil
from typing import List, Tuple

import requests
from requests_file import FileAdapter
from tqdm import tqdm

from .cran_archive import get_archive_name_versions
from .cran_parsing_functions import parse_metadata
from .filenames import PACKAGES_VERSIONS_FILENAME
from .pkg_parsing_functions import download_package_tar, process_package_tar
from .rcom import RCom
from .tuples import Package
from .urls import CRAN_PKG_LIST_URL


class CranParser:
    def __init__(
        self,
        JSON_path: pathlib.Path,
        package_list_url=CRAN_PKG_LIST_URL,
        download_path="./downloads",
        stored_packages=[],
        max_pool=32,
        keep_tar_files=False,
        timespan=2.0,
    ):
        """
        :params:
        JSON_path: string for path to data store
        package_list_url: string for url of r package list
        download_path: string for path to save dowloaded packages to
        stored_packages: list of packages already in store
        max_pool: int for maximum number of threads to use
        keep_tar_files: boolean for whether to save the tar files
        timespan: float for number of years to get package versions within
        """

        # ensure download path exists
        self.set_download_path(download_path)
        self.keep_tar_files = keep_tar_files

        # set output paths
        self.JSON_path = JSON_path
        self.set_names_versions_path(PACKAGES_VERSIONS_FILENAME)

        # get list of current packages
        self.set_cran_metadata(package_list_url)

        # create a worker pool for background tasks
        self.set_max_pool(max_pool)

        # user-specified list of stored packages
        self.stored_packages = stored_packages

        self.current_packages = []
        self.change_current = []
        self.change_archive = []

        self.timespan = timespan

    def get_r_communicator(self) -> RCom:
        """
        Gets an `RCom` object, to allow communication with R
        """
        try:
            return self.communicator
        except AttributeError:
            self.set_r_communicator()
            return self.communicator

    def set_r_communicator(self):
        """
        Adds an object that allows communication with R
        """
        print("Creating R communication object")
        self.communicator = RCom()

    def set_max_pool(self, max_pool: int):
        print("Setting max workers in pool to ", max_pool)
        self.MAX_POOL = max_pool

    def search_archive(self):
        """Searches the CRAN archive for versions of
        current packages which came out < `timespan` years ago
        """
        packages = map(lambda x: x[0], self.meta_data)
        
        futures = []
        res = []
        num_archived = []  # number of archived versions
        with concurrent.futures.ThreadPoolExecutor(self.MAX_POOL) as executor:
            for package in packages:
                future = executor.submit(
                    get_archive_name_versions, package, self.timespan
                )
                futures.append(future)
            # once they have all finished
            for f in tqdm(concurrent.futures.as_completed(futures), total=len(futures)):
                temp = f.result()
                res += temp[0]
                num_archived.append(temp[1])
        self.archive = res

    def fill_datastore(self):
        """Populates empty JSON data with all CRAN packages, including
        archived versions from the last two years
        """
        print("Search archive")
        self.search_archive()
        self.set_current_packages()
        self.detect_meta_not_stored()
        self.detect_archive_not_stored()
        package_list = self.combine_change()
        initial_length = len(package_list)
        # populate packages incrementally, 100 at a time
        while len(package_list) > 0:
            print(f"Only {len(package_list)}/{initial_length} remaining")
            if len(package_list) > 100:
                self.download_and_parse_packages(package_list[:100])
                package_list = package_list[100:]
            else:
                self.download_and_parse_packages(package_list)
                package_list = []

            self.soft_insert(self.to_insert)
            self.update_current_packages(self.to_insert)

    def update_datastore(self):
        """Updates JSON data, adding new packages and versions that
        are not currently stored
        """
        print("Get current packages")
        self.set_current_packages()
        print("Detect changes")
        self.detect_meta_not_stored()
        package_list = self.combine_change()
        self.download_and_parse_packages(package_list)
        self.soft_insert(self.to_insert)
        self.update_current_packages(self.to_insert)

    def combine_change(self) -> List[Tuple[str, str, str]]:
        """Creates a combined list of current and archived CRAN packages
        that are not currently stored

        :returns: list of packages, including name and version number
        """
        return list(
            map(lambda x: (x.name, x.version, "current"), self.change_current)
        ) + list(map(lambda x: (x.name, x.version, "archived"), self.change_archive))

    def download_and_parse_packages(self, package_list: List[Tuple[str, str, str]]):
        """Downloads and parses CRAN packages

        :params: package_list: list of packages to be parsed

        :creates: self.to_insert: list of dictionaries with imports,
        suggests, exports, functions, and news for each package
        """

        def inner(package, version, package_type):
            try:
                if package_type == "current":
                    tar_file = download_package_tar(
                        package, version, False, pathlib.Path(self.download_path)
                    )
                elif package_type == "archived":
                    tar_file = download_package_tar(
                        package, version, True, pathlib.Path(self.download_path)
                    )
                if tar_file:
                    return (
                        package,
                        version,
                        package_type,
                        process_package_tar(
                            tar_file, keep_tar_file=self.keep_tar_files
                        ),
                    )
            except Exception as e:
                print(e)

        futures = []
        self.to_insert = []
        with concurrent.futures.ThreadPoolExecutor(self.MAX_POOL) as executor:
            print("Start download and processing")
            # submit those in current list
            for package, version, package_type in package_list:
                future = executor.submit(
                    inner,
                    package=package,
                    version=version,
                    package_type=package_type,
                )
                futures.append(future)
            # as they complete, read news and enter into database
            for future in tqdm(
                concurrent.futures.as_completed(futures), total=len(futures)
            ):
                res = future.result()
                if res:
                    package, version, package_type, data = res
                    lib_loc = os.path.dirname(data["package_location"])
                    export_list = self.read_exports(package, version, lib_loc)
                    news_list = self.read_news(package, version, lib_loc)
                    data.update(
                        {
                            "exports": export_list,
                            "news": news_list,
                            "package": package,
                            "version": version,
                            "package_type": package_type,
                        }
                    )
                    self.to_insert += [data]
                    shutil.rmtree(lib_loc)  # remove package folder

    def soft_insert(self, data_vals: List[dict]):
        """Store package data in JSON files

        :params: data_vals: list of dictionaries with parsed package
        data, including imports, suggests, exports, functions, and news
        """
        names = []
        versions = []
        for data in data_vals:
            package = data["name"]
            version = data["version"]
            names.append(package)
            versions.append(version)
            version_path = os.path.join(self.JSON_path, package, version)
            # Ensure output path exists
            if not os.path.exists(version_path):
                os.makedirs(version_path)
            # Store imports, suggests, exports and news
            with open(os.path.join(version_path, "imports.json"), "w+") as f:
                f.write(json.dumps(data["imports"]))
            with open(os.path.join(version_path, "suggests.json"), "w+") as f:
                f.write(json.dumps(data["suggests"]))
            with open(os.path.join(version_path, "exports.json"), "w+") as f:
                f.write(json.dumps(data["exports"]))
            with open(os.path.join(version_path, "functions.json"), "w+") as f:
                f.write(json.dumps(data["functions"]))
            with open(os.path.join(version_path, "news.json"), "w+") as f:
                f.write(json.dumps(data["news"]))

        # Update packages-versions list
        self.insert_packages_versions(names, versions)

        # Update version list for each package
        unique = list(set(names))  # remove duplicate names
        for pkg in unique:
            pkg_versions = [v for (i, v) in enumerate(versions) if names[i] == pkg]
            versions_json = os.path.join(self.JSON_path, pkg, "versions.json")
            if os.path.exists(versions_json):
                with open(versions_json, "r") as f:
                    current = json.load(f)
            else:
                current = [
                    i["version"] for i in self.stored_packages if i["package"] == pkg
                ]
            pkg_versions.extend(current)
            with open(versions_json, "w+") as f:
                f.write(json.dumps(sorted(pkg_versions, reverse=True)))

        # Update package list
        packages_json = os.path.join(self.JSON_path, "packages.json")
        if os.path.exists(packages_json):
            with open(packages_json, "r") as f:
                current = json.load(f)
        else:
            current = [i["package"] for i in self.stored_packages]
        names.extend(current)
        names = list(set(names))  # remove duplicate names
        with open(packages_json, "w+") as f:
            f.write(json.dumps(sorted(names)))

    def insert_packages_versions(self, names: List[str], versions: List[str]):
        """Update packages-versions JSON file

        :params:
        names: list of package names (updated and new)
        versions: list of corresponding version numbers
        """
        names_versions = list(zip(names, versions))
        if os.path.exists(self.names_versions_json):
            with open(self.names_versions_json, "r") as f:
                current = json.load(f)
        else:
            current = self.stored_packages
        current = [tuple(i.values()) for i in current]
        names_versions.extend(current)
        names_versions.sort()  # sort tuples before converting to dicts
        names_versions = [{"package": i[0], "version": i[1]} for i in names_versions]
        with open(self.names_versions_json, "w+") as f:
            f.write(json.dumps(names_versions))

    def read_news(self, package: str, version: str, lib_loc: str) -> List[dict]:
        """Parses news file

        :params:
        package: package name
        version: version number
        lib_loc: location of package folder

        :returns: a list of dictionaries with news category and text
        """
        communicator = self.get_r_communicator()

        news_file = communicator.write_news(package, version, lib_loc)
        news_list = []
        if os.path.exists(news_file):
            with open(news_file, newline="") as File:
                reader = csv.reader(File)
                for row in reader:
                    if row[0] == version:
                        if row[2] == "NA":
                            category = ""
                        else:
                            category = row[2]
                        text = row[3]
                        news_dict = {"category": category, "text": text}
                        news_list.append(news_dict)
            os.remove(news_file)
        return news_list

    def read_exports(self, package: str, version: str, lib_loc: str) -> List[dict]:
        """Parses NAMESPACE file

        :params:
        package: package name
        version: version number
        lib_loc: location of package folder

        :returns: a list of dictionaries with export name and type
        """
        communicator = self.get_r_communicator()

        exports_file = communicator.write_exports(package, version, lib_loc)
        export_list = []
        if os.path.exists(exports_file):
            with open(exports_file, newline="") as File:
                reader = csv.reader(File)
                next(reader, None)  # Skip the headers
                for row in reader:
                    export_dict = {"name": row[0], "type": row[1]}
                    export_list.append(export_dict)
            os.remove(exports_file)
        return export_list

    def detect_meta_not_stored(self):
        """Identifies CRAN meta-data that is not currently stored"""
        meta = [Package(i[0], i[1]) for i in self.meta_data]
        self.change_current = list(
            filter(lambda x: not x in self.current_packages, meta)
        )

    def detect_archive_not_stored(self):
        """Identifies CRAN archive versions that are not currently stored"""
        try:
            archive = [Package(i[0], i[1]) for i in self.archive]
            self.change_archive = list(
                filter(lambda x: not x in self.current_packages, archive)
            )
        except NameError as e:
            raise Exception(
                "You must search the archive before determining what is missing"
            )

    def set_current_packages(self):
        """Populates the list of stored packages"""
        if self.stored_packages:  # checks for user-specified list
            self.current_packages = [
                Package(i["package"], i["version"]) for i in self.stored_packages
            ]
        else:
            self.search_stored_packages()

    def search_stored_packages(self):
        """Searches the local JSON data for stored packages"""
        try:
            with open(self.names_versions_json, "r") as f:
                names_versions = json.load(f)
            self.current_packages = [
                Package(i["package"], i["version"]) for i in names_versions
            ]
        except FileNotFoundError:
            self.current_packages = []

    def update_current_packages(self, inserted: List[dict]):
        """Updates the list of stored packages after filling the JSON data

        :params: inserted: list of dictionaries with inserted package data,
        including name and version
        """
        self.current_packages.extend(
            [Package(i["name"], i["version"]) for i in inserted]
        )

    def get_current_packages(self) -> List[Package]:
        """Gets a list of all stored packages

        :returns: a list of Package namedtuples
        """
        return self.current_packages

    def set_download_path(self, download_path: str):
        # set somewhere for download
        print("Preparing for downloads in ", download_path)
        self.ensure_download_path(download_path)
        self.download_path = download_path

    def set_names_versions_path(self, filename: str):
        """Define the filepath for the packages-versions JSON file

        :params: filename: name of packages-versions JSON file
        """
        self.names_versions_json = os.path.join(self.JSON_path, filename)

    def set_cran_metadata(self, url: str):
        """Obtain CRAN metadata

        :params:
        url: A URL (or local file-path "file://...") defining which packages are to be
        included here
        """
        print("Obtaining CRAN metadata from ", url)
        requests_session = requests.Session()
        requests_session.mount("file://", FileAdapter())

        response = requests_session.get(url)
        output = response.text
        self.meta_data = parse_metadata(output)

    def ensure_download_path(self, download_path: str):
        """Ensure that the provided download path exists

        :params:
        download_path: A place to store downloaded tars
        """
        os.makedirs(download_path, exist_ok=True)
