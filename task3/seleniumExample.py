# @Author  : adair_chan
# @Email   : adairchan.dream@gmail.com
# @Date    : 2019/4/10 上午11:35
# @IDE     : PyCharm
import time

from selenium import webdriver


class SeleniumTest:
    def __init__(self, email, password):
        self.email = email
        self.password = password

    def login_test(self):
        browser = webdriver.Chrome()
        browser.get("https://mail.163.com/")
        # 这里必须加睡眠等待时间，
        time.sleep(3)
        browser.switch_to.frame(0)

        email = browser.find_element_by_name('email')
        email.send_keys(self.email)
        password = browser.find_element_by_name('password')
        password.send_keys(self.password)
        time.sleep(5)
        print("put login message.... ")

        browser.find_element_by_id('dologin').click()
        time.sleep(3)
        print("login...")
        browser.close()


if __name__ == '__main__':
    test = SeleniumTest('test', 'test')
    test.login_test()




