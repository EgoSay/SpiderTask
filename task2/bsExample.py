# @Author  : adair_chan
# @Email   : adairchan.dream@gmail.com
# @Date    : 2019/4/8 上午9:32
# @IDE     : PyCharm

from bs4 import BeautifulSoup
from common import getHtmlText


def get_data(html):
    soup = BeautifulSoup(html, "lxml")
    results = list()
    datas = soup.find_all("tbody")
    for data in datas:
        try:
            user_name = data.find("div", class_="auth").get_text(strip=True)
            comment = data.find("td", class_="postbody").get_text(strip=True)
            result = "用户名:{}, 评论内容:{}\n".format(user_name, comment)
            print(result)
            results.append(result)
        except:
            pass
    return results


if __name__ == '__main__':
    url = 'http://www.dxy.cn/bbs/thread/626626#626626'
    html = getHtmlText.getHtmlText(url)
    with open("dxy.txt", "w", encoding="utf-8") as f:
        for line in get_data(html):
            f.writelines(line)

