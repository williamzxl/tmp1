import re
from selenium.webdriver.common.by import By
from testcase.common.allBasePageClass import AllBasePage


class SC_Step1_Page(AllBasePage):
    '''
    短对话第一步选择关键词
    '''
    appPackage = "com.langlib.ncee"
    page_title_id = (By.ID, "{}:id/title_iframe_title_tv".format(appPackage))
    list_num_id = (By.ID, "{}:id/fragment_word_dic_index_tv".format(appPackage))

    step_desc = (By.ID, "{}:id/fragment_short_conv_step_des".format(appPackage))
    question_id = (By.ID, "{}:id/conversation_question".format(appPackage))
    answer_a = (By.ID, "{}:id/option_a".format(appPackage))
    answer_b = (By.ID, "{}:id/option_b".format(appPackage))
    answer_c = (By.ID, "{}:id/option_c".format(appPackage))

    short_conv_sure_id = (By.ID, "{}:id/fragment_short_conv_sure_tv".format(appPackage))
    short_conv_next_id = (By.ID, "{}:id/fragment_short_conv_next_tv".format(appPackage))

    def get_step_desc(self):
        return self.getText(self.find_element(*self.step_desc))

    def get_short_conv_list_text(self):
        return self.getText(self.find_element(*self.list_num_id))

    def get_short_conv_lists_nums(self):
        text = self.getText(self.find_element(*self.list_num_id))
        text_regx = re.compile(r'.*\((\d+)\/(\d+)')
        result = text_regx.search(text).groups()
        current_num = result[0]
        total_num = result[1]
        return current_num, total_num

    def mark_words(self):
        self.find_element(*self.question_id).click()
        self.find_element(*self.answer_a).click()
        self.find_element(*self.answer_b).click()
        self.find_element(*self.answer_c).click()

    def click_short_conv_step1_sure(self):
        self.find_element(*self.short_conv_sure_id).click()

    def click_short_conv_step1_next(self):
        self.find_element(*self.short_conv_next_id).click()


if __name__ == "__main__":
    pass
