from multiprocessing import Process
import multiprocessing
import time
from time import sleep
# from appium.webdriver.webdriver import By
from selenium.webdriver.common.by import By
# from testcase.common.basePage import BasePage
from testcase.page.login_page.loginPage import LoginPage
from testcase.page.learn_center.listening.word_trans.word_translating_all_resultPage3 import WTAllAnswerPage
from testcase.interface.sysListening.word_trans.word_trans_all_answer import get_all_trans_answer,\
    right_answer_trans, wrong_answer_trans
from multiprocessing.dummy import Pool as ThreadPool

item_class = (By.CLASS_NAME, "android.widget.TextView")
evaluation_id = (By.ID, 'com.langlib.cee:id/evaluation')
action_id = (By.ID, 'com.langlib.cee:id/evaluation_begin_tv')
# com.langlib.cee:id/evaluation_begin_tv
a = "com.langlib.cee:id/fragment_word_trans_detail_answer_a"
radio_id = (By.ID, "com.langlib.cee:id/fragment_word_trans_detail_answer_a")
radio_b_id = (By.ID, "com.langlib.cee:id/fragment_word_trans_detail_answer_b")
radio_classes = (By.CLASS_NAME, "android.widget.RadioButton")
edit_id = (By.ID, "com.langlib.cee:id/write_measure_edit")
next_id = (By.ID, "com.langlib.cee:id/senavaly_quest_next_quest")
title_id = (By.ID, "com.langlib.cee:id/title_iframe_title_tv")
web_class = (By.CLASS_NAME, "android.widget.ScrollView")
step_1_id = (By.ID, "com.langlib.cee:id/measure_step_one")

def click_ele(ele):
    ele.click()


def main(ids):
    for i in ids:
        p = multiprocessing.Process(target=click_ele, args=(i,))
        p.start()
        p.join()
    print("Sub-process done.")

if __name__ == '__main__':
    ids = []
    login_page = LoginPage()
    login_page.open(noReset=True)
    radio_id_bu = login_page.find_element(*radio_id)
    next_id_bu = login_page.find_element(*next_id)
    ids.append(radio_id_bu)
    ids.append(next_id_bu)
    print(ids)
    for i in range(100):
        main(ids)


