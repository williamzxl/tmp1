from time import sleep
from testcase.page.learn_center.all_class import AllPage
from testcase.page.study_center.study_center_main_page import StudyCenter
from testcase.interface.all_interface import AllInterface


class HomeWork(AllInterface, StudyCenter, AllPage):
    pass


def word_listening(home_work, k0, k1, click_result):
    word_dict = HomeWork()
    word_answers = word_dict.get_all_dict_answer(k0, k1)
    print("Click Result", click_result)
    if int(click_result) == 2:
        home_work.click_finish_button()
        home_work.click_back_btn()
    else:
        curr, total = home_work.get_words_list_num()
        print("curr, total", curr, total)
        for j in range(int(curr), int(total) + 1):
            current_right_answer = word_dict.dict_right_answer(word_answers, j)
            current_wrong_answer = word_dict.dict_wrong_answer(word_answers, j)
            if j == int(total):
                print(current_right_answer, current_wrong_answer)
                # home_work.hideKeyboard()
                # home_work.save_screen_shot("No KEYBoard")
                home_work.fill_answer(current_right_answer)
                # home_work.save_screen_shot("题目判定页")
                home_work.click_finish_button()
                home_work.click_back_btn()
            # login_page.click_audio_button()
            else:
                print(current_right_answer, current_wrong_answer)
                # home_work.save_screen_shot(page_name="Word", file_name="播放截图")
                current_right_answer = word_dict.dict_right_answer(word_answers, j)
                current_wrong_answer = word_dict.dict_wrong_answer(word_answers, j)
                # print(current_right_answer, current_wrong_answer)
                # try:
                #     home_work.hideKeyboard()
                # except:
                #     home_work.save_screen_shot("No KEYBoard")
                home_work.fill_answer(current_right_answer)
                # home_work.save_screen_shot("题目判定页")
                # try:
                #     home_work.hideKeyboard()
                # except:
                #     pass
                home_work.click_next_button()