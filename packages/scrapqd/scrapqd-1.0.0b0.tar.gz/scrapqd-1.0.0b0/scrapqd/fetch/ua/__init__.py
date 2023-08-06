import random

from scrapqd.settings import config


def get_user_agent():
    """Gets random user-agent from settings"""
    user_agent = random.choice(config.USER_AGENTS)
    return user_agent
