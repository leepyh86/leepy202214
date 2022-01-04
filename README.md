## 项目介绍
本人自学python 测开实战演示

## 参考论坛
- [测试人论坛](https://ceshiren.com/)

## 参考链接
pytest: https://docs.pytest.org/en/stable/getting-started.html
## 作业地址
### 1.pytest中fixture的用法    2022/1/4 12:00
### 2.python中yield的用法      2022/1/4 12:30

    使用：fixture@pytest.mark.usefixtures("login")

    fixture的作用域： scope= session > module > class > function
### 3.yaml的用法:
####   
    import yaml  file = yaml.safe_load(open("datas/data.yaml"))

### 4.python的高阶函数使用
    map reduce filter sorted

### 5.python中的装饰器详解
        --新建一个装饰器--
        def test(func):
            def inner(*args,**kwargs):
                g=func(*args,**kwargs)
                g.__next__()
                return g
            return inner

        ----将装饰器注入 生成器中----
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
