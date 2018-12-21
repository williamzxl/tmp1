import requests
import json


class GetAllErrorFindResultInfo(object):
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

    def get_all_error_find_result_info(self, groupID, taskID):
        # GET http://192.168.1.155:55262/userGrammar/39967/2697/errorFindInfo HTTP/1.1
        url = "{}/userGrammar/{}/{}/errorFindInfo".format(self.baseUrl,taskID,groupID)
        response = requests.request("GET", url, headers=self.headers)
        return json.loads(response.text)