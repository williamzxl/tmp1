import requests
from utils.config import NewConfig


class PostMeasureWords(object):
    def __init__(self, common, headers, accesstoken):
        self.headers = headers
        self.baseUrl = common.get('baseUrl')
        self.accesstoken = accesstoken
        self.headers.update({"accesstoken": self.accesstoken})

    def post_measure_words(self, measureID, curr_status, userAnswer):
        url = "{}/userMeasure/{}/measureData".format(self.baseUrl, measureID)
        print(url)
        # ,"studyType":"VOC","sysQuestID":"100-0","userAnswer":"2"
        for c, u in zip(curr_status, userAnswer):
            if c == 0:
                data = {"elapsedSec":29,"stepType":0}
                data.update(u)
                response = requests.request("POST", url, headers=self.headers, json=data)
                if len(eval(response.text).get('data')) != 0:
                    return eval(response.text).get('data')
            else:
                pass


if __name__ == '__main__':
    cfg_info = NewConfig()
    devices = cfg_info.get_info('vivox6')
    c, h = cfg_info.get_info("vivox6")
    print(c)
    print(h)
    a = 'dad46a52-0542-4f39-a371-3b47e05af4b8'
    at = GetMeasureWords(c, h, a)
    s = at.get_measure_words(0)
