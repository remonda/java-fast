#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 remonda <remonda@remonda-VirtualBox>
#
# Distributed under terms of the MIT license.

"""

"""

from flask import Flask
from flask import render_template
from flask import request

from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop

import logging
import json


app = Flask(__name__)


# set route 
@app.route('/')
def hello_world():
    return 'Hello, World!'


# render_template search templates dir default
@app.route('/get.html')
def get_html():
    return render_template('get.html')


@app.route('/post.html')
def post_html():
    return render_template('post.html')

@app.route('/deal_request', methods = ['GET', 'POST'])
def deal_request():
    if request.method == "GET":
        # get通过request.args.get("param_name","")形式获取参数值
        print(request.args) 
        for key,value in request.args.items():
            print('{key}:{value}'.format(key = key, value = value))
        get_q = json.dumps(request.args)
        return get_q
    elif request.method == "POST":
        # post通过request.form["param_name"]形式获取参数值
        post_q = request.form["q"]
        return render_template("result.html", result=post_q)

if __name__ == '__main__':
    # app.run(host, port, debug, options)
    port=5000
    http_server = HTTPServer(WSGIContainer(app))
    http_server.listen(5000)
    logging.info('Listening on {}'.format(port))
    IOLoop.current().start()

