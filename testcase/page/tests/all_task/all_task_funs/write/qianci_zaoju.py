from time import sleep
from testcase.page.learn_center.all_class import AllPage
from testcase.page.study_center.study_center_main_page import StudyCenter
from testcase.interface.all_interface import AllInterface


class HomeWork(AllInterface, StudyCenter, AllPage):
    pass


def qianci_zaoju(home_work, k0, k1, click_result):
    qianci_zaoju = HomeWork()
    answers = qianci_zaoju.get_all_qianci_zaoju_answer(k0, k1)
    print("answer", answers)
    # click_result = home_work.click_one_list(home_work, g)
    sleep(10)
    print(click_result)
    if int(click_result) == 2:
        home_work.click_finish_button()
        home_work.click_back_btn()
    # if int(click_result) == 3:
    #     home_work.click_back_btn()
    else:
        curr_sen, total_sen = home_work.get_qc_curr_sen_nums()
        print("Cureent_SNE", curr_sen, "Total", total_sen)
        for curr_sen in range(curr_sen, total_sen + 1):
            curr_ques, total_ques = home_work.get_qc_current_ques_step_nums()
            for curr_ques in range(curr_ques, total_ques + 1):
                right_answer = qianci_zaoju.qianci_zaoju_right_answer(answers, sen_num=curr_sen,
                                                                      ques_num=curr_ques)
                if int(curr_sen) == int(total_sen) and curr_ques == total_ques:
                    try:
                        home_work.qc_fill_answer(right_answer)
                        home_work.hideKeyboard()
                        home_work.click_qc_submit_btn()
                        home_work.click_qc_finish_btn()
                        home_work.click_back_btn()
                    except:
                        pass
                # if int(curr_sen) != int(total_sen) and curr_ques == total_ques:
                #     home_work.qc_fill_answer(right_answer)
                #     home_work.click_qc_submit_btn()
                #     home_work.click_qc_finish_btn()
                #     home_work.click_back_btn()
                else:
                    home_work.qc_fill_answer(right_answer)
                    home_work.hideKeyboard()
                    home_work.click_qc_submit_btn()
                    home_work.click_qc_next_ques_btn()