# ================================================================================================
# Lambda
# Syntax: Function name= lambda input parameter: return value
# it takes input and return the single output as a variable and act as function

add=lambda a,b: a+b
a=add(2,3)
print(a)

mul=lambda a,b: a*b
b=mul(2,3)
print(b)

is_even=lambda a:a%2==0
c=is_even(2)
print(c)

rev_string=lambda a:a[::-1]
d=rev_string("Dhruv")
print(d)

# ================================================================================================
# Map
# Basic Syntaxx: Function name=map(funtion,list) --> It returns the object for list write this advanced syntax
# Advanced Syntax: Function name= list(map(lambda input parameter: return value))
# it takes input and return the single output as a variable and act as function

list1=[1,2,3,4]
list2=["Dhruv","Niv","Parshad","Hardik"]
print(list(map(lambda a:a**2,list1)))
print(list(map(len,list2)))

# ================================================================================================
# Filter
# Syntax is same as map
# Filter do the filter of input in given function
list1=[1,2,3,4]
print(list(filter(lambda a:a%2!=0,list1)))

# ================================================================================================
# Reduce
# reduce take one element at time from the list and apply the function on that element after that take group of next elements and compare or do operations
from functools import reduce
li=[1,2,3]
sum = reduce((lambda x,y:x*x+y*y),li)
print(sum)

f=lambda a,b: a if(a>b) else b
r = reduce(f, [47,111,42,102,13])
print(r)


