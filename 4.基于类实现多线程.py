import threading
import time
import win32api

'''
线程难点:
1.线程冲突（同时访问一个资源）
2.线程通信（寻找资源时 有一个找到了 通知另一个停止寻找）
'''

class my_thread(threading.Thread):
    def run(self):
        win32api.MessageBox(0,'message','title',2)

'''
for i in range(5):
    A = my_thread() #初始化
    A.start() #开始 #主线程等待线程执行完
    A.join()  #等待上个线程执行完再执行下一个 类似顺序风格 不需要卡死主线程 解决冲突的一种办法
'''

mythre = []

for i in range(5):
    A = my_thread()
    A.start()
    mythre.append(A)

for myth in mythre:
    myth.join()  #同时开启5个县城 并且主线程等到子线程执行完成