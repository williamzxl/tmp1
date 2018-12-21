import unittest
from testcase.api.login.login_all_api import LoginApi
from utils.config import NewConfig
from testcase.api.measure.getMeasureInfo_step1 import GetMeasureInfo
from testcase.api.measure.report.get_measure_result import GetMeasureResult
from utils.logger import logger


class TestGetMeasureResult(unittest.TestCase):
    def setUp(self):
        cfg_info = NewConfig()
        self.common, self.headers = cfg_info.get_info()
        t = LoginApi()
        self.access_token = t.get_access_token(self.common, self.headers)
        self.sevicesID = t.get_user_study_center(self.common, self.headers, self.access_token)
        get_measure_id = GetMeasureInfo(self.common, self.headers, self.access_token)
        _, self.mID, _ = get_measure_id.get_sys_id(self.sevicesID)
        self.report = GetMeasureResult(self.common, self.headers, self.access_token)
        logger.info(self.common.get("uname"))


    def tearDown(self):
        pass

    def test_get_measure_result(self):
        code, datas = self.report.get_measure_result(self.mID)
        for k, v in datas.get('measureReport').items():
            if k == "measureScoreInfo":
                # print("----------measureScoreInfo-------------", v.get('score'))
                self.assertGreaterEqual(v.get('score'), 49)
                self.assertLess(v.get('score'), 60)
        self.assertEqual(code, 0)


if __name__ == '__main__':
    unittest.main()