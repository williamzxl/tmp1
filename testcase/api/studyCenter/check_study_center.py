import threading
import multiprocessing
from testcase.api.login.login_all_api import LoginApi
from utils.config import NewConfig
from testcase.api.studyCenter.report.get_check_info import GetCheckInfo
from testcase.api.studyCenter.getServiceInfo_step1 import GetServiceInfo
from testcase.api.studyCenter.getTaskInfo_step2 import GetTaskInfo
from testcase.api.studyCenter.startLearning_step3 import StartLearning
from testcase.api.studyCenter.getTaskInfo_step4 import GetTaskInfo2

from testcase.api.common.finish_wri import finish_wri
from testcase.api.common.finish_voc import finish_voc
from testcase.api.common.finish_lis import finish_lis
from testcase.api.common.finish_rid import finish_rid
from testcase.api.common.finish_gra import finish_gra
# from utils.logger import logger


def all_task(datas, common, headers, access_token):
    print("Begin to run all  task")
    if datas.get("VOC"):
        # print("VOC --------------------------------", datas.get("VOC"))
        # pool_voc = multiprocessing.Pool(processes=10)
        # for task in datas.get("VOC")[:20]:
        #     t = threading.Thread(target=finish_voc, args=(task, common, headers, access_token))
        #     t.start()
        # print(len(datas.get("VOC")), datas.get("VOC"))
        all_tasks = datas.get("VOC")
        s_count = threading.Semaphore(5)
        for task in all_tasks:
            t = threading.Thread(target=finish_voc, args=(s_count, task, common, headers, access_token))
            t.start()
            # pool_voc.apply_async(finish_voc, args=(task, common, headers, access_token,))
        # pool_voc.close()
        # pool_voc.join()
    if datas.get("RID"):
        for task in datas.get("RID"):
            finish_rid(task, common, headers, access_token)
    if datas.get("GRA"):
        # print(datas.get("GRA"))
        for task in datas.get("GRA"):
            finish_gra(task, common, headers, access_token)
    if datas.get("LIS"):
        for task in datas.get("LIS"):
            t = threading.Thread(target=finish_lis, args=(task, common, headers, access_token))
            t.start()
    if datas.get("WRI"):
        for task in datas.get("WRI"):
            t = threading.Thread(target=finish_wri, args=(task, common, headers, access_token))
            t.start()


def finish_all_task():
    cfg_info = NewConfig()
    devices = cfg_info.get_info('vivox6')
    common, headers = cfg_info.get_info("vivox6")
    t = LoginApi()
    access_token = t.get_access_token(common, headers)
    print("access_token:".capitalize(), access_token)
    while True:
        get_chk = GetCheckInfo(common, headers, access_token)
        get_chk.get_check_info(common.get('pr').upper())
        get_chk.post_check_in(common.get('pr').upper())
        try:
            step1 = GetServiceInfo(common, headers, access_token)
            step1_ids = step1.get_service_id()
            servicesID, _, _, = step1_ids
            print("Step1 return:", step1_ids)
            step2 = GetTaskInfo(common, headers, access_token)
            step2_ids = step2.get_task_id(servicesID)
            print("step2_ids", step2_ids)
            scheduleID, _, all_currStatus = step2_ids
            print("all_currStatus", all_currStatus)
            all_currStatuses = []
            for c in all_currStatus:
                all_currStatuses.append(c.get("currStatus"))
            # if 0 not in all_currStatus:
            #     break
            print(all_currStatuses)
            step3 = StartLearning(common, headers, access_token)
            try:
                steps3_result = step3.start_to_learn(scheduleID)
            except:
                steps3_result = 1
            if steps3_result:
                step4 = GetTaskInfo2(common, headers, access_token)
                steps4_data = step4.get_all_tasks_id(servicesID)
                print("steps4_data".upper(), steps4_data)
                # from time import sleep
                # sleep(50)
                if type(steps4_data) is not tuple:
                    pool = multiprocessing.Pool(processes=4)
                    for datas in steps4_data:
                        pool.apply_async(all_task, args=(datas, common, headers, access_token))
                    pool.close()
                    pool.join()
                else:
                    break

            # return True
        except Exception as e:
            raise e
        finally:
            pass

            # return False

    # return True


if __name__ == '__main__':
    finish_all_task()
