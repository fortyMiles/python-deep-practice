from threading import Thread
from time import sleep


def printer():
    for i in range(3):
        sleep(0.1)
        print(i, end=' ')


thr = Thread(target=printer, daemon=True)
thr.start()
print('hello')
thr.join()
