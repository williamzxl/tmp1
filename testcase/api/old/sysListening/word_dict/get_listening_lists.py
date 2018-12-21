# import requests
# from pprint import pprint
# url = "http://192.168.1.154:55262/users/practices/groups"
#
# querystring = {"grpType":"1"}
#
# headers = {
#     'host': "192.168.1.154:55262",
#     'content-type': "application/json",
#     'accept': "*/*",
#     'accept-encoding': "gzip, deflate",
#     'connection': "keep-alive",
#     'appkey': "Cet_E94A599B77DA",
#     'user-agent': "LBLearnCenter/1.0 (iPhone; iOS 11.0.3; Scale/3.00)",
#     'accesstoken': "6ab38189-a25b-4c83-926d-027c578b4aef",
#     'accept-language': "zh-Hans-CN;q=1",
#     'appversion': "1.0",
#     'cache-control': "no-cache",
#     'postman-token': "432158f0-e795-9186-5fe7-8ef0774666d4"
#     }
#
# response = requests.request("GET", url, headers=headers, params=querystring)
#
# pprint(response.text)


import requests

url = "http://appncee_dev.langb.cn/sysListening/1104/wordDic"

querystring = {"taskID":"16484"}

headers = {
    'platform': "Android",
    'appkey': "Cet_E94A599B77DA",
    'appversion': "10000000",
    'appsecret': "8548C4F6-96F1-4E37-ADD6-89BEF5478B9B",
    'app': "cee",
    'accesstoken': "a6c2ae17-95de-4f33-af0f-7e43a4ca9dc5",
    'host': "appncee_dev.langb.cn",
    'connection': "Keep-Alive",
    'accept-encoding': "gzip",
    'user-agent': "okhttp/3.10.0",
    'if-none-match': "W/\"1948-OofVxdzuY/5Pa6mFerEdtPDAw1M\"",
    'cache-control': "no-cache",
    'postman-token': "a1dc1822-9b4d-6418-56ac-b3681a578dce"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)