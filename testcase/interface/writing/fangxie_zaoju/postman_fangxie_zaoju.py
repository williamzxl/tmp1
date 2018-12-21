import json
import requests

url = "http://192.168.1.154:55262/sysWriting/1925/senImitation"

querystring = {"groupID":"1925","taskID":"22449"}

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
    'postman-token': "f678d7c4-599a-5947-ddfd-c415c781535d"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

answer = response.text
json_data = json.loads(answer)
result = json_data.pop("data").pop('questGuide')
all_answers = []
all_answers_choice = []
for q in result:
    all_questAnswer = q.get('subQuestGuide')
    all_answers.append([a.get('questAnswer') for a in all_questAnswer])
print(all_answers)
# print(all_answers_choice)