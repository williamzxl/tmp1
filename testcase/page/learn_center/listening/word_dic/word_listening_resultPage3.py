from selenium.webdriver.common.by import By
from testcase.page.learn_center.listening.word_dic.word_listening_answerPage2 import WLFillAnswerPage2


class WLAllAnswerPage(WLFillAnswerPage2):
    '''
    单词听写题目判定页
    '''
    appPackage = 'com.langlib.ncee'
    answer_id = (By.ID, "{}:id/fragment_word_dic_word".format(appPackage))
    audio_icon_id = (By.ID, "{}:id/fragment_word_dic_word_phsymbol".format(appPackage))
    word_CN_id = (By.ID, "{}:id/fragment_word_dic_word_translate".format(appPackage))
    next_button_id = (By.ID, "{}:id/fragment_word_dic_next_tv".format(appPackage))
    finish_button_id = (By.ID, "{}:id/fragment_word_dic_done_tv".format(appPackage))

    def click_next_button(self):
        self.find_element(*self.next_button_id).click()

    def click_finish_button(self):
        self.find_element(*self.finish_button_id).click()


if __name__ == "__main__":
    pass