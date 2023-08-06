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

xpath_desc = f"{const.xpath_desc} This xpath is expected to be html form element."
name_desc = "name of the input element to extract from the form."


@with_error_traceback
def resolve_form_input(parser: Parser, info: ResolveInfo,
                       xpath, name=None, multi=const.MULTI_DEFAULT_VALUE):
    """Extracts given form node's input [name:value] pairs as dictionary to client.

    :param parser: Parser instance passed down from parent query.
    :param info: GraphQLResolveInfo instance which gives resolver information.
    :param xpath: 'path to locate form.'
    :param name:    {name_desc} By default, all the form inputs are extracted and sent to client. If the name is given,
                    only given input[name:value] is extracted and sent to client.
    :param multi: by default, it is set to False. Thus, when the given xpath locates multiple nodes,
               it returns first node value. if it is set `true`, it will return all the node values" \
               as list.
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
                       "xpath": Argument(NonNull(String), description=xpath_desc),
                       "multi": Argument(Boolean, description=const.multi_desc),
                       "name": Argument(String, description=name_desc),
                   },
                   description="This query will look for input elements under form and "
                               "will group name: value as dict from inputs.",
                   resolve=resolve_form_input)
