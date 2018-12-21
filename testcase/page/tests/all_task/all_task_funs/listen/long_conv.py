from time import sleep
from testcase.page.learn_center.all_class import AllPage
from testcase.page.study_center.study_center_main_page import StudyCenter
from testcase.interface.all_interface import AllInterface


class HomeWork(AllInterface, StudyCenter, AllPage):
    pass


def long_conv(home_work, k0, k1, click_result):
    long_conv = HomeWork()
    all_answers = long_conv.get_all_long_conv_answer(k0, k1)
    print(len(all_answers))
    # click_result = home_work.click_one_list(home_work, g)
    print("Click_result,", click_result)
    sleep(10)
    if click_result == 4:
        home_work.click_long_conv_words_list_finish_btn()
        home_work.click_back_btn()

    if int(click_result) == 3:
        home_work.click_back_btn()
        try:
            home_work.click_sure_button()
        except:
            pass

    if click_result == 5 or click_result == 0:
        mark_eles = home_work.find_all_long_conv_mark_eles()
        print("MarkELEs", mark_eles)
        for mark_ele in mark_eles:
            home_work.long_conv_step1_mark_words(mark_ele, len(all_answers))
        home_work.click_long_conv_step1_sure()
        home_work.click_long_conv_step1_next()
        choose_eles = home_work.find_all_long_conv_choose_question_no()
        sleep(5)
        # for choose_ele in choose_eles[:2]:
        #     ques_num = home_work.get_long_conv_question_num(choose_ele)
        #     right_answer = long_conv.long_conv_right_answer(all_answers, ques_num)
        #     print(ques_num, right_answer)
        #     home_work.choose_long_conv_step2_answer(ques_num, right_answer)
        # x, y = home_work.getSize()
        # home_work.swipeUp(x * 0.8 * 0.8, y * 0.8, 0, 200)
        # choose_eles2 = home_work.find_all_long_conv_choose_question_no()
        # print(len(all_answers) == 3)
        # print(choose_eles2)
        # if len(all_answers) == 4:
        #     for choose_ele2 in choose_eles2[-2:]:
        #         ques_num = home_work.get_long_conv_question_num(choose_ele2)
        #         right_answer = long_conv.long_conv_right_answer(all_answers, ques_num)
        #         if ques_num == 3:
        #             home_work.choose_long_conv_step2_answer(-2, right_answer)
        #         if ques_num == 4:
        #             home_work.choose_long_conv_step2_answer(-1, right_answer)
        # if len(all_answers) == 3:
        #     for choose_ele2 in choose_eles2[-1:]:
        #         ques_num = home_work.get_long_conv_question_num(choose_ele2)
        #         right_answer = long_conv.long_conv_right_answer(all_answers, ques_num)
        #         print(ques_num, right_answer)
        #         home_work.choose_long_conv_step2_answer(ques_num, right_answer)
        # home_work.click_long_conv_step2_sure()
        # home_work.click_long_conv_step2_words_list()
        # home_work.click_long_conv_words_list_finish_btn()
        home_work.click_back_btn()
        sleep(5)
        home_work.click_sure_button()

    if click_result == 6:
        choose_eles = home_work.find_all_long_conv_choose_question_no()
        for choose_ele, i in zip(choose_eles[:2], [0, 1]):
            ques_num = home_work.get_long_conv_question_num(choose_ele)
            right_answer = long_conv.long_conv_right_answer(all_answers, ques_num)
            print("Ques_num, Right_answer", ques_num, right_answer)
            home_work.choose_long_conv_step2_answer(ques_num, right_answer)
            sleep(5)
        print("Finish 1,2")
        x, y = home_work.getSize()
        home_work.swipeUp(x * 0.8 * 0.8, y * 0.8, 0, 200)
        sleep(5)
        choose_eles2 = home_work.find_all_long_conv_choose_question_no()
        all_c_item = home_work.find_all_long_conv_c_items()
        print("All 000000000000000000000000000000000", all_c_item)
        print("len(all_c_item)", len(all_c_item))
        if "4." in home_work.page_source():
            print("choose_eles2", choose_eles2)
            for choose_ele2, ques_num in zip(choose_eles2[-2:], [3, 4]):
                right_answer = long_conv.long_conv_right_answer(all_answers, ques_num)
                # ques_num = home_work.get_long_conv_question_num(choose_ele2)
                ques_num = ques_num - 2
                print("ques_num, right_answer", ques_num, right_answer)
                if right_answer == "C":
                    if len(all_c_item) == 3:
                        home_work.choose_long_conv_step2_answer(ques_num, right_answer, c=3)
                    else:
                        home_work.choose_long_conv_step2_answer(ques_num, right_answer)
                else:
                    print("Right answer", right_answer, "Ques_num", ques_num)
                    home_work.choose_long_conv_step2_answer(ques_num - 1, right_answer, c=3)
        if "4." not in home_work.page_source() and "3." in home_work.page_source():
            for choose_ele2 in choose_eles2[-1:]:
                ques_num = home_work.get_long_conv_question_num(choose_ele2)
                right_answer = long_conv.long_conv_right_answer(all_answers, ques_num)
                print(ques_num, right_answer)
                home_work.choose_long_conv_step2_answer(ques_num, right_answer)
        home_work.click_long_conv_step2_sure()
        home_work.click_long_conv_step2_words_list()
        home_work.click_long_conv_words_list_finish_btn()
        home_work.click_back_btn()