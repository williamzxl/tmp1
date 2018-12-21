import requests
import json


class GetAllMulChoiceAnswers(object):
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

    def get_all_mul_choice_answer(self, groupID, taskID):
        # GET https://appncee.langlib.com/sysGrammar/1857/mulChoice?groupID=1857&taskID=37035 HTTP/1.1
        url = "{}/sysGrammar/{}/mulChoice".format(self.baseUrl, str(groupID))
        querystring = {"taskID": "{}".format(str(taskID))}
        response = requests.request("GET", url, headers=self.headers, params=querystring)
        answer = response.text
        # print(answer)
        json_data = json.loads(answer)
        result = json_data.pop("data").pop('questGuide')
        # print(result)
        word_answers = []
        for r in result:
            if r.get("currStatus") == 0:
                # print(r.get("wordID"), r.get("questAnswer"))
                answer = {"elapsedSec":58,"groupID":groupID,"lisTimes":15,"sysID":r.get("id"),"userAnswer": r.get("questAnswer")}
                word_answers.append(answer)
        return word_answers

    def get_mul_choice_words(self, groupID, taskID, practiceType):
        url = "{}/sysGrammar/{}/MulChoice".format(self.baseUrl, groupID)
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

    def get_mul_choice_done_data(self,groupID, practiceType):
        data = {"elapsedSec": 0, "groupID": groupID, "practiceType": practiceType, "sysID": "0"}
        return data