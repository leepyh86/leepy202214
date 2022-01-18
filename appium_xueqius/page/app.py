#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @file: app.py
# @time: 2022/1/5 17:06
# @author: leepy cham
import logging
import yaml
from appium import webdriver
from  appium_xueqius.page.base_page import BasePage
from  appium_xueqius.page.main_page import MainPage
from time import sleep

with open("../datas/page/caps.yaml") as f:
    datas={}
    datas = yaml.safe_load(f)
    desires = datas['desirecaps']
    ip = datas['server']['ip']
    port = datas['server']['port']

class App(BasePage):
    def start(self):
        if self.driver == None:
            # 启动app
            # 客户端与appium 服务器建立连接的代码
            self.driver = webdriver.Remote(f"http://{ip}:{port}/wd/hub", desires)
            self.driver.implicitly_wait(15)

        else:
            # self.driver.start_activity("com.tencent.wework",".launch.LaunchSplashActivity")
            self.driver.launch_app()


        return self



    def restart(self):
        self.driver.close()
        self.driver.launch_app()

    def stop(self):
        self.driver.quit()

    def main(self) -> MainPage:
        return MainPage(self.driver)


