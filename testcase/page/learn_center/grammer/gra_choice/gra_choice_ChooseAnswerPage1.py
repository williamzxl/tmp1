import re
from selenium.webdriver.common.by import By
from testcase.common.allBasePageClass import AllBasePage
from utils.config import get_appPackage


class GCChooseAnswerPage1(AllBasePage):
    appPackage = get_appPackage()
    '''
    语法单选题目作答页
    '''
    gra_page_title_id = (By.ID, "{}:id/title_iframe_title_tv".format(appPackage))
    gra_choice_list_num_id = (By.ID, "{}:id/fragment_gra_choice_questinx".format(appPackage))
    # com.langlib.ncee:id/fragment_gra_choice_questinx
    gra_text_id = (By.ID, "{}:id/text_view".format(appPackage))

    gra_choice_answer_a_id = (By.ID, "{}:id/gra_choice_drag_answer_a".format(appPackage))
    gra_choice_answer_b_id = (By.ID, "{}:id/gra_choice_drag_answer_b".format(appPackage))
    gra_choice_answer_c_id = (By.ID, "{}:id/gra_choice_drag_answer_c".format(appPackage))
    gra_choice_answer_d_id = (By.ID, "{}:id/gra_choice_drag_answer_d".format(appPackage))
    gra_choice_i_dont_know_id = (By.ID, "{}:id/gra_choice_drag_answer_e".format(appPackage))

    gra_choose_sure_id = (By.ID, "{}:id/fragment_gra_choice_sure_tv".format(appPackage))

    def get_gra_choice_list_text(self):
        return self.getText(self.find_element(*self.gra_choice_list_num_id))

    def get_gra_choice_lists_nums(self):
        text = self.getText(self.find_element(*self.gra_choice_list_num_id))
        text_regx = re.compile(r'.*\((\d+)\/(\d+)')
        result = text_regx.search(text).groups()
        current_num = result[0]
        total_num = result[1]
        return current_num, total_num

    def gra_choice_choose_answer(self, answers):
        print("Answer.lower", answers.lower())
        try:
            if answers.lower() == 'a':
                self.find_element(*self.gra_choice_answer_a_id).click()
            if answers.lower() == 'b':
                self.find_element(*self.gra_choice_answer_b_id).click()
            if answers.lower() == 'c':
                self.find_element(*self.gra_choice_answer_c_id).click()
            if answers.lower() == 'd':
                self.find_element(*self.gra_choice_answer_d_id).click()
        except:
            self.find_element(*self.gra_choice_i_dont_know_id).click()

    def click_gra_choice_choose_sure(self):
        self.find_element(*self.gra_choose_sure_id).click()


if __name__ == "__main__":
    pass
