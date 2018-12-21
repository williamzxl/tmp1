import re
from time import sleep
from selenium.webdriver.common.by import By
from testcase.common.allBasePageClass import AllBasePage


class WTChooseAnswerPage1(AllBasePage):
    '''
    单词听译题目作答页
    '''
    appPackage = 'com.langlib.ncee'
    page_title_id = (By.ID, "{}:id/title_iframe_title_tv".format(appPackage))
    word_trans_list_num_id = (By.ID, "{}:id/fragment_word_trans_index_tv".format(appPackage))
            # com.langlib.ncee:id/fragment_word_trans_index_tv
    audio_icon_id = (By.ID, "{}:id/fragment_word_trans_detail_play_imagebtn".format(appPackage))

    answer_a_id = (By.ID, "{}:id/fragment_word_trans_detail_answer_a".format(appPackage))
    answer_b_id = (By.ID, "{}:id/fragment_word_trans_detail_answer_b".format(appPackage))
    answer_c_id = (By.ID, "{}:id/fragment_word_trans_detail_answer_c".format(appPackage))
    answer_d_id = (By.ID, "{}:id/fragment_word_trans_detail_answer_d".format(appPackage))
    i_dont_know_id = (By.ID, "{}:id/fragment_word_trans_detail_answer_e".format(appPackage))

    next_button_ele_id = "{}:id/fragment_word_trans_next_tv".format(appPackage)
    word_trans_next_button_id = (By.ID, "{}:id/fragment_word_trans_next_tv".format(appPackage))
    word_trans_finish_btn_id = (By.ID, "{}:id/fragment_word_trans_done_tv".format(appPackage))

    def get_trans_list_text(self):
        return self.getText(self.find_element(*self.word_trans_list_num_id))

    def get_words_trans_lists_nums(self):
        text = self.getText(self.find_element(*self.word_trans_list_num_id))
        text_regx = re.compile(r'.*\((\d+)\/(\d+)')
        result = text_regx.search(text).groups()
        current_num = result[0]
        total_num = result[1]
        return current_num, total_num

    def click_trans_audio_button(self):
        self.find_element(*self.audio_icon_id).click()
        sleep(0.5)

    def choose_answer(self, answers=None):
        if answers.lower() == 'a':
            self.find_element(*self.answer_a_id).click()
        if answers.lower() == 'b':
            self.find_element(*self.answer_b_id).click()
        if answers.lower() == 'c':
            self.find_element(*self.answer_c_id).click()
        if answers.lower() == 'd':
            self.find_element(*self.answer_d_id).click()
        else:
            self.find_element(*self.i_dont_know_id).click()

    def click_word_trans_next_button(self):
        self.find_element(*self.word_trans_next_button_id).click()
        sleep(2)

    def click_word_trans_finish_btn(self):
        self.find_element(*self.word_trans_finish_btn_id).click()


if __name__ == "__main__":
    pass
