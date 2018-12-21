from appium.webdriver.webdriver import By
from testcase.page.home_page.home_page import HomePage


class ProdPage(HomePage):
    '''
    产品详情页页面元素
    '''

    prod_back_btn_id = (By.ID, "com.langlib.ncee:id/title_iframe_back_btn")
    prod_title_id = (By.ID, "com.langlib.ncee:id/title_iframe_title_tv")
    page_change_classes = (By.CLASS_NAME, "android.widget.TextView")

    price_id = (By.ID, "com.langlib.ncee:id/buttom_tela_money")
    for_free_id = (By.ID, "com.langlib.ncee:id/buttom_tela_free")
    buy_id = (By.ID, "com.langlib.ncee:id/buttom_tela_buy")

    course_type_ids = (By.ID, "com.langlib.ncee:id/course_type_tv")
    course_type_cancel_id = (By.ID, "com.langlib.ncee:id/course_type_tv")

    def click_prod_back_btn(self):
        self.find_element(*self.prod_back_btn_id).click()

    def click_prod_feature(self):
        self.find_elements(*self.page_change_classes)[0].click()

    def click_class_content(self):
        self.find_elements(*self.page_change_classes)[1].click()

    def click_buy_to_know(self):
        self.find_elements(*self.page_change_classes)[2].click()

    def get_price(self):
        return self.getText(self.find_element(*self.price_id))

    def click_for_free_btn(self):
        self.find_element(*self.for_free_id).click()

    def click_to_buy(self):
        self.find_element(*self.buy_id).click()

    def choose_90_to_buy(self):
        self.find_elements(*self.course_type_ids)[0].click()

    def get_90_course_name(self):
        return self.getText(self.find_elements(*self.course_type_ids)[0])

    def choose_120_to_buy(self):
        self.find_elements(*self.course_type_ids)[1].click()

    def get_120_course_name(self):
        return self.getText(self.find_elements(*self.course_type_ids)[1])

    def choose_150_to_buy(self):
        self.find_elements(*self.course_type_ids)[2].click()

    def get_150_course_name(self):
        return self.getText(self.find_elements(*self.course_type_ids)[2])

    def click_cancel_to_choose(self):
        self.find_element(*self.course_type_cancel_id).click()


if __name__ == '__main__':
    # pass
    test = ProdPage()
    test.open()
    # test.click_learning_center()
    test.click_90()
    test.click_prod_back_btn()
    test.click_120()
    test.click_to_buy()
    test.choose_90_to_buy()