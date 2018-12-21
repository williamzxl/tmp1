from testcase.page.learn_center.all_class import AllPage
from testcase.page.study_center.study_center_main_page import StudyCenter
from testcase.interface.all_interface import AllInterface


class HomeWork(AllInterface, StudyCenter, AllPage):
    pass


def fangxiezaoju(home_work, k0, k1, click_result):
    fangxie_zaoju = HomeWork()
    fangxie_zaoju_answers = fangxie_zaoju.get_all_fangxie_zaoju_answer(k0, k1)
    # click_result = home_work.click_one_list(home_work, g)
    if int(click_result) == 2:
        home_work.click_finish_button()
        home_work.click_back_btn()
    else:
        curr_group, total = home_work.get_fangxie_zaoju_groups_nums()
        print("Cureent_Group", curr_group, "Total", total)
        for curr_sen in range(curr_group, total + 1):
            curr_ques, total_ques = home_work.get_fangxie_zaoju_step_nums()
            print("Current_ques:", curr_ques, "Total_ques", total_ques)
            for curr_ques in range(curr_ques, total_ques + 1):
                curr_group, total = home_work.get_fangxie_zaoju_groups_nums()
                if curr_ques == total_ques and curr_group == total:
                    current_right_answer = fangxie_zaoju.fangxie_zaoju_right_answer(
                        fangxie_zaoju_answers, curr_group, curr_ques)
                    current_wrong_answer = fangxie_zaoju.fangxie_zaoju_wrong_answer(
                        fangxie_zaoju_answers, curr_group, curr_ques)
                    print(current_right_answer, current_wrong_answer)
                    home_work.fangxie_zaoju_fill_CN_answer(current_right_answer)
                    home_work.click_fangxie_zaoju_submit_btn()
                    home_work.click_fangxie_zaoju_finish_btn()
                    home_work.click_back_btn()
                else:
                    current_right_answer = fangxie_zaoju.fangxie_zaoju_right_answer(
                        fangxie_zaoju_answers, curr_group, curr_ques)
                    current_wrong_answer = fangxie_zaoju.fangxie_zaoju_wrong_answer(
                        fangxie_zaoju_answers, curr_group, curr_ques)
                    print(current_right_answer, current_wrong_answer)
                    home_work.fangxie_zaoju_fill_CN_answer(current_right_answer)
                    home_work.click_fangxie_zaoju_submit_btn()
                    home_work.click_fangxie_zaoju_next_step_btn()