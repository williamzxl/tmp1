from testcase.interface.words_lists.ci_hui.get_all_words_lists import GetAllWordsListsAnswers
from testcase.interface.words_lists.ci_hui.put_all_words_lists import PutAllWordsListsDone


class AllCihuiInterface(GetAllWordsListsAnswers, PutAllWordsListsDone):
    pass

if __name__ == '__main__':
    test = AllCihuiInterface()
    task = test.get_all_words_groupId("P90")