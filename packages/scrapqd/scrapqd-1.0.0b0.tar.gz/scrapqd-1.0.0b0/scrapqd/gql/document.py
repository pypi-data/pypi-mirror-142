from graphql import GraphQLArgument as Argument
from graphql import GraphQLField as Field
from graphql import GraphQLList as List
from graphql import GraphQLNonNull as NonNull
from graphql import GraphQLObjectType as Object
from graphql import GraphQLResolveInfo as ResolveInfo
from graphql import GraphQLString as String

from scrapqd.gql import constants as const
from scrapqd.gql.helper import get_key, with_error_traceback
from scrapqd.gql.leaves.factory import LeafFactory
from scrapqd.gql.parser import Parser

# document containing all the leaves
Document = Object("Document",
                  lambda: {**multi_level, **LeafFactory().mapping()},
                  description="A character in the Star Wars Trilogy")


@with_error_traceback
def resolve_group(parser: Parser, info: ResolveInfo):
    """Groups multiple elements under single given group key.
    :param parser: Parser instance passed down from parent query.
    :param info: GraphQLResolveInfo instance which gives resolver information.
    :return: Dict
    """

    key = get_key(info)
    result = {}
    parser.caching(key, result)
    parser.cache = parser.get(key)
    return parser


@with_error_traceback
def resolve_list(parser: Parser, info: ResolveInfo, xpath):
    """Child queries will be applied on each node from list query result.

    :param parser: Parser instance passed down from parent query.
    :param info: GraphQLResolveInfo instance which gives resolver information.
    :param xpath: xpath which returns multiple elements.
    :return: List
    """
    parsers = []
    key = get_key(info)
    element = parser.extract_elements(key=key, multi=True, xpath=xpath)
    parser.cache[key] = {}
    for idx, e in enumerate(element):
        parser.cache[key][idx] = {}
        parsers.append(Parser(html_tree=e, parent=parser, cache=parser.cache[key][idx]))
    return parsers


list_field = Field(List(Document),
                   args={"xpath": Argument(NonNull(String), description=const.xpath_desc)},
                   description="This will process list of element in the given xpath.",
                   resolve=resolve_list)
group_field = Field(Document,
                    description="This query will group elements and return as dict.",
                    resolve=resolve_group)

multi_level = {
    "list": list_field,
    "group": group_field
}
