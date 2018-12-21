from selenium.webdriver.common.by import By
from testcase.page.learn_center.listening.short_conv.short_conv_step1_Page import SC_Step1_Page


class SC_Step2_Page(SC_Step1_Page):
    '''
    短对话训练第二步做题步骤
    '''
    appPackage = "com.langlib.ncee"
    audio_icon_id = (By.ID, "{}:id/frame_audio_conv_imageview".format(appPackage))
    current_time_id = (By.ID, "{}:id/frame_audio_conv_current_time".format(appPackage))
    total_time_id = (By.ID, "{}:id/frame_audio_conv_total_time".format(appPackage))

    short_answer_a_id = (By.ID, "{}:id/option_a_no".format(appPackage))
    short_answer_b_id = (By.ID, "{}:id/option_b_no".format(appPackage))
    short_answer_c_id = (By.ID, "{}:id/option_c_no".format(appPackage))

    item_text_class = (By.CLASS_NAME, "android.widget.TextView")
    short_conv_done_id = (By.ID, "{}:id/fragment_short_conv_done_tv".format(appPackage))
    short_conv_answer_next_id = (By.ID, "{}:id/fragment_short_conv_answer_next_tv".format(appPackage))

    def click_audio_icon(self):
        self.find_element(*self.audio_icon_id).click()

    def get_current_time(self):
        return self.getText(self.find_element(*self.current_time_id))

    def get_total_time(self):
        return self.getText(self.find_element(*self.total_time_id))

    def check_audio_play(self, curr, total):
        return True if curr == total else False

    def choose_short_conv_answer(self, answer):
        if answer.upper() == 'A':
            self.find_element(*self.short_answer_a_id).click()
        if answer.upper() == 'B':
            self.find_element(*self.short_answer_b_id).click()
        if answer.upper() == 'C':
            self.find_element(*self.short_answer_c_id).click()

    def click_short_conv_step2_sure(self):
        self.find_element(*self.short_conv_done_id).click()

    '''
    第二步结果页
    '''
    def click_play(self):
        self.find_elements(*self.item_text_class)[0].click()

    def click_conv_text(self):
        self.find_elements(*self.item_text_class)[1].click()

    def click_conv_answer(self):
        self.find_elements(*self.item_text_class)[2].click()

    def click_short_conv_step2_next(self):
        self.find_element(*self.short_conv_answer_next_id).click()

    # def click_words_list_button(self):
    #     self.find_element(*self.word_list_button_id).click()


if __name__ == "__main__":
    pass