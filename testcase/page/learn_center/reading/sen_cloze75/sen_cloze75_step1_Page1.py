from selenium.webdriver.common.by import By
from testcase.common.allBasePageClass import AllBasePage
from utils.config import get_appPackage


class SC75Step1Page1(AllBasePage):
    appPackage = get_appPackage()
    '''
    七选五训练Step1
    '''
    page_title_id = (By.ID, "{}:id/title_iframe_title_tv".format(appPackage))
    step1_word_list_id = (By.ID, "{}:id/fragment_word_profi_list_head_item_tv1".format(appPackage))
    next_step_btn_id = (By.ID, "{}:id/sen_cloze_next_step_tv".format(appPackage))

    def get_sc_75_words_list_text(self):
        return self.getText(self.find_element(*self.step1_word_list_id))

    def click_sc_75_next_btn(self):
        self.find_element(*self.next_step_btn_id).click()


if __name__ == "__main__":
    pass
