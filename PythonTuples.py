#Tuples are immutable
tup1=("Physics","chemistry",1997,2000)
print(tup1)
print(type(tup1))
tup1=(25,)
print(type(tup1))
tup2=("Physics","Chemistry","Mathematics",1997,2000)
print(tup2[0])
print(tup2[-1])
print(tup2[1:5])
#Updating Tuples
tup1=("Java","C++","Python","C#")
tup2=tuple(range(5))
tup3=tup1+tup2#Tuples Support Concatination
print(tup3)
#Deleting Tuples
#Del is used to delete the entire tuple
tup1=tuple(range(10))
del tup1
try:
    print(tup1)
except:
    print("The tuple was Deleted")
#Basic Tuple Operations
tup1=tuple(range(10))
tup2=tuple(range(5))
tup3=tup1+tup2
print(len(tup1))
print(tup3)
print(tup3.count(1))
print(tup3.index(7))
print(max(tup3))
print(min(tup3))






















    
