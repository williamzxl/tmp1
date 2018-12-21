import re
from time import sleep
from testcase.common.allBasePageClass import AllBasePage
from selenium.webdriver.common.by import By
# from testcase.interface.sysListening.word_dict.get_word_dict_all_answer import get_all_dict_answer


class WLLists1(AllBasePage):
    '''
    单词听写列表
    '''
    appPackage = "com.langlib.ncee"
    lists_ids = (By.ID, "{}:id/fragment_test_data_item_tv".format(appPackage))
    next_button_ele_id = "{}:id/fragment_word_dic_next_tv".format(appPackage)
    next_button_id = (By.ID, "{}:id/fragment_word_dic_next_tv".format(appPackage))
    finish_button_ele_id = "{}:id/fragment_word_dic_done_tv".format(appPackage)
    sen_ana_finish_button_ele_id = "{}:id/fragment_word_profi_done_tv".format(appPackage)
    # com.langlib.ncee:id/fragment_word_profi_done_tv
    finish_button_id = (By.ID, "{}:id/fragment_word_dic_done_tv".format(appPackage))
    learn_center_ele_class = "android.widget.TextView"
    learn_center_class = (By.CLASS_NAME, "android.widget.TextView")

    def get_all_list_ele(self):
        eles = self.find_elements(*self.lists_ids)
        return eles

    def get_list_num(self, driver, ele):
        regx = re.compile(r'(\d)+')
        text = driver.getText(ele)
        result = regx.search(text)
        return int(result.group())

    # def click_one_list(self, driver, ele):
    #     ele.click()
    #     sleep(5)
    #     all_info = driver.page_source()
    #     print("ALL INFO:", all_info)
    #     if self.next_button_ele_id in all_info:
    #         print("This is one word listening result page")
    #         return 1
    #     # if "{}".format(str(self.next_button_id).strip("(|)").split(',')[1]) in all_info:
    #     #     print("{}".format(str(self.next_button_id).strip("(|)").split(',')[1]))
    #     #     print("This is one word listening result page")
    #     #     return 1
    #     if self.finish_button_ele_id in all_info or self.sen_ana_finish_button_ele_id in all_info:
    #         print("This is the last result page")
    #         return 2
    #     # if "{}".format(str(self.finish_button_id).strip("(|)").split(',')[1]) in all_info:
    #     #     print("This is the last result page")
    #     #     return 2
    #     # if "{}".format(str(self.learn_center_class).strip("(|)").split(',')[1]) in all_info:
    #     #     print(str(self.learn_center_class).strip("(|)").split(',')[1])
    #     # # if self.getText(self.find_element(*self.learn_center_class)) in all_info:
    #     #     print("This is home_page word listening result page")
    #     #     return 3
    #     # if self.learn_center_ele_class in all_info:
    #     #     print("This is home_page word listening result page")
    #     #     return 3
    #     if "学习中心" in all_info:
    #         print("This is home_page word listening result page")
    #         return 3
    #     else:
    #         return 0


if __name__ == "__main__":
    pass
    # login_page = WLLists1()
    # login_page.open(noReset=True)
    # eles = login_page.get_all_list_ele()
    # for i in eles:
    #     num = login_page.get_list_num(login_page, i)
    #     print(get_all_dict_answer(list=num))
    #     if login_page.click_one_list(login_page, i) != 0:
    #         pass
