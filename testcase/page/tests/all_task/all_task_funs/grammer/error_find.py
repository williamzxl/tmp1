from time import sleep
from testcase.page.learn_center.all_class import AllPage
from testcase.page.study_center.study_center_main_page import StudyCenter
from testcase.interface.all_interface import AllInterface


class HomeWork(AllInterface, StudyCenter, AllPage):
    pass


def error_find(home_work, k0, k1, click_result):
    # click_result = home_work.click_one_list(home_work, g)
    print(click_result)
    sleep(2)
    home_work.click_gra_error_find_start_to_answer()
    Flag = True
    while Flag:
        Flag1 = True
        while Flag1 and "确定" not in home_work.page_source():
            x, y, y1 = home_work.get_error_find_x_y()
            counts = 0
            for j, k in zip(range(30, x, 15), range(y + 30, y + y1, 25)):
                home_work.clickEle(j, k)
                if "删除" in home_work.page_source():
                    home_work.click_error_find_delete_btn()
                    counts = counts + 1
                    home_work.click_error_find_submit_btn()
                    sleep(10)
                    if "确定" in home_work.page_source():
                        home_work.click_sure_button()
                        home_work.click_error_find_finish_btn()
                        home_work.click_back_btn()
                        break
                print("counts", counts)
                if counts >= 9:
                    print("counts >= 9", counts >= 9)
                    Flag1 = False
            break
        break
    print("Done")
    if "确定" in home_work.page_source():
        home_work.click_sure_button()
        home_work.click_error_find_finish_btn()
        home_work.click_back_btn()