import requests
from utils.config import NewConfig


class GetServiceInfo(object):
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

    def get_service_id(self):
        url = "{}/userStudyCenter/serviceInfo".format(self.baseUrl)
        querystring = {"serviceID": ""}
        response = requests.request("GET", url, headers=self.headers, params=querystring)
        data = eval(response.text).get("data")
        # print(data)
        message = eval(response.text).get("message")
        if message == "success":
            serviceID = data.get('serviceID')
            measureID = data.get("measureID")
            scheduleID = data.get("scheduleID")
            return serviceID, measureID, scheduleID
        else:
            pass
        # measureID = data.get('measureID')


if __name__ == '__main__':
    pass