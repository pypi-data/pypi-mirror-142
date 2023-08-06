import json

from immutable.immutable import immutable

from scrapqd.common.helper import is_debug_enabled, json_serializer

from ._loader import get_application_config
from ._logging import logging

logger = logging.getLogger("settings")
configs = get_application_config()

# creates namedtuple from settings dict to make settings immutable
# To make python default data structures set, dict immutable,
# frozenset and MappingProxyType used respectively
config = immutable("Config", dct=configs, clone=False, recursive=True, only_const=True)

logger.info("Config is loaded.")
if is_debug_enabled(logger):
    logger.debug("%s", json.dumps(config._asdict(), indent=4, default=json_serializer))
del configs
