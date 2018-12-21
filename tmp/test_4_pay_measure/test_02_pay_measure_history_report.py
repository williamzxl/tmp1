import unittest
from testcase.api.login.login_all_api import LoginApi
from utils.config import NewConfig
from testcase.api.studyCenter.report.get_measure_history_report import GetMeasureHistoryReport


class TestGetPayMeasureHistoryReport(unittest.TestCase):
    def setUp(self):
        cfg_info = NewConfig()
        self.common, self.headers = cfg_info.get_info()
        t = LoginApi()
        self.access_token = t.get_access_token(self.common, self.headers)
        self.sevicesID = t.get_user_study_center(self.common, self.headers, self.access_token)
        # get_measure_id = GetMeasureInfo(self.common, self.headers, self.access_token)
        # _, self.mID, _ = get_measure_id.get_sys_id(self.sevicesID)
        self.report = GetMeasureHistoryReport(self.common, self.headers, self.access_token)

    def tearDown(self):
        pass

    def test_get_measure_history_report(self):
        code, datas = self.report.get_measure_history_report(self.sevicesID)
        for k, v in datas.items():
            if k == "shareEnabled":
                self.assertTrue(v)
            if k == "measureList":
                self.assertGreaterEqual(v[0].get('measureScore'), 49)
                self.assertLess(v[0].get('measureScore'), 59)
            if k == "avgMeasureInterval":
                self.assertEqual(v, 0)


if __name__ == '__main__':
    unittest.main()