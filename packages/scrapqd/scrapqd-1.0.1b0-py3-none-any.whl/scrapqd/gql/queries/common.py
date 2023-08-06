from scrapqd.fetch.interface import Executor
from scrapqd.fetch.process import Process
from scrapqd.gql import cache as local_memory_cache
from scrapqd.gql.parser import Parser


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
