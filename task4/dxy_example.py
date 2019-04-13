# @Author  : adair_chan
# @Email   : adairchan.dream@gmail.com
# @Date    : 2019/4/13 下午7:53
# @IDE     : PyCharm
from selenium import webdriver
import time
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from lxml import etree
import requests

# 打开浏览器
browser = webdriver.Chrome()
# 访问地址
url = "http://www.dxy.cn/bbs/thread/626626#626626"
browser.get(url)

# 登陆代码


def login(browser):
    try:
        # 通过xpath定位到登录按钮，并点击
        browser.find_element_by_xpath(
            '//*[@id="headerwarp"]/div/div[1]/div/a[1]').click()
        # 点击返回电脑登录
        browser.find_element_by_xpath(
            '/html/body/div[2]/div[2]/div[1]/a[2]').click()
        # 找到账号的输入框
        elem = browser.find_element_by_name('username')
        # 清空输入框
        elem.clear()
        # 输入账号
        elem.send_keys("账号")
        # 找到密码的输入框
        elem = browser.find_element_by_name('password')
        # 清空输入框
        elem.clear()
        # s输入密码
        elem.send_keys("密码")

        print('开始登录：')
        # 点击登录按钮
        browser.find_element_by_xpath(
            '//*[@id="user"]/div[1]/div[3]/button').click()

    except TimeoutException:
        print("Time out")
    except NoSuchElementException:
        print("No Element")

# 开始爬取信息


def get_information(browser):
    print("登录成功")
    time.sleep(10)
    print("开始获取信息")
    # 利用xpath获取丁香园数据
    data = requests.get(url).text  # 以文本形式打印网页源码
    s = etree.HTML(data)  # 解析HTML文档

    for i in range(1, 5):  # rang(1,28):1 2 3 4...27,一共27楼
        try:  # 帖子内容这里的第一个帖子的div有点不一样，程序中采用分支处理。
            name = s.xpath(
                '//*[@id="post_{}"]/table/tbody/tr/td[1]/div[2]/a/text()'.format(i))  # 格式化信息
            info = s.xpath(
                '//*[@id="post_{}"]/table/tbody/tr/td[2]/div[2]/div[1]/table/tbody/tr/td/text()'.format(i))
            info1 = info[0].replace(
                " ", "").replace(
                "\n", "")  # 数据清洗：去除空格和换行符\n
            print(name[0])  # 打印第一个元素
            print(info1)
        except BaseException:
            name = s.xpath(
                '//*[@id="post_{}"]/table/tbody/tr/td[1]/div[2]/a/text()'.format(i))
            info = s.xpath(
                '//*[@id="post_{}"]/table/tbody/tr/td[2]/div[2]/div[2]/table/tbody/tr/td/text()'.format(i))
            info1 = info[0].replace(
                " ", "").replace(
                "\n", "")  # 数据清洗：去除空格和换行符\n
            print(name[0])  # 打印第一个元素
            print(info1)

# 主函数


def main():
    login(browser)  # 登录函数
    get_information(browser)  # 获取标题与链接
    time.sleep(1)  # 休眠


# 函数入口调用
if __name__ == '__main__':
    main()

    input("按任意键退出-> ")
    browser.quit()
