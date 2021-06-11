import random
import re
import time
from urllib import parse

import pangu
import requests
from loguru import logger
from pyquery import PyQuery
from urllib3.exceptions import InsecureRequestWarning

from task3.ip_proxy.randomAgent import USER_AGENTS_LIST

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


class ZsxqSpider(object):
    def __init__(self):
        self.group_id = "815118881285512"
        # self.cookies = {
        #     "UM_distinctid": "********",
        #     "abtest_env": "product",
        #     "zsxq_access_token": "0C1B2F4E-D595-8A4C-DF61-4FB5EDB49FA0_178B61428B09DA67",
        #     "sensorsdata2015jssdkcross": "********",
        # }

        self.headers = {
            "User-agent": random.choice(USER_AGENTS_LIST),
            "Accept": "application/json, text/plain, */*",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
            "cookie": "abtest_env=product; zsxq_access_token=0C1B2F4E-D595-8A4C-DF61-4FB5EDB49FA0_178B61428B09DA67",
            "origin": "https://wx.zsxq.com"
        }
        self.base_url = f"https://api.zsxq.com/v2/topics/{self.group_id}/solutions"
        self.end_time = "0"
        self.latest_time = None
        self.params = {
            "scope": "all",
            "direction": "20",
            "end_time": self.end_time,
        }
        self.data = dict()
        self.md_list = []
        self.count = 0

    def crawler(self):
        self.params["end_time"] = self.end_time
        response = requests.get(
            url=self.base_url,
            headers=self.headers,
            verify=False,
            params=self.params
        )
        self.data = response.json()
        if self.data.get("succeeded"):
            return True
        else:
            print(f"Crawler Group: {self.group_id} error!")
            return False

    def parse_topics(self):
        solutions = self.data.get("resp_data", {}).get("solutions", [])
        if solutions:
            self.end_time = solutions[-1].get("create_time").repalce(":", "%3A").replace("+", "%2B")
        if self.end_time != self.latest_time:
            self.latest_time = self.end_time
        else:
            print(f"Crawler Group: {self.group_id} finished!")
            return False
        self.count += len(solutions)
        for solution in solutions:
            md = []
            content = solution.get("solution", {}).get("text")
            md.append(self.parse_header(solution))
            md += self.parse_html(content)
            md.append(self.parse_comment(solution))
            md_text = "\n".join(md)
            self.md_list.append(md_text)
        print(f"Crawler Group: {self.group_id} {self.count} count!")
        return True

    @staticmethod
    def parse_html(content):
        content = content.replace("\n", "<br>")
        result = re.findall(r"<e [^>]*>", content)
        if result:
            for i in result:
                html = PyQuery(i)
                if html.attr("type") == "web":
                    template = "[%s](%s)" % (parse.unquote(html.attr("title")), parse.unquote(html.attr("href")))
                elif html.attr("type") == "hashtag":
                    template = " `%s` " % parse.unquote(html.attr("title"))
                elif html.attr("type") == "mention":
                    template = parse.unquote(html.attr("title"))
                else:
                    template = i
                content = content.strip().replace(i, template)
        else:
            content = pangu.spacing_text(content)
        return content

    @staticmethod
    def parse_header(topic):
        data_time = topic["create_time"]
        group = topic.get("group", {}).get("name")
        return f"# {group} - {data_time.split('T')[0]}"

    def parse_comment(self, topic):
        comments = [
            comment.get("owner").get("name") + ": " + self.parse_html(comment.get("text", ""))
            for comment in topic.get("show_comments", [])
        ]
        comment_text = "```\n" + "\n".join(comments) + "\n```" if comments else ""
        return comment_text

    def run(self):
        while True:
            time.sleep(1)
            if not self.crawler():
                break
            if not self.parse_topics():
                break
        text = "\n".join(self.md_list[::-1])
        logger.info(f"Writing into {self.group_id}.md")
        with open(f"data/{self.group_id}.md", "w") as f:
            f.write(text)
        logger.info(f"Crawler {self.group_id} Finished, Count: {self.count}")


if __name__ == "__main__":
    zsxq = ZsxqSpider()
    zsxq.run()