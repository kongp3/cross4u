# -*- coding: utf-8 -*-
import time
from flask import request, jsonify, render_template

from config import app
from api import error_handler
from application.goodboy import GoodBoy


@app.route('/link2file', methods=['GET'])
@error_handler
def link2file(**kwargs):
    start = time.time()
    response = kwargs.get("response")
    link = request.values.get("link")

    gb = GoodBoy()
    file_link = gb.link2file(link)
    end = time.time()
    delta_time = str(end - start)
    return_val = {"time": delta_time, "link": file_link}
    return response.success(data=return_val)
