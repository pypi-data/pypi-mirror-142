from ._helper import get_ua_data_file

# custom EXECUTOR implementation classes.
CRAWLERS = {}

# custom Browser implementation mapping for selenium.
BROWSERS = {}

# custom SCRAPQD fields as leaf nodes in the graphql query which returns html node values
LEAVES = {}

# custom SCRAPQD query fields in the graphql query
QUERY_FIELDS = {}

# Custom data type conversion mapping other than system defined int, float
DATATYPE_CONVERSION = {}

# Default app name
APP_NAME = "ScrapQD"

# Whether to send result as List or return single element when multi=False in the leaf nodes
NON_MULTI_RESULT_LIST = False

# Fetch results are cached to speed up development. However, lifetime of the cache will be as
# per below settings
LOCAL_CACHE_TTL = 10  # in minutes

# User agent data file to send requests. If this is not set default data file will be used
USER_AGET_DATA_FILE = get_ua_data_file()

# User agents can be set as list with this settings. If this is set, user agents from the file will be ignored
USER_AGET_DATA = []

# Chromium and FireFox driver version for Selenium
CHROMIUM_VERSION = None
GECKODRIVER_VERSION = None

# Default browser for selenium driver
DEFAULT_BROWSER = "GOOGLE_CHROME"
