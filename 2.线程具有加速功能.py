import time
import _thread

def go():
    for i in range(10):
        print('%d --- '%i)
        time.sleep(1)


if __name__ == '__main__':
    # for i in range(5): #要运行50s 只能顺序执行 等很久才能到end
    #     go()
    for i in range(5):  #很快就到end了
        _thread.start_new_thread(go,())
    for i  in range(10): #10s差不多就执行完了
        time.sleep(1)

    print('end')