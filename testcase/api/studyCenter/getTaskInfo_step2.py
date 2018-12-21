import requests
from utils.config import NewConfig


class GetTaskInfo(object):
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

    def get_task_id(self, sevicesID=None):
        url = "{}/userStudyCenter/{}/taskInfo".format(self.baseUrl, sevicesID)
        querystring = {"taskID": ""}
        response = requests.request("GET", url, headers=self.headers, params=querystring)
        data = eval(response.text).get("data")
        # print(data)
        message = eval(response.text).get("message")
        if message == "success":
            scheduleID = data.get("scheduleID")
            taskID = data.get('taskID')
            taskLists = data.get("taskList")
            return scheduleID, taskID, taskLists
        else:
            pass
        # measureID = data.get('measureID')


if __name__ == '__main__':
    cfg_info = NewConfig()
    devices = cfg_info.get_info('vivox6')
    c, h = cfg_info.get_info("vivox6")
    print(c)
    print(h)
    a = 'a29316f8-16a5-4073-b784-ce206dcb92ea'
    mI = GetTaskInfo(c,h,a)
    a = mI.get_task_id("P90")
    print(a)
