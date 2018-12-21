import os
import yaml
from utils.file_reader import YamlReader

'''
    List home_page dirs
'''
BASE_PATH = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]
CONFIG_PATH = os.path.join(BASE_PATH, 'config')
DATA_PATH = os.path.join(BASE_PATH, 'data')
APK_PATH = os.path.join(BASE_PATH, 'apk')
LOG_PATH = os.path.join(BASE_PATH, 'log')
REPORT_PATH = os.path.join(BASE_PATH, 'report')
TEST_PATH = os.path.join(BASE_PATH, 'test_case')
all_configs = CONFIG_PATH + r"\config.yml"
new_all_cfgs = CONFIG_PATH + r"\devices_cfg.yml"
# all_configs = CONFIG_PATH + r"/config.yml"
# new_all_cfgs = CONFIG_PATH + r"/devices_cfg.yml"


class Config(object):
    def __init__(self, config=all_configs):
        self.configs = YamlReader(config).data

    def get(self, element):
        for config in self.configs:
            for i in range(len(config)):
                if element in config[i]:
                    yield config[i].get(element)


class NewConfig(object):
    def __init__(self, config=new_all_cfgs):
        self.configs = YamlReader(config).data

    def get_all_devices_name(self):
        devices_names = []
        for d in self.configs:
            for d1 in d:
                devices_names.append(list(d1.keys()))
        return devices_names

    def get_info(self, devices_name='vivox6'):
        for d in self.configs:
            for d1 in d:
                try:
                    common = d1.get(devices_name).get("common")
                    headers = d1.get(devices_name).get("headers")
                    return common, headers
                except:
                    pass


cfg_info = NewConfig()


if __name__ == '__main__':
    # t = NewConfig()
    # devices = t.get_all_devices_name()
    # for d in devices:
    #     cinfo, cheader = t.get_info("".join(d))
    #     print(cinfo)
    #     print(cheader)
    # c, h = t.get_info("vivox6")
    # print(c)
    # print(h)
    c = Config()
    configs = c.get('mail_cfg')
    print(configs)
    config = [i for i in configs][0]
    print(config)