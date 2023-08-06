from graphql import GraphQLEnumType as EnumType

from scrapqd.fetch.factory import ExecutorFactory

ExecutorEnum = EnumType("Executor",
                        {d.upper(): d for d in ExecutorFactory().mapping() if d != "SELENIUM"},
                        description="Crawler executors")
