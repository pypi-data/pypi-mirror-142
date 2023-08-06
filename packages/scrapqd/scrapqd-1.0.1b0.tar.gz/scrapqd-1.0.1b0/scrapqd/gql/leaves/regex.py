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
def resolve_regex(parser: Parser, info: ResolveInfo,
                  xpath, pattern, source="text", multi=const.MULTI_DEFAULT_VALUE):
    """Applies regex on node html/node content and extracts value if regex format is found.
    It uses python `re` module `findall` method to process regex.

    :param parser: Parser instance passed down from parent query.
    :param info: GraphQLResolveInfo instance which gives resolver information.
    :param xpath: path to locate node(tag).
    :param source:  Regex will be applied on extracted node's content as default.
                    If source is set to `html`, regex is applied on node(s) html.

                    Accepted source types:
                        1. text (default)
                        2. html
    :param pattern: Regex pattern to be applied on source.
    :param multi: It is set to False as default.
                    - True  - Process multiple elements when xpath locates multiple nodes.
                    - False - Process first element when xpath locates multiple nodes.
    :return: List[values based on regex] - when multi is set to True
             value based on regex - when mult is set to False. This option can be overridden to return list with single value.
                                    using `NON_MULTI_RESULT_LIST`
    """
    key = get_key(info)
    result = parser.apply_regex(key, xpath=xpath, source=source, pattern=pattern, multi=multi)
    result = parser.get_multi_results(multi, result)
    parser.caching(key, result)
    return result


regex = Field(GenericScalar,
              args={
                  "xpath": Argument(NonNull(String), description=const.regex_xpath_desc),
                  "pattern": Argument(NonNull(String), description=const.regex_pattern_desc),
                  "source": Argument(String, description=const.regex_source_desc),
                  "multi": Argument(Boolean, description=const.multi_desc)
              },
              resolve=resolve_regex,
              description="Regex will be using re.findall from python to extract data.")
