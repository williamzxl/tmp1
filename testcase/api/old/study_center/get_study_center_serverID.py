import json
import requests
# from utils.config import get_headers
pro = "https"

class GetTaskGroupNum(object):
    def __init__(self):
        # self.headers = headers
        # self.url = self.headers.get('Host')
        pass

    def get_service_id(self, headers):
        host = headers.get("Host")
        url = "{}://{}/userStudyCenter/serviceInfo".format(pro, host)
        # http: // appncee.langb.cn / userStudyCenter / P90 / taskInfo?taskID =
        print(url)
        querystring = {"serviceID":""}
        response = requests.request("GET", url, headers=headers, params=querystring)
        result = response.text
        print(result)
        json_data = json.loads(result)
        data = json_data.pop("data")
        return (data.get('serviceID'))


    def get_task_group_id(self, headers, serviceId):
        task_group = []
        host = headers.get("Host")
        url = "{}://{}/userStudyCenter/{}/taskInfo".format(pro, host, serviceId)
        querystring = {"taskID": ""}
        response = requests.request("GET", url, headers=headers, params=querystring)
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


