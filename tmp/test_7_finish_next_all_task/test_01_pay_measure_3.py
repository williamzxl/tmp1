from utils.logger import logger
import datetime
import unittest
from dateutil.relativedelta import relativedelta
from testcase.api.login.login_all_api import LoginApi
from utils.config import NewConfig
from utils.config import new_all_cfgs
from testcase.backgroud.post_register import AutoToGetAccount

from testcase.backgroud.post_create_cee_services import CreateCeeServices
from testcase.api.studyCenter.open_next.connect_sql import SQL_OPR
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
from utils.logger import logger


class TestPayMeasure2(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        TestRound = 2
        cfg_info = NewConfig()
        common, headers = cfg_info.get_info(devices_name="vivox6")
        create_cee_services = CreateCeeServices()
        print(common.get('uname'))
        user_id = create_cee_services.get_user_id(common.get('uname'))
        db_obj = SQL_OPR()
        db = db_obj.connect_sql()
        pre_month = datetime.date.today() - relativedelta(months=+2, day=+1)
        # sql = "SELECT CompletedTime FROM CM_UserTest WHERE UserID='{}' AND ServiceID='{}' AND TestRound=1;".format(user_id,common.get('pr'))
        update_sql = "UPDATE CM_UserTest SET CompletedTime='{} 16:35:37' WHERE UserID='{}' AND ServiceID='{}' AND TestRound='{}';".format(pre_month,user_id,common.get('pr'),TestRound)
        print(update_sql)
        db_obj.update_sql(db, update_sql)
        # result, msg = create_cee_services.login_opa_create_cee_services(common.get('uname'), common.get('pr'))
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
        # if result == False or msg.upper() != "SUCCESS":
        #     account = AutoToGetAccount()
        #     s = account.register_account()
        #     _ = account.change_cfg_ymal(new_all_cfgs, s)
        #     logger.warning("warning************************************Change uname:",common.get('uname'))
        #     _, _ = create_cee_services.login_opa_create_cee_services(common.get('uname'), common.get('pr'))


    @classmethod
    def tearDownClass(cls):
        pass

    def test_0_assert_study_type(self):
        self.sysId, self.measureID, self.studyType = self.sys.get_sys_id(self.sevicesID)
        self.assertEqual(self.studyType, "VOC")

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
        import time
        time.sleep(30)
        self.sysId, self.measureID, self.studyType = self.sys.get_sys_id(self.sevicesID)
        print(self.studyType)
        if self.studyType == None:
            assert "message" in self.measureID.keys()
            assert "服务器错误" not in self.measureID.values()
        if self.studyType != "LIS" and self.studyType != None:
            assert len(self.studyType) == 3
        if self.studyType == "LIS":
            while self.studyType == "LIS":
                currStatus, measureId, currQuestIdx, data = self.mLis.get_measure_listen(self.sysId)
                all_right = self.mLis.get_all_right_answer(self.studyType, data)
                final_result = self.lis_postAnswer.post_measure_lis(self.measureID, all_right)
                logger.warning("666666666666666:{}".format(final_result))
                if final_result:
                    # sysId, measureID, studyType = self.sys.get_sys_id(self.sevicesID)
                    self.sysId, self.measureID, self.studyType = self.sys.get_sys_id(self.sevicesID)
                    if self.studyType != "LIS":
                        assert self.studyType != "LIS"
                        break
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
            count = 0
            while self.studyType == "RID":
                currStatus, measureId, currQuestIdx, data = self.mRead.get_measure_read(self.sysId)
                all_curr, all_right = self.mRead.get_all_right_answer(self.studyType, data)
                final_result = self.rid_postAnswer.post_measure_read(self.measureID, all_curr, all_right)
                # self.sysId, self.measureID, self.studyType = self.sys.get_sys_id(self.sevicesID)
                self.sysId, self.measureID, self.studyType = self.sys.get_sys_id(self.sevicesID)
                count += 1
                if count > 3:
                    self.assertLess(count, 2)
                if self.studyType != "RID":
                    assert self.studyType != "RID"
                    break
            else:
                _, _, studyType = self.sys.get_sys_id(self.sevicesID)
                assert studyType == "WRI"
                # assert len(all_curr) != 0 and len(all_right) != 0
                # assert len(final_result) == 2

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
            assert studyType == None and final_result == None


if __name__ == '__main__':
    unittest.main()