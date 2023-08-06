from graphql import GraphQLArgument as Argument
from graphql import GraphQLBoolean as Boolean
from graphql import GraphQLField as Field
from graphql import GraphQLNonNull as NonNull
from graphql import GraphQLResolveInfo as ResolveInfo
from graphql import GraphQLString as String

from scrapqd.gql import constants as const
from scrapqd.gql.helper import get_key, with_error_traceback
from scrapqd.gql.parser import Parser
from scrapqd.gql.scalar.generic import GenericScalar


@with_error_traceback
def resolve_link(parser: Parser, info: ResolveInfo,
                 xpath, base_url=None, multi=const.MULTI_DEFAULT_VALUE):
    """Extracts node's href, forms absolute url from the response and returns to client.
    If the base url is given, it will use that to form the absolute url.

    :param parser: Parser instance passed down from parent query.
    :param info: GraphQLResolveInfo instance which gives resolver information.
    :param xpath: expects xpath to <a> link node.
    :param base_url: will be used to form the absolute url.
    :param multi: by default, it is set to False. Thus, when the given xpath locates multiple nodes,
               it returns first node value. if it is set `true`, it will return all the node values" \
               as list.
    :return:    text -  when multi is set to False, This option can be overridden to return list with single value.
                        using `NON_MULTI_RESULT_LIST`
                List - when multi is set to True
    """
    if base_url is None:
        base_url = parser.headers.get("response_url")
    key = get_key(info)
    result = parser.solve_link(key, base_url=base_url, multi=multi, xpath=xpath)
    result = parser.get_multi_results(multi, result)
    parser.caching(key, result)
    return result


link = Field(GenericScalar,
             args={
                 "xpath": Argument(NonNull(String), description=const.xpath_desc),
                 "multi": Argument(Boolean, description=const.multi_desc),
                 "base_url": Argument(String,
                                      description="base url value will be used when only relative url is given. "
                                                  "\n\nEx: '/search?q=google' if the base_url=google.com given, "
                                                  "absolute url will be created as such -> google.com/search?q=google"),
             },
             resolve=resolve_link,
             description="Extracts href from <a> tag. If the base_url argument is give, "
                         "it will form the absolute url.")
