from time import sleep
from testcase.page.learn_center.all_class import AllPage
from testcase.page.study_center.study_center_main_page import StudyCenter
from testcase.interface.all_interface import AllInterface


class HomeWork(AllInterface, StudyCenter, AllPage):
    pass


def word_spell(home_work, k0, k1, click_result):
    print("单词拼写,单词拼写")
    word_spell = HomeWork()
    word_answers = word_spell.get_all_word_spell_answer(k0, k1)
    # click_result = home_work.click_one_list(home_work, g)
    if int(click_result) == 2:
        home_work.click_finish_button()
        home_work.click_back_btn()
    if int(click_result) == 3:
        home_work.click_learning_center()
    if click_result == None:
        try:
            home_work.click_back_btn()
        except:
            home_work.click_learning_center()
    else:
        curr, total = home_work.get_word_spell_list_num()
        print(curr, total)
        for j in range(int(curr), int(total) + 1):
            if j == int(total):
                current_right_answer = word_spell.word_spell_right_answer(word_answers, j)
                current_wrong_answer = word_spell.word_spell_wrong_answer(word_answers, j)
                print(current_right_answer, current_wrong_answer)
                # home_work.hideKeyboard()
                # home_work.save_screen_shot("No KEYBoard")
                home_work.fill_word_spell_answer(current_right_answer)
                # home_work.save_screen_shot("题目判定页")
                home_work.click_word_spell_finish_button()
                home_work.click_back_btn()
            # login_page.click_audio_button()
            else:
                # home_work.save_screen_shot(page_name="Word", file_name="播放截图")
                current_right_answer = word_spell.word_spell_right_answer(word_answers, j)
                current_wrong_answer = word_spell.word_spell_wrong_answer(word_answers, j)
                print(current_right_answer, current_wrong_answer)
                # try:
                #     home_work.hideKeyboard()
                # except:
                #     home_work.save_screen_shot("No KEYBoard")
                home_work.fill_word_spell_answer(current_right_answer)
                # home_work.save_screen_shot("题目判定页")
                # try:
                #     home_work.hideKeyboard()
                # except:
                #     pass
                try:
                    home_work.click_word_spell_next_button()
                except:
                    sleep(5)
                    home_work.click_word_spell_next_button()