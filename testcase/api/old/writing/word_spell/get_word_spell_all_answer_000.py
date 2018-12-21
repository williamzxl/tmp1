import requests
import json
from utils.config import get_headers


class GetAllWordSpellAnswers(object):
    def __init__(self):
        self.headers = get_headers()
        self.url = self.headers.get('Host')

    def get_all_word_spell_answer(self, groupID, taskID):
        # http: // appncee_dev.langb.cn / sysListening / 1104 / wordDic
        url = "http://{}/sysWriting/{}/wordSpell".format(self.url, str(groupID))
        querystring = {"groupID": "{}".format(groupID), "taskID": "{}".format(taskID)}
        response = requests.request("GET", url, headers=self.headers, params=querystring)
        answer = response.text
        # print(answer)
        json_data = json.loads(answer)
        result = json_data.pop("data").pop('questGuide')
        all_answers = []
        for a in result:
            answer = a.pop('questAnswer')
            position = a.pop('questPosition')
            one_word_answer = []
            for i in position:
                one_word_answer.append(answer[i])
            all_answers.append("".join(one_word_answer))
        return all_answers

    def word_spell_right_answer(self, answer, num):
        get_answer = answer[:]
        right_answer = get_answer.pop(int(num)-1)
        return right_answer

    def word_spell_wrong_answer(self, answer, num):
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
    test = GetAllWordSpellAnswers()
    word_answers = test.get_all_word_spell_answer(2346, 22448)
    print(word_answers)
    t = test.word_spell_right_answer(word_answers, 1)
    print(t)
    t1 = test.word_spell_wrong_answer(word_answers, 1)
    print(t1)
