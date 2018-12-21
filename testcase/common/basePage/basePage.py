from testcase.common.basePage.web_view import WebView
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class BasePage(WebView):
    def __init__(self, page=None, browser_type=None):
        if page:
            self.driver = page.driver
        else:
            super(BasePage, self).__init__(browser_type=browser_type)

    def get_driver(self):
        return self.driver

    def open(self):
        try:
            self.get()
        except:
            raise ValueError("Connect appium failed!")

    def find_element(self, *loc):
        try:
            WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc))
            # print("Find elements Success")
            return self.driver.find_element(*loc)
        except TimeoutError:
            print("In {} cant find {}".format(self, loc))
            return False

    def find_elements(self, *loc):
        try:
            WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc))
            # print("Find elements Success")
            return self.driver.find_elements(*loc)
        except TimeoutError:
            print("In {} cant find {}".format(self, loc))
            return False

    # def script(self, src):
    #     self.driver.execute_script(src)

    def sendKeys(self, loc, value, clear_first=True, click_first=True):
        try:
            # loc = getattr(self, "_{}".format(loc))
            if click_first:
                # self.find_element(*loc).click()
                loc.click()
            if clear_first:
                # self.find_element(*loc).clear()
                loc.clear()
            # self.find_element(*loc).send_keys(value)
                loc.send_keys(value)
        except AttributeError:
            print("{} page cant find {} element".format(self, loc))

    def get_url(self):
        return self.driver.current_url

    def getEleText(self,ele):
        return ele.text

    def getEleSize(self, ele):
        return ele.size

    def getEleLocation(self, ele):
        return ele.location

    def is_selected(self, element):
        element.is_selected()

    def is_enabled(self, element):
        element.is_enabled()

    def is_displayed(self, element):
        element.is_displayed()

    def enter(self, element):
        element.send_keys(Keys.RETURN)

    def click(self, element):
        element.click()

    def submit(self):
        pass

    def getEleAttribute(self, element, attribute):
        return element.get_attribute(attribute)

    # def getAttribute(self, ele, name):
    #     return ele.get_attribute(name)

    def getText(self, element):
        try:
            return element.text
        except SyntaxError:
            print("No such element TEXT")

    def getTitle(self):
        return self.driver.title

    def getCurrentUrl(self):
        return self.driver.current_url

    def get_contexts(self):
        return self.driver.contexts()

    def get_current_context(self):
        return self.driver.current_context()

    def get_context(self):
        return self.driver.context()

    def page_source(self):
        return self.driver.page_source

    def page_source_test(self):
        return self.driver.page_source


if __name__ == "__main__":
    test = BasePage()
    test.open()