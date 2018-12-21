from time import sleep
import re
from selenium.webdriver.common.by import By
from testcase.page.learn_center.reading.section_train.sect_tra_WordsListPage1 import STFillAnswer1
from utils.config import get_appPackage


class SAAnswerResultPage2(STFillAnswer1):
    appPackage = get_appPackage()
    '''
    段落训练第三步：句子分析
    '''
    sect_train_step3_lists_nums_id = (By.ID, "{}:id/quest_analysis_step".format(appPackage))
    answer_radio_button_classes = (By.CLASS_NAME, "android.widget.RadioButton")
    sect_train_step3_sure_btn_id = (By.ID, "{}:id/fragment_section_train_sure".format(appPackage))
    sect_train_next_question_id = (By.ID, '{}:id/fragment_section_train_nextquest'.format(appPackage))
    sect_train_step3_mask_answer_id = (By.ID, "{}:id/sen_analysis_mask_answer".format(appPackage))
    fill_CN_answer_classes = (By.CLASS_NAME, 'android.widget.EditText')
    sect_train_finish_button_id = (By.ID, "{}:id/fragment_section_train_done".format(appPackage))

    #临时
    check_result_id = (By.ID, "{}:id/fragment_section_train_result".format(appPackage))

    def return_sect_train_step3_ques_ele(self):
        return self.find_element(*self.sect_train_step3_lists_nums_id)

    def get_sect_train_step3_lists_nums(self):
        text = self.getText(self.find_element(*self.sect_train_step3_lists_nums_id))
        text_regx = re.compile(r'.*\((\d+)\/(\d+)')
        result = text_regx.search(text).groups()
        current_num = int(result[0])
        total_num = int(result[1])
        return current_num, total_num

    def sect_train_step3_choose_answer(self, answer=None, right=True):
        x, y = self.getSize()
        self.swipeUp(x * 0.5, y * 0.8, 0, 200)
        sleep(5)
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
        print("All_answer_CN", all_answer_CN)
        if answer not in all_answer_CN:
            print("正确答案不存在")
            self.save_screen_shot("正确答案不存在",file_name="句子分析不存在正确答案")
            sleep(180)
            for a in answers_ele:
                if self.getText(a) != answer:
                    a.click()

    def click_sect_train_step3_sure_btn(self):
        self.find_element(*self.sect_train_step3_sure_btn_id).click()

    def click_sect_train_step3_next_ques_btn(self):
        self.find_element(*self.sect_train_next_question_id).click()

    def click_sect_train_mask_CN(self):
        self.find_element(*self.sect_train_step3_mask_answer_id).click()

    def sect_train_step3_fill_CN_answer(self, answer):
        print("Answer", answer, str(answer))
        ele = self.find_element(*self.fill_CN_answer_classes)
        ele.click()
        ele.send_keys(str(answer))
        text = self.getText(ele)
        print(text, text != str(answer))
        while text != str(answer):
            ele.clear()
            ele.ele.send_keys(str(answer))
            text = self.getText(ele)
            if text == str(answer):
                break

    def click_sect_train_step3_finish_button(self):
        self.find_element(*self.sect_train_finish_button_id).click()

    def click_sect_train_step3_check_result_btn(self):
        self.find_element(*self.check_result_id).click()


if __name__ == "__main__":
    pass