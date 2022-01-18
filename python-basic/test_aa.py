import _thread
import urllib.request
import logging
import threading
from time import sleep, ctime
import pytest
# response = urllib.request.urlopen("https://www.baidu.com")
# response.read().decode("utf-8")
# print(response.status)
# print(response.headers)

import math

print(math.ceil(4.5))
print(math.floor(4.2))
print(math.sqrt(16))

#### math.sqrt()


logging.basicConfig(level=logging.INFO)




class MyThread(threading.Thread):
    def __init__(self, func, args, name=''):
        threading.Thread.__init__(self)
        self.func = func
        self.args = args
        self.name = name

    def run(self):
        self.func(*self.args)


def loop(nloop, nsec):
    print("star at" + ctime())
    sleep(nsec)
    print("end at" + ctime())



def test_main():
    logging.info("start all at" + ctime())
    threads = []
    loops = [2, 4]
    nloops = range(len(loops))

    for i in nloops:
        t = MyThread(loop, (i, loops[i]), loop.__name__)
        threads.append(t)
    for i in nloops:
        threads[i].start()
    for i in nloops:
        threads[i].join()

if __name__ == '__main__':
    pytest.main()


