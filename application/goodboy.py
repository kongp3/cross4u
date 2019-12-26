# -*- coding: utf-8 -*-
import wget
import requests
from config import DL_ROOT, WEB_HOST


class GoodBoy(object):
    def __init__(self):
        pass

    def link2file(self, link):
        r = requests.get(link)
        filename = wget.detect_filename(url=link, headers=r.headers, default='default.bin')
        with open(DL_ROOT + filename, 'wb') as f:
            f.write(r.content)

        return WEB_HOST + DL_ROOT.replace('./', '') + filename
