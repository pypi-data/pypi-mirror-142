from graphql import GraphQLArgument as Argument
from graphql import GraphQLField as Field
from graphql import GraphQLNonNull as NonNull
from graphql import GraphQLResolveInfo as ResolveInfo

from scrapqd.gql.helper import get_key, with_error_traceback
from scrapqd.gql.parser import Parser
from scrapqd.gql.scalar.generic import GenericScalar


@with_error_traceback
def resolve_constant(parser: Parser, info: ResolveInfo):
    return "sample-constant"


hard_constant = Field(GenericScalar,
                      resolve=resolve_constant,
                      description="Sample Constant")
