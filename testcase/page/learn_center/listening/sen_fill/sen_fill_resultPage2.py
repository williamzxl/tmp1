from selenium.webdriver.common.by import By
from testcase.page.learn_center.listening.sen_fill.senfill_FillAnswerPage import SFFillAnswerPage1


class SFAnswerResultPage2(SFFillAnswerPage1):
    '''
    句子填充题目判定页
    '''
    appPackage = "com.langlib.ncee"
    audio_icon_id = (By.ID, "{}:id/fragment_sen_fill_sen_des".format(appPackage))
    en_sen = (By.ID, "{}:id/fragment_sen_fill_sen".format(appPackage))
    cn_sen = (By.ID, "{}:id/fragment_sen_fill_word_translate".format(appPackage))
    user_en_sen = (By.ID, "{}:id/text_view".format(appPackage))
    next_button_ele_id = "{}:id/fragment_sen_fill_next_tv".format(appPackage)
    next_button_id = (By.ID, "{}:id/fragment_sen_fill_next_tv".format(appPackage))

    words_list_ele_id = "{}:id/fragment_sen_fill_word_tv".format(appPackage)
    sen_fill_word_list_button_id = (By.ID, "{}:id/fragment_sen_fill_word_tv".format(appPackage))
    back_all_result_page_id = (By.ID, "{}:id/fragment_sen_fill_next_tv".format(appPackage))
    back_all_result_page_id2 = (By.ID, "{}:id/fragment_word_profi_to_anal_tv".format(appPackage))
    sen_fill_word_list_btn_id = (By.ID, "{}:id/senavaly_quest_word".format(appPackage))

    def click_next_button(self):
        self.find_element(*self.next_button_id).click()

    def click_sen_fill_words_list_button(self):
        self.find_element(*self.sen_fill_word_list_btn_id).click()

    def click_back_all_result_page(self):
        try:
            self.find_element(*self.back_all_result_page_id).click()
        except:
            self.find_element(*self.back_all_result_page_id2).click()

    def click_sen_fill_words_list_btn(self):
        self.find_element(*self.sen_fill_word_list_button_id).click()


if __name__ == "__main__":
    pass