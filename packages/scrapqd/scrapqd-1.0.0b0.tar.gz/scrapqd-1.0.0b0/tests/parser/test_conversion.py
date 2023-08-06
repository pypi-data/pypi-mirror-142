import unittest

from scrapqd.gql.parser import Parser

TEMPLATE = """
<html>
    <body>
        <a class="menu-item selected" href="/users/?item=profile">Users
            <span class="Counter" counter="10" data-search-type="Users">89K90</span>
            <span class="Counter" counter="11" data-search-type="Repositories">10</span>
            <span class="Counter" counter="12" data-search-type="Commits">1480</span>
            <span class="Counter" counter="13" data-search-type="Forks">3</span>
            <img class="rounded-1" style="margin-top: 2px;"
                src="https://avatars.websiteusercontent.com/u/698437?s=40&amp;v=4&amp;g=13"
                width="20" height="20" alt="@abcxcom">
            <img class="rounded-1" style="margin-top: 2px;"
                src="https://avatars.websiteusercontent.com/u/698437?s1=41&amp;v1=4&amp;g=14"
                width="20" height="20" alt="@abcxcom">
        </a>
        <a class="menu-item" href="/users/?item=logout">Logout</a>
    </body>
</html>
"""


class TestParserDataTypeConversion(unittest.TestCase):
    def setUp(self):
        self.template = TEMPLATE
        self.parser = Parser(raw_html=self.template)

    def test_parser_int(self):
        expected = [844000]
        result = self.parser.data_conversion(["844k"], "int")
        self.assertEqual(expected, result)

    def test_parser_raw(self):
        expected = ["844k"]
        result = self.parser.data_conversion(["844k"], "raw")
        self.assertEqual(expected, result)

    def test_parser_raw_1(self):
        expected = ["844K"]
        result = self.parser.data_conversion(["844K"], "raw")
        self.assertEqual(expected, result)

    def test_parser_money(self):
        from scrapqd.settings import config
        with self.assertRaises(TypeError):
            config.DATATYPE_CONVERSION["round_2"] = lambda _: round(_, 2)
