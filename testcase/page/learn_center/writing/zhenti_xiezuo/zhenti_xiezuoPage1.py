from selenium.webdriver.common.by import By
from testcase.common.allBasePageClass import AllBasePage
from utils.config import get_appPackage


class ZXFillAnswerPage1(AllBasePage):
    appPackage = get_appPackage()
    '''
    真题写作作答页
    '''
    start_to_answer_btn_id = (By.ID, "{}:id/fragment_error_find_question_start_tv".format(appPackage))
    # com.langlib.ncee: id / fragment_error_find_question_start_tv

    zhenti_xiezuo_time_id = (By.ID, "{}:id/fragment_writing_detail_time".format(appPackage))
    zhenti_xiezuo_words_count_id = (By.ID, "{}:id/fragment_writing_detail_count".format(appPackage))
    zhenti_xiezuo_edit_id = (By.ID, "{}:id/fragment_writing_detail_edittext".format(appPackage))

    zhenti_xiezuo_zancun_id = (By.ID, "{}:id/frame_writing_bottom_btn_cache_tv".format(appPackage))
    zhenti_xiezuo_submit_id = (By.ID, "{}:id/frame_writing_bottom_btn_handin_tv".format(appPackage))

    def click_zhenti_xiezuo_start_to_answer_btn(self):
        self.find_element(*self.start_to_answer_btn_id).click()

    def get_zhenti_xiezuo_time(self):
        return self.getText(self.find_element(*self.zhenti_xiezuo_time_id))

    def get_zhenti_xiezuo_words_count(self):
        return self.getText(self.find_element(*self.zhenti_xiezuo_words_count_id))

    def fill_zhenti_xiezuo_answer(self, answer):
        ele = self.find_element(*self.zhenti_xiezuo_edit_id)
        ele.send_keys(str(answer))
        self.hideKeyboard()

    def click_zhenti_xiezuo_zancun_btn(self):
        self.find_element(*self.zhenti_xiezuo_zancun_id).click()

    def click_zhenti_xiezuo_submit_id(self):
        self.find_element(*self.zhenti_xiezuo_submit_id).click()


if __name__ == "__main__":
    pass
