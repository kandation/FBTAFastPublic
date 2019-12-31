import io
import unittest
import unittest.mock

from fbtapack.config.fbta_config import FBTAConfig
from fbtapack.language.fbta_lang import FBTALang


class TestUserInput(unittest.TestCase):
    def test_username_is_not_empty_get_correct(self):
        setting = FBTAConfig('username')
        self.assertEqual(setting.username, 'username')

    def test_username_is_none_get_error(self):
        with self.assertRaises(ValueError) as exc:
            FBTAConfig(None)
        self.assertEqual(str(exc.exception), FBTALang.SETTING_USERNAME_NOT_EMPTY)

    def test_username_is_empty_get_error(self):
        with self.assertRaises(ValueError) as exc:
            FBTAConfig('')
        self.assertEqual(str(exc.exception), FBTALang.SETTING_USERNAME_NOT_EMPTY)

    def test_date_process_fill_day_max_get_correct_day(self):
        setting = FBTAConfig('username')
        setting.date_process = [2019, 11, 50]
        self.assertEqual(setting.date_process, [2019, 11, 30])

    def test_date_process_fill_day_min_get_correct_day(self):
        setting = FBTAConfig('username')
        setting.date_process = [2019, 2, 0]
        self.assertEqual(setting.date_process, [2019, 2, 1])

    def test_date_process_fill_year_text_get_correct(self):
        setting = FBTAConfig('username')
        setting.date_process = ['2019', 2, 0]
        self.assertEqual(setting.date_process, [2019, 2, 1])

    def test_date_process_not_fill_date_get_default(self):
        setting = FBTAConfig('username')
        self.assertEqual(setting.date_process, [1990, 1, 1])

    def test_date_process_fill_year_not_correct_get_min_unix_year(self):
        setting = FBTAConfig('username')
        setting.date_process = [1000, 2, 0]
        self.assertEqual(setting.date_process, [1971, 2, 1])

    def test_date_process_fill_year_not_correct_text_get_error(self):
        setting = FBTAConfig('username')
        with self.assertRaises(ValueError) as exc:
            setting.date_process = ['aaaa', 2, 0]
        self.assertIn('int()', str(exc.exception))


if __name__ == '__main__':
    unittest.main()
