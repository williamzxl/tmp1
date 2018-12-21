# from testcase.interface.writing.word_spell.get_word_spell_all_answer import GetAllWordSpellAnswers
# from testcase.interface.writing.fangxie_zaoju.get_fangxie_zaoju_all_answer import GetAllFangxieZaojuAnswers
# from testcase.interface.writing.zhenti_xiezuo.get_zhenti_xiezuo_all_answer import GetAllZhentiXiezuoAnswers
# from testcase.interface.writing.qianci_zaoju.get_all_qianci_zaoju_answer import GetAllQianciZaojuAnswers
from testcase.api.studyCenter.writing.word_spell.get_word_spell_all_answer import GetAllWordSpellAnswers
from testcase.api.studyCenter.writing.word_spell.post_all_word_spell_answer import PostAllWordSpellAnswers
from testcase.api.studyCenter.writing.zhenti_xiezuo.get_zhenti_xiezuo_answer import GetAllZhentiXirzuoAnswers
from testcase.api.studyCenter.writing.zhenti_xiezuo.post_zhenti_xiezuo_answer import PostAllZhentiXiezuoAnswers
from testcase.api.studyCenter.writing.zhenti_xiezuo.get_all_zhenti_xiezuo_result_info import GetAllZhentiXiezuoResultInfo


class AllWrtInterface(GetAllWordSpellAnswers, PostAllWordSpellAnswers,
                      GetAllZhentiXirzuoAnswers, PostAllZhentiXiezuoAnswers, GetAllZhentiXiezuoResultInfo):
    pass