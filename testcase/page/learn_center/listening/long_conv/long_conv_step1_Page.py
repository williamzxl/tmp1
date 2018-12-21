import re
from selenium.webdriver.common.by import By
from testcase.common.allBasePageClass import AllBasePage
from utils.config import get_appPackage


class LC_Step1_Page(AllBasePage):
    appPackage = get_appPackage()
    '''
    长对话第一步选择关键词
    '''
    page_title_id = (By.ID, "{}:id/title_iframe_title_tv".format(appPackage))
    list_num_id = (By.ID, "{}:id/fragment_word_dic_index_tv".format(appPackage))

    step_desc = (By.ID, "{}:id/fragment_short_conv_step_des".format(appPackage))
    question_num_ids = (By.ID, "{}:id/conversation_question_no".format(appPackage))

    answer_a_ids = (By.ID, "{}:id/option_a".format(appPackage))
    answer_b_ids = (By.ID, "{}:id/option_b".format(appPackage))
    answer_c_ids = (By.ID, "{}:id/option_c".format(appPackage))

    long_conv_sure_id = (By.ID, "{}:id/fragment_short_conv_sure_tv".format(appPackage))
    long_conv_next_id = (By.ID, "{}:id/fragment_short_conv_next_tv".format(appPackage))

    def get_long_conv_step_desc(self):
        return self.getText(self.find_element(*self.step_desc))

    def get_long_conv_curr_step(self):
        return self.getText(self.find_element(*self.step_desc)).split(":")[0]

    def get_long_conv_list_text(self):
        return self.getText(self.find_element(*self.list_num_id))

    def get_long_conv_lists_nums(self):
        text = self.getText(self.find_element(*self.list_num_id))
        text_regx = re.compile(r'.*\((\d+)\/(\d+)')
        result = text_regx.search(text).groups()
        current_num = result[0]
        total_num = result[1]
        return current_num, total_num

    def find_all_long_conv_mark_eles(self):
        words_eles = self.find_elements(*self.question_num_ids)
        return words_eles

    def long_conv_step1_mark_words(self, word_ele, num=1):
        num = int(num)
        # word_ele.click()
        for i in range(1, 3):
            self.find_elements(*self.answer_a_ids)[i - 1].click()
            self.find_elements(*self.answer_b_ids)[i - 1].click()
            self.find_elements(*self.answer_c_ids)[i - 1].click()
        x, y = self.getSize()
        self.swipeUp(x * 0.8, y * 0.8, 0, 200)
        if num == 4:
            for j in range(-2,0):
                self.find_elements(*self.answer_a_ids)[j].click()
                self.find_elements(*self.answer_b_ids)[j].click()
                self.find_elements(*self.answer_c_ids)[j].click()
        if num == 3:
            self.find_elements(*self.answer_a_ids)[-1].click()
            self.find_elements(*self.answer_b_ids)[-1].click()
            self.find_elements(*self.answer_c_ids)[-1].click()



    def click_long_conv_step1_sure(self):
        self.find_element(*self.long_conv_sure_id).click()

    def click_long_conv_step1_next(self):
        self.find_element(*self.long_conv_next_id).click()


if __name__ == "__main__":
    pass
