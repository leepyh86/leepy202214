import _thread
import urllib.request
import  logging
from time import sleep,ctime
import pytest
# response = urllib.request.urlopen("https://www.baidu.com")
# response.read().decode("utf-8")
# print(response.status)
# print(response.headers)

import math
# print(math.ceil(4.5))
# print(math.floor(4.2))
# print(math.sqrt(16))

#### math.sqrt()


logging.basicConfig(level=logging.INFO)
def loop(nloop,nsec, lock):
    logging.INFO("start "+ str(nloop) +"at"+ ctime())
    sleep(nsec)
    logging.INFO("end " + str(nloop) +"at" + time.ctime())
    lock.release()

def main():
    loops=[2,4]
    nloops = range(len(loops))
    locks=[]
    for i in nloops:
        lock=_thread.allocate_lock()
        lock.acquire()
        locks.append(lock)

    for i in nloops:
        _thread.start_new_thread(loop,(i,loops[i],locks[i]))

    for i in nloops:
        while locks[i].locked():pass

    logging.INFO("end all thread"+ctime())

if __name__ == '__main__':
    pytest.main()
