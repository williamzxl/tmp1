from testcase.page.learn_center.listening.word_dic.word_listening_resultPage3 import WLAllAnswerPage
from testcase.page.learn_center.listening.word_trans.word_translating_all_resultPage3 import WTAllAnswerPage
from testcase.page.learn_center.listening.sen_fill.senfill_all_resultPage3 import SFAllAnswerPage
from testcase.page.learn_center.listening.short_conv.short_conv_all_resultPage3 import SCAllAnswerPage
from testcase.page.learn_center.listening.long_conv.long_conv_all_resultPage3 import LCAllAnswerPage


# class AllListenPage( WTAllAnswerPage):
class AllListenPage(WLAllAnswerPage, WTAllAnswerPage, SCAllAnswerPage, LCAllAnswerPage, SFAllAnswerPage):
    pass


if __name__ == '__main__':
    pass