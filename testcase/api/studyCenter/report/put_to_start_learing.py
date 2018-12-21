import requests
import json
from testcase.api.login.login_all_api import LoginApi
from utils.config import NewConfig


class StartLearning(object):
    def __init__(self, common, headers, accesstoken):
        self.headers = headers
        self.baseUrl = common.get('baseUrl')
        self.accesstoken = accesstoken
        self.headers.update({"accesstoken": self.accesstoken})

    def star_learning(self, scheduleID):
        url = "{}/userStudyCenter/{}/startLearning".format(self.baseUrl,scheduleID)
        self.headers.update({'Content-Length': '0'})
        response = requests.request("PUT", url, headers=self.headers)
        code = json.loads(response.text).get('code')
        msg = json.loads(response.text).get('message')
        return code, msg


if __name__ == '__main__':
    cfg_info = NewConfig()
    common, headers = cfg_info.get_info(devices_name="vivox6")
    t = LoginApi()
    access_token = t.get_access_token(common, headers)
    # print(access_token)
    # print(common)
    # print(headers)
    s_detail = StartLearning(common, headers, access_token)
    c, m = s_detail.star_learning(2546)
    print(c, m)