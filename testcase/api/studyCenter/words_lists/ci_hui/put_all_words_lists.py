import requests
import json


class PutAllWordsListsDone(object):
    def __init__(self, common, headers, accesstoken):
        self.headers = headers
        self.baseUrl = common.get('baseUrl')
        try:
            self.headers.pop('Content-Length')
        except:
            pass
        self.accesstoken = accesstoken
        self.headers.update({"accesstoken": self.accesstoken})

    def get_word_list_words(self, groupID, taskID, practiceType):
        # print(groupID, taskID)https://appncee.langlib.com/sysReading/2475/?groupID=2475&taskID=37037
        url = "{}/sysVoc/{}/{}/voc".format(self.baseUrl, taskID, groupID)
        # querystring = {"taskID": "{}".format(taskID)}
        response = requests.request("GET", url, headers=self.headers)
        answer = response.text
        # print("answer", answer)
        json_data = json.loads(answer)
        result = json_data.pop("data").pop('questGuide')
        stars_3 = []
        for w in result:
            # if w.get("currStatus") == 0:
            star_3 = {"groupID": groupID, "newF": 3, "oldF": w.get("familiarity"), "practiceType": practiceType,
                      "sysID": "", "taskID": taskID, "wordID": w.get("wordID")}
            stars_3.append(star_3)
        # print("Start", stars_3)
        return stars_3

    def put_wordsList_3star(self, data):
        url = "{}/vocabularies/familiarity".format(self.baseUrl)
        response = requests.request("PUT", url, headers=self.headers, json=data)
        # print("R" * 10,response, data)
        return response

    def put_all_words_lists_done(self, d):
        try:
            url = "{}/userVoc/{}/{}/vocStatus".format(self.baseUrl, d.get('taskID'), d.get('groupID'))
            data = {"elapsedSec":6590}
            # print("URL", url)
            response = requests.request("PUT", url, headers=self.headers,json=data)
            return response
        except:
            pass


if __name__ == '__main__':
    test = PutAllWordsListsDone()
    r = test.put_all_words_lists_done(34487, 2611)
    print(r)