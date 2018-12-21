import requests

url = "https://appncee.langb.cn/userStudyCenter/serviceInfo"

querystring = {"serviceID":""}

headers = {
    'platform': "Android",
    'appkey': "CEE_AA8F55B916AB",
    'appversion': '10002001',
    'appsecret': "3DB5159C-EB1E-47FE-8584-47115EF5E443",
    'app': "cee",
    'accesstoken': "b39fb77c-4f6f-48cd-95c7-e010a2c5d7d7",
    'host': "appncee.langb.cn",
    'connection': "Keep-Alive",
    'accept-encoding': "gzip",
    'user-agent': "okhttp/3.11.0"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)