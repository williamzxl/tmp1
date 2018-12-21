from selenium.webdriver.common.by import By
from testcase.page.learn_center.listening.word_trans.word_translating_ChooseAnswerPage import WTChooseAnswerPage1


class WTAnswerResultPage2(WTChooseAnswerPage1):
    '''
    单词听译题目判定页
    '''
    appPackage = 'com.langlib.ncee'
    answer_id = (By.ID, "{}:id/fragment_word_trans_word".format(appPackage))
    audio_icon_id = (By.ID, "{}:id/fragment_word_trans_word_phsymbol".format(appPackage))
    next_button_id = (By.ID, "{}:id/fragment_word_trans_next_tv".format(appPackage))
    finish_button_id = (By.ID, "{}:id/fragment_word_trans_done_tv".format(appPackage))

    def click_next_button(self):
        self.find_element(*self.next_button_id).click()

    def click_finish_button(self):
        self.find_element(*self.finish_button_id).click()


if __name__ == "__main__":
    pass