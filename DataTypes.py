#Python Numbers
var1=1
var2=10
print(var1,var2,sep="\n")
del var1
# print(var1)
print(var2)
# Complex Numbers
num1=3+4j
print(num1)
print(type(num1))
num2=56e+56j
print(num2)
print(type(num2))
#J and E are used in complex numbers
#Python Strings
myStr="Hello World"
print(myStr)
print(type(myStr))
# Slicing
print(myStr[0])
print(myStr[1])
print(myStr[2:5])
print(myStr[-1])
print(myStr*3,end=". ")
print(myStr+"Test")
# Python Lists
mylist=["abcd",789,2.23,"John",70.2]
print(mylist)
print(mylist[0])
print(mylist[2:])
print(mylist[1:3])
newlist=["This","is","new","list"]
print(newlist)
print(newlist+mylist)
# Python Tuples
tuple=("abcd",789,2.3,"john Doe",70.2)
print(tuple)
print(tuple[0])
print(tuple[1:3])
print(len(tuple))
print(tuple[2:])
print(tuple[-1])
# Python Dictionary
dict={}
print(dict)
mydict={
    'name':"John Doe",
    "code":7798,
    "dept":"IT Department"
    }
print(mydict)
print(mydict.keys())
print(mydict.items())
print(mydict.values())
print(mydict["name"])
print(f"Name: {mydict['name']}\nCode: {mydict['code']}\nDept: {mydict['dept']}")








