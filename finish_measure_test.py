from testcase.api.login.login_all_api import LoginApi
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
from utils.config import NewConfig


if __name__ == '__main__':
    cfg_info = NewConfig()
    devices = cfg_info.get_info('vivox6')
    common, headers = cfg_info.get_info("vivox6")
    # print("COMMON", common)
    # {'uname': 't002@t.com', 'pwd': 111111, 'loginUrl': 'https://proxy.langlib.com', 'loginProxy': 'proxy.langlib.com', 'baseUrl': 'https://appncee.langlib.com', 'baseProxy': 'appncee.langlib.com'}
    t = LoginApi()
    access_token = t.get_access_token(common, headers)
    # print(access_token)
    result = t.check_uname(common, headers, access_token)
    # print(result)
    sevicesID = t.get_user_study_center(common, headers, access_token)
    print(sevicesID)
    sys = GetMeasureInfo(common, headers, access_token)
    print("sys", sys)
    sysId, measureID, studyType = sys.get_sys_id(sevicesID)
    if studyType == None:
        pass
    else:
        if studyType == "VOC":
            mWords = GetMeasureWords(common,headers, access_token)
            currStatus, measureId, currQuestIdx, data = mWords.get_measure_words(sysId)
            all_curr, all_right = mWords.get_all_right_answer(studyType, data)
            print(all_curr, len(all_curr))
            print(all_right, len(all_right))
            postAnswer = PostMeasureWords(common, headers, access_token)
            final_result = postAnswer.post_measure_words(measureID, all_curr, all_right)
            if final_result:
                print("len(final_result)", len(final_result))
                sysId, measureID, studyType = sys.get_sys_id(sevicesID)
        if studyType == "GRA":
            mGra = GetMeasureGra(common, headers, access_token)
            currStatus, measureId, currQuestIdx, data = mGra.get_measure_gra(sysId)
            all_curr, all_right = mGra.get_all_right_answer(studyType, data)
            print(all_curr, len(all_curr))
            print(all_right, len(all_right))
            postAnswer = PostMeasureGra(common, headers, access_token)
            final_result = postAnswer.post_measure_gra(measureID, all_curr, all_right)
            if final_result:
                print("len(final_result)", len(final_result))
                sysId, measureID, studyType = sys.get_sys_id(sevicesID)
        while studyType == "LIS":
            mLis = GetMeasureListen(common, headers, access_token)
            currStatus, measureId, currQuestIdx, data = mLis.get_measure_listen(sysId)
            all_right = mLis.get_all_right_answer(studyType, data)
            print(all_right, len(all_right))
            postAnswer = PostMeasureLis(common, headers, access_token)
            final_result = postAnswer.post_measure_lis(measureID, all_right)
            if final_result:
                print("len(final_result)", len(final_result))
                sysId, measureID, studyType = sys.get_sys_id(sevicesID)
        if studyType == "RID":
            mRead = GetMeasureRead(common, headers, access_token)
            currStatus, measureId, currQuestIdx, data = mRead.get_measure_read(sysId)
            all_curr, all_right = mRead.get_all_right_answer(studyType, data)
            print(all_curr, len(all_curr))
            print(all_right, len(all_right))
            postAnswer = PostMeasureRead(common, headers, access_token)
            final_result = postAnswer.post_measure_read(measureID, all_curr, all_right)
            if final_result:
                print("len(final_result)", len(final_result))
                sysId, measureID, studyType = sys.get_sys_id(sevicesID)
        if studyType == "WRI":
            mWrite = GetMeasureWrite(common, headers, access_token)
            currStatus, measureId, data = mWrite.get_measure_write(sysId)
            all_right = mWrite.get_all_right_answer(studyType, data)
            print(all_right, len(all_right))
            postAnswer = PostMeasureWrite(common, headers, access_token)
            final_result = postAnswer.post_measure_Write(measureID, all_right)
            if final_result:
                print("len(final_result)", len(final_result))
                sysId, measureID, studyType = sys.get_sys_id(sevicesID)
    print("Finish")
