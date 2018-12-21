from time import sleep
# from appium.webdriver.webdriver import By
from selenium.webdriver.common.by import By
# from testcase.common.basePage import BasePage
from testcase.page.reg_login_page.login_page.loginPage import LoginPage
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
login_page = LoginPage()
login_page.open(noReset=True)
sleep(15)
# print("test", login_page)
# c = login_page.get_driver()
# print("C",c)
# sleep(15)
# print(login_page.page_source_test())
# sleep(15)
# step = login_page.find_element(*step_1_id)
# print(login_page.getText(step))
# login_page.find_element(*action_id).click()
# sleep(5)

# login_page.find_element(*edit_id).send_keys("hshhs")
# login_page.find_element(*next_id).click()
# b = login_page.get_driver()
# print("b", b)
# print(b.page_source())
# b.find_element(*edit_id).send_keys("hshhs")
# b.find_element(*next_id).click()
# print(b.current_context())


# login_page.save_screen_shot("Quick")
# print(login_page.page_source())
# login_page.find_element(*evaluation_id).click()
# login_page.find_element(*action_id).click()
# login_page.find_element(*radio_id).click()
# print("Fini")
# sleep(30)
#
# print("Test")

# print(login_page.getCurrentUrl())
# print(login_page.page_source())
# login_page.save_screen_shot("Quick")
# print(a in login_page.page_source())
# login_page.find_element(*web_class).click()
# login_page.find_elements(*radio_classes)[0].click()
# login_page.find_element(*next_id).click()
buttons = [
    radio_id,
    radio_b_id,
    next_id,
]

def click_test(ele):
    login_page.find_element(*ele).click()

for i in range(1, 102):
    try:
        pool = ThreadPool(10)
        result = pool.map(click_test, buttons)
        pool.close()
        pool.join()
    except:
        print("No Click")
        login_page.save_screen_shot("Quick")



