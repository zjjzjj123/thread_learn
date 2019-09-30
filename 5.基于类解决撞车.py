import threading
import time


'''
使用锁解决冲突问题
'''
num = 0

mx_lock = threading.Lock()

class mythread(threading.Thread):
    def run(self): #线程来了 独占被锁的部分
        global num
        if mx_lock.acquire(1):  #独占 锁住之后只能执行里面的  #只有执行完之后才能访问，锁不住就等待
            for i in range(10000000):
                num += 1
            mx_lock.release() #释放锁
        print(num)

myt = []
for i in range(5):
    t = mythread()
    t.start()
    myt.append(t)
    # t.join()  #顺序
for t in myt: #乱序  输出有冲突
    t.join()

print('game over')