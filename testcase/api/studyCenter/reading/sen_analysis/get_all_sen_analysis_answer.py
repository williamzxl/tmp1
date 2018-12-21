import requests
import json


class GetAllSenAnAAnswers(object):
    def __init__(self, common, headers, accesstoken):
        self.headers = headers
        self.baseUrl = common.get('baseUrl')
        try:
            self.headers.pop('Content-Length')
        except:
            pass
        self.accesstoken = accesstoken
        self.headers.update({"accesstoken": self.accesstoken})
        self.headers.update({"Host": common.get("baseProxy")})

    def get_all_sen_analysis_answer(self, groupID, taskID):
        # print(groupID, taskID)
        url = "{}/sysReading/{}/senAnalysis".format(self.baseUrl, groupID)
        querystring = {"taskID": "{}".format(taskID)}
        response = requests.request("GET", url, headers=self.headers, params=querystring)
        answer = response.text
        json_data = json.loads(answer)
        print(json_data)
        result = json_data.pop("data").pop('questGuide')
        print("Result: ", result)
        all_answers = []
        for q in result:
            if q.get("currStatus") == 0:
                for r in q.get("subQuestGuide"):
                    if r.get("currStatus") == 0:
                        answer = {"elapsedSec": 6805, "groupID": groupID, "sysID": r.get('id'),"userAnswer": r.get("questAnswer")}
                        all_answers.append(answer)
        return all_answers

    def get_sa_words(self, groupID, taskID, practiceType):
        # print(groupID, taskID)https://appncee.langlib.com/sysReading/2475/?groupID=2475&taskID=37037
        url = "{}/sysReading/{}/senAnalysis".format(self.baseUrl, groupID)
        querystring = {"taskID": "{}".format(taskID)}
        response = requests.request("GET", url, headers=self.headers, params=querystring)
        answer = response.text
        json_data = json.loads(answer)
        result = json_data.pop("data").pop('vocabulary')
        if result.get("currStatus") == 0:
            stars_3 = []
            words = result.get("wordsList")
            for w in words:
                # print("W", w.get('familiarity'))
                star_3 = {"groupID": groupID, "newF": 3, "oldF": w.get("familiarity"), "practiceType": practiceType,
                          "sysID": "", "taskID": taskID, "wordID": w.get("wordID")}
                stars_3.append(star_3)
            return stars_3

    def return_sa_done_data(self,groupID, practiceType):
        data = {"elapsedSec": 0, "groupID": groupID, "practiceType": practiceType, "sysID": "0"}
        return data