import unittest
from testcase.api.login.login_all_api import LoginApi
from utils.config import NewConfig
from utils.config import new_all_cfgs
from testcase.backgroud.post_register import AutoToGetAccount
from utils.log import logger
from utils.config import LOG_PATH

class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with open(r"{}\test.log".format(LOG_PATH), 'w') as fp:
            fp.truncate()
        account = AutoToGetAccount()
        s = account.register_account()
        result = account.change_cfg_ymal(new_all_cfgs, s)
        if result:
            cfg_info = NewConfig()
            cls.common, cls.headers = cfg_info.get_info()
            cls.t = LoginApi()
            logger.info("Uname:{}".format(cls.common.get("uname")))
            # print("User_name",cls.common.get("uname"))
        else:
            # stop = TestLogin()
            # stop.tearDownClass()
            pass

    def test_0_login_success(self):
        # print("Sucess", self.common)
        u'''{}'''.format(self.common.get("uname"))
        print("User_name", self.common.get("uname"))
        access_token = self.t.get_access_token(self.common, self.headers)
        result = self.t.check_uname(self.common, self.headers, access_token)
        # print(result)
        logger.info(self.common.get('uname').split("@")[0])
        logger.info("test_0_login_success:{}".format(access_token))
        assert self.common.get('uname').split("@")[0] in result

    def test_login_fail_with_wrong_uname_right_pwd(self):
        # print(self.common)
        self.common.update({'uname':self.common.get('uname') + "1"})
        access_token = self.t.get_access_token(self.common, self.headers)
        # result = self.t.check_uname(self.common, self.headers, access_token)
        logger.info("test_login_fail_with_wrong_uname_right_pwd:{}".format(access_token))
        assert access_token == None

    def test_login_fail_with_right_uname_wrong_pwd(self):
        # print(self.common)
        self.common.update({'pwd': str(self.common.get('pwd')) + "1"})
        access_token = self.t.get_access_token(self.common, self.headers)
        # result = self.t.check_uname(self.common, self.headers, access_token)
        logger.info("test_login_fail_with_right_uname_wrong_pwd:{}".format(access_token))
        assert access_token == None

    def test_login_fail_with_wrong_uname_wrong_pwd(self):
        # print(self.common)
        self.common.update({'uname': self.common.get('uname') + "1"})
        self.common.update({'pwd': str(self.common.get('pwd')) + "1"})
        access_token = self.t.get_access_token(self.common, self.headers)
        logger.info("test_login_fail_with_wrong_uname_wrong_pwd：{}".format(access_token))
        assert access_token == None

    @classmethod
    def tearDownClass(cls):
        pass


if __name__ == '__main__':
    unittest.main()