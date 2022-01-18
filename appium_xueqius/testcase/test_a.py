#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @file: test_a.py
# @time: 2022/1/5 23:03
# @author: leepy cham

# !/usr/bin/env python
# -*- encoding: utf-8 -*-
# @file: test_xueqiu.py
# @time: 2021/12/27 21:56
# @author: leepy cham
import time

from appium import webdriver
from time import sleep
import os
from selenium.webdriver.common.by import By
# import unittest


class ContactAndroidTest():
    def setUp(self):
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "adc"
        caps['udid'] = os.getenv("udid",None)
        #caps['udid'] = "127.0.0.1:7555"#1060dc500409
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        caps["skipServerInstallation"] = True
        caps['noReset'] = True
        caps["skipDeviceInitialization"] = True

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(15)


    def TearDown(self):
        self.driver.quit()

    def test_swipe(self):
        ####点击######
        ###TouchActions(self.driver).flick(100,100).release().perform()

        ###第二步
        # el11 = self.driver.find_element(By.XPATH, "//*[@resource-id='com.xueqiu.android:id/title_text'][@text='视频']")
        # el11.click()
        # self.driver.implicitly_wait(10)
        sleep(10)

        ###其次点击搜索框tv_search
        el2 = self.driver.find_element(By.ID, "com.xueqiu.android:id/home_search")
        el2.click()
        self.driver.implicitly_wait(3)
        
        el3 = self.driver.find_element(By.ID, "com.xueqiu.android:id/search_input_text")
        el3.send_keys("alibaba")
        
        # el4 = self.driver.find_element(By.XPATH,
        #                                "//*[@resource-id='com.xueqiu.android:id/name'][@text='阿里巴巴-SW'][@index='1']")
        # el4.click()

        # self.driver.find_element_by_id("stockName").click()
        ###noreset foreset


# if __name__ == '__main__':
#     suit = unittest.TestLoader().loadTestsFromTestCase(ContactAndroidTest)
#     unittest.TextTestRunner(verbosity=2).run(suit)





