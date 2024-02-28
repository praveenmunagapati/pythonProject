import _thread
import time


#
# def timenow(name,sec):
#     time.sleep(sec)
#     print(time.ctime(time.time()))
#
# # timenow()
# #
# # while True:
# #     for i in range(9000000):
# #         i +=0
# #     timenow()
#
# # timenow()
# #
# # while True:
# #     time.sleep(1)
# #     timenow()
#
# # try:
# #     _thread.start_new_thread(timenow())
# #
# # except Exception:
# #     print("bad happends")
# def timenow(name,sec):
#     time.sleep(sec)
#     print(time.ctime(time.time()),name)
# try:
#         _thread.start_new_thread(timenow,("t1",1,))
#
# except:
#     print("error")
#
#


def timenow(name, sec):
    while True:
        time.sleep(sec)
        print(time.ctime(time.time()), name)


_thread.start_new_thread(timenow,("hi",1))
_thread.start_new_thread(timenow,("bye",1))
_thread.start_new_thread(timenow,("good morning",1))
_thread.start_new_thread(timenow,("h1",1))
_thread.start_new_thread(timenow,("h2",1))
_thread.start_new_thread(timenow,("hi1",1))
_thread.start_new_thread(timenow,("by1e",1))
_thread.start_new_thread(timenow,("go1od morning",1))
_thread.start_new_thread(timenow,("h11",1))
_thread.start_new_thread(timenow,("h12",1))

while True:
    pass

