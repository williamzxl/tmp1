import json
import requests
from utils.config import NewConfig
from utils.logger import logger


class GetTaskInfo2(object):
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

    def get_all_tasks_id(self, sevicesID=None):
        # if P == None:
        url = "{}/userStudyCenter/{}/taskInfo".format(self.baseUrl, sevicesID)
        # else:
        #     url = "{}/userStudyCenter/{}/taskInfo".format(self.baseUrl, sevicesID)
        querystring = {"taskID": ""}
        response = requests.request("GET", url, headers=self.headers, params=querystring)
        logger.info("6666666666666:{}".format(json.loads(response.text)))
        data = json.loads(response.text).get("data")
        message = json.loads(response.text).get("message")
        if message.lower() == "success":
            practice = data.get('practice')
            if len(practice) == 0:
                return data.get("countdown"), data.get('scheduleID')
            else:
                all_tasks = []
                for p in practice:
                    if p.get("studyType") == "VOC":
                        lists = p.get("questGuide")
                        voc = {"VOC": lists}
                        all_tasks.append(voc)
                    if p.get("studyType") == "LIS":
                        listens = p.get("questGuide")
                        listen = {"LIS": listens}
                        all_tasks.append(listen)
                    if p.get("studyType") == "RID":
                        reads = p.get("questGuide")
                        read = {"RID": reads}
                        all_tasks.append(read)
                    if p.get("studyType") == "WRI":
                        writes = p.get("questGuide")
                        write = {"WRI": writes}
                        all_tasks.append(write)
                    if p.get("studyType") == "GRA":
                        gras = p.get("questGuide")
                        gra = {"GRA": gras}
                        all_tasks.append(gra)
                logger.info("All tasks:{},{}".format(len(all_tasks),all_tasks))
                return all_tasks


if __name__ == '__main__':
    cfg_info = NewConfig()
    devices = cfg_info.get_info('vivox6')
    c, h = cfg_info.get_info("vivox6")
    a = 'a29316f8-16a5-4073-b784-ce206dcb92ea'
    mI = GetTaskInfo2(c,h,a)
    a = mI.get_task_id("P90")
    print(a)
