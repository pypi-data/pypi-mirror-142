import unittest

from scrapqd.gql.parser import Parser

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
            <input name="rlz" value="1C5CHFA_enIN991IN9911" type="hidden">
            <input name="tbm" value="lcl1" type="hidden">
            <input name="sxsrf" value="APq-WBu3vzrA9-WQU_Mp0Zs9aq2a-PQlJg:16443276122211" type="hidden">
            <input value="vHICYpKHDaWXseMP57uWuA41" name="ei" type="hidden">
            <input value="AHkkrS4AAAAAYgKAzF3dfuu_a7YROtX7wSMb404M2sTE1" disabled="true" name="iflsig" type="hidden">
        </form>
        <form class="requestParams" id="dummy">
        </form>
    </body>
</html>
"""


class TestParserExtractForm(unittest.TestCase):
    def setUp(self):
        self.template = TEMPLATE
        self.parser = Parser(raw_html=self.template)

    def test_parser_extract_form(self):
        xpath = "//form[@id='reqAttr']"
        result = self.parser.extract_form_input(
            key="request_params", name=None, multi=False, xpath=xpath
        )
        self.assertEqual(1, len(result))

    def test_parser_extract_form_1(self):
        xpath = "//form[@id='reqAttr']"
        result = self.parser.extract_form_input(
            key="request_params", name=None, multi=False, xpath=xpath
        )
        self.assertEqual(list, type(result))

    def test_parser_extract_form_2(self):
        xpath = "//form[@class='requestParams']"
        result = self.parser.extract_form_input(
            key="request_params", name=None, multi=False, xpath=xpath
        )
        self.assertEqual(1, len(result))

    def test_parser_extract_form_2_multi(self):
        xpath = "//form[@class='requestParams']"
        result = self.parser.extract_form_input(
            key="request_params", name=None, multi=True, xpath=xpath
        )
        self.assertEqual(3, len(result))

    def test_parser_extract_form_3(self):
        xpath = "//form[@class='requestParams']"
        result = self.parser.extract_form_input(
            key="request_params", name=None, multi=False, xpath=xpath
        )
        self.assertListEqual([dict], [type(t) for t in result])

    def test_parser_extract_form_4(self):
        expected = [
            {
                "rlz": "1C5CHFA_enIN991IN9911",
                "tbm": "lcl1",
                "sxsrf": "APq-WBu3vzrA9-WQU_Mp0Zs9aq2a-PQlJg:16443276122211",
                "ei": "vHICYpKHDaWXseMP57uWuA41",
                "iflsig": "AHkkrS4AAAAAYgKAzF3dfuu_a7YROtX7wSMb404M2sTE1",
            }
        ]
        xpath = "//form[@id='apiAttr']"
        result = self.parser.extract_form_input(
            key="request_params", name=None, multi=True, xpath=xpath
        )
        self.assertListEqual(expected, result)

    def test_parser_extract_form_5(self):
        expected = [{"iflsig": "AHkkrS4AAAAAYgKAzF3dfuu_a7YROtX7wSMb404M2sTE1"}]
        xpath = "//form[@id='apiAttr']"
        result = self.parser.extract_form_input(
            key="request_params", name="iflsig", multi=True, xpath=xpath
        )
        self.assertListEqual(expected, result)

    def test_parser_extract_form_none(self):
        expected = [{}]
        xpath = "//form[@id='dummy']"
        result = self.parser.extract_form_input(
            key="request_params", name=None, multi=True, xpath=xpath
        )
        self.assertListEqual(expected, result)

    def test_parser_extract_form_name_none(self):
        expected = [{"iflsig": None}]
        xpath = "//form[@id='dummy']"
        result = self.parser.extract_form_input(
            key="request_params", name="iflsig", multi=True, xpath=xpath
        )
        self.assertListEqual(expected, result)

    def test_parser_extract_form_multi(self):
        xpath = "//form[@class='requestParams']"
        result = self.parser.extract_form_input(
            key="request_params", name=None, multi=True, xpath=xpath
        )
        self.assertListEqual([dict, dict, dict], [type(t) for t in result])

    def test_parser_extract_form_name(self):
        expected = [
            {"tbm": "lcl", "ei": "vHICYpKHDaWXseMP57uWuA4"},
            {"tbm": "lcl1", "ei": "vHICYpKHDaWXseMP57uWuA41"},
            {"tbm": None, "ei": None},
        ]
        xpath = "//form[@class='requestParams']"
        result = self.parser.extract_form_input(
            key="request_params", name=["tbm", "ei"], multi=True, xpath=xpath
        )
        self.assertListEqual(expected, result)
