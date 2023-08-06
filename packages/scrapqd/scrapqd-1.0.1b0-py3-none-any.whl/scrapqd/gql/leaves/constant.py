from graphql import GraphQLArgument as Argument
from graphql import GraphQLField as Field
from graphql import GraphQLNonNull as NonNull
from graphql import GraphQLResolveInfo as ResolveInfo

from scrapqd.gql.helper import get_key, with_error_traceback
from scrapqd.gql.parser import Parser
from scrapqd.gql.scalar.generic import GenericScalar


@with_error_traceback
def resolve_constant(parser: Parser, info: ResolveInfo, value):
    """
    Constant value can be any data type. It is sent back in the result.

    :param parser: Parser instance passed down from parent query.
    :param info: GraphQLResolveInfo instance which gives resolver information.
    :param value: Any value from the client.
    :return: Any - value received from client as it is.
    """
    key = get_key(info)
    parser.caching(key, value)
    return value


constant = Field(GenericScalar,
                 args={
                     "value": Argument(NonNull(GenericScalar), description="Constant value of any data type."),
                 },
                 resolve=resolve_constant,
                 description="Constant value can be any data type. It is sent back in the result.")
