import requests
from utils.config import NewConfig


class StartLearning(object):
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

    def start_to_learn(self, scheduleID=None):
        url = "{}/userStudyCenter/{}/startLearning".format(self.baseUrl, scheduleID)
        response = requests.request("PUT", url, headers=self.headers)
        message = eval(response.text).get("message")
        if message == "success":
            print("success")
            return 1
        else:
            pass


if __name__ == '__main__':
    cfg_info = NewConfig()
    devices = cfg_info.get_info('vivox6')
    c, h = cfg_info.get_info("vivox6")
    print(c)
    print(h)
    a = 'a29316f8-16a5-4073-b784-ce206dcb92ea'
    mI = StartLearning(c, h, a)
    a = mI.start_to_learn("2496")
    print(a)
