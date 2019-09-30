import win32api
#多线程就是多个cpu内核同时执行 程序默认是单线程
import threading
import _thread

def show(num):
    win32api.MessageBox(0, 'haha1', 'haha2', 1)
    # for i in range(5):
    #     win32api.MessageBox(0,'haha1','haha2',1) #

'''
1.创建的线程都是主线程
2.整个程序就是主线程
3.主线程结束了之后所有子线程自动结束 17-21行主线程
'''
if __name__ == '__main__':  #有6个出现因为有主线程
    for i in range(5):
        _thread.start_new_thread(show,(1,)) #传递参数时一定要是一个元组要有','
    # show(1)
    while True: #如果没有等待 子线程执行一遍之后就结束了不存在框图停留了 让主线程不死
        pass



#加入线程就可以一次出现6个框

