#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:chenshifeng
@file:base_config.py
@time:2021/04/01
"""

from base.caeate_name import CreateName


class Base():
    wwrtx_sid = "LByZgHuduBrwXVen3sfhf4wCRDsw3JtC7D4g1YjzuU4Ic46cyPEI64XzAS5prykU"

    def get_name_and_sex(self):
        createname = CreateName()
        names = createname.random_name()
        names = names.split()
        name, sex = names
        sex = 1 if sex == '男' else 2
        return [name, sex]


if __name__ == '__main__':
    base = Base()
    print(base.get_name_and_sex())
