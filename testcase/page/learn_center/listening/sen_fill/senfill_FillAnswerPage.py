import re
from time import sleep
from selenium.webdriver.common.by import By
from testcase.common.allBasePageClass import AllBasePage

class SFFillAnswerPage1(AllBasePage):
    '''
    句子填充题目作答页
    '''
    appPackage = "com.langlib.ncee"
    page_title_id = (By.ID, "{}:id/title_iframe_title_tv".format(appPackage))
    sen_fill_list_num_id = (By.ID, "{}:id/fragment_sen_fill_index_tv".format(appPackage))
    audio_icon_id = (By.ID, "{}:id/fragment_sen_fill_detail_play_imagebtn".format(appPackage))

    sen_id = (By.ID, "{}:id/text_view".format(appPackage))
    answer_edit_classes = (By.CLASS_NAME, "android.widget.EditText")

    sen_fill_next_button_id = (By.ID, "{}:id/fragment_sen_fill_next_tv".format(appPackage))
    sen_fill_words_list_id = (By.ID, "{}:id/fragment_sen_fill_word_tv".format(appPackage))

    def get_senfill_list_text(self):
        return self.getText(self.find_element(*self.sen_fill_list_num_id))

    def get_senfill_lists_nums(self):
        text = self.getText(self.find_element(*self.sen_fill_list_num_id))
        text_regx = re.compile(r'.*\((\d+)\/(\d+)')
        result = text_regx.search(text).groups()
        current_num = result[0]
        total_num = result[1]
        return current_num, total_num

    def click_senfill_audio_button(self):
        self.find_element(*self.audio_icon_id).click()
        sleep(0.5)

    def senfill_fill_answer(self, answers=None):
        answer_edit_ele = self.find_elements(*self.answer_edit_classes)
        for edit,answer in zip(answer_edit_ele, answers):
            # self.hideKeyboard()
            print("Edit and answer", edit, answers)
            edit.send_keys(answer)
            self.hideKeyboard()
        print("1")
        self.pressKeyCode("66")
        print("3")
        sleep(5)
        try:
            pass
            # print("下一题 not in self.page_source()", "下一题" in self.page_source())
            # while "下一题" not in self.page_source():
            #     for edit, answer in zip(answer_edit_ele, answers):
            #         edit.send_keys(answer)
            #     self.pressKeyCode("66")
        except:
            pass

    def click_sen_fill_next_btn(self):
        self.find_element(*self.sen_fill_next_button_id).click()

    def click_sen_fill_words_list_btn(self):
        self.find_element(*self.sen_fill_words_list_id).click()


if __name__ == "__main__":
    pass
