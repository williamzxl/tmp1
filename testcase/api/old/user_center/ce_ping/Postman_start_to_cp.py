import requests

url = "https://appncee.langlib.com/userMeasure/P120/measureInfo"

headers = {
    'platform': "Android",
    'appkey': "CEE_AA8F55B916AB",
    'appversion': "10000005",
    'appsecret': "3DB5159C-EB1E-47FE-8584-47115EF5E443",
    'app': "cee",
    'accesstoken': "828007cd-7234-4440-aebb-02ef5a08f4cc",
    'host': "appncee.langlib.com",
    'connection': "Keep-Alive",
    'accept-encoding': "gzip",
    'user-agent': "okhttp/3.11.0",
    'cache-control': "no-cache",
    'postman-token': "1793760f-335b-0648-770f-4e79435d5a55"
    }

response = requests.request("GET", url, headers=headers)

print(response.text)