import requests
from utils.config import NewConfig
from requests.cookies import RequestsCookieJar


class GetUserInfo(object):
    def __init__(self, common, headers):
        self.headers = headers
        self.loginUrl = common.get('loginUrl')
        self.uname = common.get("uname")
        self.pwd = common.get("pwd")
        self.headers.update({"Host": common.get("loginProxy"), "accesstoken":'0c7888f4-9a57-4b1f-a372-4da82652b7ca'})
        self.headers.pop('Content-Length')

    def check_uname(self):
        url = "{}/users/getUserInfo".format(self.loginUrl)
        response = requests.request("GET", url, headers=self.headers)
        print(response.text)


if __name__ == '__main__':
    cfg_info = NewConfig()
    devices = cfg_info.get_info('vivox6')
    c, h = cfg_info.get_info("vivox6")
    print(c)
    print(h)
    at = GetUserInfo(c, h)
    at.check_uname()