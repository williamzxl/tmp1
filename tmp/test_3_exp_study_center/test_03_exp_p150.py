import unittest
from testcase.api.login.login_all_api import LoginApi
from utils.config import NewConfig
from testcase.api.main_page.experience.post_experience import PostExperience
from testcase.api.common.finish_wri import finish_wri
from testcase.api.studyCenter.getTaskInfo_step4 import GetTaskInfo2
from testcase.api.studyCenter.getServiceInfo_step1 import GetServiceInfo
from testcase.api.studyCenter.writing.all_wrt_interface import GetAllZhentiXiezuoResultInfo



class TestExp150(unittest.TestCase):
    def setUp(self):
        self.pr = "P150"
        cfg_info = NewConfig()
        self.common, self.headers = cfg_info.get_info(devices_name="vivox6")
        self.t = LoginApi()
        self.access_token = self.t.get_access_token(self.common, self.headers)
        self.ex_pr = PostExperience(self.common, self.headers, self.access_token)

        self.services_info = GetServiceInfo(self.common, self.headers, self.access_token)
        self.task_info = GetTaskInfo2(self.common, self.headers, self.access_token)

        self.zt_result = GetAllZhentiXiezuoResultInfo(self.common, self.headers, self.access_token)

    def test_0_exp_150_success(self):
        response = self.ex_pr.post_experience(p=self.pr)
        code = response.get('code')
        datas = response.get('data')
        msg = response.get('message')
        self.assertEqual(code, 0)
        self.assertEqual(datas.get('nextAction'), 0)
        self.assertTrue(msg == "success")

    def test_1_exp_150_fail_with_P900(self):
        response = self.ex_pr.post_experience(p=self.pr + "0")
        code = response.get('code')
        msg = response.get('message')
        self.assertEqual(code, 500)
        self.assertEqual(msg, '服务器错误')

    def test_2_to_finih_zhenti_xiezuo(self):
        datas = self.task_info.get_all_tasks_id(self.pr)
        for tasks in datas:
            if tasks.get("WRI"):
                for task in tasks.get("WRI"):
                    taskID = task.get("taskID")
                    groupID = task.get("groupID")
                    practiceType = task.get('practiceType')
                    finish_wri(task, self.common, self.headers, self.access_token)
                    if practiceType == 12:
                        result_datas = self.zt_result.get_all_zhenti_xiezuo_result_info(groupID=groupID, taskID=taskID)
                        self.assertEqual(result_datas.get('code'), 0)
                        self.assertGreaterEqual(result_datas.get('data').get('questGuide')[0].get('score'), 10)
                        self.assertLess(result_datas.get('data').get('questGuide')[0].get('score'), 60)
                        self.assertGreater(len(result_datas.get('data').get('questGuide')[0].get('suggestions')[0].get('paragraph')), 1)
                        self.assertGreater(len(result_datas.get('data').get('questGuide')[0].get('suggestions')[0].get('suggestions')), 1)

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()