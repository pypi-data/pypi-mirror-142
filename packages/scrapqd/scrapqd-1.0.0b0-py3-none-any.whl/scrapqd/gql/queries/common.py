from scrapqd.fetch.interface import Executor
from scrapqd.fetch.process import Process
from scrapqd.gql import cache as local_memory_cache
from scrapqd.gql.parser import Parser

url_desc = "URL to crawl."
selenium_browser_desc = "By default system will execute fetch using requests library." \
                        "\n\nThis behaviour can be changed by giving the executor parameter. " \
                        "\n\nCustom crawl executor is created and registered beforehand."
json_response_desc = "This should be set to true if the url response is in json format."
executor_desc = "By default system will execute fetch using requests library." \
                "\n\nThis behaviour can be changed by giving the executor parameter." \
                "\n\nCustom crawl executor is created and registered beforehand."
payload_desc = "Payload will be used in case of other request methods are provided such as POST"
method_desc = "This is http method used to crawl. By default get."
headers_desc = "Addition request headers to the crawl request. " \
               "\n\nBy default User-Agent, Connection, Upgrade-Insecure-Requests are provided."
cache_desc = "Caches url request from web. This should be used only in text to minimize the request" \
             "while creating new query. " \
             "\n\nCache will be invalidated after 10 minutes."


def fetch(process, is_json_response):
    data = process.get_response_content()
    response_headers = process.get_response_headers()
    response_url = process.get_response_url()
    response_headers["response_url"] = response_url
    if is_json_response:
        raise Exception("system does not support json")
    parser = Parser(raw_html=data, headers=response_headers)
    return parser


def resolver(url, cache=False, is_json_response=False, **kwargs):
    process = None
    if cache:
        process: Executor = local_memory_cache.get_url(url)

    if not process:
        process: Executor = Process(url, **kwargs).crawl()
        if cache:
            local_memory_cache.cache(url, process)
    parser = fetch(process, is_json_response)
    return parser
