import requests
import json
from testcase.api.login.login_all_api import LoginApi
from utils.config import NewConfig


class GetMeasureReport(object):
    def __init__(self, common, headers, accesstoken):
        self.headers = headers
        self.baseUrl = common.get('baseUrl')
        self.accesstoken = accesstoken
        self.headers.update({"accesstoken": self.accesstoken})

    def get_measure_report(self, measureID):
        # http://192.168.1.155:55262/userMeasure/1877/measureReport?measureID=1877 HTTP
        url = "{}/userMeasure/{}/measureReport?measureID={}".format(self.baseUrl, measureID, measureID)
        self.headers.update({'Content-Length': '0'})
        # print("-----------------------------", self.headers)
        response = requests.request("GET", url, headers=self.headers)
        # print(response.text)
        datas = json.loads(response.text).get('data')
        code = json.loads(response.text).get('code')
        return code, datas


if __name__ == '__main__':
    cfg_info = NewConfig()
    common, headers = cfg_info.get_info(devices_name="vivox6")
    t = LoginApi()
    access_token = t.get_access_token(common, headers)
    print(common)
    print(headers)
    print(access_token)
    s_detail = GetMeasureReport(common, headers, access_token)
    r = s_detail.get_measure_report()
    print(r)