import threading
import time

class mythread(threading.Thread):
    def __init__(self,id,name,i):
        threading.Thread.__init__(self)
        self.id = id
        self.name = name
        self.i = i

    def timenow(self,name, sec):
        while True:
            time.sleep(sec)
            print(time.ctime(time.time()), name)
    def run(self):
        print("threasd has started")
        self.timenow(self.id,self.i)

t1 = mythread(1,"t1",1)
t2 = mythread(2,"t2",1)
t3 = mythread(3,"t3",1)

t1.start()
t2.start()
t3.start()

