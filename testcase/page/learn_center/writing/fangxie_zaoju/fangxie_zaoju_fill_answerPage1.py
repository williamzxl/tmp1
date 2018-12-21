import re
# from time import sleep
from testcase.common.allBasePageClass import AllBasePage
from selenium.webdriver.common.by import By
from utils.config import get_appPackage


class FangxieZaojuFillAnswerPage1(AllBasePage):
    appPackage = get_appPackage()
    '''
    仿写造句题目作答页
    '''
    page_title_id = (By.ID, "{}:id/title_iframe_title_tv".format(appPackage))
    total_groups_num_id = (By.ID, "{}:id/senimitation_currqinx".format(appPackage))
    fangxie_zaoju_fill_answer_id = (By.ID, "{}:id/senimitation_write_edit".format(appPackage))

    fangxie_zaoju_ques_id = (By.ID, "{}:id/senimitation_guide_questtext".format(appPackage))

    fangxie_zaoju_submit_id = (By.ID, "{}:id/senimitation_submit".format(appPackage))
    fangxie_zaoju_next_step_id = (By.ID, "{}:id/senimitation_next".format(appPackage))
    fangxie_zaoju_finish_btn_id = (By.ID, "{}:id/senimitation_sure".format(appPackage))

    def get_fangxie_zaoju_groups_nums(self):
        text = self.getText(self.find_element(*self.total_groups_num_id))
        text_regx = re.compile(r'.*\((\d+)\/(\d+)')
        result = text_regx.search(text).groups()
        current_group = int(result[0])
        total_group = int(result[1])
        return current_group, total_group

    def get_fangxie_zaoju_step_text(self):
        return self.getText(self.find_element(*self.fangxie_zaoju_ques_id))

    def get_fangxie_zaoju_step_nums(self):
        try:
            text = self.getText(self.find_element(*self.fangxie_zaoju_ques_id))
            text_regx = re.compile(r'\((\d+)\/(\d+)\)')
            result = text_regx.search(text).groups()
            current_step = int(result[0])
            total_step = int(result[1])
            return current_step, total_step
        except:
            print("Get steps num failed")
            return None, None

    def fangxie_zaoju_fill_CN_answer(self, answer):
        ele = self.find_element(*self.fangxie_zaoju_fill_answer_id)
        ele.click()
        ele.send_keys(answer)
        self.hideKeyboard()

    def click_fangxie_zaoju_submit_btn(self):
        self.find_element(*self.fangxie_zaoju_submit_id).click()

    def click_fangxie_zaoju_next_step_btn(self):
        self.find_element(*self.fangxie_zaoju_next_step_id).click()

    def click_fangxie_zaoju_finish_btn(self):
        self.find_element(*self.fangxie_zaoju_finish_btn_id).click()


if __name__ == "__main__":
    pass
