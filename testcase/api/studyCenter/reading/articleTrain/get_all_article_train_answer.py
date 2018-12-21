import requests
import json
from utils.logger import logger


class GetAllArtTrainAnswers(object):
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

    def get_all_art_train_answer(self, groupID, taskID):
        url = "{}/sysReading/{}/articleTrain".format(self.baseUrl, groupID)
        querystring = {"taskID": "{}".format(taskID)}
        logger.info("文章训练AAAAAAAAAAAAAAAA gID:{},tID：{}，URL:{}".format(groupID, taskID, url))
        response = requests.request("GET", url, headers=self.headers, params=querystring)
        answer = response.text
        logger.info("文章训练AAAAAAAAAAAAAAAA Response:{}".format(answer))
        json_data = json.loads(answer)
        result = json_data.pop("data").pop('questGuide')
        logger.info("文章训练AAAAAAAAAAAAAAAA Result:{}".format(result))
        # print("Result: ", result)
        all_answers = []
        for q in result:
            # print(q)
            if q.get("currStatus") == 0:
                for r in q.get("steps"):
                    if r.get("currStatus") == 0 and len(r.get("subQuestGuide")) == 0:
                        answer = {"groupID":groupID,"newF":3,"sysID":q.get('id'),"taskID":taskID}
                        all_answers.append(answer)
                    if r.get("currStatus") == 0 and len(r.get("subQuestGuide")) != 0:
                        for s in r.get("subQuestGuide"):
                            if s.get("currStatus") == 0 and len(s.get("subQuestGuide")) == 0:
                                answer = {"elapsedSec": 68, "groupID": groupID, "sysID": s.get('id'),
                                          "userAnswer": s.get("questAnswer"), "stepType":r.get("stepType"), "userLabel":" "}
                                all_answers.append(answer)
                            if s.get("currStatus") == 0 and len(s.get("subQuestGuide")) != 0:
                                for step3 in s.get("subQuestGuide"):
                                    answer = {"elapsedSec": 78, "groupID": groupID, "sysID": step3.get('id'),
                                          "userAnswer": step3.get("questAnswer"), "stepType":r.get("stepType"), "userLabel":""}
                                    all_answers.append(answer)
        print(all_answers)
        logger.info("文章训练AAAAAAAAAAAAAAAA All answer:{}".format(all_answers))
        return all_answers

    def get_article_train_words(self, groupID, taskID, practiceType):
        url = "{}/sysReading/{}/articleTrain".format(self.baseUrl, groupID)
        querystring = {"taskID": "{}".format(taskID)}
        response = requests.request("GET", url, headers=self.headers, params=querystring)
        logger.info("文章训练 生词表 URL:{}".format(url))
        answer = response.text
        logger.info("文章训练 生词表 Response:{}".format(answer))
        json_data = json.loads(answer)
        voc = json_data.pop("data").pop('questGuide')
        logger.info("文章训练 生词表 Result:{}".format(voc))
        result = {}
        for v in voc:
            result = v.get("vocabulary")
        # print("Result: ", result)
        if result.get("currStatus") == 0:
            stars_3 = []
            words = result.get("wordsList")
            for w in words:
                # print("W", w.get('familiarity'))
                star_3 = {"groupID": groupID, "newF": 3, "oldF": w.get("familiarity"), "practiceType": practiceType,
                          "sysID": "", "taskID": taskID, "wordID": w.get("wordID")}
                stars_3.append(star_3)
            return stars_3

    def get_articleTrain_word_done_data(self, groupID, taskID, practiceType):
        # https://appncee.langlib.com/sysReading/2491/articleTrain?taskID=37043
        # {"elapsedSec": 0, "groupID": "1880", "practiceType": 7, "sysID": "13-Shaanxi-GraFill-1"}
        url = "{}/sysReading/{}/articleTrain".format(self.baseUrl, groupID)
        querystring = {"taskID": "{}".format(taskID)}
        response = requests.request("GET", url, headers=self.headers, params=querystring)
        answer = response.text
        json_data = json.loads(answer)
        result = json_data.pop("data").pop('questGuide')
        # print("Result: ", result)
        data = []
        for q in result:
            # print(q)
            if q.get("currStatus") == 0:
                for r in q.get("steps"):
                    # print("r", r.get("stepName"), r.get("currStatus"))
                    if r.get("currStatus") == 0 and len(r.get("subQuestGuide")) == 0:
                        answer = {"elapsedSec": 10, "groupID": groupID, "practiceType": practiceType, "sysID": q.get('id')}
                        data.append(answer)
        print(data)
        return data