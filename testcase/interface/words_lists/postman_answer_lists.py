import requests

url = "http://appncee.langb.cn/userStudyCenter/P90/taskInfo"

querystring = {"taskID":""}

headers = {
    'platform': "Android",
    'appkey': "Cet_E94A599B77DA",
    'appversion': "10000000",
    'appsecret': "8548C4F6-96F1-4E37-ADD6-89BEF5478B9B",
    'app': "cee",
    'accesstoken': "1790d04b-3ab9-41da-a261-3910e31bc129",
    'host': "appncee.langb.cn",
    'connection': "Keep-Alive",
    'accept-encoding': "gzip",
    'user-agent': "okhttp/3.10.0",
    'cache-control': "no-cache",
    'postman-token': "06504454-7348-7c22-1ed2-55262584d517"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)