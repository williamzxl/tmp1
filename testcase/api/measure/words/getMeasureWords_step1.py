import requests
from utils.config import NewConfig


class GetMeasureWords(object):
    def __init__(self, common, headers, accesstoken):
        self.headers = headers
        self.baseUrl = common.get('baseUrl')
        self.accesstoken = accesstoken
        self.headers.update({"accesstoken": self.accesstoken})

    def get_measure_words(self, sysID=0):
        url = "{}/sysMeasure/{}/measureWords".format(self.baseUrl, sysID)
        response = requests.request("GET", url, headers=self.headers)
        data = eval(response.text).get("data")
        message = eval(response.text).get("message")
        if message == "success":
            currStatus = data.get("currStatus")
            measureID = data.get('measureID')
            currQuestIdx = data.get("currQuestIdx")
            questGuide = data.get("questGuide")
            return currStatus, measureID, currQuestIdx, questGuide
        else:
            pass
        # measureID = data.get('measureID')

    def get_all_right_answer(self, studyType, data):
        all_user_answers = []
        all_current_status = []
        for d in data:
            answers = d.get("questChoices")
            all_current_status.append(d.get("currStatus"))
            for answer in d.get("questChoices"):
                if answer.get("choiceTag") == "1":
                    answer_index = answers.index(answer) + 1
                    userAnswer = {"studyType": "{}".format(studyType), "sysQuestID": "{}".format(d.get("id")),
                                  "userAnswer": "{}".format(answer_index)}
                    all_user_answers.append(userAnswer)
        return all_current_status, all_user_answers


if __name__ == '__main__':
    cfg_info = NewConfig()
    devices = cfg_info.get_info('vivox6')
    c, h = cfg_info.get_info("vivox6")
    a = 'dad46a52-0542-4f39-a371-3b47e05af4b8'
    at = GetMeasureWords(c, h, a)
    s = at.get_measure_words(0)
