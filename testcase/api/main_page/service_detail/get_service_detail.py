import requests
import json
import ast
from testcase.api.login.login_all_api import LoginApi
from utils.config import NewConfig


class GetServiceDetail(object):
    def __init__(self, common, headers, accesstoken):
        self.headers = headers
        self.baseUrl = common.get('baseUrl')
        self.accesstoken = accesstoken
        self.headers.update({"accesstoken": self.accesstoken})

    def get_service_detail(self):
        url = "{}/services/detail".format(self.baseUrl)
        self.headers.update({'Content-Length': '0'})
        response = requests.request("GET", url, headers=self.headers)
        datas = json.loads(response.text).get('data')
        s_overiew = datas.pop('serviceOverview')
        for s in s_overiew:
            datas.update(s)
        return datas


if __name__ == '__main__':
    cfg_info = NewConfig()
    common, headers = cfg_info.get_info(devices_name="vivox6")
    t = LoginApi()
    access_token = t.get_access_token(common, headers)
    print(common)
    print(headers)
    print(access_token)
    s_detail = GetServiceDetail(common, headers, access_token)
    r = s_detail.get_service_detail()
    print(r)