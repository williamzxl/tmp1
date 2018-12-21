import requests
import json
from utils.config import get_headers


class GetAllShortConvAnswers(object):
    def __init__(self):
        self.headers = get_headers()
        self.url = self.headers.get('Host')

    def get_all_short_conv_answer(self, groupID, taskID):
        url = "http://{}/sysListening/{}/shortConv".format(self.url, groupID)
        # url = "http://192.168.1.154:55262/sysListening/1000/wordDic"
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


    def right_answer_short_conv(self, answer, num):
        get_answer = answer[:]
        right_answer = get_answer.pop(int(num)-1)
        return right_answer


    def wrong_answer_short_conv(self, answer, num):
        get_answer = answer[:]
        test = get_answer.pop(int(num)-1)
        if ord(test) + 1 <= 68:
            wrong_answer = chr(ord(test) + 1)
        else:
            wrong_answer = chr(ord(test) - 1)
        return wrong_answer

    #
    # answer = get_all_short_conv_answer(list=1501, taskID=1)
    # print(right_answer_sen_fill(answer, 2))
    # print(wrong_answer_sen_fill(answer, 2))
    # print(tuple(answer))

