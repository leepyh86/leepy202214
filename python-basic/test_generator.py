#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @file: test_generator.py
# @time: 2022/1/4 14:30
# @author: leepy cham
###什么是生成器：一边循环一边计算,保存的是算法而不是value
###生成器的优势：内存开销小
class TestGenerator:

    def test_generator(self):
        g =  (x*x for x in range(1,10))
        print(next(g))

        ###生成器
        def fib(max):
            n, a, b = 0, 0, 1
            while n < max:
                yield b
                a, b = b, a + b
                n = n + 1
                print(a,b,n)
            return 'done'
        f=fib(6)
        next(f)
        next(f)
        next(f)
        next(f)
        next(f)
        next(f)


    def test(func):  # func = average
        def inner(*args, **kwargs):
            g = func(*args, **kwargs)  # g = average() 给g 赋值 产生一个生成器
            g.__next__()  # 执行__next__（）方法 相当于激活生成器average（）开始运行，返回了一个 avg
            return g  # 将值g返回
        return inner


    def test_fix(self):
        ###使用装饰器去激活生成器，生成器就是迭代器中存储算法，一边循环一边计算结果.
        def test(func):
            def inner(*args,**kwargs):
                g=func(*args,**kwargs)
                g.__next__()
                return g
            return inner

        @test
        def average():
            count=0
            sum=0
            avg=0
            while True:
                num =yield avg
                sum+=num
                count+=1
                avg=sum/count


        avg_g = average()  # 接着开始调用函数 这个函数的返回值是 inner，因加括号开始调用函数inner() # 相当于avg_g = g = average()
        avg1 = avg_g.send(10)  # avg1 = 10
        print(avg1)
        avg1 = avg_g.send(120)
        print(avg1)
        avg1 = avg_g.send(120)
        print(avg1)







### def my_decorator(f)
#   def fn(*args **kwargs)
    ###扩展的逻辑 
   # return f(*args **kwargs)
   #return fn
#####

#装饰器 将函数作为参数名传递 动态扩展函数的功能 

 ####迭代器next send方法\


 
def singleton (cls, *args, **kwargs):

    instances = {}
    def get_instance (*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return get_instance
 

#创建一个带有装饰器的类

@singleton

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
student = Student('jiang', 25)

print(student)


