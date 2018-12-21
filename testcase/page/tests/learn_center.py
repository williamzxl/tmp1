from testcase.page.tests.all_task.all_task_funcs import *
from testcase.page.learn_center.all_class import AllPage
from testcase.page.study_center.study_center_main_page import StudyCenter
from testcase.interface.all_interface import AllInterface
from testcase.interface.study_center.get_study_center_serverID import GetTaskGroupNum


class HomeWork(AllInterface):
    pass


class HomeWork1(StudyCenter, AllPage, GetTaskGroupNum):
    pass


if __name__ == '__main__':
    while True:
        try:
            main1()
        except:
            pass
        finally:
            pass

























