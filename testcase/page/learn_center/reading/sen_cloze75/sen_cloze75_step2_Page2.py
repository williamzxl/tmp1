from selenium.webdriver.common.by import By
from testcase.page.learn_center.reading.sen_cloze75.sen_cloze75_step1_Page1 import SC75Step1Page1
from time import sleep
from utils.config import get_appPackage


class SC75Step2Page(SC75Step1Page1):
    appPackage = get_appPackage()
    '''
    七选五训练Step2
    '''
    sc_75_text_view_id = (By.ID, "com.langlib.ncee:id/text_view".format(appPackage))

    sc_75_answers_id = (By.ID, "{}:id/fragment_sen_cloze_vp_detail_viewpager".format(appPackage))
    sc_75_fill_answer_classes = (By.CLASS_NAME, "android.widget.TextView")

    sc_75_submit_id = (By.ID, "{}:id/sen_cloze_commit_in_tv".format(appPackage))

    sc_75_yeqian_claess = (By.CLASS_NAME, "android.widget.TextView")

    sc_75_finish_id = (By.ID, "{}:id/sen_cloze_done_tv".format(appPackage))


    def sc_75_swipe_answers_down(self):
        ele = self.find_element(*self.sc_75_answers_id)
        print("Size", self.getEleSize(ele))
        width = self.getEleSize(ele).get('width')
        height = self.getEleSize(ele).get('height')
        print("Location", self.getEleLocation(ele))
        x = self.getEleLocation(ele).get('x')
        y = self.getEleLocation(ele).get('y')
        print("int(width * 0.5), y - 35, y + height", int(width * 0.5), y - 25, y + height)
        try:
            self.swipeDown(int(width * 0.5), y - 80, y + height, 100)
            # self.swipeDown(int(width * 0.5), y - 25, y + height, 200)
            self.swipeDown(int(width * 0.5), 919, y + height, 300)
            self.swipeDown(int(width * 0.5), 915, y + height, 200)
        except:
            self.swipeDown(725, 959, y + height, 300)
        finally:
            self.swipeDown(718, y - 75, y + height, 500)

    # def sc_75_choose_answer(self, answer):
    #     answer = answer.lower()
    #     for item in range(97, 107):
    #         if answer == chr(item):
    #             self.find_element(*(By.ID, "{}:id/popwindow_option_{}_tv".format(self.appPackage, answer))).click()
    # def sc_75_choose_answer2(self, answers):
        # print("SC75----2")
        # ele = self.find_element(*self.sc_75_text_view_id)
        # print("Size", self.getEleSize(ele))
        # width = self.getEleSize(ele).get('width')
        # height = self.getEleSize(ele).get('height')
        # print("Location", self.getEleLocation(ele))
        # x = self.getEleLocation(ele).get('x')
        # y = self.getEleLocation(ele).get('y')
        # print("===============>w,h", width, height)
        # print('x,y', x, y)
        # while True:
        #     print("SC 75 2 True")
        #     self.swipeUp(x, (y + height - 10), y, 10)
        #     input_ele = "android.widget.TextView"
        #     if input_ele in self.page_source():
        #         pass



    def sc_75_choose_answer(self, answers, nums=5):
        ele = self.find_element(*self.sc_75_answers_id)
        print("Size", self.getEleSize(ele))
        width = self.getEleSize(ele).get('width')
        height = self.getEleSize(ele).get('height')
        print("Location", self.getEleLocation(ele))
        x = self.getEleLocation(ele).get('x')
        y = self.getEleLocation(ele).get('y')
        fill_eles1 = []
        all_fill_eles1 = self.find_elements(*self.sc_75_fill_answer_classes)
        for ele_text in all_fill_eles1:
            if not self.getText(ele_text):
                fill_eles1.append(ele_text)
        print("Answers", answers)
        print("空的数量", nums, len(fill_eles1))
        if nums <= len(fill_eles1):
            for fill, answer in zip(fill_eles1[:int(nums)], answers[:(int(nums))]):
                fill.click()
                answer = answer.lower()
                for item in range(97, 104):
                    if answer == chr(item):
                        answer_id_ele = (By.ID, "{}:id/popwindow_option_{}_tv".format(self.appPackage, answer))
                        self.find_element(*answer_id_ele).click()
        if nums > len(fill_eles1):
            for fill1, answer1 in zip(fill_eles1[:(len(fill_eles1))], answers[:(len(fill_eles1))]):
                fill1.click()
                answer1 = answer1.lower()
                for item in range(97, 104):
                    if answer1 == chr(item):
                        answer_id_ele = (By.ID, "{}:id/popwindow_option_{}_tv".format(self.appPackage, answer1))
                        self.find_element(*answer_id_ele).click()
            sleep(5)
            ele3 = self.find_element(*self.sc_75_answers_id)
            print("Size", self.getEleSize(ele3))
            width3 = self.getEleSize(ele3).get('width')
            height3 = self.getEleSize(ele3).get('height')
            print("Location", self.getEleLocation(ele3))
            x3 = self.getEleLocation(ele3).get('x')
            y3 = self.getEleLocation(ele3).get('y')
            # self.driver.swipe(x, y1, x, y2, t)
            self.swipeUp(width3 * 0.4, y3 - 30, 0, 200)

            fill_eles2 = []
            all_fill_eles2 = self.find_elements(*self.sc_75_fill_answer_classes)
            for ele_text2 in all_fill_eles2:
                if not self.getText(ele_text2):
                    fill_eles2.append(ele_text2)
            for fill2, answer2 in zip(fill_eles2[(len(fill_eles1)-5):], answers[(len(fill_eles1)-5):]):
                fill2.click()
                answer2 = answer2.lower()
                for item in range(97, 104):
                    if answer2 == chr(item):
                        answer_id_ele = (By.ID, "{}:id/popwindow_option_{}_tv".format(self.appPackage, answer2))
                        self.find_element(*answer_id_ele).click()

    def click_sc_75_submit_btn(self):
        self.find_element(*self.sc_75_submit_id).click()

    def click_sc_75_finish_btn(self):
        self.find_element(*self.sc_75_finish_id).click()

    def click_sc_75_play(self):
        self.find_elements(*self.sc_75_yeqian_claess)[1].click()

    def click_sc_75_answer_ana(self):
        self.find_elements(*self.sc_75_yeqian_claess)[2].click()

    def click_sc_75_cont(self):
        self.find_elements(*self.sc_75_yeqian_claess)[3].click()


if __name__ == "__main__":
    pass