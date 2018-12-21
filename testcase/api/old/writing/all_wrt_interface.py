from testcase.interface.writing.word_spell.get_word_spell_all_answer import GetAllWordSpellAnswers
from testcase.interface.writing.fangxie_zaoju.get_fangxie_zaoju_all_answer import GetAllFangxieZaojuAnswers
from testcase.interface.writing.zhenti_xiezuo.get_zhenti_xiezuo_all_answer import GetAllZhentiXiezuoAnswers
from testcase.interface.writing.qianci_zaoju.get_all_qianci_zaoju_answer import GetAllQianciZaojuAnswers


class AllWrtInterface(GetAllWordSpellAnswers, GetAllFangxieZaojuAnswers,
                      GetAllZhentiXiezuoAnswers, GetAllQianciZaojuAnswers):
    pass