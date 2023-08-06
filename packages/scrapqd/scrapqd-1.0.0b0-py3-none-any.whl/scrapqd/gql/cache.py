from datetime import datetime, timedelta

from scrapqd.gql import logger
from scrapqd.settings import config

REQUEST = {}


def get_url(url):
    """Gets executor process instance for the given url. Cache is only valid for 10 minutes.
    This can be changed using LOCAL_CACHE_TTL.

    :param url: lookup url
    :return: Process instance
    """
    current_time = datetime.now()
    delta = timedelta(minutes=config.LOCAL_CACHE_TTL)
    data = REQUEST.get(url, None)
    if data:
        timestamp = data["timestamp"]
        process = data["process"]
        if timestamp + delta > current_time:
            logger.info("Fetching %s crawl from cache.", url)
            return process
    return None


def cache(url, process):
    """Caches url's executor process.

    :param url: lookup url
    :param process: executor process
    """
    timestamp = datetime.now()
    data = {
        "timestamp": timestamp,
        "process": process
    }
    REQUEST[url] = data
