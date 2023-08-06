from scrapqd.factory_interface import ConfigItem
from scrapqd.gql.exception import LeafNotSupportedError
from scrapqd.gql.leaves.attr import attr
from scrapqd.gql.leaves.constant import constant
from scrapqd.gql.leaves.form import form_input
from scrapqd.gql.leaves.link import link
from scrapqd.gql.leaves.query_params import query_params
from scrapqd.gql.leaves.regex import regex
from scrapqd.gql.leaves.text import text
from scrapqd.settings import config

leaves = {
    "text": text,
    "attr": attr,
    "form_input": form_input,
    "query_params": query_params,
    "link": link,
    "constant": constant,
    "regex": regex,
}


class LeafFactory(ConfigItem):
    """Combines system leaf fields mapping and user config"""

    def __init__(self):
        super().__init__(config=config.LEAVES,
                         exception=LeafNotSupportedError,
                         default_config=leaves,
                         upper_keys=False,
                         default_item=None)
