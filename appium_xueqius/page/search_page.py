#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @file: search_page.py
# @time: 2022/1/5 17:07
# @author: leepy cham

import yaml
from selenium.webdriver.common.by import By

from  appium_xueqius.page.base_page import BasePage


class SearchPage(BasePage):
    def search(self, name):
        self._params["name"]=name

        self.steps("../datas/page/search.yaml")

    def add(self,name):
        self._params["name"] = name
        self.steps("../datas/page/search.yaml")

    def is_choose(self, name):
        self._params["name"] = name
        return self.steps("../datas/page/search.yaml")

    def reset(self, name):
        self._params["name"] = name
        return self.steps("../datas/page/search.yaml")
