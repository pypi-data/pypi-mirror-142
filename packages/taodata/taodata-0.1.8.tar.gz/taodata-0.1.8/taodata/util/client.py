# !/usr/bin/env python
# -*- coding: utf-8 -*-

import xlwt
import csv
import pandas as pd
from functools import partial
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

    def query(self, api_name, fields=[], **kwargs):
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

    def export(self, file_path, file_type, api_name, fields=[], **kwargs):
        data = self.query(api_name, fields, **kwargs)
        alias_fields = data['alias_fields']
        items = data['items']
        df = pd.DataFrame(columns=alias_fields, data=items)
        if file_type == 'xlsx':
            writer = pd.ExcelWriter(file_path)
            df.to_excel(writer)
            writer.save()
        elif file_type == 'csv':
            df.to_csv(file_path, sep='\t')
        elif file_type == 'html':
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write("<html>" + '\n')
                f.write("<meta charset='utf-8'>" + '\n')
                f.write(
                    "<link href='https://cdn.jsdelivr.net/npm/bootstrap@3.3.7/dist/css/bootstrap.min.css' rel='stylesheet'>" + '\n')
                f.write(df.to_html())
                f.write("<html>")
        elif file_type == 'json':
            df.to_json(file_path)

    def __getattr__(self, name):
        return partial(self.query, name)

