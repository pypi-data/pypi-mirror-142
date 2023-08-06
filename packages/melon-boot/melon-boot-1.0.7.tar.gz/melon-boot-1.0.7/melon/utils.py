# -*- encoding: utf-8 -*-
"""
@Author  : zh_o
"""
import csv
import os
import re
from typing import Text, List, Set, Dict, Union
from faker import Faker
from melon.loader import APPLICATION_FUNCTIONS

fa = Faker('zh_CN')


class CollUtil:

    @staticmethod
    def is_not_empty(coll: Union[List, Set]) -> bool:
        return coll and len(coll) > 0

    @staticmethod
    def is_empty(coll: Union[List, Set]) -> bool:
        return not CollUtil.is_not_empty(coll)


class DictUtil:

    @staticmethod
    def is_not_empty(dictionary: Dict) -> bool:
        return dictionary and len(dictionary.items()) > 0

    @staticmethod
    def is_empty(dictionary: Dict) -> bool:
        return not DictUtil.is_not_empty(dictionary)


class StrUtil:

    @staticmethod
    def is_not_blank(string: Text) -> bool:
        return string and len(string.strip()) > 0

    @staticmethod
    def is_blank(string: Text) -> bool:
        return not StrUtil.is_not_blank(string)


class ParameterizeUtil:
    """
    参数化工具
    """

    @staticmethod
    def read_csv_dict(path: Text, headers: List[Text] = None) -> List[Dict]:
        """
        读取csv内容
        :param path: csv文件路径
        :param headers: 表头(为空则默认取首行为表头)
        """
        with open(file=path, encoding='utf8', mode='rU') as csv_file:
            contents = [ParameterizeUtil.__parse_func_all(line) for line in csv_file if not line.startswith('#')]
            if CollUtil.is_empty(headers):
                reader = csv.DictReader(contents)
            else:
                reader = csv.DictReader(contents, fieldnames=headers)
            lines = list(reader)
        return lines

    @staticmethod
    def read_csv(path: Text, ignore_first_line=True) -> List[List]:
        """
        读取csv内容
        :param path: csv文件路径
        :param ignore_first_line: 是否忽略首行
        """
        with open(path, encoding='utf8', mode='rU') as csv_file:
            contents = [ParameterizeUtil.__parse_func_all(line) for line in csv_file if not line.startswith('#')]
            reader = csv.reader(contents)
            lines = list(reader)
        if ignore_first_line:
            del lines[0]
        return lines

    @staticmethod
    def __parse_expression(expression: Text):
        """
        解析表达式
        ${mock__xxx()} or ${mock__xxx}  调用 faker 中 mock 函数
        ${melon__xxx()} or ${melon__xxx}  调用 application.py 中自定义函数
        """
        regex = r'^\${(mock|app)__(\w+?)(\(\))?}$'
        res = re.search(regex, expression)
        if not res:
            return expression

        # mock 还是 application
        prefix = res.group(1)
        function_name = res.group(2)
        if prefix == 'mock':
            return eval(f'fa.{function_name}()')
        elif prefix == 'app':
            app_function = APPLICATION_FUNCTIONS.get(function_name)
            return app_function() if app_function else expression
        else:
            return expression

    @staticmethod
    def __parse_func_all(expression: Text):
        """
        解析函数表达式
        """
        pattern = r'(\${)(mock|app)(__)(\w+?)(\(\))?(})'
        matched_list = re.findall(pattern, expression)

        if not matched_list or len(matched_list) < 1:
            return expression

        # 替换解析后数值
        matched_list = [ParameterizeUtil.__eval(items[1], items[3]) or ''.join(items) for items in matched_list]

        expression = re.sub(pattern=pattern, repl="{}", string=expression)
        return expression.format(*matched_list)

    @staticmethod
    def __eval(prefix: Text, function_name: Text):
        """解析表达式"""
        try:
            if prefix == 'mock':
                return eval(f'fa.{function_name}()')
            elif prefix == 'app':
                app_function = APPLICATION_FUNCTIONS.get(function_name)
                return app_function() if app_function else None
            else:
                return None
        except AttributeError:
            return None
