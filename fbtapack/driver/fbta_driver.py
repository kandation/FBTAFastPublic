import dis
from time import time

import requests
from bs4 import BeautifulSoup
from parsel import Selector
from fbtapack.LogStream.fbta_log import log

from fbtapack.driver.fbta_driver_header import FBTADriverHeader
from fbtapack.language.fbta_lang import FBTALang


class FBTADriver:
    def __init__(self):
        self.__session: requests.Session = requests.Session()
        self.__respond: requests.Response = None
        self.__soup: BeautifulSoup = None
        self.__selector: Selector = None
        self.__request_timeout = None
        self.__raw_url = 'init'
        self.__header = self.__session.headers

        self.__path_cookie: str = ''

    def start_session(self):
        self.add_cookie_from_node_master()

    def set_cookie_path(self, path):
        self.__path_cookie = path

    @property
    def session(self) -> requests.Session:
        return self.__session

    @property
    def respond(self):
        return self.__respond

    @property
    def headers(self):
        return self.session.headers

    @headers.setter
    def headers(self, header):
        self.session.headers.update(header)

    def set_header_chrome(self):
        self.headers = FBTADriverHeader.CHROME_HEADER

    @property
    def path_cookie(self):
        if not self.__path_cookie:
            raise ValueError(FBTALang.DRIVER_ERROR_COOKIE_PATH)
        return self.__path_cookie

    @path_cookie.setter
    def path_cookie(self, path):
        if not path:
            raise ValueError(FBTALang.DRIVER_ERROR_COOKIE_PATH_SET)
        self.__path_cookie = path

    def get(self, url, stream=False, show_url=True) -> requests.Response:
        self.__raw_url = url
        if show_url:
            log(f'>> :Driver: stream={stream} get {url} ')
        self.__respond = self.__session.get(url, headers=self.__header, stream=stream, allow_redirects=True)
        if self.__respond.encoding is not None:
            self.__soup = BeautifulSoup(self.__respond.content, 'lxml')
            self.__selector = Selector(self.__respond.text)
        else:
            self.__soup = None
            self.__selector = None

        return self.__respond

    def get_stream(self, url):
        self.__respond = self.__session.get(url, allow_redirects=True)

    @property
    def raw_url(self):
        return self.__raw_url

    @property
    def current_url(self):
        if self.__respond:
            return self.__respond.url
        return ''

    @property
    def page_source(self):
        return str(self.__respond.content, encoding=self.__respond.encoding)

    def get_title(self):
        return self.__selector.css('title::text').get()

    @property
    def title(self):
        return self.get_title()

    def refresh(self):
        self.get(self.current_url)

    def add_cookie_from_node_master(self):
        if self.__settings.use_nodeMaster:
            request_cookies_browser = self.__node_master.browser.driver.get_cookies()
            for c in request_cookies_browser:
                self._session.cookies.set(c['name'], c['value'])
        else:
            print(':FastDriver: Cannot Load Cookie Frome master becuse has not NodeMaster')

    def add_cookie(self, cookie):
        for key in cookie:
            self.__session.cookies.set(str(key), str(cookie[key]))

    def get_cookies(self):
        ret = []
        for cookie in self.__session.cookies:
            ret.append({'name': cookie.name,
                        'path': cookie.path,
                        'value': cookie.value
                        })
        return ret

    def quit(self):
        self.__session.close()

    def delete_all_cookies(self):
        self.__session.cookies.clear()

    @property
    def selector(self) -> Selector:
        return self.__selector



