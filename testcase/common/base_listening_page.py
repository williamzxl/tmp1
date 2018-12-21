from testcase.common.basePage.basePage import BasePage


class ForWordDictPage(BasePage):
    pass


class ForWordTansPage(BasePage):
    pass


class ForSenFillPage(BasePage):
    pass


class ForShortConvPage(BasePage):
    pass


class ForLongConvPage(BasePage):
    pass


class WordListeningPage(ForWordDictPage, ForWordTansPage, \
                        ForSenFillPage, ForShortConvPage, ForLongConvPage):
    pass


if __name__ == '__main__':
    pass