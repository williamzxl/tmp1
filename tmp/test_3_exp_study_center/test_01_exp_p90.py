import unittest
from testcase.api.login.login_all_api import LoginApi
from utils.config import NewConfig
from testcase.api.main_page.experience.post_experience import PostExperience
from testcase.api.common.finish_rid import finish_rid
from testcase.api.studyCenter.getTaskInfo_step4 import GetTaskInfo2
from testcase.api.studyCenter.getServiceInfo_step1 import GetServiceInfo
from testcase.api.studyCenter.reading.all_reading_interface import GetAllArtTrainResultInfo
from utils.logger import logger


class TestExp90(unittest.TestCase):
    def setUp(self):
        cfg_info = NewConfig()
        self.common, self.headers = cfg_info.get_info(devices_name="vivox6")
        self.t = LoginApi()
        self.access_token = self.t.get_access_token(self.common, self.headers)
        self.ex_p90 = PostExperience(self.common, self.headers, self.access_token)

        self.services_info = GetServiceInfo(self.common, self.headers, self.access_token)
        self.task_info = GetTaskInfo2(self.common, self.headers, self.access_token)

        self.at_result = GetAllArtTrainResultInfo(self.common, self.headers, self.access_token)
        logger.info(self.common.get('uname'))

    def test_0_exp_90_success(self):
        response = self.ex_p90.post_experience(p="P90")
        code = response.get('code')
        datas = response.get('data')
        msg = response.get('message')
        self.assertEqual(code, 0)
        self.assertEqual(datas.get('nextAction'), 0)
        self.assertTrue(msg == "success")

    def test_1_exp_90_fail_with_P900(self):
        response = self.ex_p90.post_experience(p="P900")
        code = response.get('code')
        msg = response.get('message')
        self.assertEqual(code, 500)
        self.assertEqual(msg, '服务器错误')

    def test_2_to_finih_article_tarin(self):
        datas = self.task_info.get_all_tasks_id("P90")
        for tasks in datas:
            if tasks.get("RID"):
                for task in tasks.get("RID"):
                    taskID = task.get("taskID")
                    groupID = task.get("groupID")
                    practiceType = task.get('practiceType')
                    finish_rid(task, self.common, self.headers, self.access_token)
                    result_datas = self.at_result.get_all_art_train_result_info(groupID=groupID, taskID=taskID)
                    while result_datas.get('code') !=0:
                        finish_rid(task, self.common, self.headers, self.access_token)
                        result_datas = self.at_result.get_all_art_train_result_info(groupID=groupID, taskID=taskID)
                    if practiceType == 15:
                        result_datas = self.at_result.get_all_art_train_result_info(groupID=groupID, taskID=taskID)
                        self.assertEqual(result_datas.get('code'), 0)
                        self.assertEqual(result_datas.get('data').get('score'), 100)

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()