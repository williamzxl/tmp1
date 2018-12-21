from appium.webdriver.webdriver import By
from testcase.page.learn_center.reading.sen_analysis.sen_ana_SingleResultPage2 import SAAnswerResultPage2


class SAAllAnswerPage(SAAnswerResultPage2):
    appPackage = "com.langlib.ncee"
    sen_index_classes = (By.CLASS_NAME, '{}:id/recy_item'.format(appPackage))

    def click_sen_index_num(self):
        self.find_element(*self.sen_index_classes).click()


if __name__ == "__main__":
    pass