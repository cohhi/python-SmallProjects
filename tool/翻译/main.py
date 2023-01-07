import hashlib
import random
import time

import content as content
import requests
import sign as sign
from urllib3.util import url


def get_data():
    r = str(round(time.time() * 1000))
    salt = r + str(random.randint(0, 9))
    content = input("请输入:")
    data = "fanyideskweb" + content + salt + "Tbh5E8=q6U3EXe+&L[4c@"
    sign = hashlib.md5()
    sign.update(data.encode("utf-8"))
    sign = sign.hexdigest()
    # print(len(sign))
    # print(sign)
    return content, salt, sign


def send_request(content, salt, sign):
    url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'

    headers = {
        'Cookie': 'OUTFOX_SEARCH_USER_ID=-1927650476@223.97.13.65;',
        'Host': 'fanyi.youdao.com',
        'Origin': 'http://fanyi.youdao.com',
        'Referer': 'http://fanyi.youdao.com/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.146 Safari/537.36',
    }
    data = {
        'i': str(content),
        'from': 'AUTO',
        'to': 'AUTO',
        'smartresult': 'dict',
        'client': 'fanyideskweb',
        'salt': str(salt),
        'sign': str(sign),
        # 'lts': '1612879546052',
        # 'bv': '6a1ac4a5cc37a3de2c535a36eda9e149',
        # 'doctype': 'json',
        'version': '2.1',
        'keyfrom': 'fanyi.web',
        'action': 'FY_BY_REALTlME',
    }

    res = requests.post(url=url, headers=headers, data=data).json()
    print('翻译接口返回:', res['translateResult'][0][0]['tgt'])


state=True
print('作者:steam-404 for Github(建)')
print('这是一个自然语言服务翻译的免费Application')
print('V 2.4 测试版')
print('支持 中文与英语。\n输入中文翻译为英语,输入英文翻译为中文\n单词不要超过500个字符')
while state:
    if __name__ == '__main__':
        content, salt, sign = get_data()
        send_request(content, salt, sign)
        exit=str(input("是否退出?[y/n]"))
        if(exit=='y'):
            print(
                "拜拜,么么哒!!!"
            )
            state=False