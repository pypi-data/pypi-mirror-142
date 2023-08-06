from graphql import GraphQLObjectType as Object
from graphql import GraphQLSchema as Schema

from scrapqd.gql.queries.factory import QueryFieldFactory

Driver = Object("Driver", lambda: QueryFieldFactory().mapping())
schema = Schema(Driver)
