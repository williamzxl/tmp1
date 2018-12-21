import requests
import json
from utils.logger import logger


class PostAllMulChoiceAnswers(object):
    def __init__(self, common, headers, accesstoken):
        self.headers = headers
        self.baseUrl = common.get('baseUrl')
        self.headers.update({'Content-Length': '90'})
        self.accesstoken = accesstoken
        self.headers.update({"accesstoken": self.accesstoken})
        self.headers.update({"Host": common.get("baseProxy")})

    def post_all_mul_choice_answer(self, taskID, user_answer):
        url = "{}/userGrammar/{}/saveMulChoiceAnswer".format(self.baseUrl, taskID)
        data = user_answer
        response = requests.request("POST", url, headers=self.headers, json=data)
        answer = response.text
        # if answer.get("message") == "success":
        #     logger.info("[PASS] == {},{}",taskID, user_answer)
        # if answer.get("message") != "success":
        #     logger.info("[FAIL] == {},{}", taskID, user_answer)

    def put_mul_choice_words(self, data):
        # print("====================",data)
        url = "{}/vocabularies/familiarity".format(self.baseUrl)
        response = requests.request("PUT", url, headers=self.headers, json=data)
        return response

    def put_mul_choice_done(self, data, taskID):
        url = "{}/userVocabulary/{}/vocStatus".format(self.baseUrl, taskID)
        res = requests.request("PUT", url, headers=self.headers, json=data)
        return res