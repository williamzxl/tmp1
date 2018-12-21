import re
from selenium.webdriver.common.by import By
from testcase.common.allBasePageClass import AllBasePage
from utils.config import get_appPackage


class STFillAnswer1(AllBasePage):
    appPackage = get_appPackage()
    '''
    段落训练第一步
    '''
    sect_train_page_title_id = (By.ID, "{}:id/title_iframe_title_tv".format(appPackage))
    sect_train_total_list_num_id = (By.ID, "{}:id/fragment_section_train_child_tip".format(appPackage))
    sect_train_text_id = (By.ID, '{}:id/fragment_section_train_word_child_questtext'.format(appPackage))
    sect_train_step2_sure_btn_id = (By.ID, "{}:id/fragment_section_train_sure".format(appPackage))
    sect_train_next_button_id = (By.ID, "{}:id/fragment_section_train_nexttv".format(appPackage))

    '''
    段落训练第二步：段落主旨句
    '''
    ques_desc_id = (By.ID, '{}:id/quest_section_part_tip'.format(appPackage))
    answer_edit_text_id = (By.ID, "{}:id/quest_section_part_ed".format(appPackage))
    sect_train_sure_button_id = (By.ID, "{}:id/fragment_section_train_sure".format(appPackage))
    sect_train_step2_next_btn_id = (By.ID, "{}:id/fragment_section_train_nexttv".format(appPackage))
    '''
    第一步元素操作步骤
    '''

    def get_sect_train_list_text(self):
        return self.getText(self.find_element(*self.sect_train_total_list_num_id))

    def get_sect_train_text_text(self):
        return self.getText(self.find_element(*self.sect_train_text_id))

    def get_sect_train_edit_text(self):
        return self.getText(self.find_element(*self.answer_edit_text_id))

    def click_sect_train_step1_next_button(self):
        self.find_element(*self.sect_train_next_button_id).click()
        # self.find_element(*self.sect_train_step2_next_btn_id).click()


    '''
    段落训练：第二步段落主旨句元素操作步骤
    '''
    def get_ques_desc_text(self):
        return self.getText(self.find_element(*self.ques_desc_id)).split(':')[0]

    def sect_train_step2_fill_answer(self, answer):
        ele = self.find_element(*self.answer_edit_text_id)
        ele.send_keys(answer)
        text = self.getText(ele)
        times = 0
        while text != str(answer):
            ele.clear()
            ele.send_keys(str(answer))
            text = self.getText(ele)
            times += 1
            if text == str(answer):
                break
            if times > 3:
                break


    def click_sect_train_step2_sure_button(self):
        self.find_element(*self.sect_train_step2_sure_btn_id).click()

    def click_sect_train_step2_next_btn(self):
        self.find_element(*self.sect_train_step2_next_btn_id).click()


if __name__ == "__main__":
    pass
