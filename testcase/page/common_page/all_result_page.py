from selenium.webdriver.common.by import By
# from testcase.page.learn_center.listening.word_trans.word_translating_resultPage2 import WTAnswerResultPage
from testcase.common.basePage.basePage import BasePage


class All_ResultPage(BasePage):
    '''
    最后一题，底部按钮为生词表
    '''
    word_list_button_id = (By.ID, "com.langlib.cee:id/fragment_short_conv_answer_word_tv")
    '''
    生词表页，底部按钮为完成
    '''
    word_profi_done_id = (By.ID, "com.langlib.cee:id/fragment_word_profi_done_tv")
    """
    结果展示页
    """
    time_id = (By.ID, "com.langlib.cee:id/fragment_list_top_view_time")
    grade_id = (By.ID, "com.langlib.cee:id/fragment_list_top_view_grade")

    answer_lists_index_ids = (By.ID, "com.langlib.cee:id/fragment_sen_fill_list_item_index")
    # com.langlib.cee: id / fragment_sen_fill_list_item_index
    words_lists_icon = (By.ID, "com.langlib.cee:id/fragment_sen_fill_list_glossary_tv")
    learn_center_class = (By.CLASS_NAME, "android.widget.TextView")

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


if __name__ == "__main__":
    pass