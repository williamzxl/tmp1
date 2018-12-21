from selenium.webdriver.common.by import By
from testcase.page.learn_center.grammer.gra_choice.gra_choice_ChooseAnswerPage1 import GCChooseAnswerPage1
from utils.config import get_appPackage


class GCAnswerResultPage2(GCChooseAnswerPage1):
    appPackage = get_appPackage()
    '''
    语法单选题目判定页
    '''
    answer_type_ele_id = "{}:id/gra_choice_drag_answer_type".format(appPackage)
    answer_type_id = (By.ID, "{}:id/gra_choice_drag_answer_type".format(appPackage))
    gra_choice_next_button_id = (By.ID, "{}:id/fragment_gra_choice_next_tv".format(appPackage))
    gra_choice_words_list_button_id = (By.ID, "{}:id/fragment_gra_choice_word_tv".format(appPackage))

    def get_answer_type(self,driver):
        if self.answer_type_ele_id in driver.page_source():
            return self.getText(self.find_element(*self.answer_type_id))

    def click_gra_choice_next_button(self):
        self.find_element(*self.gra_choice_next_button_id).click()

    def click_gra_choice_words_list_button(self):
        self.find_element(*self.gra_choice_words_list_button_id).click()


if __name__ == "__main__":
    pass