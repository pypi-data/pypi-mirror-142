# !/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
from functools import partial
from taodata.util.dsl import BodyHelper
import json
import requests


class DataApi:

    __token = ''
    __http_url = 'http://210.22.185.58:7788/route'
    #__http_url = 'http://localhost:5000'

    def __init__(self, token, timeout=30):
        """
        Parameters
        ----------
        token: str
            API接口TOKEN，用于用户认证
        """
        self.__token = token
        self.__timeout = timeout
        self.__body_helper = BodyHelper()

    def match_phrase(self, field, value, clause='must'):
        self.__body_helper.match_phrase(field, value, clause)
        return self

    def match_all(self, clause='must'):
        self.__body_helper.match_all(clause)
        return self

    def term(self, field, value, clause='must'):
        self.__body_helper.term(field, value, clause)
        return self

    def terms(self, field, values, clause='must'):
        self.__body_helper.terms(field, values, clause)
        return self

    def set_minimum_should_match(self, minimum_should_match):
        self.__body_helper.set_minimum_should_match(minimum_should_match)
        return self

    def exists(self, field, clause='must'):
        self.__body_helper.exists(field, clause)
        return self

    def set_size(self, __size):
        self.__body_helper.set_size(__size)
        return self

    def set_from(self, __from):
        self.__body_helper.set_from(__from)
        return self

    def sort(self, field, order='asc'):
        self.__body_helper.sort(field, order)
        return self

    def range(self, field, gte=None, lte=None, gt=None, lt=None, format=None, clause='must'):
        self.__body_helper.range(field, gte, lte, gt, lt, format, clause)
        return self

    def clear(self):
        self.__body_helper = BodyHelper()
        return self

    def query(self, api_name, fields=[], **kwargs):
        # 设置action
        kwargs['action'] = 'query'
        # 判断是否有body参数
        if 'body' not in kwargs:
            kwargs['body'] = self.__body_helper.to_json()

        req_params = {
            'api_name': api_name,
            'token': self.__token,
            'params': kwargs,
            'fields': fields
        }

        res = requests.post(self.__http_url, json=req_params, timeout=self.__timeout)
        if res:
            result = json.loads(res.text)
            if result['code'] != 0:
                raise Exception(result['msg'])
            data = result['data']
            return data
        else:
            return None

    def export(self, local_file, api_name, fields=[], **kwargs):
        # 设置action
        kwargs['action'] = 'export'
        # 判断是否有body参数
        if 'body' not in kwargs:
            kwargs['body'] = self.__body_helper.to_json()

        req_params = {
            'api_name': api_name,
            'token': self.__token,
            'params': kwargs,
            'fields': fields
        }

        res = requests.post(self.__http_url, json=req_params, timeout=self.__timeout)

        f = open(local_file, 'wb')
        f.write(res.content)
        f.close()

    def __getattr__(self, name):
        return partial(self.query, name)

