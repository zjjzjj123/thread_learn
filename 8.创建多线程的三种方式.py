import time
import _thread
import threading
import win32api

def show(num):
    win32api.MessageBox(0,'2019930_'+str(num),'date',2)
'''
第一种
1.不考虑冲突
2.使用函数构建线程
'''
def fun_creat_thread():
    for i in range(5):
        _thread.start_new_thread(show,(i,))

'''
第二种 较常用
1.使用类的继承构造
2.能够考虑线程之间的冲突
'''



class mythread(threading.Thread):
    def __init__(self,num):
        threading.Thread.__init__(self) #初始化父类的构造函数
        self.num = num #传递参数
    def run(self):
        win32api.MessageBox(0, '2019930_' + str(self.num), 'date', 2)

def class_creat_thread():
    my_ = []
    for i in range(5):
        t = mythread(i)
        t.start()
        my_.append(t)
        # t.join() 顺序
    for t in my_:
        t.join()  #主进程等待子进程执行完
'''
第三种:
'''
def creat_thread():
    t = threading.Thread(target=show,args=(1,)).start()
    t = threading.Thread(target=show, args=(2,)).start()
    t = threading.Thread(target=show, args=(3,)).start()
    t = threading.Thread(target=show, args=(4,)).start()

if __name__ == '__main__':
    # fun_creat_thread()
    class_creat_thread()
    # creat_thread()
    # while True:
    #     pass