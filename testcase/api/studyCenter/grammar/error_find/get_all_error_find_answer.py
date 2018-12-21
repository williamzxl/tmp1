import requests
import json


class GetAllErrorFindAnswers(object):
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

    def get_all_error_find_answer(self, groupID, taskID):
        # http://192.168.1.155:55262/sysGrammar/1909/errorFind?taskID=39794
        url = "{}/sysGrammar/{}/errorFind".format(self.baseUrl, groupID)
        querystring = {"taskID": "{}".format(taskID)}
        response = requests.request("GET", url, headers=self.headers, params=querystring)
        answer = response.text
        json_data = json.loads(answer)
        result = json_data.pop("data").pop('questGuide')
        # print("Result: ", result)
        answer = []
        sysID = ""
        for r in result:
            sysID = r.get("id")
            if r.get("currStatus") == 0:
                subQuestGuide = r.get("subQuestGuide")
                for s in subQuestGuide:
                    pre_answer = s.get("questAnswer")[0]
                    user_answer = {"userAction": None, "userAnswer": None, "wordIdx": None}
                    if "改为" in pre_answer.get("description"):
                        user_answer.update({"userAction": "m"})
                        user_a = pre_answer.get("description").split("改为")[1].strip(" ")
                        user_answer.update({"userAnswer": user_a})
                    if "去掉" in pre_answer.get("description"):
                        user_answer.update({"userAction": "d"})
                        user_answer.update({"userAnswer": ""})
                    if "之前加" in pre_answer.get("description"):
                        user_answer.update({"userAction": "i"})
                        user_a = pre_answer.get("description").split("之前加")[1].strip(" ")
                        user_answer.update({"userAnswer": user_a})
                    user_answer.update({"wordIdx": pre_answer.get("wordIdx")})
                    # {"userAction":"d","userAnswer":"","wordIdx":8}
                    answer.append(user_answer)
        return answer, sysID


if __name__ == '__main__':
    import requests

    url = "http://192.168.1.155:55262/sysGrammar/1910/errorFind"

    querystring = {"taskID": "39799"}

    headers = {
        'app': "cee",
        'platform': "Android",
        'channel': "langlib_test",
        'accesstoken': "9ba34de5-bd1d-426b-8090-7006c4338607",
        'appkey': "CEE_AA8F55B916AB",
        'appversion': "10004004",
        'appsecret': "3DB5159C-EB1E-47FE-8584-47115EF5E443",
        'host': "192.168.1.155:55262",
        'connection': "Keep-Alive",
        'accept-encoding': "gzip",
        'user-agent': "okhttp/3.11.0",
        'cache-control': "no-cache",
        'postman-token': "80a317d9-928d-28b4-60d3-8b680eee9a16"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    # print(response.text)
    answer = response.text
    json_data = json.loads(answer)
    result = json_data.pop("data").pop('questGuide')
    # print("Result: ", result)
    answer = []
    sysID = None
    for r in result:
        sysID = r.get("id")
        if r.get("currStatus") == 0:
            subQuestGuide = r.get("subQuestGuide")
            for s in subQuestGuide:
                pre_answer = s.get("questAnswer")[0]
                user_answer = {"userAction":None,"userAnswer":None,"wordIdx":None}
                if "改为" in pre_answer.get("description"):
                    user_answer.update({"userAction":"m"})
                    user_a = pre_answer.get("description").split("改为")[1].strip(" ")
                    user_answer.update({"userAnswer": user_a})
                if "去掉" in pre_answer.get("description"):
                    user_answer.update({"userAction":"d"})
                    user_answer.update({"userAnswer": ""})
                if "之前加" in pre_answer.get("description"):
                    user_answer.update({"userAction":"i"})
                    user_a = pre_answer.get("description").split("之前加")[1].strip(" ")
                    user_answer.update({"userAnswer": user_a})
                user_answer.update({"wordIdx":pre_answer.get("wordIdx")})
                # {"userAction":"d","userAnswer":"","wordIdx":8}
                answer.append(user_answer)
    print(answer)