from scrapqd.factory_interface import ConfigItem
from scrapqd.gql.exception import QueryFieldNotSupportedError
from scrapqd.gql.queries.fetch import fetch_query
from scrapqd.gql.queries.selenium import selenium_query
from scrapqd.settings import config


class QueryFieldFactory(ConfigItem):
    """Combines system query fields mapping and user config"""

    def __init__(self):
        super().__init__(config=config.QUERY_FIELDS,
                         exception=QueryFieldNotSupportedError,
                         default_config={
                             "fetch": fetch_query,
                             "selenium": selenium_query,
                         },
                         upper_keys=False,
                         default_item=None)
