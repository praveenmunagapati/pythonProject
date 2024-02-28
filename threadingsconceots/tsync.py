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
            print(time.ctime(time.time()), self.name,self.id,self.i)
    def run(self):
        print("threasd has started")
        threadslock.acquire()
        self.timenow(self.id,self.i)
        threadslock.release()


threadslock = threading.Lock()
threads = []
t1 = mythread(1,"t1",1)
t2 = mythread(2,"t2",1)

t1.start()
t2.start()

threads.append(t1)
threads.append(t2)
for i in threads:
    i.join()
print("bye")
