from selenium.webdriver.common.by import By
from testcase.common.basePage.basePage import BasePage
from utils.config import get_appPackage


class All_ResultPage(BasePage):
    appPackage = get_appPackage()
    '''
    最后一题，底部按钮为生词表
    '''
    word_list_button_id = (By.ID, "{}:id/fragment_short_conv_answer_word_tv".format(appPackage))
    '''
    生词表页，底部按钮为完成
    '''
    word_profi_done_id = (By.ID, "{}:id/fragment_word_profi_done_tv".format(appPackage))
    """
    结果展示页
    """
    time_id = (By.ID, "{}:id/fragment_list_top_view_time".format(appPackage))
    grade_id = (By.ID, "{}:id/fragment_list_top_view_grade".format(appPackage))

    answer_lists_index_ids = (By.ID, "{}:id/fragment_sen_fill_list_item_index".format(appPackage))
    # com.langlib.cee: id / fragment_sen_fill_list_item_index
    words_lists_icon = (By.ID, "{}:id/fragment_sen_fill_list_glossary_tv".format(appPackage))
    learn_center_class = (By.CLASS_NAME, "android.widget.TextView")

    learn_card_ele_id = "{}:id/view_punch_clock_punch_btn".format(appPackage)
    learn_card_id = (By.ID, "{}:id/view_punch_clock_punch_btn".format(appPackage))
    learn_card_close_id = (By.ID, "{}:id/view_punch_clock_close".format(appPackage))

    '''
    最后一题，底部按钮为生词表
    '''
    def click_words_list_button(self):
        self.find_element(*self.word_list_button_id).click()

    '''
    生词表页，底部按钮为完成
    '''
    def click_word_finish_button(self):
        self.find_element(*self.word_profi_done_id).click()

    """
    结果展示页
    """
    def get_time(self):
        return self.getText(self.find_element(*self.time_id))

    def get_grade(self):
        return self.getText(self.find_element(*self.grade_id))

    def get_item_lists_index(self):
        eles = self.find_elements(*self.answer_lists_index_ids)
        return eles

    def click_result_num_index(self, ele):
        ele.click()

    def click_word_icon(self):
        self.find_element(*self.words_lists_icon).click()

    def click_learn_center(self):
        self.find_element(*self.learn_center_class).click()

    def click_learn_card_btn(self):
        if self.learn_card_ele_id in self.page_source():
            self.find_element(*self.learn_card_id).click()
        else:
            pass

    def click_learn_card_close_btn(self):
        print('"学习打卡" in self.page_source()', "学习打卡" in self.page_source())
        if "学习打卡" in self.page_source():
            self.find_element(*self.learn_card_close_id).click()
            return 1
        else:
            return 0

    def click_learn_card_task_btn(self):
        from time import sleep
        print('"学习打卡" in self.page_source()', "学习打卡" in self.page_source())
        self.find_element(*self.learn_card_id).click()
        sleep(2)


if __name__ == "__main__":
    pass