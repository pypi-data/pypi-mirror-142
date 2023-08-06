from graphql import GraphQLArgument as Argument
from graphql import GraphQLBoolean as Boolean
from graphql import GraphQLField as Field
from graphql import GraphQLInputField as InputField
from graphql import GraphQLInputObjectType as InputObject
from graphql import GraphQLInt as Int
from graphql import GraphQLNonNull as NonNull
from graphql import GraphQLResolveInfo as ResolveInfo
from graphql import GraphQLString as String

from scrapqd.gql import constants as const
from scrapqd.gql.document import Document
from scrapqd.gql.enum.browser import BrowserEnum
from scrapqd.gql.helper import with_error_traceback
from scrapqd.settings import config

from .common import resolver


@with_error_traceback
def resolve_selenium(root, info: ResolveInfo,
                     url, options=None, is_json_response=False, browser=config.DEFAULT_BROWSER, cache=False):
    """Crawls url using selenium executor and extracts data using defined query.

    :param root: will be None for the query start.
    :param info: GraphQLResolveInfo instance which gives resolver information.
    :param url: URL to crawl.
    :param browser: Selenium supports multiple browsers. It can be extended to multiple browser by extending SeleniumDriver.
                    System supports below browser.
                    - GOOGLE_CHROME
                    - FIREFOX
    :param options: Selenium options for crawling. Accepted options are below.
                    - xpath : selenium will wait for webpage to load this element.
                    - wait_time: selenium will wait for xpath target (wait_time) secs.
    :param is_json_response: Set `true`, if response format from url is json.
                             System does not support json format as of now. This will be a future enhancement.
    :param cache: This option should used only for testing purpose. When cache is set to `true`,
                  url response is cached and used in consecutive query execution.
                  This will help to speed up the scraping query development process.
    :return: Dict
    """
    if options is None:
        options = {}

    parser = resolver(url, is_json_response=is_json_response, cache=cache,
                      executor="selenium", browser=browser, options=options)
    return parser


SeleniumOptions = InputObject("SeleniumOptions",
                              fields=lambda: {
                                  "xpath": InputField(String,
                                                      default_value=None,
                                                      description="Selenium will wait for webpage to load this element"),
                                  "wait_time": InputField(Int, default_value=30,
                                                          description="Wait time in seconds for xpath to be "
                                                                      "loaded in the browser"),
                              })

selenium_query = Field(Document,
                       args={
                           "url": Argument(NonNull(String), description=const.crawl_url_desc),
                           "browser": Argument(BrowserEnum, description=const.crawl_selenium_browser_desc),
                           "is_json_response": Argument(Boolean, description=const.crawl_json_response_desc),
                           "cache": Argument(Boolean, description=const.crawl_cache_desc),
                           "options": Argument(SeleniumOptions, description=const.crawl_selenium_options_desc)
                       },
                       resolve=resolve_selenium,
                       description="Fetch query crawls url using configured executor and "
                                   "parsing response using lxml gql_parser")
