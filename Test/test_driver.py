import unittest

from fbtapack.driver.fbta_driver import FBTADriver
import json


class TestDriver(unittest.TestCase):
    def test_connect_should_be_get_code_200(self):
        d = FBTADriver()
        d.get('https://postman-echo.com/get?test=1')
        self.assertEqual(d.respond.status_code, 200)
        d.quit()

    def test_GET_method_should_be_get_content(self):
        d = FBTADriver()
        d.get('https://postman-echo.com/get?test=15592')
        param = json.loads(d.respond.text).get('args')
        self.assertEqual(param.get('test'), '15592')
        d.quit()

    def test_set_chrome_headers_should_be_get_content_with_chrome_headers(self):
        d = FBTADriver()
        d.set_header_chrome()
        d.get('https://postman-echo.com/get?test=15592')
        param = json.loads(d.respond.text).get('args')
        self.assertEqual(param.get('test'), '15592')
        d.quit()

    def test_set_cookie_path_by_correct_should_be_path(self):
        d = FBTADriver()
        d.set_cookie_path(r'./ResourceGitIgnore/cookies/fbta_cookies_old.pkl')
        self.assertEqual(d.path_cookie, './ResourceGitIgnore/cookies/fbta_cookies_old.pkl')
        d.quit()


if __name__ == '__main__':
    unittest.main()
