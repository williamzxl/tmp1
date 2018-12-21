import requests

url = "https://appncee.langlib.com/home"

headers = {
    'platform': "Android",
    'appkey': "CEE_AA8F55B916AB",
    'appversion': "10000005",
    'appsecret': "3DB5159C-EB1E-47FE-8584-47115EF5E443",
    'app': "cee",
    'accesstoken': "1adc0310-8c3a-41f6-aa38-1268b1e61500",
    'host': "appncee.langlib.com",
    'connection': "Keep-Alive",
    'accept-encoding': "gzip",
    'user-agent': "okhttp/3.11.0",
    'cache-control': "no-cache",
    'postman-token': "e5996c9d-a344-17fe-75bf-b37850424376"
    }

response = requests.request("GET", url, headers=headers)

print(response.text)