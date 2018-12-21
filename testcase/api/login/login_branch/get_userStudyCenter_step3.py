import requests
from utils.config import NewConfig
from testcase.api.login.login_branch.getUserInfo_step2 import GetUserInfo


class GetUserStudyCenter(GetUserInfo):
    def __init__(self):
        super(GetUserStudyCenter, self).__init__()

    def get_user_study_center(self,common, headers, accesstoken):
        self.headers = headers
        self.common = common
        self.baseUrl = self.common.get('baseUrl')
        self.headers.update({"accesstoken": accesstoken})
        self.headers.update({"Host": common.get("baseProxy")})
        url = "{}/userStudyCenter/serviceInfo".format(self.baseUrl)
        querystring = {"serviceID": ""}
        try:
            self.headers.pop('Content-Length')
        except:
            pass
        # print(self.headers)
        response = requests.request("GET", url, headers=self.headers, params=querystring)
        data = eval(response.text).get("data")
        # print(data)
        currentStatus = data.get('currStatus')
        if currentStatus or not currentStatus:
            serviceID = data.get('serviceID')
            return serviceID
        else:
            pass


if __name__ == '__main__':
    cfg_info = NewConfig()
    devices = cfg_info.get_info('vivox6')
    c, h = cfg_info.get_info("vivox6")
    print(c)
    print(h)
    a = 'd6733211-3324-4887-8b63-b173070120d4'
    at = GetUserStudyCenter()
    si= at.get_user_study_center(c, h, a)
    print(si)
