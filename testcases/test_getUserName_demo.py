#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:chenshifeng
@file:test_getUserName_demo.py
@time:2021/05/05
"""
from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase


class TestCaseRequestWithGetUserName(HttpRunner):
    config = (
        Config("test /getUserName")
        .base_url("http://localhost:5000")
        .verify(False)
        .export(*["username"])  # 这里定义出要导出的变量
    )

    teststeps = [
        Step(
            RunRequest("getUserName")
            .get("/getUserName")
            .extract()
            .with_jmespath("body.username", "username")  # 提取出目标值，赋值给username变量
            .validate()
            .assert_equal("body.username", "chenshifeng")
        ),

    ]


if __name__ == "__main__":
    TestCaseRequestWithGetUserName().test_start()
