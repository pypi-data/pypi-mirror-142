from graphql import GraphQLArgument as Argument
from graphql import GraphQLBoolean as Boolean
from graphql import GraphQLField as Field
from graphql import GraphQLNonNull as NonNull
from graphql import GraphQLResolveInfo as ResolveInfo
from graphql import GraphQLString as String

from scrapqd.gql import constants as const
from scrapqd.gql.enum.data_type import DataTypeEnum
from scrapqd.gql.helper import get_key, with_error_traceback
from scrapqd.gql.parser import Parser
from scrapqd.gql.scalar.generic import GenericScalar


@with_error_traceback
def resolve_text(parser: Parser, info: ResolveInfo,
                 xpath, data_type=const.DATA_TYPE_DEFAULT_VALUE, multi=const.MULTI_DEFAULT_VALUE):
    """Extracts node(tag) content as text using given XPath and convert to specified data type.

    :param parser: Parser instance passed down from parent query.
    :param info: GraphQLResolveInfo instance which gives resolver information.
    :param xpath: Path to locate node(tag).
    :param data_type:   Extracted text will be always in text format. When the data type is provided,
                        content is converted to that format and returned to the client.
                        Accepted data types:

                            - text (default)
                            - int
                            - float

    :param multi: It is set to False as default.
                    - True  - Process multiple elements when xpath locates multiple nodes.
                    - False - Process first element when xpath locates multiple nodes.
    :return:
            - Text - When multi is set to False, This option can be overridden to return list with single value using
            `NON_MULTI_RESULT_LIST`.
            - List - When multi is set to True
    """
    key = get_key(info)
    parser.datatype_check(key, data_type)
    result = parser.extract_text(key=key, multi=multi, xpath=xpath)
    result = parser.data_conversion(result, data_type)
    result = parser.get_multi_results(multi, result)
    parser.caching(key, result)
    return result


text = Field(GenericScalar,
             args={
                 "xpath": Argument(NonNull(String), description=const.xpath_desc),
                 "data_type": Argument(DataTypeEnum, description=const.text_data_type_desc),
                 "multi": Argument(Boolean, description=const.multi_desc),
             },
             resolve=resolve_text,
             description="Extracts text content from the give xpath.")
