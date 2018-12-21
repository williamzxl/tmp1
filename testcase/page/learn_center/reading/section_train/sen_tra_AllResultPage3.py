from appium.webdriver.webdriver import By
from testcase.page.learn_center.reading.section_train.sen_tra_Step3Page2 import SAAnswerResultPage2
from utils.config import get_appPackage


class STAllAnswerPage(SAAnswerResultPage2):
    appPackage = get_appPackage()
    sen_index_classes = (By.CLASS_NAME, '{}:id/recy_item'.format(appPackage))

    def click_sen_index_num(self):
        self.find_element(*self.sen_index_classes).click()


if __name__ == "__main__":
    pass