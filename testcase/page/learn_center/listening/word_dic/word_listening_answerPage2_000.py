import re
from time import sleep
from selenium.webdriver.common.by import By
from testcase.page.learn_center.listening.word_dic.word_listening_listsPage1 import WLLists1


class WLFillAnswerPage2(WLLists1):
    '''
    单词听写题目作答页
    '''
    appPackage = "com.langlib.ncee"
    page_title_id = (By.ID, "{}:id/title_iframe_title_tv".format(appPackage))
    list_num_id = (By.ID, "{}:id/fragment_word_dic_index_tv".format(appPackage))

    audio_icon_id = (By.ID, "{}:id/fragment_word_dic_detail_play_audio_btn".format(appPackage))
    input_btn_class = (By.CLASS_NAME, "android.widget.EditText")
    # back_btn_id = (By.ID, "com.langlib.cee:id/title_iframe_back_btn")
    # dialog_tips_text_id = "com.langlib.cee:id/dialog_descripiton_tv"
    # dialog_tips_text_id_ele = (By.ID, "com.langlib.cee:id/dialog_descripiton_tv")
    # dialog_sure_button = (By.ID, "com.langlib.cee:id/dialog_sure_button")
    # dialog_cancel_button = (By.ID, "com.langlib.cee:id/dialog_cancel_button")

    # def click_back_btn(self):
    #     self.find_element(*self.back_btn_id)
    #
    # def get_dialog_tips_text(self):
    #     return self.getText(self.find_element(*self.dialog_tips_text_id))
    #
    # def click_sure_button(self):
    #     if self.dialog_tips_text_id in self.page_source():
    #         return self.find_element(*self.dialog_sure_button)
    #
    # def click_cancel_button(self):
    #     if self.dialog_tips_text_id in self.page_source():
    #         return self.find_element(*self.dialog_cancel_button)

    def get_list_text(self):
        return self.getText(self.find_element(*self.list_num_id))

    def get_words_list_num(self):
        text = self.getText(self.find_element(*self.list_num_id))
        text_regx = re.compile(r'.*\((\d+)\/(\d+)')
        result = text_regx.search(text).groups()
        current_num = result[0]
        total_num = result[1]
        return current_num, total_num

    def click_dict_audio_button(self):
        self.find_element(*self.audio_icon_id).click()
        sleep(0.5)

    def fill_answer(self, answers=None):
        try:
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
                    for m, n in zip(answers, self.find_elements(*self.input_btn_class)):
                        n.send_keys(m)
                    fill_answer1.clear()
                    for ele in self.find_elements(*self.input_btn_class):
                        fill_answer1.append(self.getText(ele))
                print("Fill_answer:", fill_answer1)
                if str("".join(fill_answer1).strip()) == str(answers):
                    break
        except:
            self.find_elements(*self.input_btn_class).send_keys(answers)
        # sleep(3)
        self.pressKeyCode("66")


if __name__ == "__main__":
    pass
