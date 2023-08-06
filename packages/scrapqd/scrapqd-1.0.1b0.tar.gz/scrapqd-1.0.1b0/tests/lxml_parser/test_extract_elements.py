import unittest

from lxml import html

from scrapqd.gql_parser.lxml_parser import LXMLParser

TEMPLATE = """
<html>
    <body>
        <div class="requestParams" id="reqAttr">
            <input name="rlz" value="1C5CHFA_enIN991IN991" type="hidden">
            <input name="tbm" value="lcl" type="hidden">
            <input name="sxsrf" value="APq-WBu3vzrA9-WQU_Mp0Zs9aq2a-PQlJg:1644327612221" type="hidden">
            <input value="vHICYpKHDaWXseMP57uWuA4" name="ei" type="hidden">
            <input value="AHkkrS4AAAAAYgKAzF3dfuu_a7YROtX7wSMb404M2sTE" disabled="true" name="iflsig" type="hidden">
        </div>
        <div class="requestParams" id="apiAttr">
            <input name="rlz" value="1C5CHFA_enIN991IN991" type="hidden">
            <input name="tbm" value="lcl" type="hidden">
            <input name="sxsrf" value="APq-WBu3vzrA9-WQU_Mp0Zs9aq2a-PQlJg:1644327612221" type="hidden">
            <input value="vHICYpKHDaWXseMP57uWuA4" name="ei" type="hidden">
            <input value="AHkkrS4AAAAAYgKAzF3dfuu_a7YROtX7wSMb404M2sTE" disabled="true" name="iflsig" type="hidden">
        </div>
    </body>
</html>
"""


class TestLXMLParserExtractElements(unittest.TestCase):
    def setUp(self):
        self.template = TEMPLATE
        self.parser = LXMLParser(raw_html=self.template)

    def test_lxml_parser_extract_elements(self):
        xpath = "//div[@id='reqAttr']"
        result = self.parser.extract_elements(xpath=xpath)
        self.assertEqual(1, len(result))

    def test_lxml_parser_extract_elements_1(self):
        xpath = "//div[@id='reqAttr']"
        result = self.parser.extract_elements(xpath=xpath)
        self.assertEqual(html.HtmlElement, type(result[0]))

    def test_lxml_parser_extract_elements_2(self):
        xpath = "//div[@class='requestParams']"
        result = self.parser.extract_elements(xpath=xpath)
        self.assertEqual(2, len(result))

    def test_lxml_parser_extract_elements_3(self):
        xpath = "//div[@class='requestParams']"
        result = self.parser.extract_elements(xpath=xpath)
        self.assertListEqual([html.HtmlElement, html.HtmlElement], [type(t) for t in result])
