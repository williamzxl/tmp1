from selenium.webdriver.common.by import By
from time import sleep
from testcase.common.basePage.basePage import BasePage


class AllCommonEle(BasePage):
    '''
    返回按钮相关操作
    '''
    appPackage = "com.langlib.ncee"
    page_title_id = (By.ID, "{}:id/title_iframe_title_tv".format(appPackage))
    back_btn_id = (By.ID, "{}:id/title_iframe_back_btn".format(appPackage))
    dialog_tips_text_id = "{}:id/dialog_descripiton_tv".format(appPackage)
    dialog_tips_text_id_ele = (By.ID, dialog_tips_text_id)
    dialog_sure_button = (By.ID, "{}:id/dialog_sure_button".format(appPackage))
    dialog_cancel_button = (By.ID, "{}:id/dialog_cancel_button".format(appPackage))

    video_back_btn_id = (By.ID, "{}:id/activity_video_detail_back_bn".format(appPackage))

    def get_page_title(self):
        try:
            title = self.getText(*self.page_title_id)
            return title
        except:
            pass

    def clickEle(self, x, y):
        # def tapEle(self, x1, y1, x2, y2, time=0.01):
        #     self.driver.tap([(x1, y1), (x2, y2)], time)
        self.tapEle(x, y, x+50, y+50, time=200)
        sleep(5)

    def click_back_btn(self):
        self.find_element(*self.back_btn_id).click()

    def click_video_back_btn(self):
        self.find_element(*self.video_back_btn_id).click()

    def get_dialog_tips_text(self):
        return self.getText(self.find_element(*self.dialog_tips_text_id))

    def click_sure_button(self):
        if self.dialog_tips_text_id in self.page_source():
            self.find_element(*self.dialog_sure_button).click()

    def click_cancel_button(self):
        if self.dialog_tips_text_id in self.page_source():
            # return self.find_element(*self.dialog_cancel_button).click()
            self.find_element(*self.dialog_cancel_button).click()


if __name__ == '__main__':
    pass