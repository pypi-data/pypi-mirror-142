import re
from functools import partial
from urllib import parse

from scrapqd.gql import logger
from scrapqd.gql.exception import (InvalidDataTypeError,
                                   InvalidParserArgumentsError,
                                   InvalidParserError, ParserUnavailableError)
from scrapqd.gql_parser.lxml_parser import LXMLParser


def get_non_multi_result_list():
    from scrapqd.settings import config
    return config.NON_MULTI_RESULT_LIST


def get_data_type_mapping():
    from scrapqd.gql_parser.data_type import DataTypeFactory
    mapping = DataTypeFactory().mapping()
    return mapping


class BasicParser:
    def __init__(self):
        self.datatype_dict = get_data_type_mapping()

    def conversion(self, value, key, func):
        try:
            value = func(value)
        except Exception:
            logger.exception("Not able to convert to %s", key, exc_info=True)
        return value

    def non_multi_data_conversion(self, val):
        non_multi_result_list = get_non_multi_result_list()
        result = [val] if non_multi_result_list else val
        return result

    def data_conversion(self, values, datatype):
        result = []

        if not datatype:
            return result

        datatype = datatype.upper()
        for v in values:
            conversion_function = self.datatype_dict[datatype]
            v = v.strip()
            v = self.conversion(value=v, key=datatype, func=conversion_function)
            result.append(v)

        return result

    def datatype_check(self, key, data_type):
        if data_type and data_type.upper() not in self.datatype_dict:
            raise InvalidDataTypeError(key, data_type)

    def parse_query_params(self, name, url):
        parsed_url = parse.urlparse(url)
        values_tuple = parse.parse_qsl(parsed_url.query)
        query_params = dict(values_tuple)
        if name:
            keys = name if isinstance(name, list) else [name]
            query_params = {name: query_params.get(name, None) for name in keys}
        return query_params

    def get_form_inputs(self, name, form_input):
        values = {input_.name: input_.value for input_ in form_input if input_.name}
        if name:
            keys = name if isinstance(name, list) else [name]
            values = {name: values.get(name, None) for name in keys}
        return values

    def apply_partial_process(self, partial_func, multi, values):
        result = []

        if not values:
            return []

        if values and not multi:
            values = values[:1]

        for value in values:
            val = partial_func(value)
            result.append(val)

        return result

    def get_multi_results(self, multi, values):
        result = values
        if not multi and len(values) > 0:
            result = self.non_multi_data_conversion(values[0])

        return result


