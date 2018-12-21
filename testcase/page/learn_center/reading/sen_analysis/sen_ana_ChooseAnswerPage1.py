import re
from selenium.webdriver.common.by import By
from testcase.common.allBasePageClass import AllBasePage


class SAChooseAnswerPage1(AllBasePage):
    '''
    句子分析题目作答页
    '''
    appPackage = "com.langlib.ncee"
    page_title_id = (By.ID, "{}:id/title_iframe_title_tv".format(appPackage))
    total_list_num_id = (By.ID, "{}:id/fragment_sen_analysis_child_tip".format(appPackage))
    sen_text_id = (By.ID, '{}:id/fragment_sen_analysis_child_questtext'.format(appPackage))
    item_list_des_id = (By.ID, "{}:id/quest_analysis_step".format(appPackage))

    answer_radio_button_classes = (By.CLASS_NAME, 'android.widget.RadioButton')
    mask_answer_id = (By.ID, "{}:id/sen_analysis_mask_answer".format(appPackage))
    fill_CN_answer_classes = (By.CLASS_NAME, 'android.widget.EditText')
    answer_sure_id = (By.ID, "{}:id/senavaly_quest_sure".format(appPackage))

    gra_tips_id = (By.ID, "com.langlib.ncee:id/quest_analysis_group_gra_tip")
    sen_ana_next_button_id = (By.ID, 'com.langlib.ncee:id/senavaly_quest_next_quest')
    sen_ana_done_button_id = (By.ID, 'com.langlib.ncee:id/senavaly_quest_done')
    sen_ana_finish_btn_id = (By.ID, "com.langlib.ncee:id/fragment_word_profi_done_tv")

    def get_sen_ana_list_text(self):
        return self.getText(self.find_element(*self.total_list_num_id))

    def get_sen_text_text(self):
        return self.getText(self.find_element(*self.sen_text_id))

    def get_sen_ana_lists_nums(self):
        text = self.getText(self.find_element(*self.total_list_num_id))
        text_regx = re.compile(r'.*\((\d+)\/(\d+)')
        result = text_regx.search(text).groups()
        current_num = int(result[0])
        total_num = int(result[1])
        return current_num, total_num

    def get_step_text(self):
        return self.getText(self.find_element(*self.item_list_des_id))

    def get_step_nums(self):
        try:
            text = self.getText(self.find_element(*self.item_list_des_id))
            text_regx = re.compile(r'\((\d+)\/(\d+)\)')
            result = text_regx.search(text).groups()
            current_step = int(result[0])
            total_step = int(result[1])
            return current_step, total_step
        except:
            print("Get steps num failed")
            return None, None

    def sen_ana_choose_answer(self, answer=None, right=True):
        answers_ele = self.find_elements(*self.answer_radio_button_classes)
        all_answer_CN = []
        for a in answers_ele:
            all_answer_CN.append(self.getText(a))
            if right:
                if self.getText(a) == answer:
                    a.click()
            else:
                if self.getText(a) != answer:
                    a.click()
        if answer not in all_answer_CN:
            print("正确答案不存在")
            self.save_screen_shot("正确答案不存在",file_name="句子分析不存在正确答案")
            for a in answers_ele:
                if self.getText(a) != answer:
                    a.click()


    def click_to_check_CN(self):
        self.find_element(*self.mask_answer_id).click()

    def fill_CN_answer(self, answer):
        ele = self.find_element(*self.fill_CN_answer_classes)
        ele.click()
        ele.send_keys(str(answer))
        text = self.getText(ele)
        while text != str(answer):
            ele.clear()
            ele.send_keys(str(answer))
            text = self.getText(ele)
            if text == str(answer):
                break
            else:
                ele.clear()
                ele.send_keys(str(answer))
                break
        self.hideKeyboard()

    def click_sen_ana_sure_button(self):
        self.find_element(*self.answer_sure_id).click()

    def click_sen_ana_next_question(self):
        self.find_element(*self.sen_ana_next_button_id).click()

    def click_sen_ana_finish_button(self):
        try:
            self.find_element(*self.sen_ana_finish_btn_id).click()
        except:
            self.find_element(*self.sen_ana_done_button_id).click()


if __name__ == "__main__":
    pass
