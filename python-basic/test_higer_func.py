#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @file: test_higer_func.py
# @time: 2022/1/4 13:05
# @author: leepy cham
from functools import reduce


####高阶函数：将函数作为参数传递，并作用到第二个参数下
class TestHigerFunc:

    def dicttoint(s):
        print(s)
        return DISTNICT[s]


    def test_higer_func(self):

        #####map函数
        result = list(map(lambda x:x,[1,2,3,4]))
        print(result)
        print(list(map(lambda x:x.upper(),"aaaaaa")))

        ####reduce 作为参数的函数可以传递两个值
        result = reduce(lambda x,y:x+y,[1,2,3,4,5])
        print(result)


        ##构建一个字符串转为整型函数

        DISTNICT = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9 }
        s='2345023'
        print(list(map(dicttoint,s)))
        print(reduce(lambda x,y:x*10+y, map(dicttoint,s)))

    def test_map(self):
        #####map函数
        result = list(map(lambda x: x, [1, 2, 3, 4]))
        print(result)
        print(list(map(lambda x: x.upper(), "aaaaaa")))
    def test_reduce(self):
        ####reduce 作为参数的函数可以传递两个值
        result = reduce(lambda x, y: x + y, [1, 2, 3, 4, 5])
        print(result)

        ##构建一个字符串转为整型函数
        DISTNICT = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
        s = '2345023'
        print(list(map(dicttoint, s)))
        print(reduce(lambda x, y: x * 10 + y, map(dicttoint, s)))

    def test_filter(self):
        demo=['ASDSDsd','sdsd','asdSADSsdds']
        print(list(filter(lambda x:x.upper(),demo)))


    def test_sorted(self):
        #sort sorted
        list=[10,9,23,234,2,1,2,0]
        print(sorted(list))






