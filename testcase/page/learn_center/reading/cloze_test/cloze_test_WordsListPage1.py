from time import sleep
from selenium.webdriver.common.by import By
from testcase.common.allBasePageClass import AllBasePage
from utils.config import get_appPackage


class CTWordsListPage1(AllBasePage):
    appPackage = get_appPackage()
    '''
    完型训练第一步：
    '''
    cloze_test_step1_words_list_id = (By.ID, "{}:id/fragment_word_profi_list_head_item_tv1".format(appPackage))
    cloze_test_step1_next_btn_id = (By.ID, "{}:id/fragment_cloze_test_detail_next_step_tv".format(appPackage))
    '''
    完型训练第二步：
    '''
    cloze_test_ques_num_id = (By.ID, '{}:id/fragment_cloze_test_detail_item_index_tv'.format(appPackage))
    cloze_test_part1_title_id = (By.ID, "{}:id/fragment_cloze_test_detail_item_index_1_tv".format(appPackage))
    cloze_test_part1_items_ids = (By.ID, "{}:id/fragment_cloze_test_detail_item_tv".format(appPackage))

    cloze_test_part2_title_id = (By.ID, "{}:id/fragment_cloze_test_detail_item_index_2_tv".format(appPackage))
    cloze_test_part2_items_a_id = (By.ID, "{}:id/fragment_cloze_test_detail_item_rbn_a".format(appPackage))
    cloze_test_part2_items_b_id = (By.ID, "{}:id/fragment_cloze_test_detail_item_rbn_b".format(appPackage))
    cloze_test_part2_items_c_id = (By.ID, "{}:id/fragment_cloze_test_detail_item_rbn_c".format(appPackage))
    cloze_test_part2_items_d_id = (By.ID, "{}:id/fragment_cloze_test_detail_item_rbn_d".format(appPackage))

    cloze_test_part2_next_btn_id = (By.ID, "{}:id/fragment_cloze_test_detail_next_quest_tv".format(appPackage))
    cloze_test_finish_btn_id = (By.ID, "{}:id/fragment_cloze_test_detail_done_tv".format(appPackage))

    def click_cloze_test_step1_next_btn(self):
        self.find_element(*self.cloze_test_step1_next_btn_id).click()

    def get_cloze_test_curr_ques(self):
        # self.getText(self.find_element(*self.step1_word_list_id))
        # print(self.getText(self.find_element(*self.cloze_test_ques_num_id)))
        curr_num = int(self.getText(self.find_element(*self.cloze_test_ques_num_id)).strip("."))
        return curr_num

    def click_cloze_test_part1_answer(self, answer=None):
        eles = self.find_elements(*self.cloze_test_part1_items_ids)
        if answer:
            for ele in eles:
                if answer in self.getText(ele):
                    ele.click()
                    break
        else:
            eles[0].click()

    def cloze_test_choose_answer(self, answers=None):
        x, y = self.getSize()
        self.swipeUp(x * 0.5, y * 0.8, 0, 100)
        sleep(5)
        if answers.lower() == 'a':
            self.find_element(*self.cloze_test_part2_items_a_id).click()
        if answers.lower() == 'b':
            self.find_element(*self.cloze_test_part2_items_b_id).click()
        if answers.lower() == 'c':
            self.find_element(*self.cloze_test_part2_items_c_id).click()
        if answers.lower() == 'd':
            self.find_element(*self.cloze_test_part2_items_d_id).click()

    def click_cloze_test_step2_next_btn(self):
        self.find_element(*self.cloze_test_part2_next_btn_id).click()

    def click_cloze_test_finish_btn(self):
        self.find_element(*self.cloze_test_finish_btn_id).click()


if __name__ == "__main__":
    pass
