# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pdfkit
import re
import os
import uuid
from PyPDF2 import PdfFileMerger
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
</head>
<body>
{content}
</body>
</html>
"""

css = 'css/sphinx_rtd_theme.css'


def parse_url_to_html(body, name):
    html = str(body)
    html = html_template.format(content=html)
    html = html.encode("utf-8")
    with open(name, 'wb') as f:
        f.write(html)
    return name


def save_pdf(htmls, file_name):
    options = {'page-size': 'Letter', 'margin-top': '0.75in', 'margin-right': '0.75in', 'margin-bottom': '0.75in', 'margin-left': '0.75in', 'encoding': "UTF-8", 'custom-header': [('Accept-Encoding', 'gzip')],
               'cookie': [('cookie-name1', 'cookie-value1'), ('cookie-name2', 'cookie-value2'), ], 'outline-depth': 10, }
    pdfkit.from_file(htmls, file_name, options=options, css=css)


class PythondocPipeline(object):

    def __init__(self):
        self.htmls = []
        self.pdfs = []

    def process_item(self, item, spider):
        # name = item['name'][0]
        # name = str(uuid.uuid1())
        # parse_url_to_html(item['data'][0], name + '.html')
        # self.htmls.append(name + '.html')
        # try:
        #     save_pdf(name + '.html', name + '.pdf')
        # except:
        #     pass
        # self.pdfs.append(name + '.pdf')
        return item

    # def close_spider(self, spider):
        # name = 'Scrapy教程'
        # merger = PdfFileMerger()
        # for pdf in self.pdfs:
        #     merger.append(open(pdf, 'rb'))
        # output = open(name+".pdf", "wb")
        # merger.write(output)
        # for html in self.htmls:
        #     os.remove(html)
        # for pdf in self.pdfs:
        #     os.remove(pdf)
