import requests
from utils.config import NewConfig


class GetMeasureWrite(object):
    def __init__(self, common, headers, accesstoken):
        self.headers = headers
        self.baseUrl = common.get('baseUrl')
        self.accesstoken = accesstoken
        self.headers.update({"accesstoken": self.accesstoken})
        try:
            self.headers.pop("Content-Length")
        except:
            pass

    def get_measure_write(self, sysID="240001"):
        url = "{}/sysMeasure/{}/measureWriting".format(self.baseUrl, sysID)
        response = requests.request("GET", url, headers=self.headers)
        data = eval(response.text).get("data")
        message = eval(response.text).get("message")
        if message == "success":
            currStatus = data.get("currStatus")
            measureID = data.get('measureID')
            questGuide = data.get("questGuide")
            return currStatus, measureID, questGuide
        else:
            pass
        # measureID = data.get('measureID')

    def get_all_right_answer(self, studyType, data):
        all_user_answers = []
        for d in data:
            if d.get("currStatus") == 0:
                user_text = "Test " * 2
                userAnswer = {"studyType": "{}".format(studyType), "sysQuestID": "{}".format(d.get("id")),
                              "userAnswer": "{}".format(user_text)}
                all_user_answers.append(userAnswer)
        return all_user_answers



if __name__ == '__main__':
    cfg_info = NewConfig()
    devices = cfg_info.get_info('vivox6')
    c, h = cfg_info.get_info("vivox6")
    a = '1b7d0916-95c6-49db-a6c6-9fd27e66d43a'
    at = GetMeasureWrite(c, h, a)
    _, _, data = at.get_measure_write("240001")
    print(data)
    answer = at.get_all_right_answer("RID", data)
    # print(answer)