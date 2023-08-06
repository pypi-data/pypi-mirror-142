from graphql import GraphQLEnumType as EnumType

from scrapqd.executor.selenium_driver.factory import BrowserFactory

BrowserEnum = EnumType("Browser",
                       {d.upper(): d for d in BrowserFactory().mapping()},
                       description="Browser option in the selenium executor")
