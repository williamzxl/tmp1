import re
from selenium.webdriver.common.by import By
from testcase.common.allBasePageClass import AllBasePage
from utils.config import get_appPackage


class GFWordsListPage1(AllBasePage):
    appPackage = get_appPackage()
    '''
    语法填空生词表页
    '''
    gra_page_title_id = (By.ID, "{}:id/title_iframe_title_tv".format(appPackage))
    # gra_list_num_id = (By.ID, "com.langlib.cee:id/fragment_gra_fill_detail_index_tv")
    gra_list_num_id = (By.ID, "{}:id/fragment_gra_fill_word_profi_index_tv".format(appPackage))

    gra_fill_next_step_id = (By.ID, "{}:id/fragment_gra_fill_canto_next_step_tv".format(appPackage))

    def get_gra_list_text(self):
        return self.getText(self.find_element(*self.gra_list_num_id))

    def get_gra_lists_nums(self):
        text = self.getText(self.find_element(*self.gra_list_num_id))
        text_regx = re.compile(r'.*\((\d+)\/(\d+)')
        result = text_regx.search(text).groups()
        current_num = result[0]
        total_num = result[1]
        return current_num, total_num

    def click_gra_fill_next_step(self):
        self.find_element(*self.gra_fill_next_step_id).click()


if __name__ == "__main__":
    pass
