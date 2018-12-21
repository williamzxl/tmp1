import requests
import json
# from utils.config import get_headers


class GetAllWordTransAnswers(object):
    def __init__(self):
        # self.headers = headers
        # self.url = self.headers.get('Host')
        self.pas = None

    def get_all_trans_answer(self, headers, groupID, taskID):
        host = headers.get('Host')
        url = "http://{}/sysListening/{}/wordTrans".format(host, groupID)
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
        return word_answers


    def word_trans_right_answer(self, answer, num):
        get_answer = answer[:]
        right_answer = get_answer.pop(int(num)-1)
        return right_answer


    def word_trans_wrong_answer(self, answer, num):
        get_answer = answer[:]
        test = get_answer.pop(int(num)-1)
        wrong_answer = []
        if (ord(test) + 1) <= 68:
            wrong_answer.append(chr(ord(test) + 1))
        else:
            wrong_answer.append(chr(ord(test) -1))
        return "".join(wrong_answer)


    # answer = get_all_trans_answer(list=1294, taskID=1)
    # print(right_answer_trans(answer, 6))
    # print(wrong_answer_trans(answer, 6))
if __name__ == '__main__':
    t = GetAllWordTransAnswers()
    a = t.get_all_trans_answer(2176, 22458)
    print(a)
    r = t.word_trans_right_answer(a, 20)
    print(r)