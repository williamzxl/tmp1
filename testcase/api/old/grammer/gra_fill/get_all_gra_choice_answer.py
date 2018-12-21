import requests
import json
# from utils.config import get_headers


class GetAllGraChoiceAnswers(object):
    def __init__(self):
        # self.headers = headers
        # self.url = self.headers.get('Host')
        # pass
        self.pas = None

    def get_all_gra_choice_answer(self, headers,groupID, taskID):
        host = headers.get('Host')
        url = "http://{}/sysGrammar/{}/mulChoice".format(host, groupID)
        # http://192.168.1.154:55262/sysGrammar/1854/mulChoice
        querystring = {"groupID": "{}".format(groupID), "taskID": "{}".format(taskID)}
        print("URL", url)
        response = requests.request("GET", url, headers=headers, params=querystring)
        answer = response.text
        json_data = json.loads(answer)
        result = json_data.pop("data").pop('questGuide')
        print("result", result)
        word_answers = []
        for a in result:
            word_answers.append(a.pop('questAnswer'))
        print("Database_answers:", word_answers)
        return word_answers


    def gra_choice_right_answer(self, answer, num):
        get_answer = answer[:]
        right_answer = get_answer.pop(int(num)-1)
        return right_answer


    def gra_choice_wrong_answer(self, answer, num):
        get_answer = answer[:]
        test = get_answer.pop(int(num)-1)
        wrong_answer = []
        if (ord(test) + 1) <= 68:
            wrong_answer.append(chr(ord(test) + 1))
        else:
            wrong_answer.append(chr(ord(test) -1))
        return "".join(wrong_answer)


if __name__ == '__main__':
    test = GetAllGraChoiceAnswers()
    answers = test.get_all_gra_choice_answer(1866, 32454)
    print(answers)
    r = test.gra_choice_right_answer(answers, 1)
    print(r)