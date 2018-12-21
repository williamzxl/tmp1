import requests
import json
from utils.config import get_headers


class GetAllClozeTestAnswers(object):
    def __init__(self):
        self.headers = get_headers()
        self.url = self.headers.get('Host')

    def get_all_cloze_test_answer(self, groupID, taskID):
        url = "http://{}/sysReading/{}/clozeTest".format(self.url, groupID)
        querystring = {"taskID": "{}".format(taskID)}
        response = requests.request("GET", url, headers=self.headers, params=querystring)
        answer = response.text
        json_data = json.loads(answer)
        result = json_data.pop("data").pop('questGuide')
        all_answers = []
        for r in result:
            for step in (r.get('steps')):
                if step.get('subQuestGuide'):
                    for a in (step.get('subQuestGuide')):
                        all_answers.append([a.get("questWordSpeech"), a.get("questAnswer")])
        return all_answers

    def cloze_test_right_answer(self, answers, ques_num=None):
        curr_answer = answers[int(ques_num) - 1]
        CN_answer = curr_answer[0]
        EN_answer = curr_answer[1]
        return CN_answer, EN_answer

    def cloze_test_wrong_answer(self, answers, sen_num=None, ques_num=None):
        choice_EN = answers[sen_num - 1][ques_num - 1]
        return choice_EN.upper()


if __name__ == '__main__':
    test = GetAllClozeTestAnswers()
    right = test.get_all_cloze_test_answer(2511, 24761)
    print(right)
    print(len(right))
    r_CN, r_EN = test.cloze_test_right_answer(right, 1)
    print(r_CN, r_EN)