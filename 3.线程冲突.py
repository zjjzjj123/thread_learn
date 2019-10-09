import time
import _thread

'''
同时访问一个资源的时候会发生线程冲突
'''
num = 0
def add():
    global num  #引用外部的变量
    for i in range(1000000):
        num+=1
    print(num)
'''
for i in range(5): #顺序执行 有序输出
    add()
'''


#使用线程，同时访问num这个资源 这个变量
for i in range(5):
    _thread.start_new_thread(add,()) #就会出现错乱的地方
while True:
    pass


#使用类定义解决冲突
'''
num = 0

class my_thread(threading.Thread):
    def run(self):
        global num
        for i in range(1000000):
            num += 1
        print('num:', num)

for i in range(5):
    t = my_thread()
    t.start()
    t.join()

while True:
    pass
'''





