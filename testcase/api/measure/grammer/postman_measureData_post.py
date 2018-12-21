import requests

url = "https://appncee.langlib.com/userMeasure/1699/measureData"

headers = {
    'platform': "Android",
    'appkey': "CEE_AA8F55B916AB",
    'appversion': "10000005",
    'appsecret': "3DB5159C-EB1E-47FE-8584-47115EF5E443",
    'app': "cee",
    'accesstoken': "1adc0310-8c3a-41f6-aa38-1268b1e61500",
    'content-type': "application/json; charset=utf-8",
    'content-length': "86",
    'host': "appncee.langlib.com",
    'connection': "Keep-Alive",
    'accept-encoding': "gzip",
    'user-agent': "okhttp/3.11.0",
    'cache-control': "no-cache",
    'postman-token': "920c66ed-9294-8a4e-0830-113fff92ced2"
    }

data = {"elapsedSec":187,"stepType":0,"studyType":"GRA","sysQuestID":"01-AdjAdv-MulChoice-001","userAnswer":"3"}
response = requests.request("POST", url, headers=headers, json=data)

print(response.text)