import importlib
import logging
import os

from scrapqd.common.helper import is_empty

from . import _default_config as default_config

logger = logging.getLogger("settings")


class UserAgentNotProvidedError(Exception):
    def __init__(self):
        self.message = "USER_AGET_DATA should be provided."


def _get_configs(mod):
    """Gets module variables and creates dictionary"""

    if "__all__" in mod.__dict__:  # noqa
        configs = mod.__dict__["__all__"]
    else:
        configs = [x for x, v in mod.__dict__.items() if not x.startswith("__") and not callable(v)]
    configs = {k: getattr(mod, k) for k in configs}
    return configs


def get_default_config():
    """processes default settings"""

    configs = _get_configs(default_config)
    return configs


def get_user_config():
    """Processes user defined settings from SCRAPQD_CONFIG environment variable."""

    scrapqd_config = os.environ.get("SCRAPQD_CONFIG", None)
    configs = {}
    logger.info("Loading user settings %s", scrapqd_config)
    if scrapqd_config:
        mod = importlib.import_module(scrapqd_config)
        configs = _get_configs(mod)
    return configs


def get_user_agents(config):
    """Loads user-agent from data file to local memory"""

    user_agent_file = config["USER_AGET_DATA_FILE"]
    user_agents = config["USER_AGET_DATA"] if "USER_AGET_DATA" in config else None
    if not user_agents:
        logger.info("Processing user agent data from file %s", user_agent_file)
        with open(user_agent_file, "r", encoding="utf-8") as f:
            user_agents = f.readlines()
            user_agents = [ua.strip() for ua in user_agents if ua.strip()]
    else:
        logger.info("Processing user agent data from list")
    return tuple(set(user_agents))


def get_application_config():
    """Creates application settings by combining default and user settings"""

    default_config = get_default_config()
    user_configs = get_user_config()

    is_user_ua_file_defined = "USER_AGET_DATA_FILE" in user_configs and is_empty(user_configs["USER_AGET_DATA_FILE"])
    if is_user_ua_file_defined and is_empty(user_configs.get("USER_AGET_DATA", None)):
        raise UserAgentNotProvidedError()

    configs = {**default_config, **user_configs}
    user_agents = get_user_agents(configs)
    configs["USER_AGENTS"] = user_agents
    return configs
