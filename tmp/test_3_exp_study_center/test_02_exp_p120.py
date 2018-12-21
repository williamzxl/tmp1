import unittest
from testcase.api.login.login_all_api import LoginApi
from utils.config import NewConfig
from testcase.api.main_page.experience.post_experience import PostExperience
from testcase.api.common.finish_rid import finish_rid
from testcase.api.common.finish_gra import finish_gra
from testcase.api.studyCenter.getTaskInfo_step4 import GetTaskInfo2
from testcase.api.studyCenter.getServiceInfo_step1 import GetServiceInfo
from testcase.api.studyCenter.reading.all_reading_interface import GetAllArtTrainResultInfo
from testcase.api.studyCenter.reading.all_reading_interface import GetAllSenAnaResultInfo
from testcase.api.studyCenter.grammar.all_gra_interface import GetAllErrorFindResultInfo


class TestExp120(unittest.TestCase):
    def setUp(self):
        cfg_info = NewConfig()
        self.common, self.headers = cfg_info.get_info(devices_name="vivox6")
        self.t = LoginApi()
        self.access_token = self.t.get_access_token(self.common, self.headers)
        self.ex_p120 = PostExperience(self.common, self.headers, self.access_token)

        self.services_info = GetServiceInfo(self.common, self.headers, self.access_token)
        self.task_info = GetTaskInfo2(self.common, self.headers, self.access_token)

        self.at_result = GetAllArtTrainResultInfo(self.common, self.headers, self.access_token)
        self.sa_result = GetAllSenAnaResultInfo(self.common, self.headers, self.access_token)
        self.ef_result = GetAllErrorFindResultInfo(self.common, self.headers, self.access_token)

    def test_0_exp_120_success(self):
        response = self.ex_p120.post_experience(p="P120")
        code = response.get('code')
        datas = response.get('data')
        msg = response.get('message')
        self.assertEqual(code, 0)
        self.assertEqual(datas.get('nextAction'), 0)
        self.assertTrue(msg == "success")

    def test_1_exp_120_fail_with_P900(self):
        response = self.ex_p120.post_experience(p="P900")
        code = response.get('code')
        msg = response.get('message')
        self.assertEqual(code, 500)
        self.assertEqual(msg, '服务器错误')

    def test_2_to_finih_sa(self):
        datas = self.task_info.get_all_tasks_id("P120")
        for tasks in datas:
            if tasks.get("RID"):
                for task in tasks.get("RID"):
                    taskID = task.get("taskID")
                    groupID = task.get("groupID")
                    practiceType = task.get('practiceType')
                    finish_rid(task, self.common, self.headers, self.access_token)
                    if practiceType == 13:
                        result_datas = self.sa_result.get_all_sen_ana_result_info(groupID=groupID, taskID=taskID)
                        self.assertEqual(result_datas.get('code'), 0)
                        self.assertEqual(result_datas.get('data').get('score'), 100)
                    if practiceType == 15:
                        result_datas = self.at_result.get_all_art_train_result_info(groupID=groupID, taskID=taskID)
                        self.assertEqual(result_datas.get('code'), 0)
                        self.assertEqual(result_datas.get('data').get('score'), 100)
                        self.assertEqual(result_datas.get('data').get('questGuide'), 0)

    def test_3_to_finih_error_find(self):
        datas = self.task_info.get_all_tasks_id("P120")
        for tasks in datas:
            if tasks.get("GRA"):
                for task in tasks.get("GRA"):
                    taskID = task.get("taskID")
                    groupID = task.get("groupID")
                    practiceType = task.get('practiceType')
                    finish_gra(task, self.common, self.headers, self.access_token)
                    if practiceType == 8:
                        result_datas = self.ef_result.get_all_error_find_result_info(taskID=taskID, groupID=groupID)
                        score = (result_datas.get('data').get('questGuide')[0].get("avgScore"))
                        self.assertEqual(result_datas.get('code'), 0)
                        self.assertEqual(result_datas.get('message').upper(),"SUCCESS")
                        self.assertEqual(score, 100)

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()