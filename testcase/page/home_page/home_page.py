from testcase.common.basePage.basePage import BasePage
from appium.webdriver.webdriver import By


class HomePage(BasePage):
    '''
    首页页面元素
    '''
    home_title_id = (By.ID, "com.langlib.ncee:id/fragment_home_title_tv")
    home_word_ids = (By.ID, "com.langlib.ncee:id/home_card_view_item")
    nav_home_id = (By.ID, "com.langlib.ncee:id/navigation_home")
    nav_learning_center = (By.ID, "com.langlib.ncee:id/navigation_learning_center")
    nav_my_id = (By.ID, "com.langlib.ncee:id/navigation_my")

    def open(self, noReset=None):
        self.get(30, noReset)

    '''
    首页页面操作
    '''
    def click_90(self):
        self.find_elements(*self.home_word_ids)[0].click()

    def click_120(self):
        self.find_elements(*self.home_word_ids)[1].click()

    def click_150(self):
        self.find_elements(*self.home_word_ids)[2].click()

    def click_home(self):
        self.find_element(*self.nav_home_id).click()

    def click_learning_center(self):
        self.find_element(*self.nav_learning_center).click()

    def click_my(self):
        self.find_element(*self.nav_my_id).click()


if __name__ == "__main__":
    test = HomePage()
    test.open()
    test.click_my()
    test.click_learning_center()
    test.click_home()