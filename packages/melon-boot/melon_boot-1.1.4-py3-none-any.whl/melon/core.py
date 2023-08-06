# -*- encoding: utf-8 -*-
"""
@Author  : zh_o
"""
from typing import Tuple, List, Text
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.remote.switch_to import SwitchTo
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from melon.webdrivers import driver
from melon.settings import get_config


class MelonElement(WebElement):
    """单元素"""

    def __init__(self, label: Text, by: By, loc: Text, timeout=None):
        super(MelonElement, self).__init__(None, None)
        self.label = label
        self.timeout = timeout
        self.by = by
        self.loc = loc
        self.locator = (by, loc)

    def __repr__(self):
        return '{"label": "%s", "locator": ["%s", "%s"]}' % (self.label, self.by, self.loc)


class BasePage:
    """基础 page object"""

    def __init__(self):
        self.driver = driver
        self.element_dict = object.__getattribute__(self, '__dict__')
        self.label_field = '_label'

    def find_element(self, locator: Tuple) -> WebElement:
        """定位单个元素"""
        element = self.driver.find_element(*locator)
        self.__proxy_allure(element)
        return element

    def find_elements(self, locator: Tuple) -> List[WebElement]:
        """定位多个元素"""
        elements = self.driver.find_elements(*locator)
        self.__proxy_allure(*elements)
        return elements

    def find_element_await(self, locator: Tuple, timout: float) -> WebElement:
        """定位单个元素并等待"""
        element = self.webdriver_wait(timout).until(EC.presence_of_element_located(locator))
        self.__proxy_allure(element)
        return element

    def find_elements_await(self, locator: Tuple, timout: float) -> List[WebElement]:
        """定位多个元素并等待"""
        elements = self.webdriver_wait(timout).until(EC.presence_of_all_elements_located(locator))
        self.__proxy_allure(*elements)
        return elements

    def switch_to(self) -> SwitchTo:
        """切换"""
        return self.driver.switch_to

    def action_chains(self) -> ActionChains:
        """构件执行链"""
        return ActionChains(self.driver)

    def webdriver_wait(self, timout: float, poll_frequency=0.5) -> WebDriverWait:
        """显示等待"""
        return WebDriverWait(self.driver, timout, poll_frequency)

    def send_keys(self, element_name: Text, value):
        """输入"""
        self.__getattribute__(element_name).send_keys(value)

    def click(self, element_name: Text):
        """点击"""
        self.__getattribute__(element_name).click()

    def open(self, url: Text):
        """跳转至给定的 url"""
        base_url = get_config('melon.selenium.url')

        if url.startswith('http://') or url.startswith('https://'):
            self.__step(f'跳转到 {url}', self.driver.get, url)
            return
        if not url.startswith('/'):
            url = '/' + url
        if base_url.endswith('/'):
            base_url = base_url[:-1]
        url = f'{base_url}{url}'
        self.__step(f'跳转到 {url}', self.driver.get, url)

    def close(self):
        """关闭浏览器"""
        self.__step('关闭浏览器', self.driver.close)

    def __step(self, description: Text, func, *args, **kwargs):
        """allure 报告步骤"""
        with allure.step(f'{self.__class__.__name__} => {description}'):
            return func(*args, **kwargs)

    def __getattribute__(self, attr):
        """属性代理"""
        # e_ 或 _e_ 开头属性需代理
        if attr.startswith('e_') or attr.startswith('_e_'):
            # 获取目标属性(被代理属性)
            _target = self.element_dict.get(attr)
            if not _target:
                return object.__getattribute__(self, attr)

            if isinstance(_target, List) and isinstance(_target[0], MelonElement):
                # 可迭代属性
                _proxy = self.__proxy_iterable(_target)
            elif isinstance(_target, MelonElement):
                # 单属性
                _proxy = self.__proxy_single(_target)
            else:
                raise ValueError(f'not supported element [{attr}]')

            return _proxy

        return object.__getattribute__(self, attr)

    def __proxy_single(self, _target: MelonElement) -> WebElement:
        """
        代理单属性
        """
        timeout = _target.timeout
        if timeout:
            _proxy = self.find_element_await(_target.locator, timeout)
        else:
            _proxy = self.find_element(_target.locator)
        _proxy._label = _target.label
        return _proxy

    def __proxy_iterable(self, _targets: List[MelonElement]) -> List[WebElement]:
        """
        代理可迭代属性
        """
        _target = _targets[0]
        timeout = _target.timeout
        if timeout:
            _proxy = self.find_elements_await(_target.locator, timeout)
        else:
            _proxy = self.find_elements(_target.locator)
        [setattr(e, '_label', _target.label) for e in _proxy if e]
        return _proxy

    def __proxy_allure(self, *args: WebElement) -> Tuple[WebElement]:
        """代理元素生产步骤报告"""
        if not args or len(args) < 1:
            return tuple()

        for target in args:
            # 代理方法
            raw_click = target.click
            raw_send_keys = target.send_keys

            def _click():
                with allure.step(f'点击{getattr(target, self.label_field)}'):
                    raw_click()

            def _send_keys(*values):
                with allure.step(f'输入{getattr(target, self.label_field)}: {" ".join(values)}'):
                    raw_send_keys(*values)

            target.click = _click
            target.send_keys = _send_keys
        return args
