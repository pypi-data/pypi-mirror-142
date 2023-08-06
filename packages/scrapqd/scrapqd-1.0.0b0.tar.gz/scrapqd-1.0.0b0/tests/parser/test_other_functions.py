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


class TestParserExtractText(unittest.TestCase):
    def setUp(self):
        self.template = TEMPLATE
        self.parser = Parser(raw_html=self.template)

    def test_parser_regex_text(self):
        xpath = "//span[@data-search-type='Users']"
        pattern = r"(\d+)"
        result = self.parser.apply_regex(key="user_count", multi=False, source="text", pattern=pattern, xpath=xpath)
        self.assertListEqual([["89", "90"]], result)

    def test_parser_regex_source_text(self):
        xpath = "//span[@data-search-type='Users']"
        pattern = r"(\d+)"
        result = self.parser.apply_regex(key="user_count", multi=False, source=None, pattern=pattern, xpath=xpath)
        self.assertListEqual([["10", "89", "90"]], result)

    def test_parser_regex_text_multi(self):
        expected = [["89", "90"], ["10"], ["1480"], ["3"]]
        xpath = "//span"
        pattern = r"(\d+)"
        result = self.parser.apply_regex(key="user_count", multi=True, source="text", pattern=pattern, xpath=xpath)
        self.assertListEqual(expected, result)

    def test_parser_regex_source_text_multi(self):
        expected = [["10", "89", "90"], ["11", "10"], ["12", "1480"], ["13", "3"]]
        xpath = "//span"
        pattern = r"(\d+)"
        result = self.parser.apply_regex(key="user_count", multi=True, source=None, pattern=pattern, xpath=xpath)
        self.assertListEqual(expected, result)

    def test_parser_query_params(self):
        expected = [{"g": "13", "s": "40", "v": "4"}]
        xpath = "//img/@src"
        result = self.parser.solve_query_params(key="user_count", multi=False, xpath=xpath)
        self.assertEqual(expected, result)

    def test_parser_query_params_name(self):
        expected = [{"s": "40"}]
        xpath = "//img/@src"
        result = self.parser.solve_query_params(key="user_count", multi=False, name="s", xpath=xpath)
        self.assertEqual(expected, result)

    def test_parser_query_params_name_multi(self):
        expected = [{"s": "40"}, {"s": None}]
        xpath = "//img/@src"
        result = self.parser.solve_query_params(key="user_count", multi=True, name="s", xpath=xpath)
        self.assertEqual(expected, result)

    def test_parser_query_params_name_multi_1(self):
        expected = [{"g": "13"}, {"g": "14"}]
        xpath = "//img/@src"
        result = self.parser.solve_query_params(key="user_count", multi=True, name="g", xpath=xpath)
        self.assertEqual(expected, result)

    def test_parser_query_params_multi(self):
        expected = [
            {"g": "13", "s": "40", "v": "4"},
            {"g": "14", "s1": "41", "v1": "4"}
        ]
        xpath = "//img/@src"
        result = self.parser.solve_query_params(key="user_count", multi=True, xpath=xpath)
        self.assertEqual(expected, result)

    def test_parser_url(self):
        expected = ["http://scrapqd.com/users/?item=profile"]
        xpath = "//a"
        base_url = "http://scrapqd.com/"
        result = self.parser.solve_link(key="user_count", multi=False, base_url=base_url, xpath=xpath)
        self.assertEqual(expected, result)

    def test_parser_link_1(self):
        expected = ["http://scrapqd.com/users/?item=profile"]
        xpath = "//a"
        base_url = "http://scrapqd.com"
        result = self.parser.solve_link(key="user_count", multi=False, base_url=base_url, xpath=xpath)
        self.assertEqual(expected, result)

    def test_parser_link_2(self):
        expected = ["http://scrapqd.com/users/?item=profile"]
        xpath = "//a"
        base_url = "scrapqd.com"
        result = self.parser.solve_link(key="user_count", multi=False, base_url=base_url, xpath=xpath)
        self.assertNotEqual(expected, result)

    def test_parser_link_3(self):
        expected = ["http://scrapqd.com/users/?item=logout"]
        xpath = "//a[2]"
        base_url = "http://scrapqd.com"
        result = self.parser.solve_link(key="user_count", multi=False, base_url=base_url, xpath=xpath)
        self.assertEqual(expected, result)

    def test_parser_link_multi(self):
        expected = ["http://scrapqd.com/users/?item=profile",
                    "http://scrapqd.com/users/?item=logout"]
        xpath = "//a"
        base_url = "http://scrapqd.com"
        result = self.parser.solve_link(key="user_count", multi=True, base_url=base_url, xpath=xpath)
        self.assertEqual(expected, result)
