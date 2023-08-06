import unittest

from lxml import html

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
"""


class TestLXMLParserInstance(unittest.TestCase):
    def setUp(self):
        self.template = TEMPLATE

    def test_lxml_parser_instance(self):
        parser = LXMLParser(raw_html=self.template)
        self.assertEqual(html.HtmlElement, type(parser.html))

    def test_lxml_parser_instance_1(self):
        parser = LXMLParser(raw_html=bytes(self.template, "utf-8"))
        self.assertEqual(html.HtmlElement, type(parser.html))
