import requests
from utils.logger import logger

class PostAllSecTrainAnswers(object):
    def __init__(self, common, headers, accesstoken):
        self.headers = headers
        self.baseUrl = common.get('baseUrl')
        self.accesstoken = accesstoken
        self.headers.update({"accesstoken": self.accesstoken})
        self.headers.update({"Host": common.get("baseProxy")})

    def post_all_sec_train_answer(self, taskID, user_answer):
        url = "{}/userReading/{}/savesectionTrainAnswer".format(self.baseUrl, taskID)
        data = user_answer
        response = requests.request("POST", url, headers=self.headers, json=data)
        answer = response.text
        return answer

    def put_sec_train_words(self, data):
        url = "{}/vocabularies/familiarity".format(self.baseUrl)
        response = requests.request("PUT", url, headers=self.headers, json=data)
        return response

    def put_sec_train_words_done(self, taskID, data):
        url = "{}/userVocabulary/{}/vocStatus".format(self.baseUrl, taskID)
        self.headers.update({'Content-Length': '90'})
        print("URL",data, url, self.headers)
        for d in data:
            response = requests.request("PUT", url, headers=self.headers, json=d)
            return response