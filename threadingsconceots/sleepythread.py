from threading import Thread
import time


def timenow(name, sec):
    while True:
        time.sleep(sec)
        print(time.ctime(time.time()), name)

t1 = Thread(target=timenow,args= ("t1",5,))
t1.start()
