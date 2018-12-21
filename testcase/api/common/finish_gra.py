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


def finish_gra(task, common, headers, access_token):
    if task.get('currStatus') == 0 or task.get('currStatus') == 1:
        practiceType = task.get("practiceType")
        currStatus = task.get("currStatus")
        taskID = task.get("taskID")
        groupID = task.get("groupID")
        # print(taskID, groupID,practiceType)
        if currStatus == 0:
            if practiceType == 6:
                mul_choice = AllGraInterface(common, headers, access_token)
                mul_choice_answers = mul_choice.get_all_mul_choice_answer(groupID, taskID)
                # print(mul_choice_answers)
                for answer in mul_choice_answers:
                    post_mul_choice_answer = mul_choice.post_all_mul_choice_answer(taskID, answer)
                mul_choice_words = mul_choice.get_mul_choice_words(groupID, taskID, practiceType)
                mc_words = mul_choice.get_mul_choice_words(groupID, taskID, practiceType)
                for star in mc_words:
                    r = mul_choice.put_mul_choice_words(star)
                mul_choice_done_data = mul_choice.get_mul_choice_done_data(groupID, practiceType)
                mul_choice.put_mul_choice_done(mul_choice_done_data, taskID)
            if practiceType == 7:
                graFill = AllGraInterface(common, headers, access_token)
                all_answer = graFill.get_all_gra_fill_answer(groupID, taskID)
                print(all_answer)
                for a in all_answer:
                    if "newF" in list(a.keys()):
                        stars_3 = graFill.get_gra_fill_words(groupID, taskID, practiceType)
                        for star in stars_3:
                            graFill.put_gra_fill_words(star)
                        data = graFill.get_gra_fill_word_done_data(groupID, taskID, practiceType)
                        graFill.put_gra_fill_words_done(taskID, data)
                    if "newF" not in list(a.keys()):
                        graFill.post_all_gra_fill_answer(taskID, a)
            if practiceType == 8:
                error_find = AllGraInterface(common, headers, access_token)
                user_answers, sysID = error_find.get_all_error_find_answer(groupID, taskID)
                error_find.post_all_error_find_answer(taskID, groupID, user_answers, sysID)
        if currStatus == 1:
            if practiceType == 6:
                mul_choice = AllGraInterface(common, headers, access_token)
                mul_choice_words = mul_choice.get_mul_choice_words(groupID, taskID, practiceType)
                mc_words = mul_choice.get_mul_choice_words(groupID, taskID, practiceType)
                for star in mc_words:
                    if star.get("oldF") == 3:
                        pass
                    else:
                        r = mul_choice.put_mul_choice_words(star)