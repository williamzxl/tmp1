import requests
from utils.config import NewConfig


class GetMeasureRead(object):
    def __init__(self, common, headers, accesstoken):
        self.headers = headers
        self.baseUrl = common.get('baseUrl')
        self.accesstoken = accesstoken
        self.headers.update({"accesstoken": self.accesstoken})
        try:
            self.headers.pop("Content-Length")
        except:
            pass

    def get_measure_read(self, sysID="222001"):
        url = "{}/sysMeasure/{}/measureReading".format(self.baseUrl, sysID)
        print(url)
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
    a = '1b7d0916-95c6-49db-a6c6-9fd27e66d43a'
    at = GetMeasureRead(c, h, a)
    _, _, _, data = at.get_measure_read()
    answer = at.get_all_right_answer("RID", data)
    print(answer)