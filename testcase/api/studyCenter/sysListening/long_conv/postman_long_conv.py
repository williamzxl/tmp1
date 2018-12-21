import requests

url = "http://192.168.1.154:55262/sysListening/1822/longConv"

querystring = {"taskID":"23148"}

headers = {
    'platform': "Android",
    'appkey': "Cet_E94A599B77DA",
    'appversion': "10000000",
    'appsecret': "8548C4F6-96F1-4E37-ADD6-89BEF5478B9B",
    'app': "cee",
    'accesstoken': "bccf868b-735b-445c-8723-1278cac84f7a",
    'host': "192.168.1.154:55262",
    'connection': "Keep-Alive",
    'accept-encoding': "gzip",
    'user-agent': "okhttp/3.10.0",
    'cache-control': "no-cache",
    'postman-token': "73281375-2230-e512-0d99-6f9514b0c6c4"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)