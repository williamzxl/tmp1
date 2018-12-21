import requests
import json
from utils.config import get_headers


class GetAllSC75Answers(object):
    def __init__(self):
        self.headers = get_headers()
        self.url = self.headers.get('Host')

    def get_all_sc_75_answer(self, groupID, taskID):
        url = "http://{}/sysReading/{}/senCloze".format(self.url, groupID)
        querystring = {"taskID": "{}".format(taskID)}
        response = requests.request("GET", url, headers=self.headers, params=querystring)
        answer = response.text
        json_data = json.loads(answer)
        result = json_data.pop("data").pop('questGuide')
        sc_75_all_answers = []
        for i in result:
            for step in i.get('steps'):
                if step.get('subQuestGuide'):
                    for answer in step.get('subQuestGuide'):
                        sc_75_all_answers.append(answer.get('questAnswer'))
        return sc_75_all_answers

    def sc_75_right_answer(self, answers):
        right_answer = answers[:]
        return right_answer

    def sc_75_wrong_answer(self, answers):
        get_answer = answers[:]
        wrong_answer = []
        curr_index = []
        for test in get_answer:
            if (ord(test) + 1) <= 71:
                wrong_answer.append(chr(ord(test) + 1))
            else:
                curr_index1 = len(wrong_answer)
                curr_index.append(curr_index1)
                wrong_answer.append(chr(ord(test) - 1))
        not_in_item = []
        if curr_index:
            for i in curr_index:
                if chr(ord(wrong_answer[i]) - 1) not in wrong_answer:
                    wrong_answer[i] = chr(ord(wrong_answer[i]) - 1)
                elif chr(ord(wrong_answer[i]) + 1) not in wrong_answer:
                    wrong_answer[i] = chr(ord(wrong_answer[i]) + 1)
                else:
                    for item in range(97, 104):
                         if (chr(item).upper()) not in wrong_answer:
                             not_in_item.append(chr(item).upper())
        if curr_index:
            for j,k in zip(curr_index, range(1, len(curr_index) + 1)):
                wrong_answer[j] = not_in_item[k]
        return wrong_answer


if __name__ == '__main__':
    test = GetAllSC75Answers()
    sc_all = test.get_all_sc_75_answer(2538, 23281)
    r = test.sc_75_right_answer(sc_all)
    print(r)
    w = test.sc_75_wrong_answer(sc_all)
    print(w)