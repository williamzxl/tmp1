from time import sleep
import re
from selenium.webdriver.common.by import By
from testcase.common.basePage.basePage import BasePage


class WordListsResultPage(BasePage):
    """
    生词表页ID
    """
    appPackage = "com.langlib.ncee"
    time_id = (By.ID, "{}:id/fragment_list_top_view_time".format(appPackage))
    grade_id = (By.ID, "{}:id/fragment_list_top_view_grade".format(appPackage))
    answer_lists_ids = (By.ID, "{}:id/fragment_word_dic_list_item_rl".format(appPackage))
    error_answers_ids = (By.ID, "{}:id/fragment_word_dic_list_item_type".format(appPackage))
    star_ids = (By.ID, "{}:id/fragment_word_profi_tv".format(appPackage))
    start1_id = (By.ID, "{}:id/popwindow_word_profi_star1".format(appPackage))
    start2_id = (By.ID, "{}:id/popwindow_word_profi_star2".format(appPackage))
    start3_id = (By.ID, "{}:id/popwindow_word_profi_star3".format(appPackage))

    words_list_done_button_id = (By.ID, "{}:id/fragment_word_profi_done_tv".format(appPackage))
    learn_center_class = (By.CLASS_NAME, "android.widget.TextView")

    def get_time(self):
        return self.getText(self.find_element(*self.time_id))

    def get_grade(self):
        return self.getText(self.find_element(*self.grade_id))

    def get_starts_nums(self):
        starts_nums = self.find_elements(*self.star_ids)
        starts = []
        for num in starts_nums:
            starts.append(self.getText(num))
        return starts

    def list_all_starts(self):
        stars_nums = self.find_elements(*self.star_ids)
        return stars_nums

    def click_star(self, ele):
        ele.click()

    def choose_star(self, star=3):
        if star == 1:
            self.find_element(*self.start1_id).click()
        if star == 2:
            self.find_element(*self.start2_id).click()
        else:
            self.find_element(*self.start3_id).click()

    def click_words_list_finish(self):
        self.find_element(*self.words_list_done_button_id).click()

    def click_learn_center(self):
        self.find_element(*self.learn_center_class).click()


class ItemLists(BasePage):
    '''
    #单词听写题目列表页面
    '''
    appPackage = "com.langlib.ncee"
    lists_ids = (By.ID, "{}:id/fragment_test_data_item_tv".format(appPackage))
    next_button_ele_id = "{}:id/fragment_word_dic_next_tv".format(appPackage)
    next_button_id = (By.ID, "{}:id/fragment_word_dic_next_tv".format(appPackage))
    finish_button_ele_id = "{}:id/fragment_word_dic_done_tv".format(appPackage)
    finish_button_id = (By.ID, "{}:id/fragment_word_dic_done_tv".format(appPackage))
    learn_center_ele_class = "android.widget.TextView"
    learn_center_class = (By.CLASS_NAME, "android.widget.TextView")

    def get_all_list_ele(self):
        eles = self.find_elements(*self.lists_ids)
        return eles

    def get_list_num(self, driver, ele):
        regx = re.compile(r'(\d)+')
        text = driver.getText(ele)
        result = regx.search(text)
        return int(result.group())

    def click_one_list(self, driver, ele):
        print("click_one_list")
        try:
            ele.click()
        except:
            ele.click()
        sleep(3)
        all_info = self.page_source()
        if self.finish_button_ele_id in all_info:
            return 2
        if '学习中心' in all_info:
            return 3
        if '生词表' in all_info and "下一步" not in all_info:
            return 4
        if '第一步:' in all_info or '生词表' in all_info:
            return 5
        if '第二步' in all_info:
            return 6
        if '第三步' in all_info:
            return 7
        if '提交' in all_info:
            return 8
        else:
            return 0


if __name__ == "__main__":
    pass