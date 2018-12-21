from appium.webdriver.webdriver import By
from testcase.page.home_page.prod_intr_page import ProdPage
from utils.config import get_appPackage


class StudyCenter(ProdPage):
    appPackage = get_appPackage()
    '''
    学习中心页面元素
    '''

    '''
    课程名称及切换
    '''
    course_name_id = (By.ID, "{}:id/fragment_course_task_name".format(appPackage))
    course_list_close_id = (By.ID, "{}:id/dialog_class_view_close_btn".format(appPackage))
    course_lists_ids = (By.ID, "{}:id/fragment_class_item_rl".format(appPackage))
    pre_for_test_id = (By.ID, "{}:id/fragment_class_item_type_tv".format(appPackage))
    '''
    备考倒计时
    '''
    exam_days_id = (By.ID, "{}:id/view_exam_count_down".format(appPackage))

    '''
    学习报告，测评历史，打卡记录
    '''
    study_report_id = (By.ID, "{}:id/view_learing_center_study_report_rl".format(appPackage))
    test_history_id = (By.ID, "{}:id/view_learing_center_mearsure_history_rl".format(appPackage))
    card_record_id = (By.ID, "{}:id/view_learing_center_card_record_rl".format(appPackage))

    '''
    任务数及总任务数
    '''
    task_index_lists_id = (By.ID, "{}:id/fragment_course_task_index".format(appPackage))
    task_all_lists_close_btn_id = (By.ID, "{}:id/dialog_class_view_close_btn".format(appPackage))
    task_all_lists_ids = (By.ID, "{}:id/fragment_exercise_item_tv".format(appPackage))

    '''
    我的练习，查看更多
    '''
    # my_ex_id = (By.ID, '{}:id/view_course_task_my_exercise_tv'.format(appPackage))
    my_ex_id = (By.ID, "{}:id/view_course_task_my_course_tv".format(appPackage))
    # com.langlib.ncee: id / view_course_task_my_course_tv
    check_more_id = (By.ID, "{}:id/view_course_task_my_exercise_more_tv".format(appPackage))

    '''
    任务列表
    '''
    exercise_list_ids = (By.ID, "{}:id/exercise_list_item_tv".format(appPackage))

    '''
    学习中心页动作
    '''
    def return_learning_center_page_source(self):
        return self.page_source

    def click_course_name(self):
        self.find_element(*self.course_name_id).click()

    def click_course_list_close(self):
        self.find_element(*self.course_list_close_id).click()

    def click_fir_to_learn(self):
        self.find_elements(*self.course_lists_ids)[0].click()

    def click_sec_to_learn(self):
        self.find_elements(*self.course_lists_ids)[1].click()

    def click_thi_to_learn(self):
        self.find_elements(*self.course_lists_ids)[2].click()

    def click_study_report(self):
        self.find_element(*self.study_report_id).click()

    def click_test_history(self):
        self.find_element(*self.test_history_id).click()

    def click_card_record(self):
        self.find_element(*self.card_record_id).click()

    def click_task_index(self):
        self.find_element(*self.task_index_lists_id).click()

    def get_current_total_task(self):
        return self.getText(self.find_element(*self.task_index_lists_id))

    def click_task_view_close(self):
        self.find_element(*self.task_all_lists_close_btn_id).click()

    def click_task_all_lists_index(self, index):
        self.find_elements(*self.task_all_lists_ids)[int(index) - 1].click()

    def click_my_exc_check_more(self):
        self.find_element(*self.check_more_id).click()

    def return_all_test_ele(self):
        # exercies = []
        eles =  self.find_elements(*self.exercise_list_ids)
        # for ele in eles:
        #     exercies.append(self.getText(ele))
        return eles

    def get_my_ex_loc(self):
        ele = self.find_element(*self.my_ex_id)
        # print(self.getEleSize(ele))
        # print(self.getEleLocation(ele))
        x = self.getEleLocation(ele).get('x')
        y = self.getEleLocation(ele).get('y')
        # print(x, y)
        # w,h = self.getEleLocation(ele)
        # print(x, y, w, h)
        return int(x), int(y)


if __name__ == '__main__':
    pass