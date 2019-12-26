# -*- coding: utf-8 -*-

import os
import requests
import wget

url = ""
r = requests.get(url)
filename = wget.detect_filename(url=url, headers=r.headers, default='default.bin')
