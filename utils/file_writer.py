import yaml
import os
from xlrd import open_workbook
from ruamel import yaml as yaml_new
import ruamel.yaml


class YamlWriter(object):
    def __init__(self, yaml_file):
        if os.path.exists(yaml_file):
            self.yamlf = yaml_file
        else:
            raise FileNotFoundError("YAML FILE IS NOT EXISTS")
        self._data = None

    def write_data(self, new_account):
        if not self._data:
            with open(self.yamlf, 'r') as docs:
                try:
                    alldata = ruamel.yaml.safe_load(docs)
                except ruamel.yaml.YAMLError as exc:
                    print(exc)
            alldata[0].get('vivox6').get('common').update({'uname': '{}'.format(new_account)})

            with open(self.yamlf, 'w+',encoding='utf8') as outfile:
                ruamel.yaml.dump(alldata, outfile, default_flow_style=False, allow_unicode=True)
                return True


if __name__ == '__main__':
    '''Test read yaml file'''
    # pass
    # BASE_PATH = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]
    # config_path = os.path.join(BASE_PATH, 'config', 'config.yml')
    # test = YamlReader(config_path)
    # print(test.data)
    file = r"C:\Users\liuda\Desktop\CEE\API_test\CEE_api_test\config\config001.yml"
    y = YamlWriter(file)
    a = y.write_data("hh")
    print(a)