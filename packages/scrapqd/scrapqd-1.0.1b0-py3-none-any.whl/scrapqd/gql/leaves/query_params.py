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
def resolve_query_params(parser: Parser, info: ResolveInfo,
                         xpath, name=None, multi=const.MULTI_DEFAULT_VALUE):
    """Extracts query params values and returns as dictionary to client, if the xpath resolves to be an url.

    :param parser: Parser instance passed down from parent query.
    :param info: GraphQLResolveInfo instance which gives resolver information.
    :param xpath: path to locate node(tag).
    :param name:    if the name is not given, it extracts all the query params. if the name is given,
                    only extracts the given param and sends to client.
    :param multi: It is set to False as default.
                    - True  - Process multiple elements when xpath locates multiple nodes.
                    - False - Process first element when xpath locates multiple nodes.
    :return: List[Dict] - If multi is set to `true`.
             Dict -  If multi is set to `false`. This option can be overridden to return list with single value
                     using `NON_MULTI_RESULT_LIST`.
    """
    key = get_key(info)
    result = parser.solve_query_params(key=key, multi=multi, xpath=xpath, name=name)
    result = parser.get_multi_results(multi, result)
    parser.caching(key, result)
    return result


query_params = Field(GenericScalar,
                     args={
                         "xpath": Argument(NonNull(String), description=const.xpath_desc),
                         "multi": Argument(Boolean, description=const.multi_desc),
                         "name": Argument(String, description=const.query_params_name_desc),
                     },
                     resolve=resolve_query_params,
                     description="Extracts query params from the url. Xpath expected to be an URL.")
