# @Author  : codeAC
# @Email   : adairchan.dream@gmail.com
# @Date    : 2018/12/18 16:53
# @IDE     : PyCharm
import requests


def get_html(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = 'utf -8'
        return r.text
    except BaseException:
        return "Something Wrong!"


if __name__ == '__main__':
    url = 'http://www.baidu.com'
    print(get_html(url))
