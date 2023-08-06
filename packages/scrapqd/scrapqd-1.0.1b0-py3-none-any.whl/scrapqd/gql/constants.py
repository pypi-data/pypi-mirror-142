xpath_desc = "XPath to the element to extract."
multi_desc = (
    "when xpath matches multiple elements.\n"
    "- `False` Processes first element\n"
    "- `True` Processes all elements\n"
)

# TEXT field argument descriptions
text_data_type_desc = "Text value to convert to specified data type."

# QUERY_PARAMS field argument descriptions
query_params_name_desc = "Name of the query param to get from the url."

# REGEX field argument descriptions
regex_xpath_desc = f"{xpath_desc} This xpath is expected to be html form element."
regex_pattern_desc = "Regular expression pattern to apply."
regex_source_desc = (
    "Regex will be applied on source. valid values are [html, text].\n"
    "- `html` regex will be applied on html outer html code.\n"
    "- `text` regex will be applied on text content from html element.\n"
)
regex_name_desc = "Name of the input element to extract from the form."

# LINK field argument description
link_base_url_desc = (
    "Custom base url will be used to form absolute url.\n"
    "`Example` /search?q=google if the base_url=google.com given, "
    "absolute url will be created as such -> `https://google.com/search?q=google`"
)

# FORM field argument description
form_xpath_desc = f"{xpath_desc} Xpath is expected to be a form element."
form_name_desc = "Name of the form input element to extract."

# ATTR field argument description
attr_desc = "Name of the attribute to extract from the element."

# QUERY field argument description
crawl_url_desc = "URL to crawl."
crawl_selenium_browser_desc = (
    "Requests library is used to crawl server rendered websites."
    "Custom crawl executor is created and registered beforehand.\n"    
    "- REQUESTS"
)
crawl_json_response_desc = "This should be set to true if the url response is in json format."
crawl_executor_desc = (
    "System supports below browser.\n"
    "- GOOGLE_CHROME\n"
    "- FIREFOX\n"
)
crawl_payload_desc = "Payload will be used in case of other request methods are provided such as POST"
crawl_method_desc = "This is http method used to crawl. By default get."
crawl_headers_desc = (
    "Addition request headers to the crawl request. System adds below headers by default.\n"
    "- User-Agent: from the data files.\n"
    "- Connection: keep-alive\n"
    "- Upgrade-Insecure-Requests: 1\n"
    "- Accept-Language: en-US,en;q=0.9\n"
    "- Accept-Encoding: gzip, deflate, br\n"
    "- Pragma: no-cache\n"
)
crawl_cache_desc = (
    "When cache is set to `true`, url response is cached and used in consecutive query execution "
    "to speed up the development process.\n"
    "> **_NOTE:_**  This is for query development purpose and not intended to use in production."
)
crawl_selenium_options_desc = (
    "Selenium options for waiting for the webpage. Below are accepted parameters.\n"
    "- `xpath` selenium will wait for webpage to load this element.\n"
    "- `wait_time` selenium will wait for xpath target (wait_time) secs."
)

MULTI_DEFAULT_VALUE = False
DATA_TYPE_DEFAULT_VALUE = "text"
