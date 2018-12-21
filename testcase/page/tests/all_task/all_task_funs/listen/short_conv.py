import os
from time import sleep
from testcase.page.learn_center.all_class import AllPage
from testcase.page.study_center.study_center_main_page import StudyCenter
from testcase.interface.all_interface import AllInterface


class HomeWork(AllInterface, StudyCenter, AllPage):
    pass


def short_conv(home_work, k0, k1, click_result):
    short_conv = HomeWork()
    all_answers = short_conv.get_all_short_conv_answer(k0, k1)
    print("Click_result,", click_result)
    sleep(10)
    if int(click_result) == 2 or int(click_result) == 4:
        try:
            home_work.click_finish_button()
        except:
            w, h = home_work.getSize()
            home_work.tapEle(w * 0.5, h - 90, w * 0.5, h - 92, 50)
            cmd2 = 'adb shell input tap {} {}'.format(w * 0.5, h - 90)
            os.system(cmd2)
        home_work.click_back_btn()
    if int(click_result) == 6:
        Flag = True
        while Flag:
            curr, total = home_work.get_short_conv_lists_nums()
            print("curr, total", curr, total)
            for j in range(int(curr), int(total) + 1):
                current_right_answer = short_conv.right_answer_short_conv(all_answers, j)
                current_wrong_answer = short_conv.wrong_answer_short_conv(all_answers, j)
                print("current_right_answer,", current_right_answer)
                home_work.choose_short_conv_answer(current_right_answer)
                home_work.click_short_conv_step2_sure()
                home_work.click_short_conv_step2_next()
                Flag = False
    else:
        Flag = True
        while Flag:
            curr, total = home_work.get_short_conv_lists_nums()
            print("curr, total", curr, total)
            for j in range(int(curr), int(total) + 1):
                home_work.mark_words()
                home_work.click_short_conv_step1_sure()
                home_work.click_short_conv_step1_next()
                current_right_answer = short_conv.right_answer_short_conv(all_answers, j)
                current_wrong_answer = short_conv.wrong_answer_short_conv(all_answers, j)
                print("current_right_answer,", current_right_answer)
                home_work.choose_short_conv_answer(current_right_answer)
                home_work.click_short_conv_step2_sure()
                sleep(5)
                home_work.click_short_conv_step2_next()
                if curr == total:
                    try:
                        home_work.click_words_list_button()
                    except:
                        w, h = home_work.getSize()
                        home_work.tapEle(w * 0.5, h - 90, w * 0.5, h - 92, 50)
                        cmd2 = 'adb shell input tap {} {}'.format(w * 0.5, h - 90)
                        os.system(cmd2)
                    home_work.click_word_finish_button()
                    home_work.click_back_btn()
                    Flag = False