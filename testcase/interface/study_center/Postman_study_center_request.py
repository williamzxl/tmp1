import requests

url = "http://192.168.1.154:55262/userStudyCenter/serviceInfo"

querystring = {"serviceID":""}

headers = {
    'platform': "Android",
    'appkey': "Cet_E94A599B77DA",
    'appversion': "10000000",
    'appsecret': "8548C4F6-96F1-4E37-ADD6-89BEF5478B9B",
    'accesstoken': "26c0bcf4-ebcf-4c9c-ac92-a00bf7409dd8",
    'host': "192.168.1.154:55262",
    'connection': "Keep-Alive",
    'accept-encoding': "gzip",
    'user-agent': "okhttp/3.10.0",
    'cache-control': "no-cache",
    'postman-token': "ec901bbc-795b-cfe8-37cf-c4f4c3b477f7"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)