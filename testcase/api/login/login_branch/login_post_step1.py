import requests
import json
from utils.config import NewConfig


class LoginToGetAccessToken(object):
    def __init__(self, ):
        pass

    def get_access_token(self, common, headers):
        self.headers = headers
        self.loginUrl = common.get('loginUrl')
        self.uname = common.get("uname")
        self.pwd = common.get("pwd")
        self.headers.update({"Host": common.get("loginProxy")})
        url = "{}/accounts/loginByAccount".format(self.loginUrl)
        body = {"UserCredential": "{}".format(self.uname), "Password": "{}".format(self.pwd)}
        response = requests.request("POST", url, headers=self.headers, json=body)
        content = (json.loads(response.text))
        access_token = content.get("AccessToken")
        return access_token


if __name__ == '__main__':
    cfg_info = NewConfig()
    devices = cfg_info.get_info('vivox6')
    c, h = cfg_info.get_info("vivox6")
    print(c)
    print(h)
    at = LoginToGetAccessToken()
    a = at.get_access_token(c, h)
    print(a)
