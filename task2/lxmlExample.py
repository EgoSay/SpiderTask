# @Author  : adair_chan
# @Email   : adairchan.dream@gmail.com
# @Date    : 2019/4/8 下午2:06
# @IDE     : PyCharm
from lxml import etree

from common import getHtmlText


def get_data_with_xpath(req):
    html = etree.HTML(req)
    results = list()

    user_name = html.xpath('//div[@class="auth"]/a/text()')
    comment = html.xpath('//td[@class="postbody"]')

    for i in range(1, len(user_name)):
        """
        Xpath中text()，string()，data()的区别如下：
            text()仅仅返回所指元素的文本内容。
            string()函数会得到所指元素的所有节点文本内容，这些文本讲会被拼接成一个字符串。
            data()大多数时候，data()函数和string()函数通用，而且不建议经常使用data()函数，有数据表明，该函数会影响XPath的性能
        """
        result = "{},\t用户名:{}, 评论内容:{}\n".format(
            i, user_name[i].strip(), comment[i].xpath('string(.)').strip())
        print(result)
        results.append(result)

    return results


if __name__ == '__main__':
    url = 'http://www.dxy.cn/bbs/thread/626626#626626'
    req = getHtmlText.getHtmlText(url)
    with open("dxy2.txt", "w", encoding="utf-8") as f:
        for line in get_data_with_xpath(req):
            f.writelines(line)
