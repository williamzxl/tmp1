from selenium.webdriver.common.by import By
from testcase.page.learn_center.grammer.gra_fill.gra_fill_WordsListPage1 import GFWordsListPage1
from utils.config import get_appPackage


class GFAnswerResultPage2(GFWordsListPage1):
    appPackage = get_appPackage()
    '''
    语法填空题目作答页
    '''
    answer_fill_ele_class = "android.widget.EditText"
    answer_fill_classes = (By.CLASS_NAME, "android.widget.EditText")
    to_check_answer = (By.ID, "".format(appPackage))
    submit_id = (By.ID, "{}:id/fragment_gra_fill_canto_commit_tv".format(appPackage))
    done_id = (By.ID, "{}:id/fragment_gra_fill_canto_done_tv".format(appPackage))

    '''
    语法填空答案解析页
    '''
    item_text_class = (By.CLASS_NAME, "android.widget.TextView")
    done_all_id = (By.ID, "{}:id/fragment_gra_fill_canto_done_all_tv".format(appPackage))

    def gra_fill_fill_answer(self, driver, answers, nums=10):
        fill_eles1 = self.find_elements(*self.answer_fill_classes)
        if nums <= len(fill_eles1):
            for fill, answer in zip(fill_eles1[:int(nums)], answers[:(int(nums))]):
                self.hideKeyboard()
                fill.send_keys(answer)
                self.hideKeyboard()
        if nums > len(fill_eles1):
            for fill1, answer1 in zip(fill_eles1[:(len(fill_eles1))], answers[:(len(fill_eles1))]):
                self.hideKeyboard()
                fill1.send_keys(answer1)
                self.hideKeyboard()
            x, y = driver.getSize()
            driver.swipeUp(x * 0.5, y * 0.8, 0, 200)
            fill_eles2 = self.find_elements(*self.answer_fill_classes)
            for fill2, answer2 in zip(fill_eles2[(len(fill_eles1)-10):], answers[(len(fill_eles1)-10):]):
                self.hideKeyboard()
                fill2.send_keys(answer2)
                self.hideKeyboard()

    def click_gra_fill_submit(self):
        self.find_element(*self.submit_id).click()

    def click_to_check_answer(self):
        self.find_element(*self.to_check_answer).click()

    def click_gra_fill_finish_button(self):
        self.find_element(*self.done_id).click()

    '''
    答案解析页
    '''
    def click_gra_fill_play(self):
        self.find_elements(*self.item_text_class)[0].click()

    def click_gra_fill_conv_text(self):
        self.find_elements(*self.item_text_class)[1].click()

    def click_gra_fill_conv_answer(self):
        self.find_elements(*self.item_text_class)[2].click()

    def click_gra_fill_finish_all(self):
        self.find_element(*self.done_all_id).click()

if __name__ == "__main__":
    pass