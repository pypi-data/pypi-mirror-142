import logging
from datetime import datetime
from functools import lru_cache
from types import MappingProxyType


def is_empty(obj):
    """Checks if the object is None or empty

    :param obj: object to check
    :return: Boolean
    """

    empty_mapping = {
        str: "",
        list: [],
        tuple: (),
        dict: {},
        set: set(),
        frozenset: frozenset()
    }
    empty = obj == empty_mapping.get(type(obj), None)
    return empty


def json_serializer(obj):
    """Json serializer function is used for dumping python dictionary to json format.

    :param obj: python datastructure
    :return: json serializable format
    """

    if isinstance(obj, (set, frozenset)):
        return list(obj)
    if isinstance(obj, MappingProxyType):
        return dict(obj)
    if isinstance(obj, datetime):
        return obj.timestamp()
    else:
        return str(obj)


@lru_cache(maxsize=1)
def is_debug_enabled(logger):
    """Check debug is enabled for logger"""
    return logger.isEnabledFor(logging.DEBUG)
