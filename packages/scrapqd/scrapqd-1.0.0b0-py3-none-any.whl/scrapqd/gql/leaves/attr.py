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
    :param name: By default, it extracts all the attributes are extracted from the located node and
                    sent as dictionary. if the name is given, only given attribute name is extracted from located node.
    :param multi: by default, it is set to False. Thus, when the given xpath locates multiple nodes,
               it returns first node value. if it is set `true`, it will return all the node values" \
               as list.
    :return:    Dict - if multi is set to `false`.
                List[Dict] - if multi is set to `true`.
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
                 "name": Argument(String, description="name of the attribute to extract from the element."),
             },
             resolve=resolve_attr,
             description="Extracts attribute from given path. If the name argument is not provided,"
                         "all the attribute from the element will be extracted.")
