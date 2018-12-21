import requests
import json


class PostExperience(object):
    def __init__(self, common, headers, accesstoken):
        self.headers = headers
        self.baseUrl = common.get('baseUrl')
        self.accesstoken = accesstoken
        self.headers.update({"accesstoken": self.accesstoken})

    def post_experience(self, p="P90"):
        # POST http://192.168.1.155:55262/services/P90/experience HTTP/1.1
        url = "{}/services/{}/experience".format(self.baseUrl, p)
        self.headers.update({'Content-Length': '0'})
        response = requests.request("POST", url, headers=self.headers)
        return json.loads(response.text)


if __name__ == '__main__':
    pass