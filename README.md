# Article Crawler

[![PyPI Latest Release](https://img.shields.io/pypi/v/article-crawler.svg)](https://pypi.org/project/article-crawler/)
[![PyPI Downloads](https://img.shields.io/pypi/dm/article-crawler?label=PyPI%20downloads)](https://pypi.org/project/article-crawler/)
[![](https://img.shields.io/github/v/release/ltyzzzxxx/article_crawler?display_name=tag)](https://github.com/ltyzzzxxx/article_crawler/releases/tag/v0.0.1)
[![](https://img.shields.io/github/stars/ltyzzzxxx/article_crawler)](https://github.com/ltyzzzxxx/article_crawler)
[![](https://img.shields.io/github/forks/ltyzzzxxx/article_crawler)](https://github.com/ltyzzzxxx/article_crawler)
[![](https://img.shields.io/github/issues/ltyzzzxxx/article_crawler)](https://github.com/ltyzzzxxx/article_crawler/issues)
[![](https://img.shields.io/badge/license-MIT%20-yellow.svg)](https://github.com/ltyzzzxxx/article_crawler/issues)

[English Doc](./README_EN.md) | [中文文档](./README_CN.md)

## ✨ Introduction

Article Crawler is a package used to crawl articles with Markdown format from a specific webpage and store them locally in HTML / Markdown formats.

## 🚀 Quick Start

1. Install through `pip`

    ```python
    pip install article-crawler
    ```
2. Usage

    Usage: `python3 -m article_crawler -u [url] -t [type] -o [output_folder] -c [class_] -i [id]`

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
    - type: Specific websites, currently supported are CSDN, Zhihu, Juejin, and Jianshu.
    - website_tag / class_ / id:
   
      e.g. `<div id="article_content" class="article_content clearfix"></div>`
   
      - In this element, `website_tag`, `class_`, `id` is `div`, `article_content clearfix`, `article_content` respectively.
      
      > 1. You don't need to specify `type` when you specify `website_tag / class_ / id`.
      > 2. You need to use the web console to locate the position of the article.
      > 3. `website_tag / class_ / id` is used to locate the position of the article in HTML. It is possible to only use one or two of them instead of all.

## Open Source License

MIT License see https://opensource.org/license/mit/
       
