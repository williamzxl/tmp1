import requests
from utils.logger import logger

# {"elapsedSec":22,"groupID":"1909","sysID":"09-Xinkebiao-Errorfind-1","userAnswer":[{"userAction":"d","userAnswer":"","wordIdx":8},{"userAction":"d","userAnswer":"","wordIdx":19},{"userAction":"d","userAnswer":"","wordIdx":28}]}
class PostAllErrorFindAnswers(object):
    def __init__(self, common, headers, accesstoken):
        self.headers = headers
        self.baseUrl = common.get('baseUrl')
        self.headers.update({'Content-Length': '90'})
        self.accesstoken = accesstoken
        self.headers.update({"accesstoken": self.accesstoken})
        self.headers.update({"Host": common.get("baseProxy")})

    def post_all_error_find_answer(self, taskID, groupID, user_answer, sysID):
        # http://192.168.1.155:55262/userGrammar/39799/saveErrorFindAnswer HTTP/1.1
        url = "{}/userGrammar/{}/saveErrorFindAnswer".format(self.baseUrl, taskID)
        user_answers = {"elapsedSec":22,"groupID":groupID,"sysID": sysID, "userAnswer":user_answer}
        data = user_answers
        print(data)
        response = requests.request("POST", url, headers=self.headers, json=data)
        print(response)
        return response