import requests
import json
from itertools import chain
from utils.config import get_headers


class GetAllSectionTrainAnswers(object):
    def __init__(self):
        self.headers = get_headers()
        self.url = self.headers.get('Host')


    def get_all_section_train_answers(self, groupID, taskID):
        url = "http://{}/sysReading/{}/sectionTrain".format(self.url, groupID)
        querystring = {"groupID": "{}".format(groupID), "taskID": "{}".format(taskID)}

        response = requests.request("GET", url, headers=self.headers, params=querystring)
        answer = response.text
        json_data = json.loads(answer)
        result = json_data.pop("data").pop('questGuide')
        all_answers = []
        for q in result:
            steps = (q.get('steps'))
            for step in steps:
                answers = step.get('subQuestGuide')
                all_answers.append(answers)
        #     all_questAnswer = q.get('subQuestGuide')
        #     all_answers.append(all_questAnswer)
        # print(all_answers)
            # if len(all_questAnswer) != 0:
            #     all_answers.append([a.get('questAnswer') for a in all_questAnswer])
            #     all_answers_choice.append([a.get('questChoices') for a in all_questAnswer])
        return all_answers

    def sen_train_right_answer(self, answers):
        step2_answers = []
        step3_answers = []
        for step2 in answers[1]:
            step2_answers.append(step2.get('questAnswer'))
        for step3 in answers[2]:
            for s3 in step3.get('subQuestGuide'):
                if len(s3.get('questTranslation')) == 0:
                    for choice in s3.get('questChoices'):
                        if s3.get('questAnswer') == choice.get('choiceTag'):
                            step3_answers.append(choice.get('choiceCN'))
                else:
                    if s3.get('questAnswer'):
                        step3_answers.append(s3.get('questAnswer'))
                    else:
                        step3_answers.append(0)
        return step2_answers[0], step3_answers
        # choice_EN = answers[sen_num-1][ques_num - 1]
        # print("Choice_EN:", choice_EN)
        # answers_choice = list(chain(*answers_choice))
        # if choice_EN:
        #     if choice_EN.isupper():
        #         for cn in list(chain(*answers_choice)):
        #             if choice_EN == cn.get('choiceTag'):
        #                 choice_CN = cn.get('choiceCN')
        #                 if choice_CN:
        #                     return choice_CN, choice_EN
        #     else:
        #         return choice_EN, None
        # else:
        #     return 0, None

    def sen_train_wrong_answer(self, answers):
        step2_wrong_answers = []
        step3_wrong_answers = []
        for step2 in answers[1]:
            step2_wrong_answers.append("Wrong" + step2.get('questAnswer'))
        for step3 in answers[2]:
            for s3 in step3.get('subQuestGuide'):
                if len(s3.get('questTranslation')) == 0:
                    for j in s3.get('questChoices'):
                        if s3.get('questAnswer') != j.get('choiceTag'):
                            step3_wrong_answers.append(j.get('choiceCN'))
                            break
                else:
                    if s3.get('questAnswer'):
                        step3_wrong_answers.append("Wrong" + s3.get('questAnswer'))
                    else:
                        step3_wrong_answers.append(0)
        return step2_wrong_answers[0], step3_wrong_answers


# test = GetAllSectionTrainAnswers()
# all_answers = test.get_all_section_train_answers(2474, 22450)
# print(all_answers)
# w1, w2 = test.sen_train_wrong_answer(all_answers, 1)
# r1, r2 = test.sen_train_right_answer(all_answers)
# print(r1)
# print(r2[1])
# print(w1)
# print(w2)
# r = test.sen_train_right_answer()