from time import sleep
from testcase.page.learn_center.all_class import AllPage
from testcase.page.study_center.study_center_main_page import StudyCenter
from testcase.interface.all_interface import AllInterface


class HomeWork(AllInterface, StudyCenter, AllPage):
    pass


def sen_ana(home_work, k0, k1, click_result):
    sen_ana = HomeWork()
    answers, answers_choice = sen_ana.get_all_sen_analysis_answer(k0, k1)
    print("answer", answers, "answer_choice", answers_choice)
    # click_result = home_work.click_one_list(home_work, g)
    sleep(10)
    print(click_result)
    if int(click_result) == 4:
        home_work.click_sen_ana_finish_button()
        home_work.click_back_btn()
    # if int(click_result) == 3:
    #     home_work.click_back_btn()
    else:
        curr_sen, total = home_work.get_sen_ana_lists_nums()
        print("Cureent_SNE", curr_sen, "Total", total)
        for curr_sen in range(curr_sen, total + 1):
            curr_ques, total_ques = home_work.get_step_nums()
            if curr_ques == None and total_ques == None:
                break
            print("Current_ques:", curr_ques, "Total_ques", total_ques)
            for curr_ques in range(curr_ques, total_ques + 1):
                right_answer, choice_EN = sen_ana.right_answer_sen_ana(answers, answers_choice,
                                                                       sen_num=curr_sen,
                                                                       ques_num=curr_ques)
                print("right_answer:", right_answer, "choice_EN:", choice_EN)
                if str(choice_EN).isupper() and choice_EN is not None:
                    if right_answer == "副词":
                        try:
                            home_work.sen_ana_choose_answer("状语")
                        except:
                            home_work.sen_ana_choose_answer(right_answer)
                    else:
                        home_work.sen_ana_choose_answer(right_answer)
                    home_work.click_sen_ana_sure_button()
                    home_work.click_sen_ana_next_question()
                if right_answer and choice_EN is None:
                    print("填写中文句子：", right_answer)
                    try:
                        home_work.fill_CN_answer(right_answer)
                        home_work.click_sen_ana_sure_button()
                    except:
                        home_work.click_to_check_CN()
                        home_work.click_sen_ana_sure_button()
                    sleep(5)
                    try:
                        home_work.click_sen_ana_finish_button()
                        home_work.click_sen_ana_next_sen()
                    except:
                        pass
                if right_answer == 0 and choice_EN is None:
                    try:
                        home_work.click_to_check_CN()
                        home_work.click_sen_ana_sure_button()
                        home_work.click_sen_ana_finish_button()
                        home_work.click_sen_ana_next_sen()
                    except:
                        pass
                if int(curr_sen) == int(total) and curr_ques == total_ques:
                    try:
                        home_work.click_sen_ana_sure_button()
                        home_work.click_sen_ana_finish_button()
                    except:
                        pass
                if int(curr_sen) == int(total) and (right_answer == 0 or choice_EN is None):
                    # login_page.click_sen_ana_sure_button()
                    # login_page.click_sen_ana_finish_button()
                    home_work.click_sen_fill_words_list_button()
                    home_work.click_words_list_finish()
                    home_work.click_back_btn()