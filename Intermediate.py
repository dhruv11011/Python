# Conditions:
age=input("Enter Your Age")
if(age==18):
    print("You are 18 years old")
elif(age>19):
    pass
else:
    print("Your age is not valid")


# "In" Keyword in Python

name="Dhruv"
msg="My Name is dhruv"
if name in msg:
    print("Your Name is In Message.")
else:
    pass

# While looop

i=0
while(i<5):
    print(i+1)
    i=i+1
    
# ============================================================================
a=int(input("Enter Any Number Between 0-5 : "))

# match case is for python 10 update
match a:
    case 1:
        print("1")
    case 2:
        print("2")
    case 3:
        print("3")
    case 4:
        print("4")
    case 5:
        print("5")
    case 6:
        print("6")
# ============================================================================
#Dictionary is mutable thing
a={}# Empty set is Dictionary
b=set()# Empty set is represent like set()
print(a,type(a))
print(b,type(b))

subject={"maths": "21BCP132","science": "21BCP133","English": "21BCP136","All Subjects":"21BCP137"}

print(subject["maths"])
print(subject.get("All subject"))#using this if there is no match in dictionary then not give error above line is giving an error
print(subject.values())
print(subject.items())
subject.update({"C language": "21BCP128"})
print(subject)

# ============================================================================
#Write The Diffenrence Between List and Tuple

#For storing different types of values in list
l1 =[3,4,5,2,1,"Dhruv"]
l2 =[39,41,53,22,11]

print(type(l1))
print(l1)
print(l1.append(2))
print(l1.pop())
# print(l1.sort())
print(l1.remove(4))
print(l1.count(3))
print(l1)
print(type(l2))
print(l2)
print(l2.append(21))
print(l2.pop())
print(l2.sort())
print(l2)
l2[4]=90
print(l2)
print(l2.remove(41))
print(l2.count(3))
print(l2)

#This is for Tuple
t=(3,4,4,51,9)

# Tuple is immutable list which can not be change furture

print(t.count(4))
print(t)
# t[4]=90
# print(t)

# ============================================================================
# Sets
x={1,2,2,23,1,2}
y={23,12,1,0,2,7}
print(x.pop())#remove random element and show that removed element
print(x)
x.clear()
print(x)#empty set remaining
print(y)
print(x.intersection(y))

# ============================================================================

# To Convert List To String

list=["Dhruv","Parshad","hardik","Kirtan","Niv"]

print(",".join(list))
print(list)

# We use this for CSV export