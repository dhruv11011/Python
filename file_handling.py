# readfile
# open function
# read method
# seek method
# tell method
# readline method
# readlines method
# close method
# write method
# .split(",") --> Split by ","

f=open("1.txt")
print(f.tell())
print(f.read())
print(f.tell())
f.seek(0) # For Changing the position at index 0
print(f.tell())
print(f.read())
print(f.readline(),end="") # read on line Aa New Line Create Kare to end="" thi e remove thai jai
print(f.readlines(),end="") # read entire document Aa New Line Create Kare to end="" thi e remove thai jai
list=f.readlines()
for line in list:
    print(line,end="")
f.close()

with open("1.txt","r") as f:
    c=f.readlines()
    print(",".join(c)) # For Convert from list to csv format
