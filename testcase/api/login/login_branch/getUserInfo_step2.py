import requests
from testcase.api.login.login_branch.login_post_step1 import LoginToGetAccessToken
from utils.config import NewConfig
from requests.cookies import RequestsCookieJar


class GetUserInfo(LoginToGetAccessToken):
    def __init__(self):
        super(GetUserInfo).__init__()

    def check_uname(self, common, headers,accesstoken):
        self.headers = headers
        self.loginUrl = common.get('loginUrl')
        self.headers.update({"Host": common.get("loginProxy")})
        self.headers.pop('Content-Length')
        self.headers.update({"accesstoken": accesstoken})

        url = "{}/users/getUserInfo".format(self.loginUrl)
        response = requests.request("GET", url, headers=self.headers)
        return eval(response.text).get("UserName")


if __name__ == '__main__':
    cfg_info = NewConfig()
    devices = cfg_info.get_info('vivox6')
    c, h = cfg_info.get_info("vivox6")
    at = GetUserInfo()
    uname = at.check_uname(c,h, "8cb1783c-e47d-455b-9a92-0849f3d70ab1")
    print(uname)
    print("api-3" in uname)