import re
# from time import sleep
from testcase.common.allBasePageClass import AllBasePage
from selenium.webdriver.common.by import By
from utils.config import get_appPackage


class WSFillAnswerPage1(AllBasePage):
    appPackage = get_appPackage()
    '''
    单词拼写题目作答页
    '''
    page_title_id = (By.ID, "{}:id/title_iframe_title_tv".format(appPackage))
    ws_list_num_id = (By.ID, "{}:id/fragment_word_spell_index_tv".format(appPackage))
    word_spell_CN = (By.ID, "{}:id/fragment_word_spell_detail_cn".format(appPackage))

    input_btn_class = (By.CLASS_NAME, "android.widget.EditText")

    def get_word_spell_list_text(self):
        return self.getText(self.find_element(*self.ws_list_num_id))

    def get_word_spell_list_num(self):
        text = self.getText(self.find_element(*self.ws_list_num_id))
        text_regx = re.compile(r'.*\((\d+)\/(\d+)')
        result = text_regx.search(text).groups()
        current_num = result[0]
        total_num = result[1]
        return current_num, total_num

    def get_word_spell_CN(self):
        return self.getText(self.find_element(*self.word_spell_CN))

    def fill_word_spell_answer(self, answers=None):
        try:
            try:
                self.hideKeyboard()
            except:
                pass
            self.find_element(*self.input_btn_class).send_keys(answers)
            fill_answer = []
            for ele in self.find_elements(*self.input_btn_class):
                fill_answer.append(self.getText(ele))
            print("Fill Answer:", str("".join(fill_answer).strip()))
            while str("".join(fill_answer).strip()) != str(answers):
                fill_answer1 = []
                if str("".join(fill_answer1).strip()) != str(answers):
                    for ele in self.find_elements(*self.input_btn_class):
                        ele.clear()
                    self.find_elements(*self.input_btn_class)[0].click()
                    self.find_element(*self.input_btn_class).send_keys(answers)
                    fill_answer1.clear()
                    for ele in self.find_elements(*self.input_btn_class):
                        fill_answer1.append(self.getText(ele))
                if str("".join(fill_answer1).strip()) == str(answers):
                    break
        except:
            self.find_element(*self.input_btn_class).send_keys(answers)
        self.pressKeyCode("66")


if __name__ == "__main__":
    pass
