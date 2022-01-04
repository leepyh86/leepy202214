#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @file: test_fixture.py
# @time: 2022/1/4 12:10
# @author: leepy cham

import  pytest
import yaml

@pytest.fixture()
def login():
    print("\n login start")
    yield
    print("\n quit end")

class TestFixture:
    def setup(self):
        print("start")
    def teardown(self):
        print("end")



    #生成器：高阶的迭代器 循环不中断 记住上次运行结果 可以继续执行
    def get_avg(grade):
        count=0
        avg=0
        num=0
        yiled
        count +=grade
        avg = count/grade
        num+=1
        return avg




    @pytest.mark.usefixtures("login")
    def test_fix(self):
        print("hello ")



    def test_yaml_demo(self):
        file = yaml.safe_load(open("datas/data.yaml"))
        print(file['book']['history'][0])




    ###奥运会打靶求值 iterable iter next wrap 装饰器 迭代器 生成器

###python语法：高阶函数 迭代器生成器装饰器
###多线程编程
###python的库math urllib.request
###python面向对象编程










