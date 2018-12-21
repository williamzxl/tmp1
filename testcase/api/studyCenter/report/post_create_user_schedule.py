import requests
import json
from testcase.api.login.login_all_api import LoginApi
from utils.config import NewConfig


class CreateUserSchedule(object):
    def __init__(self, common, headers, accesstoken):
        self.headers = headers
        self.baseUrl = common.get('baseUrl')
        self.accesstoken = accesstoken
        self.headers.update({"accesstoken": self.accesstoken})

    def create_user_schedule(self,sysID, measureID, mounth=5):
        # http://192.168.1.155:55262/userStudyCenter/P90/createUserSchedule
        url = "{}/userStudyCenter/{}/createUserSchedule".format(self.baseUrl, sysID)
        # self.headers.update({'Content-Length': '0'})
        data = {"measureID":"{}".format(measureID),"testCycle":int('{}'.format(mounth)),"version":1}
        response = requests.request("POST", url, headers=self.headers, json=data)
        datas = json.loads(response.text).get('data')
        code = json.loads(response.text).get('code')
        return code, datas
        # print(json.loads(response.text))


if __name__ == '__main__':
    cfg_info = NewConfig()
    common, headers = cfg_info.get_info(devices_name="vivox6")
    t = LoginApi()
    access_token = t.get_access_token(common, headers)
    s_detail = CreateUserSchedule(common, headers, access_token)
    r = s_detail.create_user_schedule("P90", "1912", 9)
    print(r)