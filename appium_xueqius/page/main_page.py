#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @file: main_page.py
# @time: 2022/1/5 17:06
# @author: leepy cham
from  appium_xueqius.page.base_page import BasePage
from  appium_xueqius.page.market_page import MarketPage
from selenium.webdriver.common.by import By
class MainPage(BasePage):
    def goto_market(self):
        self.set_implicitly(15)
        self.steps("../datas/page/main.yaml")
        self.set_implicitly(5)
        return MarketPage(self.driver)


