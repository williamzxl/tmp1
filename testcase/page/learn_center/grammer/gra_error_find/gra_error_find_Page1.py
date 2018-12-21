from selenium.webdriver.common.by import By
from testcase.common.allBasePageClass import AllBasePage
from utils.config import get_appPackage


class GraErrorFindStep1Page1(AllBasePage):
    appPackage = get_appPackage()
    '''
    短文改错
    '''
    page_title_id = (By.ID, "{}:id/title_iframe_title_tv".format(appPackage))
    gra_error_find_start_to_answer_id = (By.ID, "{}:id/fragment_error_find_question_start_tv".format(appPackage))

    error_find_text_view = (By.ID, "{}:id/text_view".format(appPackage))

    error_find_delete_id = (By.ID, "{}:id/popwindow_delete_tv".format(appPackage))
    error_find_change_id = (By.ID, "{}:id/popwindow_correction_tv".format(appPackage))
    error_find_add_id = (By.ID, "{}:id/popwindow_insert_tv".format(appPackage))

    error_find_submit_id = (By.ID, "{}:id/fragment_error_find_canto_commit_tv".format(appPackage))
    error_find_finish_id = (By.ID, "{}:id/fragment_error_find_canto_done_tv".format(appPackage))

    def click_gra_error_find_start_to_answer(self):
        self.find_element(*self.gra_error_find_start_to_answer_id).click()

    def get_error_find_x_y(self):
        ele = self.find_element(*self.error_find_text_view)
        print("Size", self.getEleSize(ele))
        width = self.getEleSize(ele).get('width')
        height = self.getEleSize(ele).get('height')
        print("Location", self.getEleLocation(ele))
        x = self.getEleLocation(ele).get('x')
        y = self.getEleLocation(ele).get('y')
        return int(width), int(y), int(height)

    def click_error_find_delete_btn(self):
        self.find_element(*self.error_find_delete_id).click()

    def click_error_find_submit_btn(self):
        self.find_element(*self.error_find_submit_id).click()

    def click_error_find_finish_btn(self):
        self.find_element(*self.error_find_finish_id).click()


if __name__ == "__main__":
    pass
