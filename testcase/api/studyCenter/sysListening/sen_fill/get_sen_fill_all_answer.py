import requests
import json


class GetAllSenFillAnswers(object):
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

    def get_all_sen_fill_answer(self, groupID, taskID):
        url = "{}/sysListening/{}/senFill".format(self.baseUrl, str(groupID))
        querystring = {"taskID": "{}".format(str(taskID))}
        response = requests.request("GET", url, headers=self.headers, params=querystring)
        answer = response.text
        # print(answer)
        json_data = json.loads(answer)
        result = json_data.pop("data").pop('questGuide')
        all_answers = []
        for r in result:
            if r.get("currStatus") == 0:
                user_answer = r.get("questAnswer")
                answer = {"elapsedSec":58,"groupID":groupID,"lisTimes":15,"sysID":r.get("id"),"userAnswer": user_answer}
                all_answers.append(answer)
        return all_answers

    def get_sen_fill_words(self, groupID, taskID, practiceType):
        url = "{}/sysListening/{}/senFill".format(self.baseUrl, groupID)
        querystring = {"taskID": "{}".format(taskID)}
        # self.headers.update({"Content-Type": "application/x-www-form-urlencoded"} )
        response = requests.request("GET", url, headers=self.headers, params=querystring)
        answer = response.text
        json_data = json.loads(answer)
        result = json_data.pop("data").pop('vocabulary')
        stars_3 = []
        if result.get("currStatus") == 0:
            words = result.get("wordsList")
            for w in words:
                star_3 = {"groupID":groupID,"newF":3,"oldF":w.get("familiarity"),"practiceType":practiceType,"sysID":"","taskID":taskID,"wordID":w.get("wordID")}
                stars_3.append(star_3)
        return stars_3

    def get_sen_fill_done_data(self,groupID, practiceType):
        data = {"elapsedSec": 0, "groupID": groupID, "practiceType": practiceType, "sysID": "0"}
        return data