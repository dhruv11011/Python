# ============================================================================
#Variable name should not be start with number,space

a1="dhruv"
print(a1)

b1="bhatt"
print(a1 +" "+ b1)
c=5

print(a1*c)
# ============================================================================
#Arithmatic Oprator
a=3
b=4
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a**b)
print(a//b)

# ============================================================================
#Assignment oprators
a=5
print(a)
a+=3
print(a)
a-=3
print(a)

# ============================================================================
#Comparision Oprators
#logical Oprators

'''
==
!=
>
<
>=
<=
'''

'''
And
Or
Not
'''

a=10
b=10
c=1

print(a==b)
print(a>=b)
print(a<=b)
print(a!=c)


print(a==10 and a<=b)
print(a==10 or a<b)

# ============================================================================
#membership Oprators

'''
In
Not In
'''

#Identity Oprators
'''
Is use as == equal to
Is Not use as != not equal to
'''

a="Dhruv"
print('d' in a)
print('D' in a) #Python is case sensetive

list=[1,2,3,4,5]
print(1 in list)

a=1
b=2

print(a==b,a is b)
print(a!=b,a is not b)

# ============================================================================
#Bitwise Oprators

'''
& -> And
| -> Or
^ -> Xor
'''

a=10
b=5

print(bin(a)) # Here bin is use for binay Number Printing
print(bin(b)) # Here bin is use for binay Number Printing
print(bin(a&b),(a&b)) # here (a&b) Represent after doing on binary number & (and) opration 
print(bin(a|b),(a|b))
print(bin(a^b),(a^b))

# ============================================================================
# Typecasting

'''
int
float
eval --> best because handle both
'''

name=input("Enter Your Name:")
age=input("Enter Your Age:")
marks=int(input("Enter Your Marks in Advance Python: ")) # int only handle int value
marks1=float(input("Enter Your Marks in Python: ")) # float handle onlyfloat value
marks2=eval(input("Enter Your Marks in Advance Python: ")) # eval handle both float and in value
print(name)
print(age)
print(marks)
print(marks1)
print(marks2)

# ============================================================================
# Conditional Statements

'''
if
else if
else
'''

a=int(input("Enter Your Number:"))
if (a%2==0):
    print(a,'is Even Number')
elif (a%2==1):
    print(a,'is Odd Number')
else:
    print("input valid number")


# ============================================================================
# Loops in python

# range(a) --> start=0, condition<a, increament 1 (Default)
# range(a,b,c) --> start=a, condition<b, increament c

# For Loop

for i in range(1,11,2):
    print(i)

for j in range(1,11):
    print("11 *",j,"=",11*j)

#For Reverse loop (Need to Define 3 Parameters)

for j in range(10,0,-1):
    print("11 *",j,"=",11*j)


# While loop
'''
Syntax:
    Start
    condition
    increament/decreament
'''
i=0
while i<10:
    print("dhruv")
    i=i+1

print(i)

# ============================================================================
# String index and String Slicing

# String index
a="Dhruv is good boy"
print(a[1])
print(a[-1])
print(a[-2])

# String slicing

print(a[0:7]) # --> meaning is from index 0 to 6(<7) string slice
print(a[0::2]) # --> meaning is from index 0 to end with difference (gap) of 2 string slice


# For Reverse String
print(a[::-1])

# ============================================================================
# String Functions

a="Dhruv is Good Boy"
length = len(a)
print(length)

for i in range(length):
    print(a[i])


# Cases of Strings

s="The is a Apple"

up=s.upper()
down=s.lower()
title=s.capitalize()

# ============================================================================
# For Assci Value calculation

# chr() --> This function use for Assci to Normal Alphabet
p=chr(65)
print(p)

# ord() --> This function use for Normal to Assci Charactar
a=ord("a")
print(a)

# ============================================================================
# Declare Multiple Variable in Single Line
name,roll="Dhruv","137"
print(f'{name} has roll no {roll}')

# ============================================================================
# Split Function
fname,lname=input("Enter Your First and Last Name: ").split(" ")
print(f'First Name is {fname} And Last Name is {lname}')

name=input("Enter Your First and Last Name: ").split(" ")
print(name[0])
print(name[1])
# ============================================================================

# ============================================================================
# Typecasting in Python
num = int('256')  # Convert String to Integer
print(type(num))
num2 = float('4.98')   # Convert String to Float
print(type(num2))
num3= int('256')  # Convert String to Integer
c=str(num3)
print(type(c))

Age=int(input("Enter Your Age: "))
print(Age+1)
# ============================================================================

# ============================================================================
# String Indexing Slicing and Methods
"""
B ->0 or -9
l ->1 or -8
a ->2 or -7
c ->3 or -6
k ->4 or -5
e ->5 or -4
y ->6 or -3
e ->7 or -2
s ->8 or -1
"""
name="Blackeyes"
print(name[0])
print(name[-1])

"""
for slicing string
Syntax:[Start index: Stop index+1]
Syntax:[Start index: Stop index+1: step argument]
(how much jump) that called step argument
"""
name="Blackeyes"
print(name[0:5])
print(name[::-1]) # For printing Reverse String

name="Blackeyes"
print(len(name))
print(name.upper())
print(name.lower())
print(name.title())
print(name.split()) # for both side all space remove
# print(name.rsplit()) # for right side all space remove
# print(name.lsplit()) # for left side all space remove
print(name.count("e"))
print(name.replace("eyes","")) # Syntax replce("replace with","replace want",from which index(default 0))
print(name.find("e"))
