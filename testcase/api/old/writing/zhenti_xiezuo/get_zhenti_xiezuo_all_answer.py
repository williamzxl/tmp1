import requests
import json
# from utils.config import get_headers


class GetAllZhentiXiezuoAnswers(object):
    def __init__(self):
        # self.headers = headers
        # self.url = self.headers.get('Host')
        self.pas = None

    def get_all_zhenti_xiezuo_answer(self, headers, groupID, taskID):
        host = headers.get("Host")
        url = "http://{}/sysWriting/{}/writing".format(host, str(groupID))
        querystring = {"groupID": "{}".format(groupID), "taskID": "{}".format(taskID)}
        response = requests.request("GET", url, headers=headers, params=querystring)
        answer = response.text
        # print(answer)
        json_data = json.loads(answer)
        result = (json_data.get('data').get('questGuide'))
        print(result)
        # print(i.get('letterHead'))
        print("*" *80)
        for i in result:
            # print("head",i.get('letterHead'), len(i.get('letterHead')))
            # print("foot",i.get('letterFoot') == "\n", len(i.get('letterFoot')))
            # if (i.get('letterHead')) != "\n" and ((i.get('letterFoot')) == '' or (i.get('letterFoot')) == '\n'):
            #     head = i.get('letterHead').strip("\n")
            #     foot = i.get('letterFoot').lstrip("\n").strip(" ")
            #     all_content = i.get('modelEssay')
            #     print("All_content", head)
            #     try:
            #         fina_content = all_content.split(head)
            #         print("fina_content", fina_content)
            #     except:
            #         fina_content = all_content.split(head)[0]
            #         print("fina_content", fina_content)
            #     return fina_content
            if (i.get('letterHead')) != " " or (i.get('letterFoot')) != ' ':
                head = i.get('letterHead').strip("\n")
                foot = i.get('letterFoot').strip("\n")
                all_heads = []
                all_foots = []
                with open("temp_head.txt", "w") as fp_head:
                    fp_head.write(head)
                with open("temp_foot.txt", "w") as fp_foot:
                    fp_foot.write(foot)
                with open("temp_head.txt", 'r') as fp2_head:
                    r = fp2_head.readlines()
                    for r1 in r:
                        all_heads.append(r1.strip("\n| "))
                with open("temp_foot.txt", 'r') as fp2_foot:
                    r = fp2_foot.readlines()
                    for r1 in r:
                        all_foots.append(r1.strip("\n| "))
                print("all_heads", all_heads)
                print("all_foots", all_foots)
                all_content = i.get('modelEssay')
                with open("temp.txt", "w") as fp:
                    fp.write(all_content)
                all_contents = []
                with open("temp.txt", 'r') as fp2:
                    r = fp2.readlines()
                    for r1 in r:
                        all_contents.append(r1.strip("\n| "))
                print("all_contents", all_contents)
                # head_len = len(all_heads)
                fina_result = []
                all_answers = []
                # times = 0
                # for k in all_heads:
                    # times = times + 1
                    # try:
                    #     fina = "".join(all_contents).split(k)[-1]
                    #     if times == head_len:
                    #         fina_result.append(fina)
                    # except:
                    #     pass
                if len(all_foots) > 0:
                    if "" in all_foots:
                        fina_result.append(all_contents[len(all_heads):(-(len(all_foots)-1))])
                    else:
                        fina_result.append(all_contents[len(all_heads):(-len(all_foots))])
                else:
                    fina_result.append(all_contents[len(all_heads):])
                print("Fina",fina_result)
                for ff in fina_result:
                    # fina_result.append("".join(ff))
                    all_answers.append("".join((ff)))
                    print("FF","".join(ff))
                return all_answers
            else:
                all_content = i.get('modelEssay')
                return all_content


    def zhenti_xiezuo_right_answer(self, answer):
        get_answer = answer[:]
        right_answer = "".join(get_answer)
        return right_answer

    def zhenti_xiezuo_wrong_answer(self, answer):
        get_answer = answer[:]
        wrong_answer = "".join(get_answer).upper()
        return wrong_answer


if __name__ == '__main__':
    test = GetAllZhentiXiezuoAnswers()
    word_answers = test.get_all_zhenti_xiezuo_answer(2412, 33911)
    # print(word_answers)
    r = test.zhenti_xiezuo_right_answer(word_answers)
    print("R",r)
    # w = test.zhenti_xiezuo_wrong_answer(word_answers)
    # print(w)