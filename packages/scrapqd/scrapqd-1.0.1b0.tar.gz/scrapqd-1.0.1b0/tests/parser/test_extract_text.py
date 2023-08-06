import unittest

from scrapqd.gql.parser import Parser

TEMPLATE = """
<html>
    <body>
        <a class="menu-item selected">Users
            <span class="Counter" data-search-type="Users">89K</span>
            <span class="Counter" data-search-type="Repositories">10</span>
            <span class="Counter" data-search-type="Commits">1480</span>
            <span class="Counter" data-search-type="Forks">3</span>
        </a>
    </body>
</html>
"""


class TestParserExtractText(unittest.TestCase):
    def setUp(self):
        self.template = TEMPLATE
        self.parser = Parser(raw_html=self.template)

    def test_parser_extract_text(self):
        with self.assertRaises(TypeError):
            Parser(data=self.template)

    def test_parser_extract_text_1(self):
        xpath = "//span[@data-search-type='Users']"
        result = self.parser.extract_text(key="user_count", multi=False, xpath=xpath)
        self.assertListEqual(["89K"], result)

    def test_lxml_parser_extract_text_1(self):
        xpath = "//a/text()[1]"
        result = self.parser.extract_text(key="tag", multi=False, xpath=xpath)
        self.assertListEqual(["Users\n            "], result)

    def test_lxml_parser_extract_text_multi(self):
        xpath = "//a/text()"
        result = self.parser.extract_text(key="tag", multi=True, xpath=xpath)
        self.assertListEqual(
            [
                "Users\n            ",
                "\n            ",
                "\n            ",
                "\n            ",
                "\n        ",
            ],
            result,
        )
