import threading
import time

num = 0

# Rlock = threading.RLock()
mutex = threading.RLock()#threading.Lock() #避免单线程死锁

'''
单线程死锁 就是对一个东西或者资源进行加锁再加锁
'''
class mythread(threading.Thread):
    def run(self):
        global num
        if mutex.acquire(1):
            num += 1

            if mutex.acquire(1): #循环锁的问题 不能执行 因为上一层锁没有 #若是使用RLock则不会出现问题
                num += 10000
                mutex.release()

            print(self.name,num)
            mutex.release()

for i in range(5):
    t = mythread()
    t.start()