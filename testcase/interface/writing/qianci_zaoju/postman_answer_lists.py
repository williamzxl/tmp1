import requests

url = "http://192.168.1.154:55262/sysWriting/1949/construction"

querystring = {"groupID":"1949","taskID":"24734"}

headers = {
    'platform': "Android",
    'appkey': "Cet_E94A599B77DA",
    'appversion': "10000000",
    'appsecret': "8548C4F6-96F1-4E37-ADD6-89BEF5478B9B",
    'app': "cee",
    'accesstoken': "fe780ffc-70c7-4e16-881e-f46af8b7d28f",
    'host': "192.168.1.154:55262",
    'connection': "Keep-Alive",
    'accept-encoding': "gzip",
    'user-agent': "okhttp/3.10.0",
    'cache-control': "no-cache",
    'postman-token': "1eb852e7-61b7-19f7-619a-e954b110d270"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)