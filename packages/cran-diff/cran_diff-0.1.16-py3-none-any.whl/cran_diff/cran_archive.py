import requests
import scipy.stats as ss

from bs4 import BeautifulSoup, SoupStrainer
from datetime import datetime, timedelta
from dateutil import parser

from typing import List, Tuple

from .urls import CRAN_PKG_ARCHIVE_PATTERN


def get_archive_name_versions(package, timespan) -> Tuple[List, Tuple[str, int]]:
    """Scrapes package archive page to get previous version numbers
    within a user defined number of years

    :params:
    package: string for the package name
    timespan:float for number of years to get previous versions within
    :return: A tuple (x, y), where `x` is a list of all archived versions within
    past `timespan` years and `y` is a tuple of the package-name and the total number
    of archived versions
    """
    html_page = requests.get(CRAN_PKG_ARCHIVE_PATTERN.format(package=package))
    soup = BeautifulSoup(html_page.text, "html.parser")
    dates = [
        x.string.strip()
        for x in soup.select("body > table > tr > td:nth-child(3)")
        if len(x.string.strip()) > 0
    ]
    dates = [parser.parse(date) for date in dates]
    date_rank = ss.rankdata(dates)
    num_archived = (package, len(dates))  # number of archived versions
    version_list = []
    release_numbers = []
    i = 0
    for link in BeautifulSoup(
        html_page.text, parse_only=SoupStrainer("a"), features="html.parser"
    ):
        if link.has_attr("href"):
            if link["href"].startswith(package) and link["href"].endswith(".tar.gz"):
                date = dates[i]
                release_number = int(date_rank[i])
                i += 1
                # Check if package older than 2 years
                weeks = timespan * 52
                years_ago = datetime.now() - timedelta(weeks=weeks)
                if years_ago > date or date > datetime.now():
                    continue
                version = link["href"].split("_")[1]
                version = version.rstrip(".tar.gz")
                version_list.append(version)
                release_numbers.append(release_number)
    return (
        [
            (package, version_list[i], release_numbers[i])
            for i in range(len(version_list))
        ],
        num_archived,
    )
