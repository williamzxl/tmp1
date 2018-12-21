from testcase.common.base_all_common_ele_page import AllCommonEle
from testcase.common.base_word_lists_result import WordListsResultPage, ItemLists
from testcase.common.base_all_result_page import All_ResultPage
from testcase.common.base_listening_page import WordListeningPage
from testcase.common.base_login_pages import ForLoginPage


class AllBasePage(AllCommonEle, ForLoginPage, WordListsResultPage, ItemLists, All_ResultPage):
    pass


if __name__ == '__main__':
    test = AllBasePage()
    test.open()