class Parser(BasicParser):
    """This is gql_parser facade class to extract data using given gql_parser.
    System by default uses 'lxml' gql_parser with xpath. Selector based extraction is not supported.
    """

    def __init__(self, raw_html=None, html_tree=None, parser="lxml", parent=None, cache=None, headers=None):
        """Initiates the Parser class

        :param raw_html: plain html string
        :param html_tree: html nodes from the gql_parser
        :param parser: gql_parser to be used in the extraction process.
        :param parent: parent gql_parser when new gql_parser instance is created for chile elements.
        :param cache: local cache for leaves data on the same level.
        :param headers: local cache for leaves data on the same level.

        :raises InvalidParserArgumentsError: raises exception when raw_html or html_tree is not given
        :raises InvalidParserError: raises exception when unsupported parsers by the library
        :raises ParserUnavailableError: raises exception when parser object is None
        """

        super().__init__()
        if headers is None:
            headers = {}
        if parser == "lxml":
            if raw_html and html_tree is None:
                parser = LXMLParser(raw_html=raw_html)
            elif html_tree is not None:
                parser = LXMLParser(html_tree=html_tree)
            else:
                raise InvalidParserArgumentsError()
            self.parser = parser
        else:
            raise InvalidParserError(parser=parser)

        if self.parser is None:
            raise ParserUnavailableError()

        if cache is None:
            cache = {}

        ancestors = parent.ancestors + [parent] if parent else []
        self.cache = cache
        self.request_cache = parent.request_cache if parent else self.cache

        self.ancestors = ancestors
        self.headers = parent.headers if parent else headers

    def caching(self, key, value):
        """Caches data

        :param key: document attribute at the current level
        :param value: attribute value
        """

        self.cache[key] = value

    def get(self, key):
        """Gets data from local cache.

        :param key: document attribute at the current level
        :return: cached attribute value
        """

        return self.cache[key]

    def get_elements_source_text(self, elements):
        """Facade method to get html source of the elements.

        :param elements: list of html elements
        :return: List[string]
        """

        result = [self.parser.extract_element_source_text(e) for e in elements]
        return result

    def extract_elements(self, key, multi, xpath, **kwargs):
        """Facade method to get elements using given xpath

        :param key: current processing attribute in the query.
        :param xpath: xpath to locate the elements.
        :param multi:True/False,
                   True - should process all the elements extracted.
                   False - only process first element
        :param kwargs: additional keyword arguments for extensibility.
        :return: List[element object]
        """

        data = self.parser.extract_elements(xpath=xpath, **kwargs)
        dummy_partial = partial(lambda v: v)
        result = self.apply_partial_process(dummy_partial, multi, data)
        return result

    def extract_text(self, key, multi, xpath, **kwargs):
        """Extracts text for given xpath.

        :param key: current processing attribute in the query.
        :param xpath: xpath to locate the elements.
        :param multi:True/False,
               True - should process all the elements extracted.
               False - only process first element
        :param kwargs: additional keyword arguments for extensibility.
        :return: List[String]
        """

        data = self.parser.extract_text(xpath=xpath, **kwargs)
        dummy_partial = partial(lambda v: v)
        result = self.apply_partial_process(dummy_partial, multi, data)
        return result

    def extract_form_input(self, key, name, multi, xpath, **kwargs):
        """Extracts form inputs using given xpath. Method expects xpath to locate form node.

        :param key: current processing attribute in the query.
        :param name: to extract specific input name, otherwise all the input names will be extracted.
        :param xpath: xpath to locate the elements.
        :param multi:True/False,
               True - should process all the elements extracted.
               False - only process first element
        :param kwargs: additional keyword arguments for extensibility.
        :return: List[String]
        """

        form_inputs = self.parser.extract_form_input(xpath=xpath, **kwargs)
        form_partial = partial(self.get_form_inputs, name)
        result = self.apply_partial_process(form_partial, multi, form_inputs)
        return result

    def extract_attr(self, key, name, multi, xpath, **kwargs):
        """Extracts attributes from the node. If the name is given, only the specified attribute is extracted.

        :param key: current processing attribute in the query.
        :param name: name of the attribute to extract
        :param xpath: xpath to locate the elements.
        :param multi: True/False,

                - True - should process all the elements extracted.
                - False - only process first element

        :param kwargs: additional keyword arguments for extensibility.
        :return: List[String]
        """

        values = self.parser.extract_attr(xpath=xpath, **kwargs)

        def get_attrib(name_, attrib_):
            if name_:
                attrib_ = attrib_.get(name_, None)
            return attrib_

        get_attrib_partial = partial(get_attrib, name)
        result = self.apply_partial_process(get_attrib_partial, multi, values)
        return result

    def apply_regex(self, key, source, pattern, multi, xpath, **kwargs):
        """Applies regex on the extracted node html or content based on the source type.

        :param key: current processing attribute in the query.
        :param source: regex to be applied on source content or html.
                       Accepted data types:
                        1. text (default)
                        2. html
        :param pattern: regex pattern to be applied
        :param xpath: xpath to locate the elements.
        :param multi: True/False,

                    - True - should process all the elements extracted.
                    - False - only process first element
        :param kwargs: additional keyword arguments for extensibility.
        :return: List[String]
        """

        if source == "text":
            result = self.extract_text(key=key, multi=multi, xpath=xpath, **kwargs)
        else:
            values = self.extract_elements(key=key, multi=multi, xpath=xpath, **kwargs)
            result = self.get_elements_source_text(values)

        cre = re.compile(pattern)
        findall_partial = partial(cre.findall)
        results = self.apply_partial_process(findall_partial, multi, result)
        return results

    def solve_query_params(self, key, multi, xpath, **kwargs):
        """Extracts query params values and returns as dictionary to client, if the xpath resolves to be an url.

        :param key: current processing attribute in the query.
        :param xpath: xpath to locate the elements.
        :param multi:True/False,
               True - should process all the elements extracted.
               False - only process first element
        :param kwargs: additional keyword arguments for extensibility.
        :return: List[String]
        """

        name = kwargs.pop("name", None)
        urls = self.extract_text(key=key, multi=multi, xpath=xpath, **kwargs)
        parse_url_partial = partial(self.parse_query_params, name)
        result = self.apply_partial_process(parse_url_partial, multi, urls)
        return result

    def solve_link(self, key, multi, base_url, xpath, **kwargs):
        """Extracts node's href, forms absolute url from the response. If the base_url is given, base_url
        will be used to form absolute url.

        :param key: current processing attribute in the query.
        :param xpath: xpath to locate the elements.
        :param multi:True/False,
               True - should process all the elements extracted.
               False - only process first element:
        :param base_url: will be used to form the absolute url with relative url.
        :param kwargs: additional keyword arguments for extensibility.
        :return: List[String]
        """

        values = self.extract_elements(key=key, multi=multi, xpath=xpath, **kwargs)
        values = [value.attrib.get("href", None) for value in values if value.attrib.get("href", None)]
        urljoin_partial = partial(parse.urljoin, base_url)
        result = self.apply_partial_process(urljoin_partial, multi, values)
        return result
