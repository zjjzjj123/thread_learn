import threading
import time

'''
1.线程同步:存在多个线程时，每个线程访问共享资源的时候，保证每次只能有一个线程对其访问 
  但到底是哪个线程抢到访问权，是未知的，谁先抢到谁先 随机的
2.线程通信:每次也是只能有一个线程访问资源，但是，在当前线程结束后，可以通知指定的线程过来访问资源
  有序的，非随机的
'''



def goevent():
    e = threading.Event() # 事件
    def go():
        e.wait() #等待 #直到set
        e.clear()
        print('go')
    threading.Thread(target=go).start()
    return e
def simple(): #简单的
    t = goevent()
    # threading.Thread(target=t).start() #在这里的话只能执行到go就一直等待不会出现set
    time.sleep(5)
    t.set() #通知线程不用等待了 开始执行
'''
比较复杂的
'''
def en_goevent():
    e = threading.Event()
    def go():
        for i in range(10):
            e.wait()
            e.clear() #重置 不然wait只能使用一次等待的作用
            print(i,'go')
    threading.Thread(target=go).start()
    return e
def en_ex():
    t = en_goevent()
    for i in range(10):
        time.sleep(5)
        t.set()


if __name__ == '__main__':
    print('start')
    en_ex()
    print('end')