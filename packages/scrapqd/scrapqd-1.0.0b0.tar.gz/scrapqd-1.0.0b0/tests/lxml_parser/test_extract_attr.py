import unittest

from scrapqd.gql_parser.lxml_parser import LXMLParser

TEMPLATE = """
<html>
    <body>
        <a data-hydro-click-hmac="073231b0dd43e8e6fbcf087c39c029724f251c4337e6ba83326e95487f469fb6"
            data-hovercard-type="organization" data-hovercard-url="/orgs/abcxcom/hovercard"
            class="d-table" href="/abcxcom">
              <img class="rounded-1" style="margin-top: 2px;"
              src="https://avatars.websiteusercontent.com/u/698437?s=40&amp;v=4" width="20" height="20" alt="@abcxcom">
        </a>
        <a data-hovercard-type="organization" data-hovercard-url="/orgs/abcxcom/hovercard"
            class="d-table" href="/abcxcom1">
              <img class="rounded-1" style="margin-top: 2px;"
                src="https://avatars.websiteusercontent.com/u/698437?s=40&amp;v=4" width="20" height="20" alt="@abcxcom">
        </a>
    </body>
</html>
"""


class TestLXMLParserExtractAttr(unittest.TestCase):
    def setUp(self):
        self.template = TEMPLATE
        self.parser = LXMLParser(raw_html=self.template)
        self.maxDiff = None

    def test_lxml_parser_extract_attr(self):
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
        result = self.parser.extract_attr(xpath=xpath)
        self.assertListEqual(expected, [result[0]])

    def test_lxml_parser_extract_attr_1(self):
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
        result = self.parser.extract_attr(xpath=xpath)
        self.assertNotEqual(expected, [result[1]])

    def test_lxml_parser_extract_attr_3(self):
        xpath = "//a[@data-hovercard-type='organization']"
        result = self.parser.extract_attr(xpath=xpath)
        self.assertEqual(2, len(result))
