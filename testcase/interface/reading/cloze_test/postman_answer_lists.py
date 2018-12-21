import requests

url = "http://192.168.1.154:55262/sysReading/2511/clozeTest"

querystring = {"taskID":"24761"}

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
    'postman-token': "8d906ad0-02db-b96e-1fde-7f873d4e7e45"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)