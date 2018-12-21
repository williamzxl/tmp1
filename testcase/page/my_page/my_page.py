from testcase.common.basePage.basePage import BasePage
from testcase.page.home_page.all_home_page import AllHomePage
from appium.webdriver.webdriver import By


class MyPage(AllHomePage, BasePage):
    '''
    我的页面元素
    '''
    my_name_id = (By.ID, "com.langlib.ncee:id/fragment_my_app_name")
    my_photo_id = (By.ID, "com.langlib.ncee:id/fragment_my_user_photo")
    my_wechat_id = (By.ID, "com.langlib.ncee:id/fragment_my_wechat_group")
    my_learn_report_id = (By.ID, "com.langlib.ncee:id/fragment_my_learning_report")
    my_learn_history_id = (By.ID, "com.langlib.ncee:id/fragment_my_measure_history")
    my_hit_card_id = (By.ID, "com.langlib.ncee:id/fragment_my_punch_clock")
    my_off_line_center_id = (By.ID, "com.langlib.ncee:id/fragment_my_off_line_center")
    my_setting_id = (By.ID, "com.langlib.ncee:id/fragment_my_setting")

    '''
    我的页面操作
    '''
    def get_my_name(self):
        return self.getText(self.find_element(*self.my_name_id))

    def click_my_name(self):
        self.find_element(*self.my_name_id).click()

    def click_photo(self):
        self.find_element(*self.my_photo_id).click()

    def click_my_wechat(self):
        self.find_element(*self.my_wechat_id).click()

    def click_my_learn_report(self):
        self.find_element(*self.my_learn_report_id).click()

    def click_my_learn_history(self):
        self.find_element(*self.my_learn_history_id).click()

    def click_my_hit_card(self):
        self.find_element(*self.my_hit_card_id).click()

    def click_my_off_line(self):
        self.find_element(*self.my_off_line_center_id).click()

    def click_my_setting(self):
        self.find_element(*self.my_setting_id).click()


if __name__ == "__main__":
    test = MyPage()
    test.open()
    test.click_my()
    test.click_my_setting()
    test.click_prod_back_btn()