from testcase.page.home_page.all_home_page import AllHomePage
from testcase.page.learn_center.grammer.all_gra_page import AllGraPage
from testcase.page.learn_center.listening.all_listening_page import AllListenPage
from testcase.page.learn_center.reading.all_read_page import AllReadPage
from testcase.page.learn_center.writing.all_writing_page import AllWritingPage
from testcase.page.learn_center.words_lists.words_lists_AllResultPage2 import WordsListsAllAnswerPage


class AllPage(AllHomePage, AllListenPage, AllReadPage, AllGraPage, AllWritingPage, WordsListsAllAnswerPage):
    pass


if __name__ == '__main__':
    pass