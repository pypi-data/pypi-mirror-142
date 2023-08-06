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
    """Extracts anchor node's href attribute, forms absolute url from the response and returns to client.
    If the base url is given, it will use that to form the absolute url. Xpath expected to be anchor tag.

    :param parser: Parser instance passed down from parent query.
    :param info: GraphQLResolveInfo instance which gives resolver information.
    :param xpath: Expected to be an anchor <a> node.
    :param base_url: Custom base url to form absolute url.
    :param multi: It is set to False as default.
                    - True  - Process multiple elements when xpath locates multiple nodes.
                    - False - Process first element when xpath locates multiple nodes.
    :return:    Text -  When multi is set to False, This option can be overridden to return list with single value.
                        using `NON_MULTI_RESULT_LIST`
                List - When multi is set to True
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
                 "base_url": Argument(String, description=const.link_base_url_desc),
             },
             resolve=resolve_link,
             description="Extracts href attribute from anchor <a> tag. If the base_url argument is give, "
                         "it will form the absolute url. Xpath expected to be anchor tag.")
