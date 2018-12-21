from testcase.page.learn_center.all_class import AllPage
from testcase.page.study_center.study_center_main_page import StudyCenter
from testcase.interface.all_interface import AllInterface


class HomeWork(AllInterface, StudyCenter, AllPage):
    pass


def sec_train(home_work, k0, k1, click_result):
    title = home_work.get_page_title()
    if str(title) != "段落训练":
        pass
    if True:
        sec_train = HomeWork()
        answers = sec_train.get_all_section_train_answers(k0, k1)
        print("answer", answers)
        # click_result = home_work.click_one_list(home_work, g)
        step2_answers, _ = sec_train.sen_train_right_answer(answers)
        w_step2_answers, _ = sec_train.sen_train_wrong_answer(answers)
        _, step3_answers = sec_train.sen_train_right_answer(answers)
        _, w_step3_answers = sec_train.sen_train_wrong_answer(answers)
        print(click_result)
        if int(click_result) == 5:
            home_work.click_sect_train_step1_next_button()
            home_work.sect_train_step2_fill_answer(step2_answers)
            home_work.click_sect_train_step2_sure_button()
            home_work.click_sect_train_step2_next_btn()
            curr_q, total_q = home_work.get_sect_train_step3_lists_nums()
            for i in range(curr_q, total_q + 1):
                if i != total_q:
                    home_work.sect_train_step3_choose_answer(step3_answers[i - 1])
                    home_work.click_sect_train_step3_sure_btn()
                    home_work.click_sect_train_step3_next_ques_btn()
                if i == total_q:
                    try:
                        home_work.click_sect_train_mask_CN()
                    except:
                        home_work.sect_train_step3_fill_CN_answer(step3_answers[i - 1])
                    home_work.click_sect_train_step3_sure_btn()
                    home_work.click_sect_train_step3_finish_button()
                    home_work.click_sect_train_step3_check_result_btn()
        if int(click_result) == 6:
            home_work.sect_train_step3_fill_CN_answer("Hehe")
            home_work.click_sect_train_step3_sure_btn()
            home_work.click_sect_train_step3_next_ques_btn()
            click_result = 7
        if int(click_result) == 7:
            curr_q, total_q = home_work.get_sect_train_step3_lists_nums()
            for i in range(curr_q, total_q + 1):
                if i != total_q:
                    home_work.sect_train_step3_choose_answer(step3_answers[i - 1])
                    home_work.click_sect_train_step3_sure_btn()
                    home_work.click_sect_train_step3_next_ques_btn()
                if i == total_q:
                    try:
                        home_work.click_sect_train_mask_CN()
                    except:
                        home_work.sect_train_step3_fill_CN_answer(step3_answers[i - 1])
                    home_work.click_sect_train_step3_sure_btn()
                    home_work.click_sect_train_step3_finish_button()
                    home_work.click_sect_train_step3_check_result_btn()
        home_work.click_back_btn()