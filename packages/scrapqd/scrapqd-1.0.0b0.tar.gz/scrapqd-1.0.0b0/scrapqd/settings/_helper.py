import os
from pathlib import Path


def get_ua_data_file():
    """Gets default user agent data file path"""
    user_agent_dir = Path(__file__).resolve().parent
    user_aget_data_file = os.path.join(user_agent_dir, "user_agents.dat")
    return user_aget_data_file
