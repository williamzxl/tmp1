import re
from time import sleep
from selenium.webdriver.common.by import By
from testcase.common.allBasePageClass import AllBasePage
from utils.config import get_appPackage


class QCFillAnswerPage1(AllBasePage):
    appPackage = get_appPackage()
    '''
    遣词造句题目作答页
    '''
    qc_curr_sen_id = (By.ID, "{}:id/construction_quest_tip".format(appPackage))
    qc_CN_text_id = (By.ID, "{}:id/construction_quest_text".format(appPackage))
    qc_curr_ques_id = (By.ID, "{}:id/construction_subquest_tip".format(appPackage))
    qc_answer_edit_id = (By.ID, "{}:id/construction_subquest_edit".format(appPackage))
    qc_submit_id = (By.ID, "{}:id/construction_quest_submit".format(appPackage))

    qc_next_ques_btn_id = (By.ID, "{}:id/construction_quest_next".format(appPackage))

    qc_finish_btn_id = (By.ID, "{}:id/construction_quest_sure".format(appPackage))

    def get_qc_senNum_text(self):
        return self.getText(self.find_element(*self.qc_curr_sen_id))

    def get_qc_curr_sen_nums(self):
        text = self.getText(self.find_element(*self.qc_curr_sen_id))
        text_regx = re.compile(r'.*\((\d+)\/(\d+)')
        result = text_regx.search(text).groups()
        current_num = int(result[0])
        total_num = int(result[1])
        return current_num, total_num

    def get_qc_step_text(self):
        return self.getText(self.find_element(*self.qc_curr_ques_id))

    def get_qc_current_ques_step_nums(self):
        try:
            text = self.getText(self.find_element(*self.qc_curr_ques_id))
            print("text", text)
            text_regx = re.compile(r'\((\d+)\/(\d+)\)')
            result = text_regx.search(text).groups()
            current_step = int(result[0])
            total_step = int(result[1])
            return current_step, total_step
        except:
            print("Get steps num failed")
            return None, None

    def qc_fill_answer(self, answer=None):
        qc_edit_ele = self.find_element(*self.qc_answer_edit_id)
        # qc_edit_ele.click()
        qc_edit_ele.send_keys(answer)

    def click_qc_submit_btn(self):
        self.find_element(*self.qc_submit_id).click()

    def click_qc_next_ques_btn(self):
        self.find_element(*self.qc_next_ques_btn_id).click()

    def click_qc_finish_btn(self):
        self.find_element(*self.qc_finish_btn_id).click()


if __name__ == "__main__":
    pass
