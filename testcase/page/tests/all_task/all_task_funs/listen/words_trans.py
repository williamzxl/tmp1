from time import sleep
from testcase.page.learn_center.all_class import AllPage
from testcase.page.study_center.study_center_main_page import StudyCenter
from testcase.interface.all_interface import AllInterface


class HomeWork(AllInterface, StudyCenter, AllPage):
    pass


def word_trans(home_work, k0, k1, click_result):
    word_trans = HomeWork()
    word_answers = word_trans.get_all_trans_answer(k0, k1)
    # click_result = home_work.click_one_list(home_work, g)
    print("Click_result,", click_result)
    sleep(3)
    if int(click_result) == 3:
        # home_work.click_finish_button()
        home_work.click_back_btn()
    else:
        # print(home_work.page_source())
        # print("com.langlib.ncee:id/fragment_word_trans_index_tv" in home_work.page_source())
        curr_word_trans, total = home_work.get_words_trans_lists_nums()
        print(curr_word_trans, total)
        for j in range(int(curr_word_trans), int(total) + 1):
            print("Current num", j)
            if j == int(total):
                # home_work.save_screen_shot(page_name="Word_Trans", file_name="播放截图")
                current_right_answer = word_trans.word_trans_right_answer(word_answers, j)
                current_wrong_answer = word_trans.word_trans_wrong_answer(word_answers, j)
                print(current_right_answer, current_wrong_answer)
                # try:
                #     home_work.hideKeyboard()
                # except:
                #     # home_work.save_screen_shot("No KEYBoard")
                #     pass
                home_work.choose_answer(current_right_answer)
                # home_work.save_screen_shot("题目判定页")
                sleep(5)
                home_work.click_word_trans_finish_btn()
                try:
                    home_work.click_back_btn()
                except:
                    home_work.click_learning_center()
            # login_page.click_audio_button()
            else:
                # home_work.save_screen_shot(page_name="Word", file_name="播放截图")
                current_right_answer = word_trans.word_trans_right_answer(word_answers, j)
                current_wrong_answer = word_trans.word_trans_wrong_answer(word_answers, j)
                print(current_right_answer, current_wrong_answer)
                # try:
                #     home_work.hideKeyboard()
                # except:
                #     pass
                home_work.choose_answer(current_right_answer)
                sleep(2)
                # home_work.save_screen_shot("题目判定页")
                home_work.click_word_trans_next_button()