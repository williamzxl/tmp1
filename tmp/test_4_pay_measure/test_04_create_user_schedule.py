import time
import unittest
from testcase.api.login.login_all_api import LoginApi
from utils.config import NewConfig
from testcase.api.studyCenter.getServiceInfo_step1 import GetServiceInfo
from testcase.api.studyCenter.report.post_create_user_schedule import CreateUserSchedule
from testcase.api.studyCenter.getTaskInfo_step4 import GetTaskInfo2
from utils.logger import logger


class TestCreateUserSchedule(unittest.TestCase):
    def setUp(self):
        cfg_info = NewConfig()
        self.common, self.headers = cfg_info.get_info()
        t = LoginApi()
        self.access_token = t.get_access_token(self.common, self.headers)
        self.sevicesID = t.get_user_study_center(self.common, self.headers, self.access_token)

        m = GetServiceInfo(self.common, self.headers, self.access_token)
        _, self.measureID, _ = m.get_service_id()

        self.c = CreateUserSchedule(self.common, self.headers, self.access_token)

        self.all_task = GetTaskInfo2(self.common, self.headers, self.access_token)

    def tearDown(self):
        pass

    def test_0_create_user_schedule_succeed(self):
        code, msg = self.c.create_user_schedule(self.sevicesID, self.measureID, 3)
        time.sleep(10)
        all_ta,_ = self.all_task.get_all_tasks_id(self.sevicesID)
        self.assertEqual(int(all_ta),90)
        self.assertEqual(code, 0)
        self.assertEqual(msg, None)

    def test_1_create_user_schedule_not_succeed(self):
        code, msg = self.c.create_user_schedule(self.sevicesID, self.measureID, 3)
        logger.info("Create USER Schedule Fail: code is {}, msg is {}".format(code, msg))
        self.assertEqual(code, 11003)
        self.assertEqual(msg,None)


if __name__ == '__main__':
    unittest.main()