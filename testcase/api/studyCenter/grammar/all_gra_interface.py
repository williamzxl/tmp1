from testcase.api.studyCenter.grammar.mulChoice.get_mul_choice_all_answer import GetAllMulChoiceAnswers
from testcase.api.studyCenter.grammar.mulChoice.post_all_mul_choice_answer import PostAllMulChoiceAnswers
from testcase.api.studyCenter.grammar.graFill.get_all_gra_fill_answer import GetAllGraFillnAnswers
from testcase.api.studyCenter.grammar.graFill.post_all_gra_fill_answer import PostAllGraFillAnswers
from testcase.api.studyCenter.grammar.error_find.get_all_error_find_answer import GetAllErrorFindAnswers
from testcase.api.studyCenter.grammar.error_find.post_all_error_find_answer import PostAllErrorFindAnswers
from testcase.api.studyCenter.grammar.error_find.get_all_error_find_result_info import GetAllErrorFindResultInfo


class AllGraInterface(GetAllMulChoiceAnswers, PostAllMulChoiceAnswers, GetAllGraFillnAnswers,
                      PostAllGraFillAnswers, GetAllErrorFindAnswers, PostAllErrorFindAnswers, GetAllErrorFindResultInfo):
    pass