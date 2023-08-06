from .data_type import boolean
from .leaf import hard_constant
from .puppeteer import Puppeteer

# custom EXECUTOR implementation classes.
CRAWLERS = {
    'PUPPETEER': Puppeteer
}

# custom SCRAPQD fields as leaf nodes in the graphql query which returns html node values
LEAVES = {
    'hard_constant': hard_constant
}

# custom SCRAPQD query fields in the graphql query
QUERY_FIELDS = {
}

# Custom data type conversion mapping other than system defined int, float
DATATYPE_CONVERSION = {
    'BOOLEAN': boolean
}

# Default app name
APP_NAME = "ScrapQD"

# Whether to send result as List or return single element when multi=False in the leaf nodes
NON_MULTI_RESULT_LIST = False

# Load sample page as url. This page is available for testing the query from graphql UI by default.
LOAD_SAMPLE_PAGE = True

# Fetch results are cached to speed up development. However, lifetime of the cache will be as
# per below settings
LOCAL_CACHE_TTL = 20  # in minutes

# Chromium and FireFox driver version for Selenium
CHROMIUM_VERSION = "97.0.4692.71"
GECKODRIVER_VERSION = None
