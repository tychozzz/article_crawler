import parsel
import re
from bs4 import BeautifulSoup
from article_crawler.article_crawler import ArticleCrawler


class JianshuCrawler(ArticleCrawler):
    def __init__(self, url, output_folder, tag="article", class_='_2rhmJa', id=''):
        super().__init__(url=url, output_folder=output_folder, tag=tag, class_=class_, id=id)

    def parse_detail(self, response):
        html = response.text
        selector = parsel.Selector(html)
        title = selector.xpath("//h1[@class='_1RuRku']/text()").get()
        soup = BeautifulSoup(html, 'lxml')
        content = soup.find(self.tag, class_=self.class_)
        html = self.html_str.format(article=content)
        self.write_content(html, title)

    def change_title(self, title):
        mode = re.compile(r'[\\\/\:\?\*\"\<\>\|\!]')
        new_title = re.sub(mode, '_', title)
        return str(new_title)

    def start(self):
        response = self.send_request(self.url)
        if response:
            self.parse_detail(response)
