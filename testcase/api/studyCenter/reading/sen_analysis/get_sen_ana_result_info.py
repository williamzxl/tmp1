import requests
import json
from utils.logger import logger


class GetAllSenAnaResultInfo(object):
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

    def get_all_sen_ana_result_info(self, groupID, taskID):
        # GET http://192.168.1.155:55262/userReading/39967/2696/senAnalysisInfo?groupID=2696&taskID=39967 HTTP/1.1
        url = "{}/userReading/{}/{}/senAnalysisInfo".format(self.baseUrl, taskID,groupID,)
        response = requests.request("GET", url, headers=self.headers)
        return json.loads(response.text)
