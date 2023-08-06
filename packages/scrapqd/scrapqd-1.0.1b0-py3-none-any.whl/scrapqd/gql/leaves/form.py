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
def resolve_form_input(parser: Parser, info: ResolveInfo,
                       xpath, name=None, multi=const.MULTI_DEFAULT_VALUE):
    """Extracts form inputs and returns dictionary (name, value pair).

    :param parser: Parser instance passed down from parent query.
    :param info: GraphQLResolveInfo instance which gives resolver information.
    :param xpath: Xpath is expected to be a form
    :param name:
                - All the form inputs are extracted if name is not provided and sent to client.
                - If the name is given, only given input[name:value] is extracted and sent to client.
    :param multi: It is set to False as default.
                    - True  - Process multiple elements when xpath locates multiple nodes.
                    - False - Process first element when xpath locates multiple nodes.
    :return: List[Dict] - if multi is set to `true`.
             Dict -  if multi is set to `false`. This option can be overridden to return list with single value
                     using `NON_MULTI_RESULT_LIST`.
    """
    key = get_key(info)
    result = parser.extract_form_input(key=key, name=name, multi=multi, xpath=xpath)
    result = parser.get_multi_results(multi, result)
    parser.caching(key, result)
    return result


form_input = Field(GenericScalar,
                   args={
                       "xpath": Argument(NonNull(String), description=const.form_xpath_desc),
                       "multi": Argument(Boolean, description=const.multi_desc),
                       "name": Argument(String, description=const.form_name_desc),
                   },
                   description="Extracts form inputs and returns as dictionary (name, value pair).",
                   resolve=resolve_form_input)
