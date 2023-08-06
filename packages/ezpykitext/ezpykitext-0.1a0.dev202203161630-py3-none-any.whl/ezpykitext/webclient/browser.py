#!/usr/bin/env python3
from functools import lru_cache

from ezpykit.allinone import install_module, T
from ezpykit.config import EnVarConfig
from ezpykit.stdlib.urllib.parse import tolerant_urlparse

try:
    import splinter as ___
except ImportError:
    install_module('splinter')

import splinter.driver.webdriver


def make_proxy_settings(http: tuple = None, ssl: tuple = None):
    if not http and not ssl:
        env_proxy = EnVarConfig().get_proxy()
        _http = env_proxy.get('http')
        _https = env_proxy.get('https')
        if _http:
            http = _http['hostname'], _http['port']
        if _https:
            ssl = _https['hostname'], _https['port']
    if http and not ssl:
        ssl = http
    elif ssl and not http:
        http = ssl
    elif not http and not ssl:
        return {}
    return {
        'network.proxy.type': 1,
        'network.proxy.http': http[0],
        'network.proxy.http_port': http[1],
        'network.proxy.ssl': ssl[0],
        'network.proxy.ssl_port': ssl[1],
    }


class EzBrowser:
    def __init__(
            self, b: splinter.driver.webdriver.BaseWebDriver = None,
            driver_name='firefox', headless=False,
            proxy=False, block_images=False,
            **kwargs
    ):
        if b:
            self.browser = b
            return
        profile_preferences = {}
        if block_images:
            profile_preferences['permissions.default.image'] = 2
        if proxy is False:
            pass
        elif proxy is ...:
            profile_preferences.update(make_proxy_settings())
        else:
            if isinstance(proxy, str):
                r = tolerant_urlparse(proxy)
                proxy = r.hostname, r.port
            if isinstance(proxy, tuple):
                profile_preferences.update(make_proxy_settings(http=proxy, ssl=proxy))
            else:
                raise TypeError('invalid proxy type', type(proxy))
        self.browser = splinter.Browser(driver_name, profile_preferences=profile_preferences, headless=headless,
                                        **kwargs)

    def __getattr__(self, name):
        x = getattr(self.browser, name)
        self.__dict__[name] = x
        return x

    def get_cookies_dict(self):
        return self.cookies.all()

    def get_cookies_list(self):
        return self.driver.get_cookies()

    def update_cookies(self, cookies, url=None, domain=None, reload=False):
        if url:
            self.visit(url)
        self.cookies.add(cookies)
        for c in self.get_cookies_list():
            c['domain'] = domain
            self.driver.add_cookie(c)
        if reload:
            self.reload()

    @lru_cache()
    def _element_method(self, predicate, by):
        if predicate == 'find_link':
            return getattr(self.browser.links, f'find_by_{by}')
        return getattr(self.browser, f'{predicate}_by_{by}')

    def _batch_predicate_element(self, predicate, **kwargs):
        func_kwargs = {}
        wait_time_k = 'wait_time'
        if wait_time_k in kwargs:
            func_kwargs[wait_time_k] = kwargs.pop(wait_time_k)
        if len(kwargs) == 1:
            for k, v in kwargs.items():
                if isinstance(v, T.Iterable) and not isinstance(v, str):
                    return {i: self._element_method(predicate, k)(i, **func_kwargs) for i in v}
                else:
                    return self._element_method(predicate, k)(v, **func_kwargs)
        r = {}
        for k, v in kwargs.items():
            kd = r.setdefault(k, {})
            if isinstance(v, T.Iterable) and not isinstance(v, str):
                for i in v:
                    kd[i] = self._element_method(predicate, k)(i, **func_kwargs)
            else:
                kd[v] = self._element_method(predicate, k)(v, **func_kwargs)
        return r

    def find(self, wait_time=None, **kwargs):
        return self._batch_predicate_element('find', wait_time=wait_time, **kwargs)

    def find_link(self, **kwargs):
        return self._batch_predicate_element('find_link', **kwargs)

    def exist(self, wait_time=None, **kwargs):
        return self._batch_predicate_element('is_element_present', wait_time=wait_time, **kwargs)

    def not_exist(self, wait_time=None, **kwargs):
        return self._batch_predicate_element('is_element_not_present', wait_time=wait_time, **kwargs)

    def visible(self, wait_time=None, **kwargs):
        return self._batch_predicate_element('is_element_visible', wait_time=wait_time, **kwargs)

    def not_visible(self, wait_time=None, **kwargs):
        return self._batch_predicate_element('is_element_not_visible', wait_time=wait_time, **kwargs)
