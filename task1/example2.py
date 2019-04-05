# @Author  : adairchan
# @Email   : adairchan.dream@gmail.com
# @Date    : 2019/4/5 22:38
# @IDE     : PyCharm

import requests

hd = {'User-agent': '123'}
r = requests.get('http://www.baidu.com', headers=hd)
print("返回状态码为:{}".format(r.status_code))
print("打印请求头:{}".format(r.request.headers))