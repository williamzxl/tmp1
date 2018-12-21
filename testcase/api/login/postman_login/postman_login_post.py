import requests
import json

url = "https://proxy.langlib.com/accounts/loginByAccount"

headers = {
    'platform': "Android",
    'appkey': "CEE_AA8F55B916AB",
    'appversion': "10000005",
    'appsecret': "3DB5159C-EB1E-47FE-8584-47115EF5E443",
    'app': "cee",
    'content-length': "55",
    'host': "proxy.langlib.com",
    'accept-encoding': "gzip",
    'Connection': 'Keep-Alive',
    'user-agent': "okhttp/3.11.0",
    'content-type': "application/json",
    'cache-control': "no-cache",
    }
body = {"UserCredential": "test_pay@t.com", "Password": "111111"}
response = requests.request("POST", url, headers=headers, json=body)
content = (json.loads(response.text))
print(content.get("AccessToken"))
print(type(content))