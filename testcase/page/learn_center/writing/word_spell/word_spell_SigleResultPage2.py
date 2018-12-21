from selenium.webdriver.common.by import By
from testcase.page.learn_center.writing.word_spell.word_spell_answerPage1 import WSFillAnswerPage1
from utils.config import get_appPackage


class WSSingleResultPage2(WSFillAnswerPage1):
    appPackage = get_appPackage()
    '''
    单词拼写题目判定页
    '''
    EN_answer_id = (By.ID, "{}:id/fragment_word_spell_word".format(appPackage))
    audio_icon_id = (By.ID, "{}:id/fragment_word_spell_word_phsymbol".format(appPackage))
    word_CN_id = (By.ID, "{}:id/fragment_word_spell_word_translate".format(appPackage))
    ws_next_button_id = (By.ID, "{}:id/fragment_word_spell_next_tv".format(appPackage))
    test = 'com.langlib.ncee:id/fragment_word_spell_next_tv'
    ws_finish_button_id = (By.ID, "{}:id/fragment_word_spell_done_tv".format(appPackage))

    def get_ws_single_result_EN(self):
        return self.getText(self.find_element(*self.EN_answer_id))

    def get_ws_single_result_CN(self):
        return self.getText(self.find_element(*self.word_CN_id))

    def click_word_spell_single_result_audio(self):
        self.find_element(*self.audio_icon_id).click()

    def click_word_spell_next_button(self):
        # print("hhhhhhhhhhhhhh",self.test in self.page_source())
        self.find_element(*self.ws_next_button_id).click()

    def click_word_spell_finish_button(self):
        self.find_element(*self.ws_finish_button_id).click()


if __name__ == "__main__":
    pass