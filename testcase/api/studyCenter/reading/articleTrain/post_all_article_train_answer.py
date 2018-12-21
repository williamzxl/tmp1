import requests
from utils.logger import logger
from utils.logger import logger


class PostAllArtTrainAnswers(object):
    def __init__(self, common, headers, accesstoken):
        self.headers = headers
        self.baseUrl = common.get('baseUrl')
        self.headers.update({'Content-Length': '90'})
        self.accesstoken = accesstoken
        self.headers.update({"accesstoken": self.accesstoken})
        self.headers.update({"Host": common.get("baseProxy")})

    def post_all_art_train_answer(self, taskID, user_answer):
        url = "{}/userReading/{}/saveArticleTrainAnswer".format(self.baseUrl, taskID)
        data = user_answer
        logger.info("文章训练 tID：{}，URL:{}".format(taskID, url))
        logger.info("文章训练 Post data:{}".format(data))
        response = requests.request("POST", url, headers=self.headers, json=data)
        answer = response.text
        logger.info("文章训练 Response:{}".format(answer))
        # if answer.get("message") == "success":
        #     logger.info("[PASS] == {},{}",taskID, user_answer)
        # if answer.get("message") != "success":
        #     logger.info("[FAIL] == {},{}", taskID, user_answer)

    def put_article_train_words(self, data):
        url = "{}/vocabularies/familiarity".format(self.baseUrl)
        logger.info("文章训练 Put 生词表 URL:{}".format(url))
        response = requests.request("PUT", url, headers=self.headers, json=data)
        logger.info("文章训练 Put 生词表 Response:{}".format(response))
        return response

    def put_article_train_done(self, taskID, data):
        url = "{}/userVocabulary/{}/vocStatus".format(self.baseUrl, taskID)
        logger.info("文章训练 Done 生词表 URL:{}".format(url))
        for d in data:
            response = requests.request("PUT", url, headers=self.headers, json=d)
            logger.info("文章训练 Done 生词表 Response:{}".format(response))
            return response