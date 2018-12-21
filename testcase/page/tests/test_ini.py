import configparser

cfg = configparser.ConfigParser()
cfg.read_file(open('cfg.ini'))
d = cfg.get('vivox6','d')
print(d)
h = cfg.get('vivox6', 'h')
print(h)