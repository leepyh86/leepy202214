#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @file: market_page.py
# @time: 2022/1/5 18:45
# @author: leepy cham
from selenium.webdriver.common.by import By

from  appium_xueqius.page.base_page import BasePage
from  appium_xueqius.page.search_page import SearchPage


class MarketPage(BasePage):
    def goto_search(self):
        self.set_implicitly(3)
        return SearchPage(self.driver)
