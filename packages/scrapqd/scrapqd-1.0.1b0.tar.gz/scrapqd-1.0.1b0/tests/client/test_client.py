import unittest

from scrapqd.client import execute_sync


class TestClient(unittest.TestCase):
    def setUp(self):
        self.query = r"""
                    query test_query($url: String!, $name: GenericScalar!) {
                      result: fetch(url: $url) {
                        name: constant(value: $name)
                        website: link(xpath: "//a[contains(@class, 'site-link')]")
                        summary: group {
                          total_emp_expenses: text(xpath: "//*[@id='emp-exp-total']", data_type: INT)
                          total_shown_expenses: text(xpath: "//*[@id='exp-total']/span[2]", data_type: INT)
                          total_approved_expenses: text(xpath: "//*[@id='emp-exp-approved']/span[2]", data_type: INT)
                        }
                        summary1: group {
                          total_shown_expenses: regex(xpath: "//*[@id='exp-total']", pattern: "(\\d+)")
                        }
                        exp_details: list(xpath: "//div[@class='card']") {
                          name: text(xpath: "//div[contains(@class,'expense-emp-name')]")
                          user_id: query_params(xpath: "//a/@href", name: "user")
                          amount: group {
                            money: text(xpath: "//h6[contains(@class,'expense-amount')]/span[1]", data_type: INT)
                            name: text(xpath: "//h6[contains(@class,'expense-amount')]/span[2]")
                          }
                          approval_id: attr(xpath: "//button[contains(@class, 'expense-approve')]", name: "id")
                        }
                        exp_details_method2: list(xpath: "//div[@class='card']") {
                          name: text(xpath: "//div[@class='card-title title expense-emp-name']")
                        }
                        exp_details_method3: list(xpath: "//div[@class='card']") {
                          name1: text(xpath: ".//div[@class='card-title title expense-emp-name']")
                          name2: text(xpath: ".//div[contains(@class,'expense-emp-name')]")
                        }
                      }
                    }
                """
        self.expected_result = {
            "result": {
                "name": "local-testing",
                "website": "http://localhost:5000/scrapqd",
                "summary": {
                    "total_emp_expenses": 309,
                    "total_shown_expenses": 40,
                    "total_approved_expenses": 4
                },
                "summary1": {
                    "total_shown_expenses": [
                        "40"
                    ]
                },
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
                ],
                "exp_details_method2": [
                    {
                        "name": "Friedrich-Wilhelm, Langern"
                    },
                    {
                        "name": "Sebastian, Bien"
                    },
                    {
                        "name": "Rosa, Becker"
                    },
                    {
                        "name": "Ines, Gröttner"
                    },
                    {
                        "name": "Clarissa, Bonbach"
                    },
                    {
                        "name": "Zbigniew, Stolze"
                    },
                    {
                        "name": "Ines, Mentzel"
                    },
                    {
                        "name": "Rosa, Becker"
                    },
                    {
                        "name": "Sigismund, Rosemann"
                    },
                    {
                        "name": "Edelbert, van der Dussen"
                    },
                    {
                        "name": "Clarissa, Bonbach"
                    },
                    {
                        "name": "Lilli, Heintze"
                    },
                    {
                        "name": "Gabriele, Gerlach"
                    },
                    {
                        "name": "Olivia, Dussen van"
                    },
                    {
                        "name": "Albina, Neureuther"
                    },
                    {
                        "name": "Friedrich-Wilhelm, Langern"
                    },
                    {
                        "name": "Lilli, Heintze"
                    },
                    {
                        "name": "Clarissa, Bonbach"
                    },
                    {
                        "name": "Rolf, Kühnert"
                    },
                    {
                        "name": "Alexa, Reising"
                    },
                    {
                        "name": "Ines, Gröttner"
                    },
                    {
                        "name": "Gabriele, Gerlach"
                    },
                    {
                        "name": "Albina, Neureuther"
                    },
                    {
                        "name": "Abdul, Bolnbach"
                    },
                    {
                        "name": "Alexa, Reising"
                    },
                    {
                        "name": "Albina, Neureuther"
                    },
                    {
                        "name": "Alida, Niemeier"
                    },
                    {
                        "name": "Sibylle, Eimer"
                    },
                    {
                        "name": "Alida, Niemeier"
                    },
                    {
                        "name": "Albina, Neureuther"
                    },
                    {
                        "name": "Alida, Niemeier"
                    },
                    {
                        "name": "Abdul, Bolnbach"
                    },
                    {
                        "name": "Clarissa, Bonbach"
                    },
                    {
                        "name": "Edelbert, van der Dussen"
                    },
                    {
                        "name": "Hans-Georg, Bärer"
                    },
                    {
                        "name": "Sebastian, Bien"
                    },
                    {
                        "name": "Ines, Gröttner"
                    },
                    {
                        "name": "Abdul, Bolnbach"
                    },
                    {
                        "name": "Albina, Neureuther"
                    },
                    {
                        "name": "Zbigniew, Stolze"
                    }
                ],
                "exp_details_method3": [
                    {
                        "name1": "Friedrich-Wilhelm, Langern",
                        "name2": "Friedrich-Wilhelm, Langern"
                    },
                    {
                        "name1": "Sebastian, Bien",
                        "name2": "Sebastian, Bien"
                    },
                    {
                        "name1": "Rosa, Becker",
                        "name2": "Rosa, Becker"
                    },
                    {
                        "name1": "Ines, Gröttner",
                        "name2": "Ines, Gröttner"
                    },
                    {
                        "name1": "Clarissa, Bonbach",
                        "name2": "Clarissa, Bonbach"
                    },
                    {
                        "name1": "Zbigniew, Stolze",
                        "name2": "Zbigniew, Stolze"
                    },
                    {
                        "name1": "Ines, Mentzel",
                        "name2": "Ines, Mentzel"
                    },
                    {
                        "name1": "Rosa, Becker",
                        "name2": "Rosa, Becker"
                    },
                    {
                        "name1": "Sigismund, Rosemann",
                        "name2": "Sigismund, Rosemann"
                    },
                    {
                        "name1": "Edelbert, van der Dussen",
                        "name2": "Edelbert, van der Dussen"
                    },
                    {
                        "name1": "Clarissa, Bonbach",
                        "name2": "Clarissa, Bonbach"
                    },
                    {
                        "name1": "Lilli, Heintze",
                        "name2": "Lilli, Heintze"
                    },
                    {
                        "name1": "Gabriele, Gerlach",
                        "name2": "Gabriele, Gerlach"
                    },
                    {
                        "name1": "Olivia, Dussen van",
                        "name2": "Olivia, Dussen van"
                    },
                    {
                        "name1": "Albina, Neureuther",
                        "name2": "Albina, Neureuther"
                    },
                    {
                        "name1": "Friedrich-Wilhelm, Langern",
                        "name2": "Friedrich-Wilhelm, Langern"
                    },
                    {
                        "name1": "Lilli, Heintze",
                        "name2": "Lilli, Heintze"
                    },
                    {
                        "name1": "Clarissa, Bonbach",
                        "name2": "Clarissa, Bonbach"
                    },
                    {
                        "name1": "Rolf, Kühnert",
                        "name2": "Rolf, Kühnert"
                    },
                    {
                        "name1": "Alexa, Reising",
                        "name2": "Alexa, Reising"
                    },
                    {
                        "name1": "Ines, Gröttner",
                        "name2": "Ines, Gröttner"
                    },
                    {
                        "name1": "Gabriele, Gerlach",
                        "name2": "Gabriele, Gerlach"
                    },
                    {
                        "name1": "Albina, Neureuther",
                        "name2": "Albina, Neureuther"
                    },
                    {
                        "name1": "Abdul, Bolnbach",
                        "name2": "Abdul, Bolnbach"
                    },
                    {
                        "name1": "Alexa, Reising",
                        "name2": "Alexa, Reising"
                    },
                    {
                        "name1": "Albina, Neureuther",
                        "name2": "Albina, Neureuther"
                    },
                    {
                        "name1": "Alida, Niemeier",
                        "name2": "Alida, Niemeier"
                    },
                    {
                        "name1": "Sibylle, Eimer",
                        "name2": "Sibylle, Eimer"
                    },
                    {
                        "name1": "Alida, Niemeier",
                        "name2": "Alida, Niemeier"
                    },
                    {
                        "name1": "Albina, Neureuther",
                        "name2": "Albina, Neureuther"
                    },
                    {
                        "name1": "Alida, Niemeier",
                        "name2": "Alida, Niemeier"
                    },
                    {
                        "name1": "Abdul, Bolnbach",
                        "name2": "Abdul, Bolnbach"
                    },
                    {
                        "name1": "Clarissa, Bonbach",
                        "name2": "Clarissa, Bonbach"
                    },
                    {
                        "name1": "Edelbert, van der Dussen",
                        "name2": "Edelbert, van der Dussen"
                    },
                    {
                        "name1": "Hans-Georg, Bärer",
                        "name2": "Hans-Georg, Bärer"
                    },
                    {
                        "name1": "Sebastian, Bien",
                        "name2": "Sebastian, Bien"
                    },
                    {
                        "name1": "Ines, Gröttner",
                        "name2": "Ines, Gröttner"
                    },
                    {
                        "name1": "Abdul, Bolnbach",
                        "name2": "Abdul, Bolnbach"
                    },
                    {
                        "name1": "Albina, Neureuther",
                        "name2": "Albina, Neureuther"
                    },
                    {
                        "name1": "Zbigniew, Stolze",
                        "name2": "Zbigniew, Stolze"
                    }
                ]
            }
        }
        self.maxDiff = None

    def test_library_sample_query_with_variables(self):

        query_variables = {
            "url": "http://localhost:5000/scrapqd/sample_page/",
            "name": "local-testing"
        }
        result = execute_sync(self.query, query_variables)
        self.assertDictEqual(self.expected_result, result.data)

    def test_library_sample_query_without_variables(self):
        query = r"""
                query test_query {
                  result: fetch(url: "http://localhost:5000/scrapqd/sample_page/") {
                    name: constant(value: "local-testing")
                    website: link(xpath: "//a[contains(@class, 'site-link')]")
                    summary: group {
                      total_emp_expenses: text(xpath: "//*[@id='emp-exp-total']", data_type: INT)
                      total_shown_expenses: text(xpath: "//*[@id='exp-total']/span[2]", data_type: INT)
                      total_approved_expenses: text(xpath: "//*[@id='emp-exp-approved']/span[2]", data_type: INT)
                    }
                    summary1: group {
                      total_shown_expenses: regex(xpath: "//*[@id='exp-total']", pattern: "(\\d+)")
                    }
                    exp_details: list(xpath: "//div[@class='card']") {
                      name: text(xpath: "//div[contains(@class,'expense-emp-name')]")
                      user_id: query_params(xpath: "//a/@href", name: "user")
                      amount: group {
                        money: text(xpath: "//h6[contains(@class,'expense-amount')]/span[1]", data_type: INT)
                        name: text(xpath: "//h6[contains(@class,'expense-amount')]/span[2]")
                      }
                      approval_id: attr(xpath: "//button[contains(@class, 'expense-approve')]", name: "id")
                    }
                    exp_details_method2: list(xpath: "//div[@class='card']") {
                      name: text(xpath: "//div[@class='card-title title expense-emp-name']")
                    }
                    exp_details_method3: list(xpath: "//div[@class='card']") {
                      name1: text(xpath: ".//div[@class='card-title title expense-emp-name']")
                      name2: text(xpath: ".//div[contains(@class,'expense-emp-name')]")
                    }
                  }
                }
            """
        result = execute_sync(query)
        self.assertDictEqual(self.expected_result, result.data)
