import threading
import multiprocessing
from testcase.api.login.login_all_api import LoginApi
from utils.config import NewConfig
from testcase.api.studyCenter.getServiceInfo_step1 import GetServiceInfo
from testcase.api.studyCenter.getTaskInfo_step2 import GetTaskInfo
from testcase.api.studyCenter.startLearning_step3 import StartLearning
from testcase.api.studyCenter.getTaskInfo_step4 import GetTaskInfo2

from testcase.api.studyCenter.words_lists.all_cihui import AllCihuiInterface
from testcase.api.studyCenter.sysListening.all_listening_interface import AllListenInterface
from testcase.api.studyCenter       .reading.all_reading_interface import AllReadInterface
from testcase.api.studyCenter.grammar.all_gra_interface import AllGraInterface
from testcase.api.studyCenter.writing.all_wrt_interface import AllWrtInterface


def finish_rid(task, common, headers, access_token):
    practiceType = task.get("practiceType")
    currStatus = task.get("currStatus")
    taskID = task.get("taskID")
    groupID = task.get("groupID")
    if currStatus == 0:
        if practiceType == 13:
            # print(taskID, groupID)
            sa = AllReadInterface(common, headers, access_token)
            all_answer = sa.get_all_sen_analysis_answer(groupID, taskID)
            # print("句子分析", all_answer)
            if len(all_answer) != 0:
                # print("a", all_answer)
                for a in all_answer:
                    # print("AAAA", a)
                    sa.post_all_sen_analysis_answer(taskID, a)
            sa_words = sa.get_sa_words(groupID, taskID, practiceType)
            for star in sa_words:
                r = sa.put_sa_words(star)
                # print(r)
            sa_done_data = sa.return_sa_done_data(groupID, practiceType)
            sa.put_sa_done(sa_done_data, taskID)
        if practiceType == 14:
            st = AllReadInterface(common, headers, access_token)
            all_answer = st.get_all_sec_train_answer(groupID, taskID)
            # print("all_answer", all_answer)
            for a in all_answer:
                if "newF" in list(a.keys()):
                    stars_3 = st.get_sec_train_words(groupID, taskID, practiceType)
                    for star in stars_3:
                        ne_re = st.put_sec_train_words(star)
                    st_data = st.get_sec_train_word_done_data(groupID, taskID, practiceType)
                    re = st.put_sec_train_words_done(taskID, st_data)
                else:
                    st.post_all_sec_train_answer(taskID, a)
        if practiceType == 15:
            at = AllReadInterface(common, headers, access_token)
            all_answer = at.get_all_art_train_answer(groupID, taskID)
            # print("文章训练", all_answer)
            for a in all_answer:
                print("A==============", a, a.get('stepType'))
                # if "newF" not in list(a.keys()):
                # while True:
                if a.get("stepType") == 3:
                    at.post_all_art_train_answer(taskID, a)
                    # break
                if a.get("stepType") == None:
                    if "newF" in list(a.keys()):
                        stars_3 = at.get_article_train_words(groupID, taskID, practiceType)
                        for star in stars_3:
                            at.put_article_train_words(star)
                        at_data = at.get_articleTrain_word_done_data(groupID, taskID, practiceType)
                        at.put_article_train_done(taskID, at_data)
                    # break
                if a.get("stepType") == 2:
                    at.post_all_art_train_answer(taskID, a)
                    # break
                if a.get("stepType") == 4:
                    at.post_all_art_train_answer(taskID, a)
                    # break

        if practiceType == 16:
            clozeTest = AllReadInterface(common, headers, access_token)
            all_answer = clozeTest.get_all_ClozeTest_answer(groupID, taskID)
            # print(all_answer)
            for a in all_answer:
                if "newF" in list(a.keys()):
                    stars_3 = clozeTest.get_ClozeTest_words(groupID, taskID, practiceType)
                    for star in stars_3:
                        clozeTest.put_ClozeTest_words(star)
                    data = clozeTest.get_ClozeTest_word_done_data(groupID, taskID, practiceType)
                    clozeTest.put_ClozeTest_words_done(taskID, data)
                if "newF" not in list(a.keys()):
                    clozeTest.post_all_clozeTest_answer(taskID, a)
        if practiceType == 17:
            cloze75 = AllReadInterface(common, headers, access_token)
            all_answer = cloze75.get_all_Cloze75_answer(groupID, taskID)
            for a in all_answer:
                if "newF" in list(a.keys()):
                    stars_3 = cloze75.get_Cloze75_words(groupID, taskID, practiceType)
                    for star in stars_3:
                        cloze75.put_Cloze75_words(star)
                    data = cloze75.get_Cloze75_word_done_data(groupID, taskID, practiceType)
                    cloze75.put_Cloze75_words_done(taskID, data)
                if "newF" not in list(a.keys()):
                    try:
                        data = cloze75.get_Cloze75_word_done_data(groupID, taskID, practiceType)
                        cloze75.put_Cloze75_words_done(taskID, data)
                    except:
                        pass
                    cloze75.post_all_cloze75_answer(taskID, a)
    else:
        pass