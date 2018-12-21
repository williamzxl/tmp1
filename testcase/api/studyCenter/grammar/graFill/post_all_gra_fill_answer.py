import requests
from utils.logger import logger


class PostAllGraFillAnswers(object):
    def __init__(self, common, headers, accesstoken):
        self.headers = headers
        self.baseUrl = common.get('baseUrl')
        self.headers.update({'Content-Length': '90'})
        self.accesstoken = accesstoken
        self.headers.update({"accesstoken": self.accesstoken})
        self.headers.update({"Host": common.get("baseProxy")})

    def post_all_gra_fill_answer(self, taskID, user_answer):
        url = "{}/userGrammar/{}/savegraFillAnswer".format(self.baseUrl, taskID)
        data = user_answer
        # print(user_answer)
        response = requests.request("POST", url, headers=self.headers, json=(data))
        answer = response.text
        # if answer.get("me/ssage") == "success":
        #     logger.info("[/PASS] == {},{}",taskID, user_answer)
        # if answer.get("message") != "success":
        #     logger.info("[FAIL] == {},{}", taskID, user_answer)

    def put_gra_fill_words(self, data):
        url = "{}/vocabularies/familiarity".format(self.baseUrl)
        response = requests.request("PUT", url, headers=self.headers, json=data)
        return response

    def put_gra_fill_words_done(self, taskID, data):
        # {"elapsedSec": 0, "groupID": "1880", "practiceType": 7, "sysID": "13-Shaanxi-GraFill-1"}
        # https://appncee.langlib.com/userVocabulary/37038/vocStatus HTTP/1.1
        url = "{}/userVocabulary/{}/vocStatus".format(self.baseUrl, taskID)
        response = requests.request("PUT", url, headers=self.headers, json=data)
        print("GRA_FIL", data)
        return response