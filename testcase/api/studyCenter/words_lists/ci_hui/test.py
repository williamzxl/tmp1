import requests

url = "https://adm-opa.langb.cn/userLabel/labelManagement/ajax/userLabelChannelLabelsFindAll"

headers = {

    'content-type': "application/json;charset=utf-8",
    'cookie': "__root_domain_v=.langb.cn; _qddaz=QD.pktt7g.zdvf2m.jj3ociby; ckname=dlone; ckpwd=8F5F3FB2BD07AFBEB45680FEAE728624; lbsid=s%3AYVpqDf07dye0SZdoqZ-PiF7URksZqn63.ioHQf6A1yjixBmtuPfaLEb5pwrJ8j2pEkQD7swN8nus; userCredential=dlone",

    }

response = requests.request("GET", url, headers=headers)

print(response.text)