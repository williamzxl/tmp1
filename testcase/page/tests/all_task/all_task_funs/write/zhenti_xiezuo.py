import os
from time import sleep
from testcase.page.learn_center.all_class import AllPage
from testcase.page.study_center.study_center_main_page import StudyCenter
from testcase.interface.all_interface import AllInterface


class HomeWork(AllInterface, StudyCenter, AllPage):
    pass


def zhenti_xiezuo(home_work, k0, k1, click_result):
    try:
        zhenti_xiezuo = HomeWork()
        all_answers = zhenti_xiezuo.get_all_zhenti_xiezuo_answer(k0, k1)
        zt_right_answer = zhenti_xiezuo.zhenti_xiezuo_right_answer(all_answers)
        zt_wrong_answer = zhenti_xiezuo.zhenti_xiezuo_wrong_answer(all_answers)
        print("zt_wrong_answer", zt_right_answer, zt_wrong_answer)
        try:
            home_work.click_zhenti_xiezuo_start_to_answer_btn()
        except:
            pass
        if "暂存" in home_work.page_source():
            pass
        while "暂存" not in home_work.page_source():
            try:
                home_work.click_zhenti_xiezuo_start_to_answer_btn()
            except:
                pass
            if "暂存" in home_work.page_source():
                break
            if "暂存" not in home_work.page_source():
                w, h = home_work.getSize()
                home_work.tapEle(w * 0.5, h - 90, w * 0.5, h - 92, 50)
                cmd2 = 'adb shell input tap {} {}'.format(w * 0.5, h - 90)
                os.system(cmd2)
        home_work.fill_zhenti_xiezuo_answer(zt_right_answer)
        home_work.click_zhenti_xiezuo_zancun_btn()
        home_work.click_zhenti_xiezuo_submit_id()
        sleep(5)
        home_work.click_sure_button()
        sleep(3)
        home_work.click_back_btn()
        try:
            home_work.click_sure_button()
        except:
            home_work.click_learning_center()
    except:
        try:
            home_work.click_zhenti_xiezuo_start_to_answer_btn()
        except:
            pass
        if "暂存" in home_work.page_source():
            pass
        while "暂存" not in home_work.page_source():
            try:
                home_work.click_zhenti_xiezuo_start_to_answer_btn()
            except:
                pass
            if "暂存" in home_work.page_source():
                break
            if "暂存" not in home_work.page_source():
                w, h = home_work.getSize()
                home_work.tapEle(w * 0.5, h - 90, w * 0.5, h - 92, 50)
                cmd2 = 'adb shell input tap {} {}'.format(w * 0.5, h - 90)
                os.system(cmd2)
        wrong_answers = "a " * 80
        home_work.fill_zhenti_xiezuo_answer(wrong_answers)
        home_work.click_zhenti_xiezuo_zancun_btn()
        home_work.click_zhenti_xiezuo_submit_id()
        sleep(5)
        home_work.click_sure_button()
        sleep(3)
        home_work.click_back_btn()
        try:
            home_work.click_sure_button()
        except:
            home_work.click_learning_center()