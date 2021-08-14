#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:chenshifeng
@file:test_flask_demo.py
@time:2021/03/12
"""
from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/getUserName', methods=['GET'])
def get_user_name():
    if request.method == 'GET':
        return {
            "username": "chenshifeng",
            "age": "18",
            "from": "China",
        }


@app.route('/joinStr', methods=['GET'])
def str_join():
    if request.method == 'GET':
        str1 = request.args.get("str1")
        str2 = request.args.get("str2")
        after_join = str1 + " " + str2
        return {
            "result": after_join
        }


if __name__ == '__main__':
    app.run()
