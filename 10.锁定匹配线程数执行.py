'''
指定数量的线程再执行
'''
import threading
import time

#为了合理利用资源 必须3个一起执行
bar = threading.Barrier(3) #此时是只有匹配够两个线程才能执行

def serve():
    print(threading.current_thread().name,'start')
    bar.wait()
    time.sleep(5)
    print(threading.current_thread().name,'end')

for i in range(5):
    threading.Thread(target=serve).start()

