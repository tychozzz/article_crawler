# Article Crawler

[![PyPI Latest Release](https://img.shields.io/pypi/v/article-crawler.svg)](https://pypi.org/project/article-crawler/)
[![PyPI Downloads](https://img.shields.io/pypi/dm/article-crawler?label=PyPI%20downloads)](https://pypi.org/project/article-crawler/)
[![](https://img.shields.io/github/v/release/ltyzzzxxx/article_crawler?display_name=tag)](https://github.com/ltyzzzxxx/article_crawler/releases/tag/v0.0.1)
[![](https://img.shields.io/github/stars/ltyzzzxxx/article_crawler)](https://github.com/ltyzzzxxx/article_crawler)
[![](https://img.shields.io/github/forks/ltyzzzxxx/article_crawler)](https://github.com/ltyzzzxxx/article_crawler)
[![](https://img.shields.io/github/issues/ltyzzzxxx/article_crawler)](https://github.com/ltyzzzxxx/article_crawler/issues)
[![](https://img.shields.io/badge/license-MIT%20-yellow.svg)](https://github.com/ltyzzzxxx/article_crawler/issues)

[English Doc](./README_EN.md) | [中文文档](./README_CN.md)

## ✨ 简介

Article Crawler 是一个用于从指定网站中爬取文章并以 Markdown 格式存储于本地的 Python 包。

## 🚀 快速开始

1. 通过 `pip` 安装包

    ```python
    pip install article-crawler
    ```
2. 使用方式

    命令: `python3 -m article_crawler -u [url] -t [type] -o [output_folder] -c [class_] -i [id]`

    ```
    Options:
      --version             show program's version number and exit
      -h, --help            show this help message and exit
      -u URL, --url=URL     crawled url (required)
      -t TYPE, --type=TYPE  crawled article type [csdn] | [juejin] | [zhihu] | [jianshu]
      -o OUTPUT_FOLDER, --output_folder=OUTPUT_FOLDER
                            output html / markdown / pdf folder (required)
      -w WEBSITE_TAG, --website_tag=WEBSITE_TAG
                            position of the article content in HTML (not required if 'type' is specified)
      -c CLASS_, --class=CLASS_
                            position of the article content in HTML (not required if 'type' is specified)
      -i ID, --id=ID        position of the article content in HTML (not required if 'type' is specified)
    ```
    - type: 具体的网站类型，当前支持：CSDN、知乎、掘金、简书
    - website_tag / class_ / id:
   
      举个🌰： `<div id="article_content" class="article_content clearfix"></div>`
   
      - 在这里，对应的 `tag` 为 `div`，`class_` 为 `article_content clearfix`，`id` 为 `article_content`。
      
      > 1. 当 `website_tag / class_ / id` 被指定时，无需指定 `type`，反之亦然
      > 2. 通过使用网页控制台，得到对应的文章位置
      > 3. `website_tag / class_ / id` 用于定位文章内容在 HTML 中的位置。可能只需要用到其中的一个或两个而不是所有。

## 开源协议

MIT License see https://opensource.org/license/mit/
       
