import requests
import time
import json
from random import randrange
from utils.file_writer import YamlWriter
from utils.file_reader import YamlReader
from utils.logger import logger


class AutoToGetAccount(object):
    def __init__(self):
        self.url_login_register = None
        self.url_register = "https://background.langb.cn/SystemUser/UserService/Register"
        self.headers_register = {
            'host': "background.langb.cn",
            'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0",
            'accept': "application/json, text/javascript, */*; q=0.01",
            'accept-language': "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
            'accept-encoding': "gzip, deflate, br",
            'referer': "https://background.langb.cn/SystemUser/UserService/AutoRegisterMng",
            'content-type': "application/json;charset=utf-8",
            'x-requested-with': "XMLHttpRequest",
            'content-length': "75",
            'connection': "keep-alive",
            'cookie': "__root_domain_v=.langb.cn; _qddaz=QD.pktt7g.zdvf2m.jj3ociby; ckname=dlone; ckpwd=8F5F3FB2BD07AFBEB45680FEAE728624; username=dlone",
            'cache-control': "no-cache",
            'postman-token': "253a4b1d-e4dd-90d0-748a-bfabc5f95003"
        }

    def register_account(self):
        self.data = {"emails": "t-{}@t.com".format(time.strftime('%m%d-%M')), "fromSource": "-1",
                     "userLabel": "9,-1,-1,-1,-1"}
        response = requests.request("POST", self.url_register, headers=self.headers_register, json=self.data)
        result = json.loads(response.text)
        # return result.get('Success'), self.data.get('emails')
        # print(result)
        if result.get('Success') == 1:
            return self.data.get('emails')
        if result.get('Success') == 0:
            time.sleep(70)
            self.data.update({"emails": "t-{}@t.com".format(time.strftime('%m%d-%M-{}'.format(randrange(0,99,2))))})
            # print(self.data)
            logger.warning("warning*************************change uname:{}".format(self.data.get('emails')))
            requests.request("POST", self.url_register, headers=self.headers_register, json=self.data)
            return self.data.get('emails')
        else:
            return False

    def change_cfg_ymal(self, file, new_account):
        write_account = YamlWriter(file)
        result = write_account.write_data(new_account)
        read_account = YamlReader(file)
        read_info = read_account.data
        if read_info[0][0].get('vivox6').get('common').get('uname') == new_account:
            return True
        else:
            return False


if __name__ == '__main__':
    file = r"C:\Users\liuda\Desktop\CEE\API_test\CEE_api_test\config\config001.yml"
    account = AutoToGetAccount()
    code, a = account.register_account()
    print(code, a)
    if code == 1:
        a = code
    else:
        pass
    # print(s)
    # result = account.change_cfg_ymal(file, s)
    # print(result)


