import functools

from graphql import GraphQLResolveInfo as ResolveInfo

from scrapqd.gql import logger


def get_key(info: ResolveInfo):
    """Gets current key from which is getting resolved if graphql.

    :param info: 'GraphQLResolveInfo instance which gives resolver information.'
    :return: String
    """
    return info.path.key


def with_error_traceback(func):
    # TODO: Rename to log exception for graphql resolvers.

    @functools.wraps(func)
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logger.exception("%s", e, exc_info=True)
            raise e

    return inner
