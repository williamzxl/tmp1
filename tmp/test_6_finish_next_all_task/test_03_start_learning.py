import unittest
from testcase.api.login.login_all_api import LoginApi
from utils.config import NewConfig
from testcase.api.main_page.experience.post_experience import PostExperience
from testcase.api.common.finish_rid import finish_rid
from testcase.api.studyCenter.getTaskInfo_step4 import GetTaskInfo2
from testcase.api.studyCenter.getServiceInfo_step1 import GetServiceInfo
from testcase.api.studyCenter.reading.all_reading_interface import GetAllArtTrainResultInfo
from testcase.api.studyCenter.report.put_to_start_learing import StartLearning
from utils.logger import logger


class TestStartLearing(unittest.TestCase):
    def setUp(self):
        cfg_info = NewConfig()
        self.common, self.headers = cfg_info.get_info(devices_name="vivox6")
        self.t = LoginApi()
        self.access_token = self.t.get_access_token(self.common, self.headers)
        # self.ex_p90 = PostExperience(self.common, self.headers, self.access_token)
        self.sevicesID = self.t.get_user_study_center(self.common, self.headers, self.access_token)
        self.services_info = GetServiceInfo(self.common, self.headers, self.access_token)
        self.task_info = GetTaskInfo2(self.common, self.headers, self.access_token)

        # m = GetServiceInfo(self.common, self.headers, self.access_token)
        # _, self.measureID, _ = m.get_service_id()

        self.sch_id = GetTaskInfo2(self.common, self.headers, self.access_token)

        self.start = StartLearning(self.common, self.headers, self.access_token)

        logger.info(self.common.get('uname'))

    def test_0_start_learing(self):
        result = self.sch_id.get_all_tasks_id(self.sevicesID)
        print(result)
        if len(result) == 1:
            logger.info("*******************:已经开始学习了。")
        else:
            code, msg = self.start.star_learning(result[1])
            self.assertEqual(code, 0)
            self.assertEqual(msg.upper(), "SUCCESS")

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()