import os
from appium.webdriver.webdriver import By
from testcase.page.learn_center.all_class import AllPage
from testcase.page.study_center.study_center_main_page import StudyCenter
from testcase.interface.all_interface import AllInterface
from utils.config import get_device_name


class HomeWork(AllInterface, StudyCenter, AllPage):
    pass


def wenzhang_xunlian(home_work, k0, k1, click_result):
    print("文章训练,====>")
    Flag = True
    while Flag:
        while "第一步" in home_work.page_source():
            print("第一步")
            if "android.widget.EditText" not in home_work.page_source():
                print('"android.widget.EditText" not in')
                x, y = home_work.getSize()
                print("x,y", x, y)
                devices_name = get_device_name()
                for j in range(int(y * 0.6), y, 25):
                    print("x * 0.5 * 0.5, j", x * 0.5 * 0.5, j)
                    cmd1 = 'adb -s {} shell input tap {} {}'.format(devices_name, x * 0.5 * 0.5, j)
                    os.system(cmd1)
                w, h = home_work.getSize()
                home_work.tapEle(w * 0.5, h - 90, w * 0.5, h - 92, 50)
                cmd2 = 'adb -s {} shell input tap {} {}'.format(devices_name, w * 0.5, h - 90)
                os.system(cmd2)
            input_id = (By.CLASS_NAME, "android.widget.EditText")
            if "android.widget.EditText" in home_work.page_source():
                print('"android.widget.EditText" in')
                try:
                    ele = home_work.find_element(*input_id)
                    ele.click()
                    ele.send_keys("Test")
                except:
                    pass
                home_work.hideKeyboard()
                w, h = home_work.getSize()
                home_work.tapEle(w * 0.5, h - 90, w * 0.5, h - 92, 50)
                cmd2 = 'adb -s {} shell input tap {} {}'.format(devices_name, w * 0.5, h - 90)
                os.system(cmd2)

        while "第二步" in home_work.page_source():
            print('"第二步"')
            w, h = home_work.getSize()
            home_work.tapEle(w * 0.5, h - 90, w * 0.5, h - 92, 50)
            cmd2 = 'adb -s {} shell input tap {} {}'.format(devices_name, w * 0.5, h - 90)
            os.system(cmd2)

        input_id2 = (By.ID, "com.langlib.ncee:id/fragment_article_train_section_train_quest_2_et")
        while "段落主旨句" in home_work.page_source():
            print("部分")
            try:
                ele = home_work.find_element(*input_id2)
                ele.click()
                ele.send_keys("Test")
            except:
                pass
            home_work.hideKeyboard()
            w, h = home_work.getSize()
            home_work.tapEle(w * 0.5, h - 90, w * 0.5, h - 92, 50)
            cmd2 = 'adb -s {} shell input tap {} {}'.format(devices_name, w * 0.5, h - 90)
            os.system(cmd2)

        choose_class_id = (By.CLASS_NAME, "android.widget.RadioButton")
        while "真题模考" in home_work.page_source():
            print("真题模考")
            try:
                ele = home_work.find_element(*choose_class_id)
                ele.click()
            except:
                pass
            w, h = home_work.getSize()
            home_work.tapEle(w * 0.5, h - 90, w * 0.5, h - 92, 50)
            cmd2 = 'adb -s shell input tap {} {}'.format(devices_name, w * 0.5, h - 90)
            os.system(cmd2)
        if "学习中心" in home_work.page_source():
            print("学习中心")
            w, h = home_work.getSize()
            home_work.tapEle(w * 0.5, h - 90, w * 0.5, h - 92, 50)
            cmd2 = 'adb -s shell input tap {} {}'.format(devices_name, w * 0.5, h - 90)
            os.system(cmd2)
            break
        if "学习打卡" in home_work.page_source():
            home_work.click_learn_card_close_btn()
            break
        else:
            break