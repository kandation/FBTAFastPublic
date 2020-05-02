import datetime

from fbtapack.config.fbta_config_constant import FBTAConfigConstant
from fbtapack.language.fbta_lang import FBTALang


class FBTAConfigInterface:
    def __init__(self):
        self.__username: str = ''
        self.__cluster_num: int = 10
        self.__cluster_limit: int = 50
        self.__db_prefix: str = 'fbta'
        self.__db_name: str = ''
        self.__index_renew: bool = True

        self.__dir_path: str = './'
        self.__dir_path_detail: str = ''
        self.__driver_path: str = r'./'

        self.__use_node_master_remove_on_end: bool = True
        self.__use_node_master: bool = True
        self.__use_node_master_cookie: bool = False
        self.__use_node_worker: bool = True

        self.__is_auto_db_name: bool = True
        self.__date_process: list = [1990, 1, 1]
        self.__dir_save_path: str = r'./'
        self.__file_password: str = './'

        self.__test_step: list = []
        self.__kill_driver_on_end: bool = True

    def get_project_path(self, path) -> str:
        return self.dir_path + '/' + path

    @property
    def db_prefix(self):
        if self.__db_prefix:
            return self.__db_prefix
        raise ValueError(FBTALang.SETTING_DB_PREFIX_HAS_NOT_VALUE)

    @db_prefix.setter
    def db_prefix(self, prefix: str):
        if prefix is None:
            raise ValueError(FBTALang.SETTING_DB_PREFIX_SHOULD_NOT_NONE)
        self.__db_prefix = prefix

    @property
    def kill_driver_on_end(self):
        return self.__kill_driver_on_end

    @kill_driver_on_end.setter
    def kill_driver_on_end(self, cond: bool):
        self.__kill_driver_on_end = bool(cond)

    @property
    def username(self) -> str:
        return self.__username

    @username.setter
    def username(self, username):
        if not username:
            raise ValueError(FBTALang.SETTING_USERNAME_NOT_EMPTY)
        else:
            self.__username = username

    @property
    def cluster_num(self):
        return self.__cluster_num

    @cluster_num.setter
    def cluster_num(self, num):
        if num != 10:
            print(FBTALang.SETTING_CLUSTER_RECOMMENDED)
        self.__cluster_num = int(num) if int(num) <= self.__cluster_limit else self.__cluster_limit
        try:
            self.__cluster_num = int(num) if int(num) <= self.__cluster_limit else self.__cluster_limit
        except BaseException:
            raise ValueError(FBTALang.SETTING_CLUSTER_ERROR_NOT_CORRECT_FORMAT)

    @property
    def db_name(self):
        return self.__get_db_name()

    @db_name.setter
    def db_name(self, name):
        if name == '':
            raise ValueError(FBTALang.SETTING_ERROR_DB_NAME_MUST_NOT_EMPTY)
        elif name is None:
            self.__init_db_name()
        else:
            self.__db_name = name

    def __get_db_name(self):
        if not self.__db_name:
            self.__is_auto_db_name = True
            return f'{self.db_prefix}_{self.__db_name}'
        return self.__db_name

    def _auto_init(self):
        self.__init_db_name()
        self.__init_dir_path_name()

    def __init_db_name(self):
        _dir_db_str = '%Y%m%d_%H%M'
        now_db = datetime.datetime.now().strftime(_dir_db_str)
        self.db_name = f'{self.db_prefix}_{str(now_db)}'

    @property
    def renew_index(self):
        return self.__index_renew

    @renew_index.setter
    def renew_index(self, cond=True):
        self.__index_renew = bool(cond)

    def __str__(self):
        _name = str(self.__class__.__name__)
        maxl = len(max(self.__dict__, key=len)) - (len(_name) + 1)
        s = str('')
        pp = '{: <' + str(maxl) + '} = {!r}\n'
        for i in self.__dict__:
            s += pp.format(str(i).replace('_' + _name, ''), self.__dict__.get(i))
        return s

    def __init_dir_path_name(self):
        _dir_dir_str = '%Y%m%d'

        if self.__dir_path_detail == FBTAConfigConstant.DIR_DETAIL_NEW_ALL_RUN:
            _dir_dir_str = '%Y%m%d_%H%M'

        now_dir = datetime.datetime.now().strftime(_dir_dir_str)
        now_dir = f'{self.dir_save_path}save_{now_dir}'

        self.__dir_path = now_dir

    @property
    def dir_path(self) -> str:
        if not self.__dir_path:
            self.__init_dir_path_name()
        return self.__dir_path

    @dir_path.setter
    def dir_path(self, path: str):
        if not self.__dir_path:
            self.__init_dir_path_name()

    @property
    def dir_save_path(self):
        return self.__dir_save_path

    @dir_save_path.setter
    def dir_save_path(self, dir='./'):
        if not dir:
            self.__dir_save_path = './'
        else:
            self.__dir_save_path = f'{dir[:-1]}/' if dir[-1] != '/' else dir

    @property
    def dir_path_detail(self):
        return self.__dir_path_detail

    @dir_path_detail.setter
    def dir_path_detail(self, level):
        cond = [FBTAConfigConstant.DIR_DETAIL_NEW_ON_DAY, FBTAConfigConstant.DIR_DETAIL_NEW_ALL_RUN]
        if level not in cond:
            raise ValueError(FBTALang.SETTING_ERROR_DIR_PATH_NOT_IN_LIST)
        self.__dir_path_detail = level
        self.__init_dir_path_name()

    @property
    def driver_path(self):
        return self.__driver_path

    @driver_path.setter
    def driver_path(self, m_dir='./'):
        if not m_dir:
            raise ValueError(FBTALang.SETTING_ERROR_DIR_CHROME)
        self.__driver_path = m_dir[:-1] if m_dir[-1] == '/' else m_dir

    @property
    def date_process(self):
        if self.__date_process:
            return self.__date_process
        raise ValueError(FBTALang.SETTING_ERROR_DATE_PROCESS_IS_NONE)

    @date_process.setter
    def date_process(self, date: list):
        t_date = [1990, 1, 1]
        self.__date_process = t_date if not date else self.__date_process_cal(date, t_date)

    def __date_process_cal(self, date, t_date):
        _temp_date = t_date
        from calendar import monthrange
        for i, d in enumerate(date):
            if i == 0:
                cond = len(str(d)) == 4
                year = datetime.datetime.now().year + 1
                _temp_date[i] = self.__date_process_claim(d, 1971, year, cond,
                                                          FBTALang.SETTING_ERROR_DATE_YEAR_NOT_CORRECT)

            elif i == 1:
                cond = len(str(d)) <= 2 and (0 < int(d) <= 12)
                _temp_date[i] = self.__date_process_claim(d, 1, 12, cond, FBTALang.SETTING_ERROR_DATE_MONTH_NOT_CORRECT)

            elif i == 2:
                cond = not (len(str(d)) <= 2 and (0 < int(d) <= 31))
                mr = monthrange(_temp_date[0], _temp_date[1])
                _temp_date[i] = self.__date_process_claim(d, 1, mr[1], cond,
                                                          FBTALang.SETTING_ERROR_DATE_DAY_NOT_CORRECT)

        return _temp_date

    @staticmethod
    def __date_process_claim(val, v_min, v_max, cond, error, auto=False):
        if cond or auto:
            m_val = int(val)

            # claim v_val between v_min <= v_val <= v_max
            ret = min(max(m_val, v_min), v_max)

            return ret
        if not cond and auto:
            print(error)
        else:
            raise ValueError(error)

    @property
    def cluster_limit(self):
        return self.__cluster_limit

    @cluster_limit.setter
    def cluster_limit(self, limit: int):
        try:
            self.__cluster_limit = int(limit)
        except:
            self.__cluster_limit = self.__cluster_limit if self.__cluster_limit else 15

    @property
    def test_step(self):
        return self.__test_step

    @test_step.setter
    def test_step(self, step=None):
        if step is None:
            self.__test_step = []
        elif isinstance(step, list):
            print(FBTALang.SETTING_STEP_TEST_CURRENT.format(step=step))
            self.__test_step = step
        else:
            raise ValueError(FBTALang.SETTING_ERROR_TEST_STEP_SHOULD_NOT_NONE)

    @property
    def path_password(self) -> str:
        return self.__file_password

    @path_password.setter
    def path_password(self, file):
        if not file:
            ValueError(FBTALang.SETTING_ERROR_DIR_PD)
        self.__file_password = self.__check_password_file(file)

    @property
    def password(self):
        with open(self.path_password, mode='r', encoding='utf8') as fo:
            data = fo.read()
        return data

    @staticmethod
    def __check_password_file(file=None):
        import os
        default_file = r'./password.text'
        new_file_path = default_file if not file else file
        if not os.path.exists(new_file_path):
            raise FileNotFoundError(FBTALang.SETTING_ERROR_FILE_PD_NOT_FOUND.format(file=file))
        return file

    @property
    def use_node_master(self) -> bool:
        return self.__use_node_master

    @use_node_master.setter
    def use_node_master(self, cond=True):
        self.__use_node_master = bool(cond)

    @property
    def use_node_worker(self) -> bool:
        return self.__use_node_worker

    @use_node_worker.setter
    def use_node_worker(self, cond=True):
        self.__use_node_worker = bool(cond)

    @property
    def use_node_master_load_cookie(self):
        return self.__use_node_master_cookie

    @use_node_master_load_cookie.setter
    def use_node_master_load_cookie(self, cond=True):
        self.__use_node_master_cookie = bool(cond)

    @property
    def use_node_master_remove_on_end(self) -> bool:
        return self.__use_node_master_remove_on_end

    @use_node_master_remove_on_end.setter
    def use_node_master_remove_on_end(self, cond=True):
        self.__use_node_master_remove_on_end = bool(cond)
