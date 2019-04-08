# @Author  : adair_chan
# @Email   : adairchan.dream@gmail.com
# @Date    : 2018/4/7 下午4:49
# @IDE     : PyCharm

import requests


def getHtmlText(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except BaseException:
        return "Something Wrong!"
