# @Author  : adair_chan
# @Email   : adairchan.dream@gmail.com
# @Date    : 2019/4/10 上午11:36
# @IDE     : PyCharm
import os
import random
from time import sleep

from lxml import etree

from common.getHtmlText import getHtmlText
from task3.ip_proxy.randomAgent import USER_AGENTS_LIST

def ip_proxy():
    # 根据不同的代理种类进入不同的链接页面爬取IP
    types = {'国内高匿代理': 'nn', '国内透明代理': 'nt', 'https代理': 'wn', 'http代理': 'wt', 'socks代理': 'qq'}
    base_url = "https://www.xicidaili.com/"
    for k, v in types.items():
        path = "{}/data/{}.txt".format(os.getcwd(), k)
        file = open(path, 'w+', encoding='utf-8')
        sleep(1)
        url = base_url + v + '/'
        ip = '163.204.242.209:9999'
        # 有很多页，这里我只爬取一部分
        for i in range(1, 2):
            page_url = url + str(i) + '/'
            # 随机设置请求头
            hd = {"User-agent": random.choice(USER_AGENTS_LIST)}
            text = getHtmlText(page_url, hd, proxies={'http': ip})
            html = etree.HTML(text)
            # ip_list = html.xpath('//*[ @id = "ip_list"]/tbody/')
            proxy_list = html.xpath('//tr[@class="odd"]')
            for li in proxy_list:
                # // *[ @ id = "ip_list"] / tbody / tr[2] / td[2]
                # // *[ @ id = "ip_list"] / tbody / tr[17] / td[2]
                # // *[ @ id = "ip_list"] / tbody / tr[17] / td[3]
                # // *[ @ id = "ip_list"] / tbody / tr[101] / td[2]
                ip = li.xpath('td/text()')[0]
                port = li.xpath('td/text()')[1]
                address = li.xpath('td/a/text()')
                # print("ip:{}, 端口:{}, 服务器地址:{}".format(ip, port, address))
                # file.write("ip:{}, 端口:{}, 服务器地址:{}\n".format(ip, port, address))
                file.write("{}:{}\n".format(ip, port))
        file.close()


if __name__ == '__main__':
    ip_proxy()

