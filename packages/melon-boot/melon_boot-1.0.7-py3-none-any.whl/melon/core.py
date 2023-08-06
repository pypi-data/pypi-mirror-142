# -*- encoding: utf-8 -*-
"""
@Author  : zh_o
"""
from typing import Tuple, List, Text
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webelement import WebElement
from melon.webdrivers import driver
from melon.settings import get_config


_LOCATOR_ROUTER = {
    'css': By.CSS_SELECTOR,
    'id_': By.ID,
    'xpath': By.XPATH,
    'name': By.NAME,
    'class_name': By.CLASS_NAME,
    'tag_name': By.TAG_NAME,
    'link_text': By.LINK_TEXT,
    'partial_link_text': By.PARTIAL_LINK_TEXT,
}


class MelonElement(WebElement):
    """单元素"""

    def __init__(self, label: Text, **kwargs):
        super().__init__('', '')
        self.label = label
        if not kwargs:
            raise ValueError('locator must not be null')
        if len(kwargs) > 1:
            raise ValueError('locator must be unique')
        key, val = next(iter(kwargs.items()))
        if key not in _LOCATOR_ROUTER.keys():
            raise ValueError(f'invalid locator [{key}]')
        self.locator = (_LOCATOR_ROUTER[key], val)


class MelonElements(MelonElement):
    """可迭代元素"""

    def __init__(self, label: Text, **kwargs):
        super(MelonElements, self).__init__(label, **kwargs)


class BasePage:
    """基础 page object"""

    def __init__(self):
        self.driver = driver
        self.element_dict = object.__getattribute__(self, '__dict__')

    def find_element(self, locator: Tuple) -> WebElement:
        """定位单个元素"""
        _element = self.driver.find_element(*locator)
        original_click = _element.click
        original_send_keys = _element.send_keys

        def _click():
            with allure.step(f'点击{getattr(_element, "_label")}'):
                original_click()

        def _send_keys(*value):
            with allure.step(f'输入{getattr(_element, "_label")}: {" ".join(value)}'):
                original_send_keys(*value)

        _element.click = _click
        _element.send_keys = _send_keys
        return _element

    def find_elements(self, locator: Tuple) -> List[WebElement]:
        """定位多个元素"""
        _elements = self.driver.find_elements(*locator)
        return _elements

    def switch_to_frame(self, frame_reference):
        """切换至给定的 frame_reference"""
        self.driver.switch_to_frame(frame_reference)

    def switch_to_alert(self):
        """切换至 alert"""
        self.driver.switch_to_alert()

    def action_chains(self) -> ActionChains:
        """构件执行链"""
        return ActionChains(self.driver)

    def open(self, url: Text):
        """跳转至给定的 url"""
        base_url = get_config('melon.selenium.url')

        if url.startswith('http://') or url.startswith('https://'):
            self.driver.get(url)
            return
        if not url.startswith('/'):
            url = '/' + url
        if base_url.endswith('/'):
            base_url = base_url[:-1]
        self.driver.get(f'{base_url}{url}')

    def close(self):
        """关闭浏览器"""
        self.__step('关闭浏览器', self.driver.close)

    def __step(self, description: Text, func):
        """allure 报告步骤"""
        with allure.step(f'{self.__class__.__name__} => {description}'):
            return func()

    def __getattribute__(self, attr):
        """属性代理"""
        # e_ 或 _e_ 开头属性需代理
        if attr.startswith('e_') or attr.startswith('_e_'):
            # 获取目标属性(被代理属性)
            _target = self.element_dict[attr]
            if not _target:
                return object.__getattribute__(self, attr)

            if isinstance(_target, MelonElements):
                # 可迭代属性
                _proxy = self.__proxy_iterable(_target)
            elif isinstance(_target, MelonElement):
                # 单属性
                _proxy = self.__proxy_single(_target)
            else:
                raise ValueError(f'not supported element [{_target.__class__}]')

            return _proxy

        return object.__getattribute__(self, attr)

    def __proxy_single(self, _target: MelonElement):
        """
        代理单属性
        """
        _proxy = self.find_element(_target.locator)
        _proxy._label = _target.label
        return _proxy

    def __proxy_iterable(self, _target: MelonElements):
        """
        代理可迭代属性
        """
        _proxy = self.find_elements(_target.locator)
        [setattr(e, '_label', _target.label) for e in _proxy if e]
        return _proxy
