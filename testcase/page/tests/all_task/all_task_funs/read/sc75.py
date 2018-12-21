from time import sleep
from testcase.page.learn_center.all_class import AllPage
from testcase.page.study_center.study_center_main_page import StudyCenter
from testcase.interface.all_interface import AllInterface


class HomeWork(AllInterface, StudyCenter, AllPage):
    pass


def sc75(home_work, k0, k1, click_result):
    sc_75 = HomeWork()
    print("k[0], k[1]", k0, k1)
    sc_answers = sc_75.get_all_sc_75_answer(k0, k1)
    print("SC 75 answers", sc_answers)
    # click_result = home_work.click_one_list(home_work, g)
    sleep(10)
    sc_right_answers = sc_75.sc_75_right_answer(sc_answers)
    if click_result == 5:
        home_work.click_sc_75_next_btn()
        home_work.sc_75_swipe_answers_down()
        # try:
        #     home_work.sc_75_choose_answer2(sc_right_answers)
        # except:
        home_work.sc_75_choose_answer(sc_right_answers)
        home_work.click_sc_75_submit_btn()
        home_work.click_sc_75_finish_btn()
        home_work.click_back_btn()

    if click_result == 6:
        home_work.sc_75_swipe_answers_down()
        # try:
        #     home_work.sc_75_choose_answer2(sc_right_answers)
        # except:
        home_work.sc_75_choose_answer(sc_right_answers)
        home_work.click_sc_75_submit_btn()
        home_work.click_sc_75_finish_btn()
        home_work.click_back_btn()