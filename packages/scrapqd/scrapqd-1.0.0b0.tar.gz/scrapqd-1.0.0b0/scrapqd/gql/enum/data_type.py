from graphql import GraphQLEnumType as EnumType

from scrapqd.gql_parser.data_type import DataTypeFactory

DataTypeEnum = EnumType("DataType",
                        {d.upper(): d for d in DataTypeFactory().mapping()},
                        description="data type")
