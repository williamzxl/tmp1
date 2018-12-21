from appium.webdriver.webdriver import By
from testcase.page.my_page.my_page import MyPage


class PersonalPage(MyPage):
    my_per_info_title_id = (By.ID, "com.langlib.ncee:id/account_title_layout_title")
    my_per_info_back_btn_id = (By.ID, "com.langlib.ncee:id/account_title_layout_left_btn")

    # 个人信息页
    my_per_info_photo_id = (By.ID, "com.langlib.ncee:id/activity_personal_center_photo_rl")
    take_picture_id = (By.ID, "com.langlib.ncee:id/dialog_take_picture")
    photo_album_id = (By.ID, "com.langlib.ncee:id/dialog_photo_album")
    picture_cancel_id = (By.ID, "com.langlib.ncee:id/dialog_select_picture_canel")

    my_per_info_name_id = (By.ID, "com.langlib.ncee:id/activity_personal_center_name")
    my_per_info_name_title_id = (By.ID, "com.langlib.ncee:id/account_title_layout_title")
    # my_per_info_name_btn_id = (By.ID, "com.langlib.ncee:id/account_title_layout_left_btn")
    my_per_info_name_update_name_id = (By.ID, "com.langlib.ncee:id/activity_update_user_name_name")
    my_per_info_name_clear_uname_id = (By.ID, "com.langlib.ncee:id/activity_update_user_name_close_iv")
    my_per_info_name_update_sure_btn_id = (By.ID, "com.langlib.ncee:id/activity_update_user_btn")

    def click_per_info_photo(self):
        self.find_element(*self.my_per_info_photo_id).click()

    def cancel_update_photo(self):
        self.find_element(*self.picture_cancel_id).click()

    def get_per_info_name(self):
        return self.getText(*self.find_element(*self.my_per_info_name_id))

    def click_per_info_name(self):
        self.find_element(*self.my_per_info_name_id).click()

    def click_clear_my_name(self):
        self.find_element(*self.my_per_info_name_clear_uname_id).click()

    def input_my_name(self, uname):
        self.find_element(*self.my_per_info_name_update_name_id).send_keys(uname)

    def click_update_name_sure_btn(self):
        self.find_element(*self.my_per_info_name_update_sure_btn_id).click()

    def click_update_name_back_btn(self):
        self.find_element(*self.my_per_info_back_btn_id).click()


if __name__ == '__main__':
    test = PersonalPage()
    test.open()
    test.click_my()
    test.click_photo()
    test.click_per_info_name()
    test.click_clear_my_name()
    test.input_my_name("William")
    test.click_update_name_sure_btn()
    test.click_update_name_back_btn()