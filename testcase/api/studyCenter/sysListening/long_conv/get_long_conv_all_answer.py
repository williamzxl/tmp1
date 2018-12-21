import requests
import json
from utils.config import get_headers


class GetAllLongConvAnswers(object):
    def __init__(self):
        self.headers = get_headers()
        self.url = self.headers.get('Host')

    def get_all_long_conv_answer(self, groupID, taskID):
        url = "http://{}/sysListening/{}/longConv".format(self.url, groupID)
        querystring = {"taskID": "{}".format(taskID)}

        response = requests.request("GET", url, headers=self.headers, params=querystring)
        answer = response.text
        json_data = json.loads(answer)
        result = json_data.pop("data").pop('questGuide')
        word_answers = []
        for r in result:
            for answer in r.pop('subQuestGuide'):
                word_answers.append(answer.get('questAnswer'))
        print("Database_answers:", word_answers)
        return (word_answers)


    def long_conv_right_answer(self, answer, num):
        get_answer = answer[:]
        right_answer = get_answer.pop(int(num)-1)
        return right_answer


    def long_conv_wrong_answer(self, answer, num):
        get_answer = answer[:]
        test = get_answer.pop(int(num)-1)
        if ord(test) + 1 <= 67:
            wrong_answer = chr(ord(test) + 1)
        else:
            wrong_answer = chr(ord(test) - 1)
        return wrong_answer
        # get_answer = answer[:]
        # test = get_answer.pop(int(num)-1)
        # wrong_answer = []
        # for test in get_answer:
        #     if ord(test) + 1 <= 67:
        #         wrong_answer.append(chr(ord(test) + 1))
        #     else:
        #         wrong_answer.append(chr(ord(test) - 1))
        # return wrong_answer


if __name__ == '__main__':
    a = GetAllLongConvAnswers()
    answer = a.get_all_long_conv_answer(1826, 23289)
    print(len(answer))
    print(a.long_conv_right_answer(answer, 1))
    print(a.long_conv_wrong_answer(answer, 1))
    print(tuple(answer))

