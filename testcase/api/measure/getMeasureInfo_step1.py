import requests
from utils.config import NewConfig


class GetMeasureInfo(object):
    def __init__(self, common, headers, accesstoken):
        self.headers = headers
        self.baseUrl = common.get('baseUrl')
        try:
            self.headers.pop('Content-Length')
        except:
            pass
        self.accesstoken = accesstoken
        self.headers.update({"accesstoken": self.accesstoken})

    def get_sys_id(self, serviceID="0"):
        url = "{}/userMeasure/{}/measureInfo".format(self.baseUrl, serviceID)
        response = requests.request("GET", url, headers=self.headers)
        data = eval(response.text).get("data")
        message = eval(response.text).get("message")
        if message == "success":
            sysID = data.get('sysID')
            measureID = data.get("measureID")
            studyType = data.get("studyType")
            return sysID, measureID, studyType
        else:
            return None ,eval(response.text), None


if __name__ == '__main__':
    cfg_info = NewConfig()
    devices = cfg_info.get_info('vivox6')
    c, h = cfg_info.get_info("vivox6")
    print(c)
    print(h)
    a = 'a29316f8-16a5-4073-b784-ce206dcb92ea'
    mI = GetMeasureInfo(c,h,a)
    a = mI.get_sys_id("P90")
    print(a)
