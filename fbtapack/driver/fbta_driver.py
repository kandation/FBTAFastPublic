from fbtapack.driver.fbta_driver_interface import FBTADriverInterface
import requests
from bs4 import BeautifulSoup
from parsel import Selector


class FBTADriver(FBTADriverInterface):
    def __connect(self):
        return "Connect"

    def pp(self):
        Selector("<p><a>sss</a></p>")
