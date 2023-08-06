from graphql import GraphQLArgument as Argument
from graphql import GraphQLBoolean as Boolean
from graphql import GraphQLField as Field
from graphql import GraphQLInputField as InputField
from graphql import GraphQLInputObjectType as InputObject
from graphql import GraphQLInt as Int
from graphql import GraphQLNonNull as NonNull
from graphql import GraphQLResolveInfo as ResolveInfo
from graphql import GraphQLString as String

from scrapqd.gql.document import Document
from scrapqd.gql.enum.browser import BrowserEnum
from scrapqd.gql.helper import with_error_traceback
from scrapqd.settings import config

from .common import (cache_desc, json_response_desc, resolver,
                     selenium_browser_desc, url_desc)


@with_error_traceback
def resolve_selenium(root, info: ResolveInfo,
                     url, options=None, is_json_response=False, browser=config.DEFAULT_BROWSER, cache=False):
    """Crawls url using selenium executor and extracts data using defined query.

    :param root: will be None for the query start.
    :param info: GraphQLResolveInfo instance which gives resolver information.
    :param url: URL to crawl.
    :param browser: Selenium supports multiple browsers. It can be extended to multiple browser by extending SeleniumDriver.
                    System supports below browser.
                    1. GOOGLE_CHROME
                    3. FIREFOX
    :param options: Selenium options for crawling. Accepted options are below.
                    1. xpath : selenium will wait for webpage to load this element.
                    2. wait_time: selenium will wait for xpath target (wait_time) secs.
    :param is_json_response: Set `true`, if response format from url is json.
                             Currently system does not support json format.
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
                                                      description="selenium will wait for webpage to load this element"),
                                  "wait_time": InputField(Int, default_value=30,
                                                          description="wait time in seconds for xpath to be "
                                                                      "loaded in the browser"),
                              })

selenium_options_desc = """selenium options for waiting for the webpage. Below are accepted parameters
       \n\n1. xpath : selenium will wait for webpage to load this element.
       \n\n2. wait_time: selenium will wait for xpath target (wait_time) secs."""

selenium_query = Field(Document,
                       args={
                           "url": Argument(NonNull(String), description=url_desc),
                           "browser": Argument(BrowserEnum, description=selenium_browser_desc),
                           "is_json_response": Argument(Boolean, description=json_response_desc),
                           "cache": Argument(Boolean, description=cache_desc),
                           "options": Argument(SeleniumOptions, description=selenium_options_desc)
                       },
                       resolve=resolve_selenium,
                       description="Fetch query crawls url using configured executor and "
                                   "parsing response using lxml gql_parser")
