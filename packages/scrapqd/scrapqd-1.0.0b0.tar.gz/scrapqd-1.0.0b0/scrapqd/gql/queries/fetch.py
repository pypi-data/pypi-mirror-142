from graphql import GraphQLArgument as Argument
from graphql import GraphQLBoolean as Boolean
from graphql import GraphQLField as Field
from graphql import GraphQLNonNull as NonNull
from graphql import GraphQLResolveInfo as ResolveInfo
from graphql import GraphQLString as String

from scrapqd.gql.document import Document
from scrapqd.gql.enum.executor import ExecutorEnum
from scrapqd.gql.helper import with_error_traceback
from scrapqd.gql.scalar.dictionary import Dictionary

from .common import (cache_desc, executor_desc, headers_desc,
                     json_response_desc, method_desc, payload_desc, resolver,
                     url_desc)


@with_error_traceback
def resolve_fetch(root, info: ResolveInfo,
                  url, is_json_response=False, cache=False, method="get", executor="requests", headers=None):
    """Crawls url using executor and extracts data using defined query.

    :param root: will be None for the query start.
    :param info: GraphQLResolveInfo instance which gives resolver information.
    :param url: data to extract
    :param method: requests supports multiple methods. By default, most requests are GET.
                   Additional POST method can be used.
    :param executor: By default, system uses "requests" library to process regular websites.
                     There are other libraries like asyncio can use used to extract.
                     Currently system only support "requests" library.
                     Additional executors can be implemented by extending Crawler interface. Refer to guides.
    :param headers: headers in the form of json object or python dictionary. Some websites need additional headers.
                    These headers are used in crawl process.
    :param is_json_response: Set `true`, if response format from url is json.
                             Currently system does not support json format.
    :param cache: This option should used only for testing purpose. When cache is set to `true`,
                  url response is cached and used in consecutive query execution.
                  This will help to speed up the scraping query development process.
    :return: Dict
    """

    if headers is None:
        headers = {}

    parser = resolver(url, is_json_response=is_json_response, cache=cache,
                      headers=headers, executor=executor, method=method)
    return parser


fetch_query = Field(Document,
                    args={
                        "url": Argument(NonNull(String), description=url_desc),
                        "headers": Argument(Dictionary, description=headers_desc),
                        "executor": Argument(ExecutorEnum, description=executor_desc),
                        "method": Argument(String, description=method_desc),
                        "payload": Argument(Dictionary, description=payload_desc),
                        "is_json_response": Argument(Boolean, description=json_response_desc),
                        "cache": Argument(Boolean, description=cache_desc)
                    },
                    resolve=resolve_fetch,
                    description="Crawls the given url using configured executor and "
                                "parsing response using lxml gql_parser.")
