# -*- encoding: utf-8 -*-
"""
@Author  : zh_o
"""
import os
import importlib
from typing import Dict, Text, Callable
from types import FunctionType


def locate_file(start_path: Text, file_name: Text) -> Text:
    """定位文件路径"""
    if os.path.isfile(start_path):
        start_dir_path = os.path.dirname(start_path)
    elif os.path.isdir(start_path):
        start_dir_path = start_path
    else:
        raise Exception(f"invalid path: {start_path}")

    file_path = os.path.join(start_dir_path, file_name)
    if os.path.isfile(file_path):
        return os.path.abspath(file_path)
    parent_dir = os.path.dirname(start_dir_path)
    if parent_dir == start_dir_path:
        raise Exception(f"{file_name} not found in {start_path}")

    return locate_file(parent_dir, file_name)


CONFIG_PATH = locate_file('./', 'melon.toml')
ROOT_DIR = os.path.abspath(os.path.dirname(CONFIG_PATH))


def load_module_functions(module) -> Dict[Text, Callable]:
    """加载模块中所有函数"""
    module_functions = {}

    for name, item in vars(module).items():
        if isinstance(item, FunctionType):
            module_functions[name] = item

    return module_functions


def load_application_functions() -> Dict[Text, Callable]:
    """加载 application.py 中所有函数"""
    melon_path = f'{ROOT_DIR}{os.path.sep}application.py'

    if not melon_path:
        return {}

    try:
        module = importlib.import_module('application')
    except Exception as e:
        raise ImportError(f'error occurred in application.py [{e.args[0]}]')
    module = importlib.reload(module)
    return load_module_functions(module)


APPLICATION_FUNCTIONS = load_application_functions()

