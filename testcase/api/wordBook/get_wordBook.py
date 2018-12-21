import requests
import json
import threading
# prep-appwb.langlib.com
host = "https://appwb.langlib.com"
# host = "https://prep-appwb.langlib.com"
# PUT https://prep-appwb.langlib.com/wordBooks/382126/updateFamiliarity HTTP/1.1
# PUT https://appwb.langlib.com/wordBooks/382049/updateFamiliarity HTTP/1.1
accesstoken = 'ce77f1be-2bfb-4405-90c5-5c1856168f6d'


headers = {
    'host': "appwb.langlib.com",
    'accept': "*/*",
    'appversion': "2017121201",
    'accept-encoding': "br, gzip, deflate",
    'accept-language': "zh-cn",
    'accesstoken': accesstoken,
    'content-type': "application/json",
    'content-length': "52",
    'user-agent': "LanglibCEE/10005005 CFNetwork/893.14.2 Darwin/17.3.0",
    'appkey': "Toefl_58E397E6C683",
    'connection': "keep-alive",
    'cookie': "lbsid=s%3AGOAslaFYKxeujEZ8PFVQM3Ne6waO_sB0.PB%2FUg51dzoWsr%2Fj879mDvQFi%2FoIrSuaAVgD1jAhIPJI",
    'cache-control': "no-cache",
    'postman-token': "5a8643d4-f090-a375-67f6-0c76cbeeb768"
}


def get_all_word_books(host, headers):
    url = "{}/wordBooks/findUserWordBooks".format(host)
    print(url)
    headers.update({'content-length': "0",})
    response = requests.request("GET", url, headers=headers)
    answer = response.text
    print(answer)
    json_data = json.loads(answer)
    return json_data.get("UserWordBookList")

def get_WordBook(all_books, WordBookName):
    for book in all_books:
        if WordBookName in list(book.values()):
            UserWordBookID = book.get("UserWordBookID")
            WordBookType = book.get("WordBookType")
            return UserWordBookID, WordBookType

def findAllTask(host, headers, UserWordBookID):
    url = "{}/wordBooks/{}/findTasks".format(host, UserWordBookID)
    response = requests.request("GET", url, headers=headers)
    answer = response.text
    json_data = json.loads(answer)
    # print(json_data.get("CurrentTask"))
    currentTask = []
    ct = json_data.get("CurrentTask")
    currentTask.append(str(ct.get("RoutineIdx")))
    all_new_task = []
    for unit in json_data.get("TaskInfos"):
        for task in unit:
            if task.get("R") == 0:
                all_new_task.append(task)
            # if task.get("C") == 0 and task.get("R") == 0:
            #     all_new_task.append(task)
            # if task.get("C") == 1:
            #     all_new_task.append(task)
            if task.get("R") != 0:
                task.update({'R': "00"})
                all_new_task.append(task)
    # print(len(all_new_task))
    # print(all_new_task)
    return all_new_task, currentTask

def get_words_info(host, headers, UserWordBookID, index):
    url = "{}/wordBooks/{}/findP1Words?unitIdx={}".format(host, UserWordBookID, index)
    print(url)
    try:
        headers.pop('Content-Length')
    except:
        pass
    # print(headers)
    response = requests.request("GET", url, headers=headers)
    answer = response.text
    # print(answer)
    json_data = json.loads(answer)
    # print(json_data)
    return json_data.get("WordInfos")

def put_words_to_3_star(host, headers, UserWordBookID, id):
    url = "{}/wordBooks/{}/updateFamiliarity".format(host, UserWordBookID)
    data = {"SysWordID": "{}".format(id), "Phase": 2, "OldFamiliarity": 1, "NewFamiliarity": 2}
    response = requests.request("PUT", url, headers=headers, json=data)
    print("*" * 80)
    print(response.text)
    print("*" * 80)
    # return response

def post_6_done(host, headers, UserWordBookID, index, RID):
    url = "{}/wordBooks/{}/markTaskItemComplete".format(host, UserWordBookID)
    data = {"UnitIdx":int("{}".format(index)),"RoutineIdx":int("{}".format(int(RID)))}
    headers.update({'Content-Length': '71'})
    print("*" * 50)
    print(headers)
    print(data)
    response = requests.request("POST", url, headers=headers, json=(data))
    try:
        headers.pop('Content-Length')
    except:
        pass
    print("Done", response, response.status_code)
    return response.status_code


all_books = get_all_word_books(host, headers)
# print(all_books)
# all_books = {'1':'高考英语 3500 词'}
UserWordBookID, WordBookType = get_WordBook(all_books, "高考 3500 词")
# print(UserWordBookID, WordBookType)
# import time
# time.sleep(120)
while True:
    all_new_task, current_task = findAllTask(host, headers, UserWordBookID)
    # print("all_new_task", all_new_task)
    # print("current_task", current_task)
    RID = "".join(current_task)
    Flag = 1
    while Flag:
        for new_task in all_new_task[:]:
            print("NewTask", new_task)
            index = new_task.get("U")
            if new_task.get("C") == 1:
                print("Begin to change to 3 stars", index)
                if new_task.get("R") == "00":
                    try:
                        status = post_6_done(host, headers, UserWordBookID, index, RID)
                        print("Status", status)
                        if status != 200:
                            Flag = 0
                    except:
                        pass
                try:
                    post_6_done(host, headers, UserWordBookID, index, RID)
                except:
                    pass
                ids = get_words_info(host, headers, UserWordBookID, index)
                for id in ids:
                    t = threading.Thread(target=put_words_to_3_star, args=(host, headers, UserWordBookID, id.get("Id")))
                    t.start()
                    t.join()
                # for id in ids:
                #     res = put_words_to_3_star(host, headers, UserWordBookID, id.get("Id"))
                #     print(res)
            # index = new_task.get("U")
            if new_task.get("C") == 0:
                print("Begin to change to 3 stars", index)
                if new_task.get("R") == "00":
                    try:
                        status = post_6_done(host, headers, UserWordBookID, index, RID)
                        print("Status" , status)
                        if status != 200:
                            Flag = 0
                    except:
                        pass
                else:
                    ids = get_words_info(host,headers, UserWordBookID, index)
                    print("IDS", ids)
                    for id in ids:
                        t = threading.Thread(target=put_words_to_3_star,
                                             args=(host, headers, UserWordBookID, id.get("Id")))
                        t.start()
                    # for id in ids:
                    #     res = put_words_to_3_star(host, headers, UserWordBookID, id.get("Id"))
                    try:
                        status = post_6_done(host, headers, UserWordBookID, index, RID)
                        if status != 200:
                            Flag = 0
                    except:
                        pass