import os
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
from testcase.api.studyCenter.check_study_center import finish_all_task, all_task
from testcase.api.studyCenter.report.get_study_stage_report import GetStudyStageReport


class TestStartToFinishLearing(unittest.TestCase):
    def setUp(self):
        result = True
        finish_all_task()
        if result:
            cfg_info = NewConfig()
            self.common, self.headers = cfg_info.get_info(devices_name="vivox6")
            self.t = LoginApi()
            self.access_token = self.t.get_access_token(self.common, self.headers)
            self.sevicesID = self.t.get_user_study_center(self.common, self.headers, self.access_token)
            self.services_info = GetServiceInfo(self.common, self.headers, self.access_token)
            self.task_info = GetTaskInfo2(self.common, self.headers, self.access_token)
            self.sch_id = GetTaskInfo2(self.common, self.headers, self.access_token)
            self.start = StartLearning(self.common, self.headers, self.access_token)
            logger.info(self.common.get('uname'))

            self.report = GetStudyStageReport(self.common, self.headers, self.access_token)
        else:
            pass

    def test_0_check_finish_all_task(self):
        code, datas = self.report.get_study_stage_report(self.sevicesID)
        for k, v in datas.items():
            if k == "taskInfo":
                for k1, v1 in v.items():
                    if k1 == "taskDetails":
                        for t in v1:
                            if t.get("studyType") == "GRA":
                                self.assertEqual(t.get('score'), 100)
                            if t.get("studyType") == "LIS":
                                self.assertEqual(t.get('score'), 100)
                            if t.get("studyType") == "RID":
                                self.assertEqual(t.get('score'), 100)
                            else:
                                self.assertGreaterEqual(t.get('score'), 95)

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()