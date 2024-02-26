#print(8/0)

"""
try:
statements

raise calsserror

except typesclasserror e:
 print(e)
 
 finally:
 statemetns


"""

try:
    result = 8/10
    print(result)
# except Exception : #super class
#     print("error")
except ArithmeticError :
    print("arth error")
finally:
    print(" i allwas run")


class myexception (Exception):
    def __init__(self,message):
        self.msg = message
    def __str__(self):
        return "myexception {0}".format(self.msg)
try:
    raise myexception("oops")
finally:
    print("ok")

