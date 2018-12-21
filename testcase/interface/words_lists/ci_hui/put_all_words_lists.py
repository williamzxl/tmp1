import requests
import json
from utils.config import get_headers


class PutAllWordsListsDone(object):
    def __init__(self):
        self.headers = get_headers()
        self.url = self.headers.get('Host')
        self.http = self.headers.get('http')

    def put_all_words_lists_done(self, taskID, groupID):
        url = "https://{}/userVoc/{}/{}/vocStatus".format(self.url, taskID, groupID)
        # print(self.headers)
        response = requests.request("PUT", url, headers=self.headers)
        return response


if __name__ == '__main__':
    test = PutAllWordsListsDone()
    r = test.put_all_words_lists_done(34487, 2611)
    print(r)