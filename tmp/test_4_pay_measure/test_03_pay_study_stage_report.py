import unittest
from testcase.api.login.login_all_api import LoginApi
from utils.config import NewConfig
# from testcase.api.measure.getMeasureInfo_step1 import GetMeasureInfo
from testcase.api.studyCenter.report.get_study_stage_report import GetStudyStageReport


class TestGetPayStudyStageReport(unittest.TestCase):
    def setUp(self):
        cfg_info = NewConfig()
        self.common, self.headers = cfg_info.get_info()
        t = LoginApi()
        self.access_token = t.get_access_token(self.common, self.headers)
        self.sevicesID = t.get_user_study_center(self.common, self.headers, self.access_token)
        self.report = GetStudyStageReport(self.common, self.headers, self.access_token)

    def tearDown(self):
        pass

    def test_get_study_stage_report(self):
        code, datas = self.report.get_study_stage_report(self.sevicesID)
        for k, v in datas.items():
            if k == "taskInfo":
                for k1, v1 in v.items():
                    if k1 == "taskDetails":
                        for t in v1:
                            if t.get("studyType") == "GRA":
                                self.assertEqual(t.get('score'), 0)
                            if t.get("studyType") == "LIS":
                                self.assertEqual(t.get('score'), 0)
                            else:
                                self.assertGreaterEqual(t.get('score'), 0)


if __name__ == '__main__':
    unittest.main()