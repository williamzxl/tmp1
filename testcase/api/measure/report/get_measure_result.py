import requests
import json
from testcase.api.login.login_all_api import LoginApi
from utils.config import NewConfig


class GetMeasureResult(object):
    def __init__(self, common, headers, accesstoken):
        self.headers = headers
        self.baseUrl = common.get('baseUrl')
        self.accesstoken = accesstoken
        self.headers.update({"accesstoken": self.accesstoken})

    def get_measure_result(self, measureID):
        # GET http://192.168.1.155:55262/userStudyCenter/1878/measureResult HTTP/1.1
        url = "{}/userStudyCenter/{}/measureResult".format(self.baseUrl, measureID)
        self.headers.update({'Content-Length': '0'})
        response = requests.request("GET", url, headers=self.headers)
        datas = json.loads(response.text).get('data')
        code = json.loads(response.text).get('code')
        return code, datas


if __name__ == '__main__':
    pass