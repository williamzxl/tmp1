import requests
import json
from itertools import chain
from utils.config import get_headers


class GetAllSenAnAAnswers(object):
    def __init__(self):
        self.url = "appncee_dev.langb.cn"
        self.headers = get_headers()
        self.url = self.headers.get('Host')

    def get_all_sen_analysis_answer(self, groupID, taskID):
        url = "http://{}/sysReading/{}/senAnalysis".format(self.url, groupID)
        querystring = {"taskID": "{}".format(taskID)}
        response = requests.request("GET", url, headers=self.headers, params=querystring)
        answer = response.text
        json_data = json.loads(answer)
        result = json_data.pop("data").pop('questGuide')
        all_answers = []
        all_answers_choice = []
        for q in result:
            all_questAnswer = q.get('subQuestGuide')
            all_answers.append([a.get('questAnswer') for a in all_questAnswer])
            all_answers_choice.append([a.get('questChoices') for a in all_questAnswer])
        return all_answers, all_answers_choice

    def right_answer_sen_ana(self, answers, answers_choice, sen_num=None, ques_num=None):
        try:
            choice_EN = answers[sen_num-1][ques_num - 1]
        except:
            pass
        print("Choice_EN:", choice_EN)
        answers_choice = list(chain(*answers_choice))
        if choice_EN:
            if choice_EN.isupper():
                for cn in list(chain(*answers_choice)):
                    if choice_EN == cn.get('choiceTag'):
                        choice_CN = cn.get('choiceCN')
                        if choice_CN:
                            return choice_CN, choice_EN
            else:
                return choice_EN, None
        else:
            return 0, None

    def wrong_answer_sen_ana(self, answers, answers_choice, sen_num=None, ques_num=None):
        choice_EN = answers[sen_num - 1][ques_num - 1]
        print("Choice_EN:", choice_EN)
        answers_choice = list(chain(*answers_choice))
        if choice_EN:
            if choice_EN.isupper():
                print(list(chain(*answers_choice)))
                for cn in list(chain(*answers_choice)):
                    if choice_EN == cn.get('choiceTag'):
                        choice_CN = cn.get('choiceCN')
                        if choice_CN:
                            return choice_CN
            else:
                return choice_EN + "Test"
        else:
            return 0


if __name__ == '__main__':
    test = GetAllSenAnAAnswers()
    answers, answers_choice = test.get_all_sen_analysis_answer(2549, 22605)
    # right = test.right_answer_sen_ana(answers, answers_choice, 3, 1)
    # wrong  = wrong_answer_sen_ana(answers, answers_choice, 5, 2)
    # print(right)
    # print(wrong)
    print(answers)
    right = test.right_answer_sen_ana(answers, answers_choice, 3, 2)
    print(right)
    print(answers_choice)
