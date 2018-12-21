from time import sleep
from selenium.webdriver.common.by import By
from testcase.page.learn_center.listening.long_conv.long_conv_all_resultPage3 import LCAllAnswerPage
from testcase.interface.sysListening.long_conv.get_long_conv_all_answer import get_all_long_conv_answer,\
    right_answer_long_conv, wrong_answer_long_conv


item_class = (By.CLASS_NAME, "android.widget.TextView")

login_page = LCAllAnswerPage()
login_page.open(noReset=True)
items = login_page.find_elements(*item_class)
for item in items:
    # print(login_page.getText(item))
    if login_page.getText(item) == "长对话":
        item.click()
        eles = login_page.get_all_list_ele()
        for i in eles[3:]:
            num = login_page.get_list_num(login_page, i)
            result = login_page.click_one_list(login_page, i)
            print(num, result)
            # answers = get_all_short_conv_answer(list=int(num))
            # curr, total = login_page.get_short_conv_lists_nums()
            # login_page.mark_words()
            # login_page.click_short_conv_step1_sure()
            # login_page.click_short_conv_step1_next()
            Flag = True
            while Flag:
                if result == 3:
                    login_page.click_back_btn()
                    Flag = False
                if result == 4:
                    login_page.click_word_finish_button()
                    login_page.click_back_btn()
                    Flag = False
                if result == 5:
                    answers = get_all_long_conv_answer(list=int(num))
                    curr, total = login_page.get_long_conv_lists_nums()
                    print(curr, total)
                    for j in range(int(curr), int(total) + 1):

                        mark_eles = login_page.find_all_mark_eles()
                        for mark_ele in mark_eles:
                            num = login_page.get_question_num(mark_ele)
                            login_page.mark_words(num, mark_ele)
                        login_page.click_long_conv_step1_sure()
                        login_page.click_long_conv_step1_next()
                            # current_right_answer = right_answer_long_conv(answers, j)
                            # current_wrong_answer = wrong_answer_long_conv(answers, j)
                            # login_page.choose_answer(current_right_answer)
                            # login_page.click_long_conv_step2_sure()
                            # login_page.click_long_conv_step2_next()
                            # question, question_num = login_page.find_all_choose_question()
                    question = login_page.find_all_choose_question_no()
                    for q in question:
                        num = login_page.get_question_num(q)
                        current_right_answer = right_answer_long_conv(answers, num)
                        print("Current right answer:", num, current_right_answer)
                        current_wrong_answer = wrong_answer_long_conv(answers, num)
                        login_page.choose_answer(num, current_right_answer)
                    sleep(1)
                    login_page.click_long_conv_step2_sure()
                    # login_page.click_long_conv_step2_next()
                    result = 5
                    print("Now result 5")
                    login_page.click_words_list_button()
                    login_page.click_word_finish_button()
                    login_page.click_back_btn()
                    Flag = False

                if result == 6:
                    answers = get_all_long_conv_answer(list=int(num))
                    curr, total = login_page.get_long_conv_lists_nums()
                    print(curr, total)
                    # for j in range(int(curr), int(total) + 1):
                    question = login_page.find_all_choose_question_no()
                    print("Question", question)
                    for q in question:
                        num = login_page.get_question_num(q)
                        current_right_answer = right_answer_long_conv(answers, num)
                        print("Current right answer:", num, current_right_answer)
                        current_wrong_answer = wrong_answer_long_conv(answers, num)
                        login_page.choose_answer(num, current_right_answer)

                    login_page.click_long_conv_step2_sure()
                    # login_page.click_long_conv_step2_next()
                    result = 5
                    print("Now result 5")
                    login_page.click_words_list_button()
                    login_page.click_word_finish_button()
                    login_page.click_back_btn()
                    Flag = False
