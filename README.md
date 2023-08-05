# Article Crawler

## ✨ Introduction

Article Crawler is a package used to crawl articles with Markdown format from a specific webpage and store them locally in HTML / Markdown formats.

## 🚀 Quick Start

1. Install through `pip`

    ```python
    pip install article_crawler
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
       
