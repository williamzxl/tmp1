import requests
import json


class GetAllZhentiXirzuoAnswers(object):
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

    def get_all_zhenti_xiezuo_answer(self, groupID, taskID):
        url = "{}/sysWriting/{}/writing".format(self.baseUrl, str(groupID))
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
                userAnswer = ""
                allAnswer = ""
                if r.get("letterHead"):
                    # print('r.get("letterHead")',r.get("letterHead"))
                    letterHead = r.get("letterHead")
                    try:
                        allAnswer = r.get("modelEssay").split(letterHead)[1]
                    except:
                        pass
                if r.get("letterFoot"):
                    letterFoot = r.get("letterFoot")
                    try:
                        userAnswer = "".join(allAnswer).split(letterFoot)[0]
                    except:
                        pass
                userAnswer = "a " * 90
                answer = {"elapsedSec": 30, "groupID":groupID,"sysID":r.get("id"),"userAnswer": userAnswer,"userAction": 2}
                word_answers.append(answer)
        return word_answers