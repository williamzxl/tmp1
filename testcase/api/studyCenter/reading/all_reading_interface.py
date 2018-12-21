from testcase.api.studyCenter.reading.sen_analysis.get_all_sen_analysis_answer import GetAllSenAnAAnswers
from testcase.api.studyCenter.reading.sen_analysis.post_all_sen_analysis_answer import PostAllSenAnAAnswers
from testcase.api.studyCenter.reading.sen_analysis.get_sen_ana_result_info import GetAllSenAnaResultInfo
from testcase.api.studyCenter.reading.section_train.get_all_sec_train_answer import GetAllSecTrainAnswers
from testcase.api.studyCenter.reading.section_train.post_all_sec_train_answer import PostAllSecTrainAnswers
# from testcase.api.studyCenter.reading.sen_cloze75.get_all_sc_75_answer import GetAllSC75Answers
from testcase.api.studyCenter.reading.clozeTest.get_all_clozeTest_answer import GetAllClozeTestnAnswers
from testcase.api.studyCenter.reading.clozeTest.post_all_clozeTest_answer import PostAllClozeTestlAnswers
from testcase.api.studyCenter.reading.articleTrain.get_all_article_train_answer import GetAllArtTrainAnswers
from testcase.api.studyCenter.reading.articleTrain.post_all_article_train_answer import PostAllArtTrainAnswers
from testcase.api.studyCenter.reading.articleTrain.get_article_result_info import GetAllArtTrainResultInfo
from testcase.api.studyCenter.reading.sen_cloze75.get_all_cloze75_answer import GetAllSenCloze75Answers
from testcase.api.studyCenter.reading.sen_cloze75.post_all_cloze75_answer import PostAllCloze75lAnswers

class AllReadInterface(GetAllSenAnAAnswers,PostAllSenAnAAnswers, GetAllSenAnaResultInfo,\
                       GetAllSecTrainAnswers, PostAllSecTrainAnswers, \
                       GetAllClozeTestnAnswers, PostAllClozeTestlAnswers, \
                       GetAllArtTrainAnswers, PostAllArtTrainAnswers, GetAllArtTrainResultInfo, \
                       GetAllSenCloze75Answers, PostAllCloze75lAnswers, \
                       ):
    pass