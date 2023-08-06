import time
import requests


def BaiduTime():
    response = requests.get('http://www.baidu.com')
    return time.localtime(time.mktime(time.strptime(response.headers['date'][5:25], "%d %b %Y %H:%M:%S"))+ 8 * 3600)
