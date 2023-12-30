#comments

# types

# single line

"""
    multi
            line
                    comment
"""

"""
block of code

    |
    |
    |
    
    IF CONDITION
        |
        |
        |
        
PYTHON IS "SPACE" SENSITIVE
PYTHON IS ALSO "CAESSENSITIVE"

"""


# DATATYPES

# 8 Types

nonetype = None

#integertypes

intergers = 12

floating  = 12.0

stringsingle = 'a' # use for single charactors

stringmultiple = "ram"


stringpara = """

    para graph
    
"""

#complex numbers

complex = 5 + 6j

#list
listnumbers = []

listnumbers = [floating,nonetype,stringmultiple,intergers]

print(listnumbers)

#tuples # immutable
tuplet =(floating,nonetype,stringmultiple,intergers)
print(tuplet)

#using class contructor
tuplet = tuple(listnumbers)
print(tuplet)

#set no duplicates

sets = {}
sets = set(listnumbers)
print(sets)

set = {1,1,2,"ram","ram"}
print(set)


#dictionary

dictionary = {1:"ram",2:"sita"}

print(dictionary)
print(dictionary.keys())
print(dictionary.values())
print(dictionary[1])

