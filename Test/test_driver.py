import unittest

from fbtapack.driver.fbta_driver import FBTADriver


class TestDriver(unittest.TestCase):
    def test_crate(self):
        FBTADriver()



if __name__ == '__main__':
    unittest.main()
