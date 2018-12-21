import requests

url = "https://proxy.langlib.com/users/getUserInfo"

headers = {
    'platform': "Android",
    'appkey': "CEE_AA8F55B916AB",
    'appversion': "10000005",
    'appsecret': "3DB5159C-EB1E-47FE-8584-47115EF5E443",
    'app': "cee",
    'accesstoken': "828007cd-7234-4440-aebb-02ef5a08f4cc",
    'host': "proxy.langlib.com",
    'connection': "Keep-Alive",
    'accept-encoding': "gzip",
    'user-agent': "okhttp/3.11.0",
    'cache-control': "no-cache",
    'postman-token': "1e1992ad-8811-4a47-94f8-afe94ab70795"
    }

response = requests.request("GET", url, headers=headers)

print(response.text)