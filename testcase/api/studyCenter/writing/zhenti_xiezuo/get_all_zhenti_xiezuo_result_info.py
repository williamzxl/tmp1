import requests
import json


class GetAllZhentiXiezuoResultInfo(object):
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

    def get_all_zhenti_xiezuo_result_info(self, groupID, taskID):
        # GET http://192.168.1.155:55262/sysWriting/2700/writing?groupID=2700&taskID=39968 HTTP/1.1
        url = "{}/sysWriting/{}/writing?groupID={}&taskID={}".format(self.baseUrl,groupID,groupID, taskID)
        response = requests.request("GET", url, headers=self.headers)
        return json.loads(response.text)