# @Author  : adairchan
# @Email   : adairchan.dream@gmail.com
# @Date    : 2019/4/5 22:53
# @IDE     : PyCharm
import csv
import requests
from lxml import etree


movies_info = list()


# 利用xpath抓取
def get_movie_info_with_xpath(url):
    r = requests.get(url).text

    html = etree.HTML(r)

    for i in range(1, 26):
        root_path = '//*[@id="content"]/div/div[1]/ol/li[{}]'.format(i)

        rank = html.xpath(
            root_path + '/div/div[1]/em/text()')[0]
        names = html.xpath(
            root_path + '/div/div[2]/div[1]/a/span/text()')[0]
        director = html.xpath(
            root_path +
            '/div/div[2]/div[2]/p[1]/text()[1]')[0].strip().split(" ")[1]
        years = html.xpath(
            root_path + '/div/div[2]/div[2]/p[1]/text()[2]')[0].strip()[:4]
        scores = html.xpath(
            root_path + '/div/div[2]/div[2]/div/span[2]/text()')
        movie_info = "排名:{},影名:{},导演:{},年份:{},评分:{}\n".format(
            str(rank), str(names), str(director), str(years), scores[0])
        print(movie_info)
        global movies_info
        movies_info.append(movie_info)


# 利用正则抓取
def get_movie_info_with_regex(url):
    """

    :param url:
    :return:
    """


if __name__ == '__main__':

    for i in range(0, 250, 25):
        url = 'https://movie.douban.com/top250?start={}&filter='.format(i)
        # get_movie_info_with_regex(url)
        get_movie_info_with_xpath(url)

        # 写入到文本文件
        with open('movie_info.txt', 'w', encoding='utf-8', newline='\n') as text_file:
            text_file.writelines(movies_info)
