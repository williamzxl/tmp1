import requests
import json


class PostOrdersSettlement(object):
    def __init__(self, common, headers, accesstoken):
        self.headers = headers
        self.baseUrl = common.get('baseUrl')
        self.accesstoken = accesstoken
        self.headers.update({"accesstoken": self.accesstoken})

    def post_orders_settlement(self, data):
        # http://192.168.1.155:55262/orders/settlement HTTP/1.1
        url = "{}/orders/settlement".format(self.baseUrl)
        self.headers.update({'Content-Length': '100'})
        response = requests.request("POST", url, headers=self.headers, json=data)
        datas = json.loads(response.text).get('data')
        return datas


if __name__ == '__main__':
    pass