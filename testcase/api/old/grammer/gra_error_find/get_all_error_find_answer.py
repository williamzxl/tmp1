import requests
import json


def get_all_gra_error_find_answer(list, taskID=1):
    url = "http://192.168.1.154:55262/sysGrammar/{}/errorFind".format(list)
    querystring = {"taskID": "{}".format(taskID)}
    headers = {
        'platform': "Android",
        'appversion': "1.0",
        'appkey': "Cet_E94A599B77DA",
        'app': "cee",
        'appsecret': "8548C4F6-96F1-4E37-ADD6-89BEF5478B9B",
        'accesstoken': "b9e93792-d6f9-4e5d-bd80-f00bead144e1",
        'host': "192.168.1.154:55262",
        'connection': "Keep-Alive",
        'accept-encoding': "gzip",
        'user-agent': "okhttp/3.7.0",
        'cache-control': "no-cache",
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    answer = response.text
    json_data = json.loads(answer)
    result = json_data.pop("data").get('questGuide')[0].get('subQuestGuide')
    word_answers = []
    for r in result:
        word_answers.append(r.get('questAnswer'))
    return word_answers


def right_answer_gra_error_find(answer):
    get_answer = answer[:]
    # right_answer = get_answer.pop(int(num)-1)
    for a in get_answer:
        if "去掉" in a[0].get('description'):
            wordIdx = a[0].get('wordIdx')
            word = a[0].get('description').split('去掉')[1]
            action = 'delete'
            print("Action:",action,wordIdx,word)
        if "改为" in a[0].get('description'):
            wordIdx = a[0].get('wordIdx')
            wordBefore = a[0].get('description').split('改为')[0]
            wordAfter = a[0].get('description').split('改为')[1]
            action = 'change'
            print("Action:", action, wordIdx, wordBefore, "to", wordAfter)
        if "之前加" in a[0].get('description'):
            wordIdx = a[0].get('wordIdx')
            wordBefore = a[0].get('description').split('之前加')[0]
            addedWord = a[0].get('description').split('之前加')[1]
            action = 'insert'
            print("Action:", action, wordIdx, wordBefore, "add", addedWord)


def wrong_answer_gra_error_find(answer):
    get_answer = answer[:]
    # right_answer = get_answer.pop(int(num)-1)
    for a in get_answer:
        if "去掉" in a[0].get('description'):
            wordIdx = int(a[0].get('wordIdx')) + 1
            word = a[0].get('description').split('去掉')[1]
            action = 'delete'
            print("Action:", action, wordIdx, word)
        if "改为" in a[0].get('description'):
            wordIdx = a[0].get('wordIdx')
            wordBefore = a[0].get('description').split('改为')[0]
            wordAfter = a[0].get('description').split('改为')[1] + 's'
            action = 'change'
            print("Action:", action, wordIdx, wordBefore, "to", wordAfter)
        if "之前加" in a[0].get('description'):
            wordIdx = a[0].get('wordIdx')
            wordBefore = a[0].get('description').split('之前加')[0]
            addedWord = a[0].get('description').split('之前加')[1] + 's'
            action = 'insert'
            print("Action:", action, wordIdx, wordBefore, "add", addedWord)

#
# def wrong_answer_gra_choice(answer, num):
#     get_answer = answer[:]
#     test = get_answer.pop(int(num)-1)
#     wrong_answer = []
#     for w in test:
#         if chr(ord(w.lower()) + 1).isalpha():
#             wrong_answer.append(chr(ord(w.lower()) + 1))
#         else:
#             wrong_answer.append(chr(ord(w.lower()) - 1))
#     return "".join(wrong_answer)

#
answer = get_all_gra_error_find_answer(list=1580, taskID=1)
print(answer)
# print(right_answer_gra_error_find(answer))
print(wrong_answer_gra_error_find(answer))

