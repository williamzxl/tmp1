import requests
import json


class CreateCeeServices(object):
    def __init__(self):
        self.uname = "13121868833"
        self.pwd = "123456"
        self.login_opa_url = "http://adm-opa.langb.cn/ajax/login"
        self.headers_login_opa = {
            'host': "adm-opa.langb.cn",
            'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0",
            'accept': "application/json, text/javascript, */*; q=0.01",
            'accept-language': "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
            'accept-encoding': "gzip, deflate, br",
            'referer': "https://adm-opa.langb.cn/login",
            'content-type': "application/json;charset=utf-8",
            'x-requested-with': "XMLHttpRequest",
            'content-length': "48",
            'connection': "keep-alive",
            'cache-control': "no-cache",
        }
        self.url_create_services = "http://adm-opa.langb.cn/ceeService/ajax/createCEEService"
        self.get_user_id_url = "http://adm-opa.langb.cn/ceeService/ajax/messages/findUserServiceByCredential"

    def login_opa_create_cee_services(self, account, servicesID):
        session = requests.Session()
        data = {"UserCredential":self.uname,"Password":self.pwd}
        response = session.post(self.login_opa_url, headers=self.headers_login_opa, json=data)
        result = json.loads(response.text)
        if result.get('CellPhone') == data.get('UserCredential'):
            create_services_data = {"cellPhone" : "{}".format(account),"serviceID":"{}".format(servicesID),"payAmount":0,"userRemark":""}
            c_response = session.post(self.url_create_services, headers=self.headers_login_opa, json=create_services_data)
            # print(c_response.text)
            if json.loads(c_response.text).get('Code') == 0:
                return True, json.loads(c_response.text).get('Message')
            if json.loads(c_response.text).get('Code') != 0:
                return True, json.loads(c_response.text).get('Message')
        else:
            return False,None

    def get_user_id(self, account):
        session = requests.Session()
        data = {"UserCredential": self.uname, "Password": self.pwd}
        response = session.post(self.login_opa_url, headers=self.headers_login_opa, json=data)
        result = json.loads(response.text)
        print(result)
        querystring = {"credential": "{}".format(account)}
        self.headers_login_opa.update({'content-length': "0"})
        r = session.get(self.get_user_id_url, headers=self.headers_login_opa, params=querystring)
        res = json.loads(r.text)
        print(res,querystring)
        return res[0].get('UserID')


if __name__ == '__main__':
    c = CreateCeeServices()
    msg = c.get_user_id("t-1204-08@t.com")
    print(msg)