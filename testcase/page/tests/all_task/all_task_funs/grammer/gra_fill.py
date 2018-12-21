import os
from time import sleep
from testcase.page.learn_center.all_class import AllPage
from testcase.page.study_center.study_center_main_page import StudyCenter
from testcase.interface.all_interface import AllInterface


class HomeWork(AllInterface, StudyCenter, AllPage):
    pass


def gra_fill(home_work, k0, k1, click_result):
    print("开始作答语法填空")
    gra_fill = HomeWork()
    answers = gra_fill.get_all_gra_fill_answer(k0, k1)
    print("answer", answers)
    # click_result = home_work.click_one_list(home_work, g)
    print("click_result", click_result)
    right_answer = gra_fill.gra_fill_right_answer(answers)
    if click_result == 3:
        home_work.click_back_btn()
    if click_result == 5:
        home_work.click_gra_fill_next_step()
        home_work.gra_fill_fill_answer(home_work, answers=right_answer, nums=10)
        home_work.click_gra_fill_submit()
        home_work.click_sure_button()
        sleep(5)
        try:
            home_work.click_to_check_answer()
        except:
            w, h = home_work.getSize()
            home_work.tapEle(w * 0.5, h - 90, w * 0.5, h - 92, 50)
            cmd2 = 'adb shell input tap {} {}'.format(w * 0.5, h - 90)
            os.system(cmd2)
        home_work.click_gra_fill_finish_button()
        home_work.click_gra_fill_finish_all()
        home_work.click_back_btn()

    if click_result == 8:
        home_work.gra_fill_fill_answer(home_work, answers=right_answer, nums=10)
        home_work.click_gra_fill_submit()
        home_work.click_sure_button()
        home_work.click_finish_button()
        home_work.click_gra_fill_finish_all()
        home_work.click_back_btn()