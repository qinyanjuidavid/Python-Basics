list1=['physics','Chemistry',1997,2000]
print(list1)
print(type(list1))
print(list1[0])
list2=[1,2,3,4,5,6,7,8,9]
print(list2)
print(list2[1:5])
print(list2[-1])
#Updating Lists
myList=["physics","Chemistry",1997,2000]
print(myList)
myList[3]="biology"
print(myList)
myList.append("Mathematics")
print(myList)
lis=[1,2,3,4,5]
print(lis)
del lis
try:
    print(lis)
except:
    print("List not available")
myList.remove(1997)
print(myList)
myList.append("Programming")
print(myList)
myList.pop(-1)
print(myList)
#Basic List Operation
newList=["c++","Java","Python"]
print(newList)
print(len(newList))
print(newList[0])
print(newList[:-1])
print(newList[1:])
#built in List method
#len() Checks the length of the function
list1=["Physics","Chemistry","Biology"]
print(list1)
print(len(list1))
newList=list(range(10))
print(newList)
print(len(newList))
myList=[1,22,56,32,78,56]
print(max(myList))
print(min(myList))
atuple=(123,"C++","Java","Python")
print(type(atuple))
aList=list(atuple)
print(aList)
print(type(aList))




















