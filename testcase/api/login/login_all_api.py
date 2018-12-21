from testcase.api.login.login_branch.get_userStudyCenter_step3 import GetUserStudyCenter
from utils.config import NewConfig


class LoginApi(GetUserStudyCenter):
    def __init__(self):
        super(GetUserStudyCenter, self).__init__()


if __name__ == '__main__':
    cfg_info = NewConfig()
    devices = cfg_info.get_info('vivox6')
    common, headers = cfg_info.get_info("vivox6")
    t = LoginApi()
    access_token = t.get_access_token(common, headers)
    print(access_token)
    result = t.check_uname(common, headers, access_token)
    print(result)
    sevicesID = t.get_user_study_center(common, headers, access_token)
    print(sevicesID)