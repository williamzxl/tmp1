import os
from time import sleep
from testcase.page.learn_center.all_class import AllPage
from testcase.page.study_center.study_center_main_page import StudyCenter
from testcase.interface.all_interface import AllInterface


class HomeWork(AllInterface, StudyCenter, AllPage):
    pass


def wanxing_xunlian(home_work, k0, k1, click_result):
    title = home_work.get_page_title()
    if str(title) != "完型训练":
        pass
    if True:
        cloze_test = HomeWork()
        answers = cloze_test.get_all_cloze_test_answer(k0, k1)
        sleep(10)
        if int(click_result) == 2:
            home_work.click_finish_button()
            home_work.click_back_btn()

        if click_result == 5:
            try:
                print("Click next step")
                home_work.click_cloze_test_step1_next_btn()
            except:
                w, h = home_work.getSize()
                home_work.tapEle(w * 0.5, h - 90, w * 0.5, h - 92, 50)
                cmd2 = 'adb shell input tap {} {}'.format(w * 0.5, h - 90)
                print(cmd2)
                os.system(cmd2)

            for ct in range(1, len(answers) + 1):
                CN_answer, EN_answer = cloze_test.cloze_test_right_answer(answers, ct)
                home_work.click_cloze_test_part1_answer(CN_answer)
                home_work.cloze_test_choose_answer(EN_answer)
                if ct != len(answers):
                    home_work.click_cloze_test_step2_next_btn()
                else:
                    home_work.click_cloze_test_finish_btn()
                    home_work.click_back_btn()

        if click_result == 6:
            curr_cloze_ques = home_work.get_cloze_test_curr_ques()
            for ct2 in range(curr_cloze_ques, len(answers) + 1):
                CN_answer, EN_answer = cloze_test.cloze_test_right_answer(answers, ct2)
                print(CN_answer, EN_answer)
                home_work.click_cloze_test_part1_answer(CN_answer)
                home_work.cloze_test_choose_answer(EN_answer)
                if ct2 != len(answers):
                    home_work.click_cloze_test_step2_next_btn()
                else:
                    home_work.click_cloze_test_finish_btn()
                    home_work.click_back_btn()