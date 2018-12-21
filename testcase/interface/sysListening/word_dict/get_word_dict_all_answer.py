import requests
import json
from utils.config import get_headers


class GetAllWordDictAnswers(object):
    def __init__(self):
        self.headers = get_headers()
        self.url = self.headers.get('Host')

    def get_all_dict_answer(self, groupID, taskID):
        # http: // appncee_dev.langb.cn / sysListening / 1104 / wordDic
        url = "http://{}/sysListening/{}/wordDic".format(self.url, str(groupID))
        querystring = {"taskID": "{}".format(str(taskID))}
        response = requests.request("GET", url, headers=self.headers, params=querystring)
        answer = response.text
        # print(answer)
        json_data = json.loads(answer)
        result = json_data.pop("data").pop('questGuide')
        word_answers = []
        for a in result:
            word_answers.append(a.pop('wordEN'))
        print("Database_answers:", word_answers)
        return word_answers

    def dict_right_answer(self, answer, num):
        get_answer = answer[:]
        right_answer = get_answer.pop(int(num)-1)
        return right_answer

    def dict_wrong_answer(self, answer, num):
        get_answer = answer[:]
        test = get_answer.pop(int(num)-1)
        wrong_answer = []
        for i in test:
            if chr(ord(i) + 1).isalpha():
                wrong_answer.append(chr(ord(i) + 1))
            else:
                wrong_answer.append(chr(ord(i) -1))
        wrong_answer = "".join(wrong_answer)
        return wrong_answer


if __name__ == '__main__':
    test = GetAllWordDictAnswers()
    word_answers = test.get_all_dict_answer(1104, 16484)
    print(word_answers)
    test.dict_right_answer(word_answers, 1)
