#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:chenshifeng
@file:test_joinStr_demo.py
@time:2021/05/05
"""
from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
from testcases.test_getUserName_demo import TestCaseRequestWithGetUserName as RequestWithGetUserName   # 记得要导入引用的类


class TestCaseRequestWithJoinStr(HttpRunner):
    config = (
        Config("test /joinStr")
        .base_url("http://localhost:5000")
        .verify(False)
    )

    teststeps = [
        Step(
            RunTestCase("setUp getUserName")
            .call(RequestWithGetUserName)   # 导入后就可以调用了
            .export(*["username"])  # 在RunTestCase步骤中定义这个变量的导出
        ),
        Step(
            RunRequest("joinStr")
            .get("/joinStr")
            .with_params(**{"str1": "hello", "str2": "$username"})  # 在第二个传参中引用导出的变量
            .validate()
            .assert_equal("body.result", "hello $username")   # 断言的预期值也引用变量
        ),

    ]


if __name__ == "__main__":
    TestCaseRequestWithJoinStr().test_start()   # 这里
