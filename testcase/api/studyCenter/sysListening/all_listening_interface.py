from testcase.api.studyCenter.sysListening.word_dict.get_word_dict_all_answer import GetAllWordDictAnswers
from testcase.api.studyCenter.sysListening.word_dict.post_all_word_dict_answer import PostAllWordDictAnswers
from testcase.api.studyCenter.sysListening.word_trans.get_word_tran_all_answer import GetAllWordTranAnswers
from testcase.api.studyCenter.sysListening.word_trans.post_all_word_tran_answer import PostAllWordTransAnswers
from testcase.api.studyCenter.sysListening.sen_fill.get_sen_fill_all_answer import GetAllSenFillAnswers
from testcase.api.studyCenter.sysListening.sen_fill.post_all_sen_fill_answer import PostAllSenFillAnswers


class AllListenInterface(GetAllWordDictAnswers, PostAllWordDictAnswers, GetAllWordTranAnswers, \
                         PostAllWordTransAnswers, GetAllSenFillAnswers, PostAllSenFillAnswers):
    pass