# -*- coding: utf-8 -*-
import wget
import requests
from config import DL_ROOT, WEB_HOST


class GoodBoy(object):
    def __init__(self):
        pass

    def link2file(self, link):
        r = requests.get(link)

        name_url = wget.filename_from_url(link) or ''
        name_headers = wget.filename_from_headers(r.headers) or ''
        filename = name_headers or name_url or 'default.bin'

        # filename = wget.detect_filename(url=link, headers=r.headers, default='default.bin')
        with open(DL_ROOT + filename, 'wb') as f:
            f.write(r.content)

        return WEB_HOST + DL_ROOT.replace('./', '') + filename
