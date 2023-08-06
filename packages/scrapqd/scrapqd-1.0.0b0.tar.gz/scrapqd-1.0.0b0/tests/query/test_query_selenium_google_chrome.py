import unittest

from graphql import graphql_sync

from scrapqd.gql.schema import schema


class TestParserExtractText(unittest.TestCase):
    def setUp(self):
        self.variable_values = {
            "url": "http://127.0.0.1:5000/scrapqd/sample_page/",
            "cache": True,
        }
        self.maxDiff = None

    def test_query_text(self):
        expected = {
            "result": {
                "total_emp_expenses": 309
            }
        }
        result = graphql_sync(
            schema,
            """
          query test_query($url: String!, $cache: Boolean) {
              result: selenium(url: $url, cache: $cache) {
                total_emp_expenses: text(xpath: "//*[@id='emp-exp-total']", data_type: INT)
              }
            }
          """,
            variable_values=self.variable_values,
        )
        self.assertDictEqual(expected, result.data)

    def test_query_text_multi_ture(self):
        expected = {
            "result": {
                "total_emp_expenses": [309]
            }
        }
        result = graphql_sync(
            schema,
            """
          query test_query($url: String!, $cache: Boolean) {
              result: selenium(url: $url, cache: $cache) {
                total_emp_expenses: text(xpath: "//*[@id='emp-exp-total']", data_type: INT, multi: true)
              }
            }
          """,
            variable_values=self.variable_values,
        )
        self.assertDictEqual(expected, result.data)

    def test_query_group_constant(self):
        expected = {
            "result": {
                "content": {
                    "name": "local-testing"
                }
            }
        }

        result = graphql_sync(
            schema,
            """
          query test_query($url: String!, $cache: Boolean) {
              result: selenium(url: $url, cache: $cache) {
                content: group{
                  name: constant(value:"local-testing")
                }
              }
            }
          """,
            variable_values=self.variable_values,
        )
        self.assertDictEqual(expected, result.data)

    def test_query_url(self):
        expected = {
            "result": {
                "website": "http://127.0.0.1:5000/scrapqd",
            }
        }

        result = graphql_sync(
            schema,
            """
          query test_query($url: String!, $cache: Boolean) {
              result: selenium(url: $url, cache: $cache) {
                website: link(xpath: "//a[contains(@class, 'site-link')]")
              }
            }
          """,
            variable_values=self.variable_values,
        )
        self.assertDictEqual(expected, result.data)

    def test_query_link_multi(self):
        expected = {
            "result": {
                "website": ["http://127.0.0.1:5000/scrapqd"],
            }
        }
        result = graphql_sync(
            schema,
            """
          query test_query($url: String!, $cache: Boolean) {
              result: selenium(url: $url, cache: $cache) {
                website: link(xpath: "//a[contains(@class, 'site-link')]", multi: true)
              }
            }
          """,
            variable_values=self.variable_values,
        )
        self.assertDictEqual(expected, result.data)

    def test_query_data_type_int(self):
        expected = {
            "result": {
                "money": [
                    8800,
                    3365,
                    6700,
                    8427,
                    1609,
                    8789,
                    1750,
                    7293,
                    997,
                    4573,
                    6533,
                    3102,
                    21,
                    6945,
                    139,
                    8250,
                    6258,
                    7274,
                    6077,
                    2534,
                    5377,
                    6478,
                    2495,
                    7068,
                    3916,
                    7647,
                    8568,
                    2155,
                    2261,
                    2345,
                    8240,
                    1114,
                    3573,
                    1571,
                    468,
                    2013,
                    893,
                    2065,
                    245,
                    9453
                ]
            }
        }
        result = graphql_sync(
            schema,
            """
          query test_query($url: String!, $cache: Boolean) {
              result: selenium(url: $url, cache: $cache) {
                money: text(xpath: "//h6[contains(@class,'expense-amount')]/span[1]", data_type: INT, multi: true)
              }
            }
          """,
            variable_values=self.variable_values,
        )
        self.assertDictEqual(expected, result.data)

    def test_query_data_type_raw(self):
        expected = {
            "result": {
                "money": [
                    "8800.00",
                    "3365.00",
                    "6700.00",
                    "8427.00",
                    "1609.00",
                    "8789.00",
                    "1750.00",
                    "7293.00",
                    "997.00",
                    "4573.00",
                    "6533.00",
                    "3102.00",
                    "21.00",
                    "6945.00",
                    "139.00",
                    "8250.00",
                    "6258.00",
                    "7274.00",
                    "6077.00",
                    "2534.00",
                    "5377.00",
                    "6478.00",
                    "2495.00",
                    "7068.00",
                    "3916.00",
                    "7647.00",
                    "8568.00",
                    "2155.00",
                    "2261.00",
                    "2345.00",
                    "8240.00",
                    "1114.00",
                    "3573.00",
                    "1571.00",
                    "468.00",
                    "2013.00",
                    "893.00",
                    "2065.00",
                    "245.00",
                    "9453.00"
                ]
            }
        }
        result = graphql_sync(
            schema,
            """
          query test_query($url: String!, $cache: Boolean) {
              result: selenium(url: $url, cache: $cache) {
                money: text(xpath: "//h6[contains(@class,'expense-amount')]/span[1]", data_type: RAW, multi: true)
              }
            }
          """,
            variable_values=self.variable_values,
        )
        self.assertDictEqual(expected, result.data)

    def test_query_list(self):
        expected = {
            "result": {
                "exp_details": [
                    {
                        "name": "Friedrich-Wilhelm, Langern",
                        "user_id": {
                            "user": "friwilan0123"
                        },
                        "amount": {
                            "money": 8800,
                            "name": "egp"
                        },
                        "approval_id": "APPROVE-5bbd5c2f-435d-4529-8a5b-f05f1f89db5a"
                    },
                    {
                        "name": "Sebastian, Bien",
                        "user_id": {
                            "user": "sb0891"
                        },
                        "amount": {
                            "money": 3365,
                            "name": "mkd"
                        },
                        "approval_id": "APPROVE-cce88426-53cf-4475-9204-32f50268911b"
                    },
                    {
                        "name": "Rosa, Becker",
                        "user_id": {
                            "user": "rosbec647"
                        },
                        "amount": {
                            "money": 6700,
                            "name": "xof"
                        },
                        "approval_id": "APPROVE-a3ec6508-2c2c-439d-b090-b10ffef8189e"
                    },
                    {
                        "name": "Ines, Gröttner",
                        "user_id": {
                            "user": "inesgro1682"
                        },
                        "amount": {
                            "money": 8427,
                            "name": "npr"
                        },
                        "approval_id": "APPROVE-f8053cc8-9178-4afd-be51-573e749323e7"
                    },
                    {
                        "name": "Clarissa, Bonbach",
                        "user_id": {
                            "user": "clarbon1528"
                        },
                        "amount": {
                            "money": 1609,
                            "name": "fjd"
                        },
                        "approval_id": "APPROVE-10b88f2c-82ad-4f5d-bd1b-a03925934f0c"
                    },
                    {
                        "name": "Zbigniew, Stolze",
                        "user_id": {
                            "user": "zbisto0543"
                        },
                        "amount": {
                            "money": 8789,
                            "name": "ern"
                        },
                        "approval_id": "APPROVE-c60cf612-50be-437d-9ba8-2492de96e9c4"
                    },
                    {
                        "name": "Ines, Mentzel",
                        "user_id": {
                            "user": "inesmen135"
                        },
                        "amount": {
                            "money": 1750,
                            "name": "srd"
                        },
                        "approval_id": "APPROVE-73717d32-2228-48f2-a09f-2e90eeb94056"
                    },
                    {
                        "name": "Rosa, Becker",
                        "user_id": {
                            "user": "rosbec098"
                        },
                        "amount": {
                            "money": 7293,
                            "name": "mga"
                        },
                        "approval_id": "APPROVE-2e7ceca7-a40e-4bf5-ab43-f40ec9938b6a"
                    },
                    {
                        "name": "Sigismund, Rosemann",
                        "user_id": {
                            "user": "sigros1029"
                        },
                        "amount": {
                            "money": 997,
                            "name": "lbp"
                        },
                        "approval_id": "APPROVE-bb6e32a2-8167-456b-8433-5bb897e65e5d"
                    },
                    {
                        "name": "Edelbert, van der Dussen",
                        "user_id": {
                            "user": "edvan1230"
                        },
                        "amount": {
                            "money": 4573,
                            "name": "azn"
                        },
                        "approval_id": "APPROVE-f4fb98be-348a-4171-8d0e-622dcccb67e1"
                    },
                    {
                        "name": "Clarissa, Bonbach",
                        "user_id": {
                            "user": "clabon10"
                        },
                        "amount": {
                            "money": 6533,
                            "name": "mxn"
                        },
                        "approval_id": "APPROVE-23bd3e8a-3991-4a60-b2af-9e408dc8567e"
                    },
                    {
                        "name": "Lilli, Heintze",
                        "user_id": {
                            "user": "lilhen0987"
                        },
                        "amount": {
                            "money": 3102,
                            "name": "kwd"
                        },
                        "approval_id": "APPROVE-b3a5db8c-b20a-4327-8001-f4a60a034b34"
                    },
                    {
                        "name": "Gabriele, Gerlach",
                        "user_id": {
                            "user": "gabger1620"
                        },
                        "amount": {
                            "money": 21,
                            "name": "wst"
                        },
                        "approval_id": "APPROVE-e928c7f0-30e0-4e57-a149-f41b09d8961a"
                    },
                    {
                        "name": "Olivia, Dussen van",
                        "user_id": {
                            "user": "olidvan072"
                        },
                        "amount": {
                            "money": 6945,
                            "name": "kpw"
                        },
                        "approval_id": "APPROVE-6e03afc0-d380-4c55-9319-23dda59e19a2"
                    },
                    {
                        "name": "Albina, Neureuther",
                        "user_id": {
                            "user": "alb1021"
                        },
                        "amount": {
                            "money": 139,
                            "name": "kyd"
                        },
                        "approval_id": "APPROVE-1ed63b1b-4158-43a5-9553-3b3969776ef2"
                    },
                    {
                        "name": "Friedrich-Wilhelm, Langern",
                        "user_id": {
                            "user": "frlan1267"
                        },
                        "amount": {
                            "money": 8250,
                            "name": "mro"
                        },
                        "approval_id": "APPROVE-3d166482-1932-40f3-a96a-db2b72162f24"
                    },
                    {
                        "name": "Lilli, Heintze",
                        "user_id": {
                            "user": "lilhei1090"
                        },
                        "amount": {
                            "money": 6258,
                            "name": "shp"
                        },
                        "approval_id": "APPROVE-745869fa-dccb-4660-a043-28b7b9ae3a0d"
                    },
                    {
                        "name": "Clarissa, Bonbach",
                        "user_id": {
                            "user": "clabon1331"
                        },
                        "amount": {
                            "money": 7274,
                            "name": "bhd"
                        },
                        "approval_id": "APPROVE-30dc7b09-4b5d-4a2f-a8a1-09b0f36c5ebe"
                    },
                    {
                        "name": "Rolf, Kühnert",
                        "user_id": {
                            "user": "rolfk1089"
                        },
                        "amount": {
                            "money": 6077,
                            "name": "htg"
                        },
                        "approval_id": "APPROVE-0e6ed73d-57f8-4178-ad32-1235808ca7dd"
                    },
                    {
                        "name": "Alexa, Reising",
                        "user_id": {
                            "user": "alexa0012"
                        },
                        "amount": {
                            "money": 2534,
                            "name": "huf"
                        },
                        "approval_id": "APPROVE-49eeff26-62fc-411c-a02f-b64ae58448f7"
                    },
                    {
                        "name": "Ines, Gröttner",
                        "user_id": {
                            "user": "igro1654"
                        },
                        "amount": {
                            "money": 5377,
                            "name": "ltl"
                        },
                        "approval_id": "APPROVE-bc4c6801-f135-4cfd-ab88-999215b6a69c"
                    },
                    {
                        "name": "Gabriele, Gerlach",
                        "user_id": {
                            "user": "gab06781"
                        },
                        "amount": {
                            "money": 6478,
                            "name": "kwd"
                        },
                        "approval_id": "APPROVE-2c9b1501-034a-46af-81ad-b4f5ecadb051"
                    },
                    {
                        "name": "Albina, Neureuther",
                        "user_id": {
                            "user": "albneu1190"
                        },
                        "amount": {
                            "money": 2495,
                            "name": "sll"
                        },
                        "approval_id": "APPROVE-f9b126b0-ffbe-4873-81f0-bb0fafeec55e"
                    },
                    {
                        "name": "Abdul, Bolnbach",
                        "user_id": {
                            "user": "abdul1895"
                        },
                        "amount": {
                            "money": 7068,
                            "name": "all"
                        },
                        "approval_id": "APPROVE-c4f53406-410f-4dce-87dd-119d465a487d"
                    },
                    {
                        "name": "Alexa, Reising",
                        "user_id": {
                            "user": "alres1258"
                        },
                        "amount": {
                            "money": 3916,
                            "name": "cny"
                        },
                        "approval_id": "APPROVE-dbb04ad5-c896-42be-9596-0bd07ef0c6bd"
                    },
                    {
                        "name": "Albina, Neureuther",
                        "user_id": {
                            "user": "albn1199"
                        },
                        "amount": {
                            "money": 7647,
                            "name": "bbd"
                        },
                        "approval_id": "APPROVE-f61e5f2f-3596-425c-9d3d-114dc8497963"
                    },
                    {
                        "name": "Alida, Niemeier",
                        "user_id": {
                            "user": "alida0018"
                        },
                        "amount": {
                            "money": 8568,
                            "name": "cny"
                        },
                        "approval_id": "APPROVE-bd82e97d-8d97-414b-affe-3911b17798b9"
                    },
                    {
                        "name": "Sibylle, Eimer",
                        "user_id": {
                            "user": "eimer7610"
                        },
                        "amount": {
                            "money": 2155,
                            "name": "bam"
                        },
                        "approval_id": "APPROVE-bbad5ce0-bb8d-459f-b2ce-7ab42deda8e6"
                    },
                    {
                        "name": "Alida, Niemeier",
                        "user_id": {
                            "user": "nie3910"
                        },
                        "amount": {
                            "money": 2261,
                            "name": "byr"
                        },
                        "approval_id": "APPROVE-602e798a-e9d8-40c2-9b9c-abc707910f51"
                    },
                    {
                        "name": "Albina, Neureuther",
                        "user_id": {
                            "user": "albe00191"
                        },
                        "amount": {
                            "money": 2345,
                            "name": "cop"
                        },
                        "approval_id": "APPROVE-dcee1983-0edd-4fe3-9e0b-6a91764055c7"
                    },
                    {
                        "name": "Alida, Niemeier",
                        "user_id": {
                            "user": "alni10168"
                        },
                        "amount": {
                            "money": 8240,
                            "name": "lrd"
                        },
                        "approval_id": "APPROVE-1ad71dbb-5753-4fa2-98d0-afee10682210"
                    },
                    {
                        "name": "Abdul, Bolnbach",
                        "user_id": {
                            "user": "10273458"
                        },
                        "amount": {
                            "money": 1114,
                            "name": "brl"
                        },
                        "approval_id": "APPROVE-2de51261-325b-4f8b-a90f-b1965bd2d968"
                    },
                    {
                        "name": "Clarissa, Bonbach",
                        "user_id": {
                            "user": "091110168"
                        },
                        "amount": {
                            "money": 3573,
                            "name": "ils"
                        },
                        "approval_id": "APPROVE-fc2c52a1-05c2-47e2-a04d-035830eebf97"
                    },
                    {
                        "name": "Edelbert, van der Dussen",
                        "user_id": {
                            "user": "0912168"
                        },
                        "amount": {
                            "money": 1571,
                            "name": "zwd"
                        },
                        "approval_id": "APPROVE-61ce0628-7562-43a5-9dd2-20e681ca2370"
                    },
                    {
                        "name": "Hans-Georg, Bärer",
                        "user_id": {
                            "user": "11210168"
                        },
                        "amount": {
                            "money": 468,
                            "name": "tjs"
                        },
                        "approval_id": "APPROVE-ca739d44-0108-47c2-966f-a24b5ed21eaa"
                    },
                    {
                        "name": "Sebastian, Bien",
                        "user_id": {
                            "user": "981010168"
                        },
                        "amount": {
                            "money": 2013,
                            "name": "mvr"
                        },
                        "approval_id": "APPROVE-2f45973e-9ae3-41f8-938a-72b0df5be061"
                    },
                    {
                        "name": "Ines, Gröttner",
                        "user_id": {
                            "user": "1010168"
                        },
                        "amount": {
                            "money": 893,
                            "name": "ggp"
                        },
                        "approval_id": "APPROVE-704a6ee6-b5d8-42e2-92f0-ad0094c5b187"
                    },
                    {
                        "name": "Abdul, Bolnbach",
                        "user_id": {
                            "user": "56610168"
                        },
                        "amount": {
                            "money": 2065,
                            "name": "sll"
                        },
                        "approval_id": "APPROVE-6bcf66eb-9761-4a7f-a9c1-b90ec6c014fd"
                    },
                    {
                        "name": "Albina, Neureuther",
                        "user_id": {
                            "user": "alni10128"
                        },
                        "amount": {
                            "money": 245,
                            "name": "spl"
                        },
                        "approval_id": "APPROVE-513eb588-fb56-450a-8b4a-456b8afb4441"
                    },
                    {
                        "name": "Zbigniew, Stolze",
                        "user_id": {
                            "user": "zb1213e"
                        },
                        "amount": {
                            "money": 9453,
                            "name": "dkk"
                        },
                        "approval_id": "APPROVE-13851cd2-9c9d-412d-8fd1-65f99df176fb"
                    }
                ]
            }
        }
        result = graphql_sync(
            schema,
            """
          query test_query($url: String!, $cache: Boolean) {
              result: selenium(url: $url, cache: $cache) {
                exp_details: list(xpath: "//div[@class='card']") {
                  name: text(xpath: "//div[contains(@class,'expense-emp-name')]")
                  user_id: query_params(xpath: "//a/@href", name: "user")
                  amount: group {
                    money: text(xpath: "//h6[contains(@class,'expense-amount')]/span[1]", data_type: INT)
                    name: text(xpath: "//h6[contains(@class,'expense-amount')]/span[2]")
                  }
                  approval_id: attr(xpath: "//button[contains(@class, 'expense-approve')]", name: "id")
                }
              }
            }
          """,
            variable_values=self.variable_values,
        )
        self.assertDictEqual(expected, result.data)
