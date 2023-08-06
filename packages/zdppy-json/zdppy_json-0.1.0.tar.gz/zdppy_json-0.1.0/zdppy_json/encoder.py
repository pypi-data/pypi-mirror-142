#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/3/7 23:51
# @Author  : 张大鹏
# @Site    : 
# @File    : encoder.py
# @Software: PyCharm
import json
import decimal


class DecimalEncoder(json.JSONEncoder):
    """
    decimal解析器
    """

    def default(self, o):
        if isinstance(o, decimal.Decimal):  # 将decimal类型转换为float类型
            return float(o)
        super(DecimalEncoder, self).default(o)
