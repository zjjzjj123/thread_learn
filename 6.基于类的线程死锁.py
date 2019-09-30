import threading
import time
'''
使用锁解决冲突问题
死锁: 你先给我我在给你  
锁住就要释放 不然会出现死锁
'''

boymutex = threading.Lock()
girlmutex = threading.Lock()

class boythread(threading.Thread):
    def run(self):
        if boymutex.acquire(1):
            print(self.name+'boy say is sorry up')
            time.sleep(3)
            # boymutex.release()  #放在这里解决死锁 因为boy先解锁了 girl的类也可以先解锁
            if girlmutex.acquire(1):
                print(self.name + 'boy say is sorry down')
                girlmutex.release()
            boymutex.release() #放在这里就是死锁 因为两个都锁住了没有任何一个先释放锁所以死锁

class girlthread(threading.Thread):
    def run(self):
        if girlmutex.acquire(1):
            print(self.name+'girl say is sorry up')
            time.sleep(3)
            if boymutex.acquire(1):
                print(self.name + 'girl say is sorry down')
                boymutex.release()
            girlmutex.release()
boy = boythread()
boy.start()
girl = girlthread()
girl.start()
print('\ngame over')