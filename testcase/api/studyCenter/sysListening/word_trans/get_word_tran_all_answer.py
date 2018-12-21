import requests
import json


class GetAllWordTranAnswers(object):
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

    def get_all_word_tran_answer(self, groupID, taskID):
        url = "{}/sysListening/{}/wordTrans".format(self.baseUrl, str(groupID))
        querystring = {"taskID": "{}".format(str(taskID))}
        response = requests.request("GET", url, headers=self.headers, params=querystring)
        answer = response.text
        # print(answer)
        json_data = json.loads(answer)
        result = json_data.pop("data").pop('questGuide')
        word_answers = []
        for r in result:
            if r.get("currStatus") == 0:
                # print(r.get("wordID"), r.get("questAnswer"))
                answer = {"elapsedSec":58,"groupID":groupID,"lisTimes":15,"sysID":r.get("wordID"),"userAnswer": r.get("questAnswer")}
                word_answers.append(answer)
        return word_answers

    def get_word_trans_words(self, groupID, taskID, practiceType):
        url = "{}/sysListening/{}/wordTrans".format(self.baseUrl, groupID)
        querystring = {"taskID": "{}".format(taskID)}
        response = requests.request("GET", url, headers=self.headers, params=querystring)
        answer = response.text
        json_data = json.loads(answer)
        result = json_data.pop("data").pop('questGuide')
        stars_3 = []
        for w in result:
            if w.get("currStatus") == 1:
                star_3 = {"groupID":groupID,"newF":3,"oldF":w.get("familiarity"),"practiceType":practiceType,"sysID":"","taskID":taskID,"wordID":w.get("wordID")}
                stars_3.append(star_3)
        return stars_3