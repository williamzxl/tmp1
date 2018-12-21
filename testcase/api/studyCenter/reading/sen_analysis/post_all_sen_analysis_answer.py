import requests
from utils.logger import logger


class PostAllSenAnAAnswers(object):
    def __init__(self, common, headers, accesstoken):
        self.headers = headers
        self.baseUrl = common.get('baseUrl')
        self.headers.update({'Content-Length': '90'})
        self.accesstoken = accesstoken
        self.headers.update({"accesstoken": self.accesstoken})
        self.headers.update({"Host": common.get("baseProxy")})

    def post_all_sen_analysis_answer(self, taskID, user_answer):
        url = "{}/userReading/{}/saveSenAnalysisAnswer".format(self.baseUrl, taskID)
        data = user_answer
        response = requests.request("POST", url, headers=self.headers, json=data)
        answer = response.text
        print("response.text", response.text)
        # if answer.get("message") == "success":
        #     logger.info("[PASS] == {},{}", taskID, user_answer)
        # if answer.get("message") != "success":
        #     logger.info("[FAIL] == {},{}", taskID, user_answer)
        # return True

    def put_sa_words(self, data):
        url = "{}/vocabularies/familiarity".format(self.baseUrl)
        response = requests.request("PUT", url, headers=self.headers, json=data)
        return response

    def put_sa_done(self, data, taskID):
        url = "{}/userVocabulary/{}/vocStatus".format(self.baseUrl, taskID)
        res = requests.request("PUT", url, headers=self.headers, json=data)
        return res