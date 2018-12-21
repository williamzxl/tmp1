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


def finish_voc(s_count,task, common, headers, access_token):
    s_count.acquire()
    practiceType = task.get("practiceType")
    currStatus = task.get("currStatus")
    taskID = task.get("taskID")
    groupID = task.get("groupID")
    # # if currStatus == 0:
    if currStatus == 1:
        print("Finish VOC", practiceType, currStatus, taskID, groupID)
        pass
    else:
        words_post = AllCihuiInterface(common, headers, access_token)
        data_1 = words_post.get_word_list_words(groupID, taskID, practiceType)
        for star in data_1:
            words_post.put_wordsList_3star(star)
            # t = threading.Thread(target=words_post.put_wordsList_3star, args=(star,))
            # t.start()
        d = {"taskID": taskID, "groupID": groupID}
        words_post.put_all_words_lists_done(d)

    s_count.release()