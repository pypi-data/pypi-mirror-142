import unittest

from scrapqd.gql.parser import Parser

TEMPLATE = """
<html>
    <body>
        <a data-hydro-click-hmac="073231b0dd43e8e6fbcf087c39c029724f251c4337e6ba83326e95487f469fb6"
            data-hovercard-type="organization" data-hovercard-url="/orgs/abcxcom/hovercard"
            class="d-table" href="/abcxcom">
              <img class="rounded-1" style="margin-top: 2px;"
                src="https://avatars.websiteusercontent.com/u/698437?s=40&amp;v=4"
                width="20" height="20" alt="@abcxcom">
        </a>
        <a data-hydro-click-hmac="073231b0dd43e8e6fbcf087c39c029724f251c4337e6ba83326e95487f469fb6"
            data-hovercard-type="organization" data-hovercard-url="/orgs/abcxcom1/hovercard"
            class="d-table" href="/abcxcom1">
              <img class="rounded-1" style="margin-top: 2px;"
                src="https://avatars.websiteusercontent.com/u/698437?s=40&amp;v=4"
                width="20" height="20" alt="@abcxcom">
        </a>
        <a id="dummyAttr"><a>
    </body>
</html>
"""


class TestParserExtractAttr(unittest.TestCase):
    def setUp(self):
        self.template = TEMPLATE
        self.parser = Parser(raw_html=self.template)
        self.maxDiff = None

    def test_parser_extract_attr(self):
        expected = [
            {
                "data-hydro-click-hmac": "073231b0dd43e8e6fbcf087c39c029724f251c4337e6ba83326e95487f469fb6",
                "data-hovercard-type": "organization",
                "data-hovercard-url": "/orgs/abcxcom/hovercard",
                "class": "d-table",
                "href": "/abcxcom",
            }
        ]
        xpath = "//a[@data-hovercard-type='organization']"
        result = self.parser.extract_attr(
            key="user_attr", name=None, multi=False, xpath=xpath
        )
        self.assertListEqual(expected, result)

    def test_parser_extract_attr_1(self):
        expected = [
            {
                "data-hydro-click-hmac": "073231b0dd43e8e6fbcf087c39c029724f251c4337e6ba83326e95487f469fb6",
                "data-hovercard-type": "organization",
                "data-hovercard-url": "/orgs/abcxcom/hovercard",
                "class": "d-table",
                "href": "/abcxcom",
            }
        ]
        xpath = "//a[@data-hovercard-type='organization'][2]"
        result = self.parser.extract_attr(
            key="user_attr", name=None, multi=False, xpath=xpath
        )
        self.assertNotEqual(expected, result)

    def test_parser_extract_attr_multi(self):
        xpath = "//a[@data-hovercard-type='organization']"
        result = self.parser.extract_attr(
            key="user_attr", name=None, multi=True, xpath=xpath
        )
        self.assertEqual(2, len(result))

    def test_parser_extract_attr_name(self):
        expected = ["/orgs/abcxcom1/hovercard"]
        xpath = "//a[@data-hovercard-type='organization'][2]"
        result = self.parser.extract_attr(
            key="user_attr", name="data-hovercard-url", multi=True, xpath=xpath
        )
        self.assertEqual(expected, result)

    def test_parser_extract_attr_name_multi(self):
        expected = ["/orgs/abcxcom/hovercard", "/orgs/abcxcom1/hovercard"]
        xpath = "//a[@data-hovercard-type='organization']"
        result = self.parser.extract_attr(
            key="user_attr", name="data-hovercard-url", multi=True, xpath=xpath
        )
        self.assertEqual(expected, result)

    def test_parser_extract_attr_2(self):
        expected = []
        xpath = "//a[@data-hovercard-type='organization'][3]"
        result = self.parser.extract_attr(
            key="user_attr", name="data-hovercard-url", multi=False, xpath=xpath
        )
        self.assertEqual(expected, result)
