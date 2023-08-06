import os.path

import requests
from bs4 import BeautifulSoup
import html2text
import random

html_str = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Document</title>
</head>
<body>
{article}
</body>
</html>
"""

USER_AGENT_LIST = [
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
    "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36"
]


class ArticleCrawler():
    def __init__(self, url, output_folder, tag, class_, id=''):
        self.url = url
        self.headers = {
            'user-agent': random.choice(USER_AGENT_LIST)
        }
        self.tag = tag
        self.class_ = class_
        self.id = id
        self.html_str = html_str
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)
            print(f"{output_folder} does not exist, automatically create...")
        self.output_folder = output_folder

    def send_request(self, url):
        response = requests.get(url=url, headers=self.headers)
        response.encoding = "utf-8"
        if response.status_code == 200:
            return response

    def parse_detail(self, response):
        html = response.text
        soup = BeautifulSoup(html, 'lxml')
        content = soup.find(self.tag, id=self.id, class_=self.class_)
        html = self.html_str.format(article=content)
        self.write_content(html, 'article')

    def write_content(self, content, name):
        if not os.path.exists(self.output_folder + '/HTML'):
            os.makedirs(self.output_folder + '/HTML')
        if not os.path.exists(self.output_folder + '/MD'):
            os.makedirs(self.output_folder + '/MD')
        name = self.change_title(name)
        html_path = os.path.join(self.output_folder, "HTML", name + ".html")
        md_path = os.path.join(self.output_folder, "MD", name + ".md")

        with open(html_path, 'w', encoding="utf-8") as f:
            f.write(content)
            print(f"create {name}.html in {self.output_folder} successfully")

        html_text = open(html_path, 'r', encoding='utf-8').read()
        markdown_text = html2text.html2text(html_text)
        with open(md_path, 'w', encoding='utf-8') as file:
            file.write(markdown_text)
            print(f"create {name}.md in {self.output_folder} successfully")

    def change_title(self, title):
        return title

    def start(self):
        response = self.send_request(self.url)
        if response:
            self.parse_detail(response)
