from lxml import html

from scrapqd.gql_parser.exception import InvalidParserObjectError


class LXMLParser:
    """This is concerete implementation for lxml gql_parser to parse html text."""

    def __init__(self, raw_html=None, html_tree=None):
        """creates instance for LXML Parser

        :param raw_html: plain html string
        :param html_tree: html nodes from the gql_parser
        :raises InvalidParserObjectError: raises exception when system is not able to create parser object
                using given html string or bytes
        """
        if html_tree is not None and raw_html is None:
            raw_html = html.tostring(html_tree)
            html_tree = None
        if raw_html and html_tree is None:
            if isinstance(raw_html, str):
                try:
                    raw_html = bytes(raw_html, "utf-8")
                except UnicodeEncodeError:
                    raw_html = bytes(raw_html, "latin-1")
            html_tree = html.fromstring(raw_html)

        if html_tree is None:
            raise InvalidParserObjectError()

        self.html = html_tree

    def xpath_element(self, element, xpath=None, **kwargs):
        """extract target node using xpath from given html element.

        :param element: html element.
        :param xpath: xpath to locate the elements.
        :param kwargs: additional keyword arguments for extensibility.
        :return: List[HTMLElement]
        """
        target_element = element.xpath(xpath) if element is not None and xpath else None
        return target_element

    def xpath_text(self, element, xpath, **kwargs):
        """Extracts text for given xpath.

        :param element: html element.
        :param xpath: xpath to locate the elements.
        :param kwargs: additional keyword arguments for extensibility.
        :return: List[String]
        """
        target_element = self.xpath_element(element, xpath=xpath, **kwargs)
        result = []
        for t in target_element:
            value = t.text_content() if isinstance(t, html.HtmlElement) else t
            result.append(value)
        return result

    def extract_element_source_text(self, element):
        """Extracts source html content

        :param element: html element.
        :return: String
        """
        txt_bytes = html.tostring(element)
        return txt_bytes.decode()

    def extract_text(self, xpath, **kwargs):
        """Extracts text content from element.

        :param xpath: xpath to locate the elements.
        :param kwargs: additional keyword arguments for extensibility.
        :return: List[String]
        """
        return self.xpath_text(self.html, xpath=xpath, **kwargs)

    def extract_elements(self, xpath, **kwargs):
        """Extracts nodes from given html element.

        :param xpath: xpath to locate the elements.
        :param kwargs: additional keyword arguments for extensibility.
        :return: List[HTMLElement]
        """
        return self.xpath_element(element=self.html, xpath=xpath, **kwargs)

    def extract_attr(self, xpath, **kwargs):
        """Extracts attributes from the html element.

        :param xpath: xpath to locate the elements.
        :param kwargs: additional keyword arguments for extensibility.
        :return: List[Dict]
        """
        result = []
        target_element = self.xpath_element(self.html, xpath=xpath, **kwargs)
        for t in target_element:
            value = dict(t.attrib) if isinstance(t, html.HtmlElement) else t
            result.append(value)
        return result

    def extract_form_input(self, xpath, **kwargs):
        """Extracts form inputs using given xpath. Method expects xpath to locate form node.

        :param xpath: xpath to locate the elements.
        :param kwargs: additional keyword arguments for extensibility.
        :return: List[Dict]
        """
        forms = self.xpath_element(self.html, xpath=xpath, **kwargs)
        form_inputs = []
        for form in forms:
            if isinstance(form, html.HtmlElement):
                input_ = self.xpath_element(form, xpath=".//input", multi=True)
                form_inputs.append(input_)
        return form_inputs
