#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:chenshifeng
@file:ymldemo.py
@time:2021/04/01
"""
import yaml

with open('contacts.yml',encoding='UTF-8') as f:
    yaml_data = yaml.safe_load(f)

print(yaml_data)

with open('contacts.yml',mode='w',encoding='UTF-8') as f2:
    uid = {'uid': 123789}
    yaml.safe_dump(uid,f2)