from time import sleep, ctime
# from appium.webdriver.webdriver import By
from selenium.webdriver.common.by import By
# from testcase.common.basePage import BasePage
from testcase.page.reg_login_page.login_page.loginPage import LoginPage
import os

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


def find_eles(driver, ele_id):
    # ele1 = []
    # ele1.append(driver.find_element(*ele_id))
    print(driver.find_element(*ele_id))
    return driver.find_element(*ele_id)

def click_ele(ele):
    print("Start Time:",ctime())
    ele.click()
    print("End Time:", ctime())

def click_next(driver):
    print("Start Tap Time:", ctime())
    driver.tap(0,1782,1080,1920,0.01)
    print("End Tap Time:", ctime())


# ele_ids = [radio_id, next_id]
ele_ids = [radio_id]

jd_back_id = (By.ID, "com.jingdong.app.mall:id/fg")

cmds = 'adb shell input tap 542 626'
cmds2 = 'adb shell input tap 550 1008'
def main(login_page):
    print("Now Time:",ctime())
    # jd_back_ele = login_page.find_element(*jd_back_id)
    # print(login_page.getText(jd_back_ele))
    while True:
        c = ctime().split(" ")[3].split(":")
        print(c, c[0], c[1])
        if c[0] == "10" or c[1] == "59":
            while True:
                print("Click")
                os.system(cmds)
                sleep(0.05)
                os.system(cmds2)
        else:
            print("Time is not ready")

    # eles = []
    # threads = []
    # #
    # for i in ele_ids:
    #     eles.append(find_eles(login_page, i))
    #
    # nloops = range(len(eles))
    # for i in nloops:
    #     t0 = threading.Thread(target=find_eles, args=(login_page, eles))
    #     print(t0)
    #     t1 = threading.Thread(target=click_ele, args=(eles[i],))
    #     t2 = threading.Thread(target=click_next, args=(login_page,))
    #     threads.append(t1)
    # print(threads)
    #
    # for i in nloops:
    #     t0.start()
    #     threads[i].start()
    #     t2.start()
    #     t2.join()

    # for i in nloops:
    #     threads[i].join()
    #     t2.join()


if __name__ == '__main__':
    login_page = LoginPage()
    login_page.open(noReset=True)
    sleep(15)
    main(login_page)
    # for i in range(100):
    #     main(login_page)