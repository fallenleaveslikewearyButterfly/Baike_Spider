import requests

__author__ = "Liang"
__Date__ = 2017 / 8 / 13


class HtmlDownloader(object):
    def download(self, url):
        if url is None:
            return None
        headers={"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0",
                 "Host":"baike.baidu.com","Upgrade-Insecure-Requests":1}
        resp=requests.get(url)
        resp.encoding="utf-8"
        if resp.status_code!=200:
            return None
        return resp.text