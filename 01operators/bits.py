"""
bitwise & | ~ ^

"""


a = 10
b = 10

print(bin(a))
print(bin(b))
print(1&1)
print(1&0)
print(0&1)
print(0&0)
print(bin(a&b))

b = 5
print(bin(a))
print(bin(b))
print(bin(a&b))

# | bitwise or
a = 10
b = 10
print(1|1)
print(1|0)
print(0|1)
print(0|0)
print(bin(a))
print(bin(b))
print(bin(a|b))
b = 5
print(bin(a))
print(bin(b))
print(bin(a|b))
print(a|b)

# ^ bitwise xor
a = 10
b = 10
print(1^1)
print(1^0)
print(0^1)
print(0^0)
print(bin(a))
print(bin(b))
print(bin(a^b))
b = 5
print(bin(a))
print(bin(b))
print(bin(a^b))
print(a^b)



#coMplement ~

print(~b)
print(~(~b))


# left shift <<
print(b)
print(bin(b))
print(b<<1)
print(bin(b<<1))


""""
b 5 -> 101  

101<<1 -> 1010

"""

print(b)
print(b<<2)
print(bin(b<<2))


# right shift
# >>  binary varible >> value


c = 40
print(bin(c))

print(c>>2)
print(bin(c>>2).lstrip('-0b'))



# VHF9H-NXBBB-638P6-6JHCY-88JWH




