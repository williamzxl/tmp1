import requests
import json
from itertools import chain
from utils.config import get_headers


class GetAllQianciZaojuAnswers(object):
    def __init__(self):
        self.url = "appncee_dev.langb.cn"
        self.headers = get_headers()
        self.url = self.headers.get('Host')

    def get_all_qianci_zaoju_answer(self, groupID, taskID):
        url = "http://{}/sysWriting/{}/construction".format(self.url, groupID)
        querystring = {"groupID": "{}".format(groupID), "taskID": "{}".format(taskID)}
        response = requests.request("GET", url, headers=self.headers, params=querystring)
        answer = response.text
        json_data = json.loads(answer)
        result = json_data.pop("data").pop('questGuide')
        all_CN_answers = []
        for q in result:
            all_questAnswer = q.get('subQuestGuide')
            all_CN_answers.append([a.get('questAnswer') for a in all_questAnswer])
        return all_CN_answers

    def qianci_zaoju_right_answer(self, answers, sen_num=None, ques_num=None):
        choice_EN = answers[sen_num-1][ques_num - 1]
        return choice_EN

    def qianci_zaoju_wrong_answer(self, answers, sen_num=None, ques_num=None):
        choice_EN = answers[sen_num - 1][ques_num - 1]
        return choice_EN.upper()


if __name__ == '__main__':
    test = GetAllQianciZaojuAnswers()
    right = test.get_all_qianci_zaoju_answer(1949, 24734)
    print(right)
    # print(answers_choice)
    r1 = test.qianci_zaoju_right_answer(right,1,3)
    print(r1)
    w1 = test.qianci_zaoju_wrong_answer(right,1,3)
    print(w1)