# coding=utf-8

import sys
import json
import base64
import cv2
import os
import time
import re


# 保证兼容python2以及python3
IS_PY3 = sys.version_info.major == 3
if IS_PY3:
    from urllib.request import urlopen
    from urllib.request import Request
    from urllib.error import URLError
    from urllib.parse import urlencode
    from urllib.parse import quote_plus
else:
    import urllib2
    from urllib import quote_plus
    from urllib2 import urlopen
    from urllib2 import Request
    from urllib2 import URLError
    from urllib import urlencode

# 防止https证书校验不正确
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

API_KEY = '5mmEwvMKCAlL4s9fPxWIxsQi'

SECRET_KEY = 'TVqI6dtb5GV0j1O7CKhOMFBhvSUpa7hh'


OCR_URL = "https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic"


"""  TOKEN start """
TOKEN_URL = 'https://aip.baidubce.com/oauth/2.0/token'


"""
    获取token
"""
def fetch_token():
    params = {'grant_type': 'client_credentials',
              'client_id': API_KEY,
              'client_secret': SECRET_KEY}
    post_data = urlencode(params)
    if (IS_PY3):
        post_data = post_data.encode('utf-8')
    req = Request(TOKEN_URL, post_data)
    try:
        f = urlopen(req, timeout=5)
        result_str = f.read()
    except URLError as err:
        print(err)
    if (IS_PY3):
        result_str = result_str.decode()


    result = json.loads(result_str)

    if ('access_token' in result.keys() and 'scope' in result.keys()):
        if not 'brain_all_scope' in result['scope'].split(' '):
            print ('please ensure has check the  ability')
            exit()
        return result['access_token']
    else:
        print ('please overwrite the correct API_KEY and SECRET_KEY')
        exit()

"""
    读取文件
"""
def read_file(image_path):
    f = None
    try:
        f = open(image_path, 'rb')
        return f.read()
    except:
        print('read image file fail')
        return None
    finally:
        if f:
            f.close()


"""
    调用远程服务
"""
def request(url, data):
    req = Request(url, data.encode('utf-8'))
    has_error = False
    try:
        f = urlopen(req)
        result_str = f.read()
        if (IS_PY3):
            result_str = result_str.decode()
        return result_str
    except  URLError as err:
        print(err)

def getImg(img_path):
    img = cv2.imread(img_path)
    button_color = [122, 182, 238]
    margin_color = [241, 241, 241]

    button_list = []
    i = 400
    while i < 1920:
        # 找按钮
        if (img[i][540] == button_color).all(): # and (img[i + 5][540] == button_color).any() and (img[i + 10][540] == button_color).any():
            i += 10
            button_list.append(i)

            # 找白框
            while i < 1920:
                if (img[i][540] == margin_color).all():
                    break
                i += 1
        i += 1
    print(button_list)
    return button_list

target_num = 847
if __name__ == '__main__':

    # 获取access token
    token = fetch_token()

    # 拼接通用文字识别高精度url
    image_url = OCR_URL + "?access_token=" + token
    next_qu = "input tap 900 1900"
    index = 0
    while target_num >= 0:
        time.sleep(0.5)
        # 获取图片
        os.system('adb shell screencap -p /sdcard/capture.png')
        filename = 'img_' + str(index) + '.png'
        os.system('adb pull /sdcard/capture.png imgs/'+ filename)
        index += 1

        # 读取图片解析
        file_content = read_file('imgs/' + filename)
        # 调用文字识别服务
        result = request(image_url, urlencode({'image': base64.b64encode(file_content)}))
        result_json = json.loads(result)
        # print(result_json)
        text = ""
        for words_result in result_json["words_result"]:
            text = text + words_result["words"]

        # 解析文字内容
        if "开始挑战" in text:
            os.system('adb shell input tap 540 1400')
            continue

        if "获取积分" in text:
            temp = re.findall(r"获取积分:\d+",text)
            temp = re.findall(r"\d+",temp[0])
            target_num -= int(temp[0])
            os.system('adb shell input tap 540 1300')
            print(target_num)
            continue

        tap_list = getImg('imgs/' + filename)
        if len(tap_list) == 0:
            continue

        # 单选选A
        if "单选" in text:
            cmd = "input tap 540 " + str(tap_list[0]) + "; " + next_qu
            os.system('adb shell "' + cmd + '"')
            continue

        if "多选" in text:
            cmd = ""
            for tap_pos in tap_list:
                cmd += 'input tap 540 ' + str(tap_pos) + "; "
            cmd += 'input tap 900 1900'
            os.system('adb shell "' + cmd + '"')
            continue
