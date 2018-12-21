import requests

url = "http://192.168.1.154:55262/sysReading/2474/sectionTrain"

querystring = {"groupID":"2474","taskID":"22450"}

headers = {
    'platform': "Android",
    'appkey': "Cet_E94A599B77DA",
    'appversion': "10000000",
    'appsecret': "8548C4F6-96F1-4E37-ADD6-89BEF5478B9B",
    'app': "cee",
    'accesstoken': "4deb545e-d033-4f0a-9f2c-420fee24d577",
    'host': "192.168.1.154:55262",
    'connection': "Keep-Alive",
    'accept-encoding': "gzip",
    'user-agent': "okhttp/3.10.0",
    'cache-control': "no-cache",
    'postman-token': "d26d6f3a-090a-d93c-c293-52726df3d16e"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)