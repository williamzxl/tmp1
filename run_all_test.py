#! /usr/bin/python3
# coding=utf-8
import unittest
import os, time
from utils.config import REPORT_PATH, TEST_PATH, Config, DATA_PATH
from BeautifulReport import BeautifulReport
# >>> git clone https://github.com/TesterlifeRaymond/BeautifulReport
# >>> cp -R BeautifulReport to/python/site-packages/
from utils.config import NewConfig
from utils.mail import SendMail
print(REPORT_PATH)

def add_case(case_path=TEST_PATH,rule='test_*.py'):
    '''加载所有的测试用例'''
    print(case_path)
    discover = unittest.defaultTestLoader.discover(case_path,
                                                  pattern=rule,
                                                  top_level_dir=case_path)
    return discover


def run(test_suit):
    print(test_suit)
    result = BeautifulReport(test_suit)
    tm = time.strftime('%y-%m-%d_%H_%M_%S', time.localtime(time.time()))
    cfg_info = NewConfig()
    common, _ = cfg_info.get_info()
    result.report(filename=r'CEE_API_Test_Report_{}.html'.format(tm),
                  description='CEE API Test Report 测试报告',
                  log_path=REPORT_PATH)


if __name__ == "__main__":
    cfg_info = NewConfig()
    # file = os.listdir(REPORT_PATH)
    # if file:
    #     for f in file:
    #         os.remove(r'{}\{}'.format(REPORT_PATH,f))
    cases = add_case()
    run(cases)
    common, _ = cfg_info.get_info()
    uname = common.get('uname')
    data = os.listdir(DATA_PATH)
    with open(r'{}\uname_lists.log'.format(DATA_PATH), "a") as fp:
    # with open(r'{}/uname_lists.log'.format(DATA_PATH), "a") as fp:
        fp.writelines(uname + "\n")


