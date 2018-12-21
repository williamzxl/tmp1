import requests

url = "http://192.168.1.154:55262/sysReading/2538/senCloze"

querystring = {"taskID":"23281"}

headers = {
    'platform': "Android",
    'appkey': "Cet_E94A599B77DA",
    'appversion': "10000000",
    'appsecret': "8548C4F6-96F1-4E37-ADD6-89BEF5478B9B",
    'app': "cee",
    'accesstoken': "a0c27990-57a4-4c8d-b02b-59621499cafc",
    'host': "192.168.1.154:55262",
    'connection': "Keep-Alive",
    'accept-encoding': "gzip",
    'user-agent': "okhttp/3.10.0",
    'if-none-match': "W/\"2577-6p9VNQzhQKkuHG+tffiOQ63RJm0\"",
    'cache-control': "no-cache",
    'postman-token': "9621d039-4dcc-2581-5bc2-aa5624849cf4"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)