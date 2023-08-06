import unittest

from lxml import html

from scrapqd.gql_parser.lxml_parser import LXMLParser

TEMPLATE = """
<html>
    <body>
        <form class="requestParams" id="reqAttr">
            <input name="rlz" value="1C5CHFA_enIN991IN991" type="hidden">
            <input name="tbm" value="lcl" type="hidden">
            <input name="sxsrf" value="APq-WBu3vzrA9-WQU_Mp0Zs9aq2a-PQlJg:1644327612221" type="hidden">
            <input value="vHICYpKHDaWXseMP57uWuA4" name="ei" type="hidden">
            <input value="AHkkrS4AAAAAYgKAzF3dfuu_a7YROtX7wSMb404M2sTE" disabled="true" name="iflsig" type="hidden">
        </form>
        <form class="requestParams" id="apiAttr">
            <input name="rlz" value="1C5CHFA_enIN991IN991" type="hidden">
            <input name="tbm" value="lcl" type="hidden">
            <input name="sxsrf" value="APq-WBu3vzrA9-WQU_Mp0Zs9aq2a-PQlJg:1644327612221" type="hidden">
            <input value="vHICYpKHDaWXseMP57uWuA4" name="ei" type="hidden">
            <input value="AHkkrS4AAAAAYgKAzF3dfuu_a7YROtX7wSMb404M2sTE" disabled="true" name="iflsig" type="hidden">
        </form>
    </body>
</html>
"""


class TestLXMLParserExtractForm(unittest.TestCase):
    def setUp(self):
        self.template = TEMPLATE
        self.parser = LXMLParser(raw_html=self.template)

    def test_lxml_parser_extract_form_input(self):
        xpath = "//form[@id='reqAttr']"
        result = self.parser.extract_form_input(xpath=xpath)
        self.assertEqual(1, len(result))

    def test_lxml_parser_extract_form_input_1(self):
        xpath = "//form[@id='reqAttr']"
        result = self.parser.extract_form_input(xpath=xpath)
        self.assertEqual(list, type(result[0]))

    def test_lxml_parser_extract_form_input_2(self):
        xpath = "//form[@class='requestParams']"
        result = self.parser.extract_form_input(xpath=xpath)
        self.assertEqual(2, len(result))

    def test_lxml_parser_extract_form_input_3(self):
        xpath = "//form[@class='requestParams']"
        result = self.parser.extract_form_input(xpath=xpath)
        self.assertListEqual([list, list], [type(t) for t in result])

    def test_lxml_parser_extract_form_input_4(self):
        xpath = "//form[@class='requestParams']"
        result = self.parser.extract_form_input(xpath=xpath)
        expected = []
        result_elements = []
        for res in result:
            for t in res:
                result_elements.append(type(t))
                expected.append(html.InputElement)
        self.assertListEqual(expected, result_elements)
