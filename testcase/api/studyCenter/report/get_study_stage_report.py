import requests
import json
from testcase.api.login.login_all_api import LoginApi
from utils.config import NewConfig


class GetStudyStageReport(object):
    def __init__(self, common, headers, accesstoken):
        self.headers = headers
        self.baseUrl = common.get('baseUrl')
        self.accesstoken = accesstoken
        self.headers.update({"accesstoken": self.accesstoken})

    def get_study_stage_report(self, sysID):
        # GET http://192.168.1.155:55262/userStudyCenter/P90/studyStageReport?scheduleID= HTTP/1.1
        url = "{}/userStudyCenter/{}/studyStageReport?scheduleID=".format(self.baseUrl, sysID)
        self.headers.update({'Content-Length': '0'})
        response = requests.request("GET", url, headers=self.headers)
        datas = json.loads(response.text).get('data')
        code = json.loads(response.text).get('code')
        return code, datas


if __name__ == '__main__':
    cfg_info = NewConfig()
    common, headers = cfg_info.get_info(devices_name="vivox6")
    t = LoginApi()
    access_token = t.get_access_token(common, headers)
    s_detail = GetStudyStageReport(common, headers, access_token)
    code, datas = s_detail.get_study_stage_report("P90")
    for k, v in datas.items():
        if k == "taskInfo":
            for k1, v1 in v.items():
                if k1 == "taskDetails":
                    for t in v1:
                        print(t.get('score'))