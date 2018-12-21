import re
from time import sleep
from testcase.page.tests.all_task.all_task_funs.grammer.error_find import error_find
from testcase.page.tests.all_task.all_task_funs.grammer.gra_choice import gra_choice
from testcase.page.tests.all_task.all_task_funs.grammer.gra_fill import gra_fill

from testcase.page.tests.all_task.all_task_funs.listen.word_listening import word_listening
from testcase.page.tests.all_task.all_task_funs.listen.long_conv import long_conv
from testcase.page.tests.all_task.all_task_funs.listen.sen_fill import sen_fill
from testcase.page.tests.all_task.all_task_funs.listen.short_conv import short_conv
from testcase.page.tests.all_task.all_task_funs.listen.words_trans import word_trans

from testcase.page.tests.all_task.all_task_funs.read.sc75 import sc75
from testcase.page.tests.all_task.all_task_funs.read.sec_train import sec_train
from testcase.page.tests.all_task.all_task_funs.read.sen_ana_fun import sen_ana
from testcase.page.tests.all_task.all_task_funs.read.wanxing_xunlian import wanxing_xunlian
from testcase.page.tests.all_task.all_task_funs.read.wenzhang_xunlian import wenzhang_xunlian

from testcase.page.tests.all_task.all_task_funs.write.fangxiezaoju import fangxiezaoju
from testcase.page.tests.all_task.all_task_funs.write.qianci_zaoju import qianci_zaoju
from testcase.page.tests.all_task.all_task_funs.write.word_spell import word_spell
from testcase.page.tests.all_task.all_task_funs.write.zhenti_xiezuo import zhenti_xiezuo

from testcase.page.tests.all_task.all_task_funs.ci_hui.words_lists import words_lists

from testcase.page.learn_center.all_class import AllPage
from testcase.page.study_center.study_center_main_page import StudyCenter
from testcase.interface.all_interface import AllInterface
from testcase.interface.study_center.get_study_center_serverID import GetTaskGroupNum


class HomeWork(AllInterface):
    pass


class HomeWork1(StudyCenter, AllPage, GetTaskGroupNum):
    pass


def main1():
    try:
        print("Begin")
        home_work = HomeWork1()
        print("Begin01")
        home_work.open()
        home_work.click_learning_center()
        sleep(5)
        print("Begin2")
        try:
            home_work.click_learn_card_task_btn()
            sleep(5)
            home_work.click_back_btn()
        except:
            pass
        ex_x, ex_y = home_work.get_my_ex_loc()
        print("ex_x, ex_y", ex_x, ex_y)
        sleep(10)
        while True:
            try:
                home_work.click_learn_card_task_btn()
                sleep(5)
                home_work.click_back_btn()
            except:
                pass
            sleep(5)
            print("ex_x, ex_y", ex_x, ex_y)
            home_work.swipeUp(ex_x, ex_y, 1, 500)
            sleep(2)
            task_CN_lists = home_work.return_all_test_ele()
            task_group = GetTaskGroupNum()
            serviceID = task_group.get_service_id()
            result = task_group.get_task_group_id(serviceID)
            task_group_ids = []
            for i in result:
                task_group_ids.append([i.get("groupID"), i.get("taskID"), i.get("currStatus")])
            times = []
            print(task_CN_lists)
            print(task_group_ids)
            # a = []
            # b = []
            for k1 in task_group_ids:
                print("k1", k1)
                if None in k1:
                    a = task_CN_lists[::-1]
                    b = task_group_ids[::-1]
                else:
                    a = task_CN_lists[:]
                    b = task_group_ids[:]
                print("a", a)
                print("b", b)
                for g, k in zip(a, b):
                    print("k[-1]", k1[-1], g)
                    print("GGGGGGGGGGGGGGGGGGgg", home_work.getText(g))
                    if k[-1] == 1 or k[0] is None:
                        print("Append 1")
                        times.append("1")
                        home_work.swipeUp(ex_x, ex_y, 10, 200)
                        pass
                    elif "词汇" in home_work.page_source() and "List" in home_work.page_source():
                        words_lists(home_work, k[1], serviceID)
                        try:
                            home_work.click_my()
                            home_work.click_learning_center()
                        except:
                            pass
                    else:
                        print("Append 0")
                        times.append("0")
                        try:
                            str_regx = re.compile("([^\x00-\xff]+)(\d)+")
                            content = str_regx.search(home_work.getText(g))
                            result = str((content.groups(0)[0]))
                        except:
                            try:
                                str_regx = re.compile("([^\x00-\xff]+)( )(\d)+")
                                content = str_regx.search(home_work.getText(g))
                                result = str((content.groups(0)[0]))
                                print(content.groups(0)[0], content.groups(0)[2])
                            except:
                                pass
                        print("Times", times, len(times))
                        if len(times) >= 1:
                            home_work.swipeUp(ex_x, ex_y, 10, 500)
                            sleep(5)
                            try:
                                home_work.click_learn_card_task_btn()
                                sleep(5)
                                home_work.click_back_btn()
                            except:
                                pass
                        print("Result === >", result)
                        if "课" in result:
                            times.append("0")
                        else:
                            click_result = home_work.click_one_list(home_work, g)
                            try:
                                home_work.click_video_back_btn()
                            except:
                                pass

                            if result == "仿写造句":
                                fangxiezaoju(home_work, k[0], k[1], click_result)

                            if result == "句子分析":
                                sen_ana(home_work, k[0], k[1], click_result)

                            if result == "单词听写":
                                word_listening(home_work, k[0], k[1], click_result)

                            if result == "单词听译":
                                word_trans(home_work, k[0], k[1], click_result)

                            if result == "句子填充":
                                sen_fill(home_work, k[0], k[1], click_result)

                            if result == "单词拼写":
                                word_spell(home_work, k[0], k[1], click_result)

                            if result == "单项选择":
                                gra_choice(home_work, k[0], k[1], click_result)

                            if result == "段落训练":
                                sec_train(home_work, k[0], k[1], click_result)

                            if result == "语法填空":
                                gra_fill(home_work, k[0], k[1], click_result)

                            if result == "遣词造句":
                                qianci_zaoju(home_work, k[0], k[1], click_result)

                            if result == "完形训练":
                                wanxing_xunlian(home_work, k[0], k[1], click_result)

                            if result == "短对话":
                                short_conv(home_work, k[0], k[1], click_result)

                            if result == "长对话":
                                long_conv(home_work, k[0], k[1], click_result)

                            if result == "真题写作":
                                zhenti_xiezuo(home_work, k[0], k[1], click_result)

                            if result == "七选五":
                                sc75(home_work, k[0], k[1], click_result)

                            if result == "文章训练":
                                wenzhang_xunlian(home_work, k[0], k[1], click_result)

                            if result == "短文改错":
                                error_find(home_work, k[0], k[1], click_result)
    except:
        pass


if __name__ == '__main__':
    pass