import requests
from utils.config import NewConfig


class GetMeasureListen(object):
    def __init__(self, common, headers, accesstoken):
        self.headers = headers
        self.baseUrl = common.get('baseUrl')
        self.accesstoken = accesstoken
        self.headers.update({"accesstoken": self.accesstoken})
        try:
            self.headers.pop("Content-Length")
        except:
            pass

    def get_measure_listen(self, sysID="232001"):
        url = "{}/sysMeasure/{}/measureListening".format(self.baseUrl, sysID)
        response = requests.request("GET", url, headers=self.headers)
        data = eval(response.text).get("data")
        message = eval(response.text).get("message")
        if message == "success":
            currStatus = data.get("currStatus")
            measureID = data.get('measureID')
            currStepIdx = data.get("currStepIdx")
            steps = data.get("steps")
            return currStatus, measureID, currStepIdx, steps
        else:
            pass
        # measureID = data.get('measureID')

    def get_all_right_answer(self, studyType, steps):
        all_user_answers = []
        for s in steps:
            if s.get("currStatus") == 0:
                curr_steps = s.get("subQuestGuide")
                for branch in curr_steps:
                    if branch.get("currStatus") == 0:
                        if len(branch.get("subQuestGuide")) != 0:
                            stepType = 1
                            answer_indexs = []
                            for step1 in branch.get("subQuestGuide"):
                                answers = step1.get("questChoices")
                                for answer in step1.get("questChoices"):
                                    if answer.get("choiceTag") == "1":
                                        answer_index = answers.index(answer) + 1
                                        answer_indexs.append(str(answer_index))
                            print("answer_indexs = []", answer_indexs)
                            userAnswer = {"stepType": stepType,"studyType": "{}".format(studyType), "sysQuestID": "{}".format(branch.get("id")),
                                      "userAnswer": "{}".format("".join(answer_indexs))}
                            all_user_answers.append(userAnswer)
                        if len(branch.get("subQuestGuide")) == 0:
                            stepType = 2
                            if branch.get("currStatus") == 0:
                                answers = branch.get("questChoices")
                                for answer in branch.get("questChoices"):
                                    if answer.get("choiceTag") == "1":
                                        answer_index = answers.index(answer) + 1
                                        userAnswer = {"stepType":stepType,"studyType": "{}".format(studyType), "sysQuestID": "{}".format(branch.get("id")),
                                                      "userAnswer": "{}".format(answer_index)}
                                        all_user_answers.append(userAnswer)
        return all_user_answers


if __name__ == '__main__':
    cfg_info = NewConfig()
    devices = cfg_info.get_info('vivox6')
    c, h = cfg_info.get_info("vivox6")
    a = '1b7d0916-95c6-49db-a6c6-9fd27e66d43a'
    at = GetMeasureListen(c, h, a)
    _,_,_,steps = at.get_measure_listen("232001")
    # print(steps)
    ss = at.get_all_right_answer("LIS", steps)
    print(ss)