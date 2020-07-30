import threading
import time

def dance():
    for i in range(5):
        print("学习")
        time.sleep(1)

def sing():
    for i in  range(5):
        print("休息")
        time.sleep(1)


t1 = threading.Thread(target=dance)
t1.start()

t2 = threading.Thread(target=sing)
t2.start()

for i in range(7):
    print(threading.enumerate())
    time.sleep(1)