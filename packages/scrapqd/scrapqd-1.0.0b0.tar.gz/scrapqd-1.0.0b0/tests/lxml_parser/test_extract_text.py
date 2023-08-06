import unittest

from scrapqd.gql_parser.lxml_parser import LXMLParser

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


class TestLXMLParserExtractText(unittest.TestCase):
    def setUp(self):
        self.template = TEMPLATE
        self.parser = LXMLParser(raw_html=self.template)

    def test_lxml_parser_extract_text(self):
        xpath = "//span[@data-search-type='Users']"
        result = self.parser.extract_text(xpath=xpath)
        self.assertListEqual(["89K"], result)

    def test_lxml_parser_extract_text_1(self):
        xpath = "//a/text()[1]"
        result = self.parser.extract_text(xpath=xpath)
        self.assertListEqual(["Users\n            "], result)

    def test_lxml_parser_extract_text_1_1(self):
        xpath = "//a/text()"
        result = self.parser.extract_text(xpath=xpath)
        self.assertListEqual(
            ["Users\n            ", "\n            ", "\n            ", "\n            ", "\n        "], result)

    def test_lxml_parser_extract_text_2(self):
        xpath = "//span[@class='Counter']"
        result = self.parser.extract_text(xpath=xpath)
        self.assertListEqual(["89K", "10", "1480", "3"], result)

    def test_lxml_parser_extract_text_3(self):
        xpath = "//span[@class='CounterUser']"
        result = self.parser.extract_text(xpath=xpath)
        self.assertListEqual([], result)

    def test_lxml_parser_extract_text_arg_xpath(self):
        with self.assertRaises(TypeError):
            self.parser.extract_text()
