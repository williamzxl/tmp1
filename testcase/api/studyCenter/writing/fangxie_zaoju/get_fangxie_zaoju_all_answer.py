import requests
import json
from utils.config import get_headers


class GetAllFangxieZaojuAnswers(object):
    def __init__(self):
        self.headers = get_headers()
        self.url = self.headers.get('Host')

    def get_all_fangxie_zaoju_answer(self, groupID, taskID):
        # http: // appncee_dev.langb.cn / sysListening / 1104 / wordDic
        url = "http://{}/sysWriting/{}/senImitation".format(self.url, str(groupID))
        # http://192.168.1.154:55262/sysWriting/1925/senImitation
        querystring = {"groupID": "{}".format(groupID), "taskID": "{}".format(taskID)}
        response = requests.request("GET", url, headers=self.headers, params=querystring)
        answer = response.text
        # print(answer)
        json_data = json.loads(answer)
        result = json_data.pop("data").pop('questGuide')
        all_answers = []
        for q in result:
            all_questAnswer = q.get('subQuestGuide')
            all_answers.append([a.get('questAnswer') for a in all_questAnswer])
        return all_answers

    def fangxie_zaoju_right_answer(self, answer, sen_num=None, ques_num=None):
        get_answer = answer[:]
        right_answer = get_answer.pop(int(sen_num)-1)
        return right_answer

    def fangxie_zaoju_wrong_answer(self, answer, sen_num=None, ques_num=None):
        get_answer = answer[:]
        right_answer = get_answer.pop(int(sen_num) - 1)
        wrong_answer = []
        for i in right_answer:
            upper_answer = (i.upper())
            wrong_answer.append(upper_answer)
        return wrong_answer


if __name__ == '__main__':
    test = GetAllFangxieZaojuAnswers()
    word_answers = test.get_all_fangxie_zaoju_answer(1925, 22449)
    print(word_answers)
    r = test.fangxie_zaoju_right_answer(word_answers, 2, 1)
    print(r)
    w = test.fangxie_zaoju_wrong_answer(word_answers, 1, 1)
    print(w)