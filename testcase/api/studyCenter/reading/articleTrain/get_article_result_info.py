import requests
import json
from utils.logger import logger


class GetAllArtTrainResultInfo(object):
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

    def get_all_art_train_result_info(self, groupID, taskID):
        url = "{}/userReading/{}/{}/articleTrainInfo".format(self.baseUrl, taskID,groupID,)
        response = requests.request("GET", url, headers=self.headers)
        return json.loads(response.text)
