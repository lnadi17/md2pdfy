import PyChromeDevTools
import base64
import os
from urllib.parse import urlparse, urljoin
from urllib.request import pathname2url
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class Pdfy:
    def __init__(self, executable_path=None, debug_port=9222, options=None):
        if options is None:
            self.options = {"paperWidth": 8.5,
                            "paperHeight": 11,
                            "marginTop": 0,
                            "marginBottom": 0,
                            "marginLeft": 0,
                            "marginRight": 0,
                            "printBackground": True,
                            "preferCSSPageSize": False,
                            "scale": 1,
                            "landscape": False}
        else:
            self.options = options

        chrome_options = Options()
        chrome_options.add_argument("--remote-debugging-port=" + str(debug_port))
        chrome_options.add_argument("--headless")

        webdriver_params = {
            'chrome_options': chrome_options
        }
        if executable_path:
            webdriver_params['executable_path'] = executable_path

        self.driver = webdriver.Chrome(**webdriver_params)
        self.chrome = PyChromeDevTools.ChromeInterface(port=debug_port)
        self.chrome.Page.enable()

    def __del__(self):
        try:
            self.driver.quit()
        except:
            pass

    def __resolve_path(self, html_path):
        if self.__is_url(html_path):
            return html_path
        elif os.path.isabs(html_path):
            return self.__path_to_url(html_path)
        abs_path = os.path.abspath(html_path)
        return self.__path_to_url(abs_path)

    def __is_url(self, url):
        return urlparse(url).scheme != ""

    def __path_to_url(self, path):
        return urljoin('file:', pathname2url(path))

    def html_to_pdf(self, html_path, pdf_path=None):
        self.chrome.Page.navigate(url=self.__resolve_path(html_path))
        self.chrome.wait_event("Page.frameStoppedLoading", timeout=60)
        pdf_data = self.chrome.Page.printToPDF(**self.options)[0]['result']['data']
        if pdf_path is None:
            return pdf_data
        else:
            with open(pdf_path, "wb") as f:
                f.write(base64.b64decode(pdf_data))
