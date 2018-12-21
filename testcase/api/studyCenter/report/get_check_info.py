import requests
import json
from testcase.api.login.login_all_api import LoginApi
from utils.config import NewConfig


class GetCheckInfo(object):
    def __init__(self, common, headers, accesstoken):
        self.headers = headers
        self.baseUrl = common.get('baseUrl')
        self.accesstoken = accesstoken
        self.headers.update({"accesstoken": self.accesstoken})

    def get_check_info(self, sysID):
        # GET http://192.168.1.155:55262/userStudyCenter/checkInInfo?serviceID=P90 HTTP/1.1
        url = "{}/userStudyCenter/checkInInfo?serviceID={}".format(self.baseUrl, sysID)
        self.headers.update({'Content-Length': '0'})
        response = requests.request("GET", url, headers=self.headers)
        datas = json.loads(response.text).get('data')
        code = json.loads(response.text).get('code')
        return code, datas

    def post_check_in(self, sysID):
        # POST http://192.168.1.155:55262/userStudyCenter/P90/checkIn HTTP/1.1
        url = "{}/userStudyCenter/{}/checkIn".format(self.baseUrl, sysID)
        self.headers.update({'Content-Length': '0'})
        response = requests.request("POST", url, headers=self.headers)
        msg = json.loads(response.text).get('message')
        code = json.loads(response.text).get('code')
        return code, msg


if __name__ == '__main__':
    cfg_info = NewConfig()
    common, headers = cfg_info.get_info(devices_name="vivox6")
    t = LoginApi()
    access_token = t.get_access_token(common, headers)
    s_detail = GetCheckInfo(common, headers, access_token)
    code, datas = s_detail.get_check_info("P90")
    print(code)
    print(datas.get('userName'))
    print(datas.get('markWord'))
    print(datas.get('knowledgePoint'))
    print(datas.get('higherThan'))
    # for k, v in datas.items():
    #     if k == "taskInfo":
    #         for k1, v1 in v.items():
    #             if k1 == "taskDetails":
    #                 for t in v1:
    #                     print(t.get('score'))