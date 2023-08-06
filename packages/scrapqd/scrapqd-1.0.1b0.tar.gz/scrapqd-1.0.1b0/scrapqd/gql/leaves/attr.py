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
def resolve_attr(parser: Parser, info: ResolveInfo,
                 xpath, name=None, multi=const.MULTI_DEFAULT_VALUE):
    """
    Extracts node(tag) attribute values.

    :param parser: Parser instance passed down from parent query.
    :param info: GraphQLResolveInfo instance which gives resolver information.
    :param xpath: path to locate node(tag).
    :param name:
                - It extracts all the attributes are extracted If the attribute name is not provided.
                - If the name is given, only given attribute name is extracted.
    :param multi: It is set to False as default.
                    - True  - Process multiple elements when xpath locates multiple nodes.
                    - False - Process first element when xpath locates multiple nodes.
    :return:    Dict - If multi is set to `false`.
                List[Dict] - If multi is set to `true`.
    """
    key = get_key(info)
    result = parser.extract_attr(key=key, name=name, multi=multi, xpath=xpath)
    result = parser.get_multi_results(multi, result)
    parser.caching(key, result)
    return result


attr = Field(GenericScalar,
             args={
                 "xpath": Argument(NonNull(String), description=const.xpath_desc),
                 "multi": Argument(Boolean, description=const.multi_desc),
                 "name": Argument(String, description=const.attr_desc),
             },
             resolve=resolve_attr,
             description="Extracts attributes from the element.")
