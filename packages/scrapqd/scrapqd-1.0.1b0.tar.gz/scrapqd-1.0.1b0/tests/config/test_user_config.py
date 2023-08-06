import unittest

from scrapqd.client import execute_sync
from scrapqd.settings import config


class TestUserConfig(unittest.TestCase):
    def test_custom_user_config(self):
        """Testing custom user config"""
        self.assertEqual(config.LOCAL_CACHE_TTL, 20)

    def test_user_executor(self):
        query = r"""
                query test_query($url: String!, $name: GenericScalar!) {
                  result: fetch(url: $url, executor: PUPPETEER) {
                    name: constant(value: $name)
                    website: link(xpath: "//a[contains(@class, 'site-link')]")                
                  }
                }
            """
        expected_result = {
            "result": {
                "name": "local-testing",
                "website": "http://localhost:5000/scrapqd"
            }
        }
        query_variables = {
            "url": "http://localhost:5000/scrapqd/sample_page/",
            "name": "local-testing"
        }
        result = execute_sync(query, query_variables)
        self.assertDictEqual(expected_result, result.data)

    def test_user_data_type(self):
        query = r"""
                query test_query($url: String!, $name: GenericScalar!) {
                  result: fetch(url: $url) {
                    name: constant(value: $name)
                    total_emp_expenses: text(xpath: "//*[@id='emp-exp-total']", data_type: BOOLEAN)
                  }
                }

            """
        expected_result = {
            "result": {
                "name": "local-testing",
                "total_emp_expenses": True
            }
        }
        query_variables = {
            "url": "http://localhost:5000/scrapqd/sample_page/",
            "name": "local-testing"
        }
        result = execute_sync(query, query_variables)
        self.assertDictEqual(expected_result, result.data)

    def test_user_leaf_query(self):
        query = r"""
                query test_query($url: String!) {
                  result: fetch(url: $url) {
                    hard_constant
                    total_emp_expenses: text(xpath: "//*[@id='emp-exp-total']", data_type: INT)
                    total_emp_expenses1: text(xpath: "//*[@id='emp-exp-total']", data_type: BOOLEAN)
                  }
                }
            """
        expected_result = {
            "result": {
                "hard_constant": "sample-constant",
                "total_emp_expenses": 309,
                "total_emp_expenses1": True
            }
        }
        query_variables = {
            "url": "http://localhost:5000/scrapqd/sample_page/",
            "name": "local-testing"
        }
        result = execute_sync(query, query_variables)
        self.assertDictEqual(expected_result, result.data)
