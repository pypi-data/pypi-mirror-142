import json

from scrapqd.factory_interface import ConfigItem
from scrapqd.gql.exception import RawDatatypeNotSupportedError
from scrapqd.settings import config


def _int(value):
    """
    Converts integer string values to integer

    >>>  _int('500K')
    >>>  500000

    :param value: string
    :return: integer
    """

    value = value.replace(",", "")
    num_map = {"K": 1000, "M": 1000000, "B": 1000000000}
    if value.isdigit():
        value = int(value)
    else:
        if len(value) > 1:
            value = value.strip()
            value = float(value[:-1]) * num_map.get(value[-1].upper(), 1)
    return int(value)


class DataTypeFactory(ConfigItem):
    """Combines system data type conversion mapping and user config"""

    def __init__(self):
        self.datatype_dict = {
            "TEXT": str,
            "INT": _int,
            "FLOAT": float,
            "JSON": json.loads,
            "RAW": lambda _: _
        }
        super().__init__(config=config.DATATYPE_CONVERSION,
                         exception=RawDatatypeNotSupportedError,
                         default_config=self.datatype_dict,
                         default_item="TEXT")
