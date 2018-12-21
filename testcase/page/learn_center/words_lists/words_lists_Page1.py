from selenium.webdriver.common.by import By
from testcase.common.allBasePageClass import AllBasePage
from utils.config import get_appPackage


class WordsListsPage1(AllBasePage):
    appPackage = get_appPackage()
    '''
    词汇
    '''
    page_title_id = (By.ID, "{}:id/title_iframe_title_tv".format(appPackage))
    wl_start_ele_id = (By.ID, "{}:id/frame_word_profi_iv".format(appPackage))
    wl_star_1 = (By.ID, "{}:id/popwindow_word_profi_star1".format(appPackage))
    wl_star_2 = (By.ID, "{}:id/popwindow_word_profi_star2".format(appPackage))
    wl_star_3 = (By.ID, "{}:id/popwindow_word_profi_star3".format(appPackage))

    def get_wl_all_star_eles(self):
        eles = self.find_elements(*self.wl_start_ele_id)
        return eles

    def click_wl_start1_btn(self):
        self.find_element(*self.wl_star_1).click()

    def click_wl_start2_btn(self):
        self.find_element(*self.wl_star_2).click()

    def click_wl_start3_btn(self):
        self.find_element(*self.wl_star_3).click()


if __name__ == "__main__":
    pass
