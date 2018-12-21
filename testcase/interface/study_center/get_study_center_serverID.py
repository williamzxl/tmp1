import json
import requests
from utils.config import get_headers


class GetTaskGroupNum(object):
    def __init__(self):
        # self.url = "appncee_dev.langb.cn"
        self.headers = get_headers()
        self.url = self.headers.get('Host')

    def get_service_id(self):
        url = "http://{}/userStudyCenter/serviceInfo".format(self.url)
        # http: // appncee.langb.cn / userStudyCenter / P90 / taskInfo?taskID =
        print(url)
        querystring = {"serviceID":""}
        response = requests.request("GET", url, headers=self.headers, params=querystring)
        result = response.text
        print(result)
        json_data = json.loads(result)
        data = json_data.pop("data")
        return (data.get('serviceID'))


    def get_task_group_id(self, serviceId):
        task_group = []
        url = "http://{}/userStudyCenter/{}/taskInfo".format(self.url, serviceId)
        querystring = {"taskID": ""}
        response = requests.request("GET", url, headers=self.headers, params=querystring)
        json_data = json.loads(response.text)
        try:
            result0 = json_data.get("data").get('userCourse').get('mtdCourse')
        except:
            pass
        result = json_data.get("data").get('practice')
        try:
            for n in result0:
                task_group.append(n)
        except:
            pass
        for i in result:
            for j in i.get("questGuide"):
                task_group.append(j)
        return task_group


if __name__ == '__main__':
    task_group = GetTaskGroupNum()
    serviceID = task_group.get_service_id()
    print(serviceID)
    result = task_group.get_task_group_id(serviceID)
    for i in result:
        print(i.get("groupID"), i.get("taskID"), i.get("currStatus"))


