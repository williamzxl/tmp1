import requests
from utils.logger import logger


class PostAllZhentiXiezuoAnswers(object):
    def __init__(self, common, headers, accesstoken):
        self.headers = headers
        self.baseUrl = common.get('baseUrl')
        self.headers.update({'Content-Length': '90'})
        self.accesstoken = accesstoken
        self.headers.update({"accesstoken": self.accesstoken})
        self.headers.update({"Host": common.get("baseProxy")})

    def post_all_zhenti_xiezuo_answer(self, taskID, user_answer):
        url = "{}/userWriting/{}/saveWritingAnswer".format(self.baseUrl, taskID)
        data = user_answer
        response = requests.request("POST", url, headers=self.headers, json=data)
        answer = response.text
        try:
            if answer.get("message") == "success":
                logger.info("[PASS] == {},{}", taskID, user_answer)
            if answer.get("message") != "success":
                logger.info("[FAIL] == {},{}", taskID, user_answer)
        except:
            pass

    def put_word_spell_words(self, data):
        url = "{}/vocabularies/familiarity".format(self.baseUrl)
        response = requests.request("PUT", url, headers=self.headers, json=data)
        return response