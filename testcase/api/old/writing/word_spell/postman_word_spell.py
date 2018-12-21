import requests
import json

url = "http://192.168.1.154:55262/sysWriting/2346/wordSpell"

querystring = {"groupID":"2346","taskID":"22448"}

headers = {
    'platform': "Android",
    'appkey': "Cet_E94A599B77DA",
    'appversion': "10000000",
    'appsecret': "8548C4F6-96F1-4E37-ADD6-89BEF5478B9B",
    'app': "cee",
    'accesstoken': "7333a58f-4e12-4167-b8a6-8cbb83033d42",
    'host': "192.168.1.154:55262",
    'connection': "Keep-Alive",
    'accept-encoding': "gzip",
    'user-agent': "okhttp/3.10.0",
    'cache-control': "no-cache",
    'postman-token': "0955f62b-059b-50ca-7ae3-08e5cf491ba1"
    }

response = requests.request("GET", url, headers=headers, params=querystring)
answer = response.text
print(response.text)
json_data = json.loads(answer)
result = json_data.pop("data").pop('questGuide')
all_answers = []
for a in result:
    answer = a.pop('questAnswer')
    position =  a.pop('questPosition')
    one_word_answer = []
    for i in position:
        one_word_answer.append(answer[i])
    all_answers.append("".join(one_word_answer))
print(all_answers)