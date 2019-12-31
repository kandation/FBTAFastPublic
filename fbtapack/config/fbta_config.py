from fbtapack.config.fbta_config_constant import FBTAConfigConstant
from fbtapack.config.fbta_config_interface import FBTAConfigInterface


class FBTAConfig(FBTAConfigInterface):

    def __init__(self, username):
        FBTAConfigInterface.__init__(self)
        self.username = username

        # Node
        self.start_master_browser = True
        self.cluster_limit = 50
        self.cluster_num = 4
        self.renew_index = False

        # Database
        self.db_prefix = 'fbta'
        self.db_name = None

        # Setting
        self.renew_login = False
        self.date_process = None
        self.use_nodeMaster = True
        self.use_nodeMaster_loadCookie = False
        self.use_nodeMaster_remove_on_end = True

        # Directory
        self.dir_driver_path = r'.'
        self.dir_save_path = r'./save/'
        self.dir_cookies = r'./'
        self.dir_path = r'./'
        self.dir_path_detail = FBTAConfigConstant.DIR_DETAIL_NEW_ON_DAY

        # Testing
        self.test_step = []

        # Information
        self.__user_info = {}
        self._auto_init()

        self.kill_driver_on_end = True

    @property
    def user_information(self) -> dict:
        return self.__user_info

    def set_user_information(self, key, val):
        self.__user_info[key] = val
