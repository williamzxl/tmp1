from selenium.webdriver.common.by import By
from testcase.page.learn_center.listening.long_conv.long_conv_step1_Page import LC_Step1_Page
from utils.config import get_appPackage


class LC_Step2_Page(LC_Step1_Page):
    appPackage = get_appPackage()
    '''
    长对话训练第二步做题步骤
    '''
    audio_icon_id = (By.ID, "{}:id/frame_audio_conv_imageview".format(appPackage))
    current_time_id = (By.ID, "{}:id/frame_audio_conv_current_time".format(appPackage))
    total_time_id = (By.ID, "{}:id/frame_audio_conv_total_time".format(appPackage))

    question_num_ids = (By.ID, "{}:id/conversation_question_no".format(appPackage))
    question_items_ids = (By.ID, "{}:id/conversation_question".format(appPackage))
    long_conv_answer_a_id = (By.ID, "{}:id/option_a_no".format(appPackage))
    long_conv_answer_b_id = (By.ID, "{}:id/option_b_no".format(appPackage))
    long_conv_answer_c_id = (By.ID, "{}:id/option_c_no".format(appPackage))
    long_conv_answer_c_items = (By.ID, "{}:id/option_c_no".format(appPackage))

    item_text_class = (By.CLASS_NAME, "android.widget.TextView")
    long_conv_done_id = (By.ID, "{}:id/fragment_short_conv_done_tv".format(appPackage))
    long_conv_answer_words_list_id = (By.ID, "{}:id/fragment_short_conv_answer_word_tv".format(appPackage))

    long_conv_words_List_finish_btn_id = (By.ID, "{}:id/fragment_word_profi_done_tv".format(appPackage))

    def click_long_conv_audio_icon(self):
        self.find_element(*self.audio_icon_id).click()

    def get_long_conv_audio_current_time(self):
        current_time = self.getText(self.find_element(*self.current_time_id))
        print("Current_time", current_time)
        return current_time

    def get_long_conv_audio_total_time(self):
        total_time = self.getText(self.find_element(*self.total_time_id))
        print("Total time", total_time)
        return total_time

    def check_long_conv_audio_play_result(self, curr, total):
        return True if curr == total else False

    def find_all_long_conv_c_items(self):
        eles = self.find_elements(*self.long_conv_answer_c_items)
        print("ELES", eles)
        return eles

    def find_all_long_conv_choose_question_no(self):
        question_ele = self.find_elements(*self.question_num_ids)
        print("Q ELEs",question_ele)
        return question_ele

    def get_long_conv_question_num(self, ele):
        question_num = str(self.getText(ele)).split('.')[0]
        return int(question_num)

    def choose_long_conv_step2_answer(self, num, answer, c=0):
        print("Answer", answer, "Num", num)
        if answer.upper() == 'A':
            print("Choose A", num, c)
            # print(self.find_elements(*self.long_conv_answer_a_id)[num - 1])
            # print(self.find_elements(*self.long_conv_answer_a_id))
            # self.find_elements(*self.long_conv_answer_a_id)[num - 1].click()
            if c:
                print('"4." in self.page_source() or "3." in self.page_source()',"4." in self.page_source() or "3." in self.page_source())
                if ("4." in self.page_source() or "3." in self.page_source()) and num == 0:
                    self.find_elements(*self.long_conv_answer_b_id)[0].click()
                if num == 1:
                    self.find_elements(*self.long_conv_answer_a_id)[1].click()
                if num == 2:
                    try:
                        self.find_elements(*self.long_conv_answer_b_id)[2].click()
                    except:
                        self.find_elements(*self.long_conv_answer_b_id)[1].click()
            else:
                if c == 4:
                    self.find_elements(*self.long_conv_answer_a_id)[num - 2].click()
                else:
                    try:
                        self.find_elements(*self.long_conv_answer_a_id)[num - 1].click()
                    except:
                        self.find_elements(*self.long_conv_answer_a_id)[num - 2].click()
        if answer.upper() == 'B':
            print("Choose B", num, c)
            # print(self.find_elements(*self.long_conv_answer_a_id)[num - 1])
            # print(self.find_elements(*self.long_conv_answer_b_id))
            # self.find_elements(*self.long_conv_answer_b_id)[num - 1].click()
            if c:
                print('"4." in self.page_source() or "3." in self.page_source()',"4." in self.page_source() or "3." in self.page_source())
                if ("4." in self.page_source() or "3." in self.page_source()) and num == 0:
                    self.find_elements(*self.long_conv_answer_b_id)[0].click()
                if num == 1:
                    self.find_elements(*self.long_conv_answer_b_id)[1].click()
                if num == 2:
                    try:
                        self.find_elements(*self.long_conv_answer_b_id)[2].click()
                    except:
                        self.find_elements(*self.long_conv_answer_b_id)[1].click()
            else:
                if c == 4:
                    self.find_elements(*self.long_conv_answer_b_id)[num - 2].click()
                else:
                    try:
                        self.find_elements(*self.long_conv_answer_b_id)[num - 1].click()
                    except:
                        try:
                            self.find_elements(*self.long_conv_answer_b_id)[num - 2].click()
                        except:
                            pass

        if answer.upper() == 'C':
            print("Choose C", num, "CCCCCCCCCCCCCcc", c)
            print(self.find_elements(*self.long_conv_answer_b_id))
            # print("len(se", len(self.find_elements(*self.long_conv_answer_c_id)))
            if c:
                if num == 1:
                    self.find_elements(*self.long_conv_answer_c_id)[1].click()
                if num == 2:
                    try:
                        self.find_elements(*self.long_conv_answer_b_id)[2].click()
                    except:
                        self.find_elements(*self.long_conv_answer_b_id)[1].click()
            else:
                if c == 4:
                    self.find_elements(*self.long_conv_answer_c_id)[num - 2].click()
                else:
                    try:
                        self.find_elements(*self.long_conv_answer_b_id)[num - 1].click()
                    except:
                        try:
                            self.find_elements(*self.long_conv_answer_b_id)[num - 2].click()
                        except:
                            pass

        # except:
        #     print("第二步第三题第四题挡住了")
            # x, y = self.getSize()
            # # self, x, y1, y2, t=500
            # self.swipeUp(x * 0.8, y * 0.8, 0, 200)
            # if answer.upper() == 'A':
            #     self.find_elements(*self.answer_a_id)[num - 1].click()
            # if answer.upper() == 'B':
            #     self.find_elements(*self.answer_b_id)[num - 1].click()
            # if answer.upper() == 'C':
            #     self.find_elements(*self.answer_c_id)[num - 1].click()

    def click_long_conv_step2_sure(self):
        self.find_element(*self.long_conv_done_id).click()

    '''
    第二步结果页
    '''
    def click_long_conv_play_text(self):
        self.find_elements(*self.item_text_class)[0].click()

    def click_long_conv_conv_text(self):
        self.find_elements(*self.item_text_class)[1].click()

    def click_long_conv_conv_answer(self):
        self.find_elements(*self.item_text_class)[2].click()

    def click_long_conv_step2_words_list(self):
        self.find_element(*self.long_conv_answer_words_list_id).click()

    def click_long_conv_words_list_finish_btn(self):
        self.find_element(*self.long_conv_words_List_finish_btn_id).click()

    # def click_words_list_button(self):
    #     self.find_element(*self.word_list_button_id).click()


if __name__ == "__main__":
    pass