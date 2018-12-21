import unittest
from testcase.api.login.login_all_api import LoginApi
from utils.config import NewConfig
from utils.logger import logger
from testcase.api.measure.getMeasureInfo_step1 import GetMeasureInfo
from testcase.api.measure.words.getMeasureWords_step1 import GetMeasureWords
from testcase.api.measure.words.postmeasureWords_step2 import PostMeasureWords
from testcase.api.measure.grammer.getMeasureGra_step1 import GetMeasureGra
from testcase.api.measure.grammer.postmeasureGra_step2 import PostMeasureGra
from testcase.api.measure.listen.getMeasureListen_step1 import GetMeasureListen
from testcase.api.measure.listen.postmeasureListen_step2 import PostMeasureLis
from testcase.api.measure.read.getMeasureRead_step1 import GetMeasureRead
from testcase.api.measure.read.postmeasureRead_step2 import PostMeasureRead
from testcase.api.measure.write.getMeasureWrite_step1 import GetMeasureWrite
from testcase.api.measure.write.postmeasureWrite_step2 import PostMeasureWrite


class TestMeasure(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cfg_info = NewConfig()
        common, headers = cfg_info.get_info(devices_name="vivox6")
        t = LoginApi()
        cls.access_token = t.get_access_token(common, headers)
        cls.sevicesID = t.get_user_study_center(common, headers, cls.access_token)
        cls.sys = GetMeasureInfo(common, headers, cls.access_token)

        cls.mWords = GetMeasureWords(common, headers, cls.access_token)
        cls.word_postAnswer = PostMeasureWords(common, headers, cls.access_token)

        cls.mGra = GetMeasureGra(common, headers, cls.access_token)
        cls.gra_postAnswer = PostMeasureGra(common, headers, cls.access_token)

        cls.mLis = GetMeasureListen(common, headers, cls.access_token)
        cls.lis_postAnswer = PostMeasureLis(common, headers, cls.access_token)

        cls.mRead = GetMeasureRead(common, headers, cls.access_token)
        cls.rid_postAnswer = PostMeasureRead(common, headers, cls.access_token)

        cls.mWrite = GetMeasureWrite(common, headers, cls.access_token)
        cls.wri_postAnswer = PostMeasureWrite(common, headers, cls.access_token)

        logger.info(common.get('uname'))

    @classmethod
    def tearDownClass(cls):
        pass

    def test_1_words(self):
        self.sysId, self.measureID, self.studyType = self.sys.get_sys_id(self.sevicesID)
        if self.studyType == None:
            assert "message" in self.measureID.keys()
            assert "服务器错误" not in self.measureID.values()
        if self.studyType != "VOC" and self.studyType != None:
            assert len(self.studyType) == 3
        if self.studyType == "VOC":
            currStatus, measureId, currQuestIdx, data = self.mWords.get_measure_words(self.sysId)
            all_curr, all_right = self.mWords.get_all_right_answer(self.studyType, data)
            assert len(all_curr) != 0 and len(all_right) !=0
            final_result = self.word_postAnswer.post_measure_words(self.measureID, all_curr, all_right)
            assert len(final_result) == 2

    def test_2_grammer(self):
        self.sysId, self.measureID, self.studyType = self.sys.get_sys_id(self.sevicesID)
        if self.studyType == None:
            assert "message" in self.measureID.keys()
            assert "服务器错误" not in self.measureID.values()
        if self.studyType != "GRA" and self.studyType != None:
            assert len(self.studyType) == 3
        if self.studyType == "GRA":
            currStatus, measureId, currQuestIdx, data = self.mGra.get_measure_gra(self.sysId)
            all_curr, all_right = self.mGra.get_all_right_answer(self.studyType, data)
            assert len(all_curr) != 0 and len(all_right) != 0
            final_result = self.gra_postAnswer.post_measure_gra(self.measureID, all_curr, all_right)
            assert len(final_result) == 2

    def test_3_listen(self):
        self.sysId, self.measureID, self.studyType = self.sys.get_sys_id(self.sevicesID)
        if self.studyType == None:
            assert "message" in self.measureID.keys()
            assert "服务器错误" not in self.measureID.values()
        if self.studyType != "LIS" and self.studyType != None:
            assert len(self.studyType) == 3
        if self.studyType == "LIS":
            studyType = "LIS"
            while studyType == "LIS":
                currStatus, measureId, currQuestIdx, data = self.mLis.get_measure_listen(self.sysId)
                all_right = self.mLis.get_all_right_answer(self.studyType, data)
                final_result = self.lis_postAnswer.post_measure_lis(self.measureID, all_right)
                if final_result:
                    sysId, measureID, studyType = self.sys.get_sys_id(self.sevicesID)
                    # print("66666666666666", studyType)
            else:
                _, _, studyType = self.sys.get_sys_id(self.sevicesID)
                assert studyType == "RID"

    def test_4_read(self):
        self.sysId, self.measureID, self.studyType = self.sys.get_sys_id(self.sevicesID)
        if self.studyType == None:
            assert "message" in self.measureID.keys()
        if self.studyType != "RID" and self.studyType != None:
            assert len(self.studyType) == 3
        if self.studyType == "RID":
            currStatus, measureId, currQuestIdx, data = self.mRead.get_measure_read(self.sysId)
            all_curr, all_right = self.mRead.get_all_right_answer(self.studyType, data)
            assert len(all_curr) != 0 and len(all_right) != 0
            final_result = self.rid_postAnswer.post_measure_read(self.measureID, all_curr, all_right)
            assert len(final_result) == 2

    def test_5_write(self):
        self.sysId, self.measureID, self.studyType = self.sys.get_sys_id(self.sevicesID)
        if self.studyType == None:
            assert "message" in self.measureID.keys()
            assert "服务器错误" not in self.measureID.values()
        if self.studyType != "WRI" and self.studyType != None:
            assert len(self.studyType) == 3
        if self.studyType == "WRI":
            currStatus, measureId, data = self.mWrite.get_measure_write(self.sysId)
            all_right = self.mWrite.get_all_right_answer(self.studyType, data)
            final_result = self.wri_postAnswer.post_measure_Write(self.measureID, all_right)
            _, _, studyType = self.sys.get_sys_id(self.sevicesID)
            assert studyType == "WRI" and final_result == None


if __name__ == '__main__':
    unittest.main()