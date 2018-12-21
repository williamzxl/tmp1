import requests
import json
# from utils.config import get_headers


class GetAllSenFillAnswers(object):
    def __init__(self):
        # self.headers = headers
        # self.url = self.headers.get('Host')
        self.pas = None

    def get_all_sen_fill_answer(self, headers, groupID, taskID):
        host = headers.get('Host')
        url = "http://{}/sysListening/{}/senFill".format(host, groupID)
        # url = "http://192.168.1.154:55262/sysListening/1000/wordDic"
        querystring = {"taskID": "{}".format(taskID)}
        response = requests.request("GET", url, headers=headers, params=querystring)
        answer = response.text
        json_data = json.loads(answer)
        result = json_data.pop("data").pop('questGuide')
        word_answers = []
        for a in result:
            word_answers.append(a.pop('questAnswer'))
        print("Database_answers:", word_answers)
        return (word_answers)


    def sen_fill_right_answer(self, answer, num):
        get_answer = answer[:]
        right_answer = get_answer.pop(int(num)-1)
        return right_answer


    def sen_fill_wrong_answer(self, answer, num):
        get_answer = answer[:]
        test = get_answer.pop(int(num)-1)
        wrong_answer = []
        for i in test:
            wrong_answer.append(i[::-1])
        # wrong_answer = "".join(wrong_answer)
        return wrong_answer

    #
    # answer = get_all_sen_fill_answer(list=1431, taskID=1)
    # print(right_answer_sen_fill(answer, 1))
    # print(wrong_answer_sen_fill(answer, 1))
    # print(tuple(answer))
    #
