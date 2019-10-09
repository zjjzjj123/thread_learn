import threading
import time

sem = threading.Semaphore(2) #限制线程存在的数量

def gothread():
    with sem:
        for i in range(10):
            print(threading.current_thread().name)
            time.sleep(1)

for i in range(5): #虽然开启5个线程 但是由于限制了线程的数量 所以只能执行两个
    threading.Thread(target=gothread).start()
