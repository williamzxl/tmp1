from selenium.webdriver.common.by import By
from testcase.page.learn_center.reading.sen_analysis.sen_ana_ChooseAnswerPage1 import SAChooseAnswerPage1


class SAAnswerResultPage2(SAChooseAnswerPage1):
    '''
    句子分析单句题目结果页
    '''
    appPackage = "com.langlib.ncee"
    page_titles_classes = (By.CLASS_NAME, "android.widget.TextView")
    question_num_id = (By.ID, '{}:id/sigle_tv'.format(appPackage))
    back_answer_card_id = (By.ID, '{}:id/senavaly_quest_sheetpage'.format(appPackage))
    next_sen_button_id = (By.ID, "{}:id/senavaly_quest_next_sen".format(appPackage))
    words_list_button = (By.ID, '{}:id/senavaly_quest_word'.format(appPackage))

    finish_button_id = (By.ID, "{}:id/fragment_word_dic_done_tv".format(appPackage))
    # com.langlib.ncee: id / fragment_word_trans_done_tv

    def click_play_tv(self):
        self.find_elements(*self.page_titles_classes)[0].click()

    def click_answer_card(self):
        self.find_elements(*self.page_titles_classes)[1].click()

    def click_question_num(self):
        num_eles = self.find_elements(*self.question_num_id)
        for num in num_eles:
            num.click()
            self.find_element(self.back_answer_card_id).click()

    def click_sen_ana_next_sen(self):
        self.find_element(*self.next_sen_button_id).click()

    def click_finish_button(self):
        self.find_element(*self.finish_button_id).click()

    def click_words_list_button(self):
        self.find_element(*self.words_list_button).click()



if __name__ == "__main__":
    pass