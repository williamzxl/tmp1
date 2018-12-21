import requests
import json
# from utils.config import get_headers

pro = "https"


class PutAllWordsListsDone(object):
    def __init__(self):
        # self.headers = headers
        # self.url = self.headers.get('Host')
        # self.http = self.headers.get('http')
        self.pas = None

    def put_all_words_lists_done(self, headers, taskID, groupID):
        host = headers.get("Host")
        if taskID == None or groupID == None:
            pass
        else:
            url = "{}://{}/userVoc/{}/{}/vocStatus".format(pro, host, taskID, groupID)
            print("URL", url)
            headers.update({'Content-Type': 'application/json; charset=utf-8','Content-Length': '0'})
            print(headers)
            response = requests.request("PUT", url, headers=headers)
            print("response", response)
            return response


if __name__ == '__main__':
    test = PutAllWordsListsDone()
    headers = {'Platform': 'Android', 'appkey': 'CEE_AA8F55B916AB', 'appversion': '10000004', 'AppSecret': '3DB5159C-EB1E-47FE-8584-47115EF5E443', 'App': 'cee', 'accesstoken': 'd5a1206b-d1bd-4d70-932d-dbededb9b40b', 'Host': 'appncee.langlib.com', 'Connection': 'Keep-Alive', 'Accept-Encoding': 'gzip', 'User-Agent': 'okhttp/3.11.0', 'Content-Type': 'application/json; charset=utf-8', 'Content-Length': '0'}
    r = test.put_all_words_lists_done(headers, 34874, 2607)
    print(r)