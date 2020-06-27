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
#In built List  methods
#Append() This method adds an object into an existing list
list1=["C++","Python","Java"]
print(list1)
list1.append("C#")
print(list1)
#count()
aList=[123,"xyz","zara","abc",123]
print(aList.count(123))
#extends()
#It appends a list on  another list
myList=["Physics","Mathematics","Chemistry"]
print(myList)
newList=list(range(10))
print(newList)
newList=[1,2,3,4,5,6]
myList.extend(newList)
print(myList)
#index()
myList=["Python","C#","Java","C++"]
print(myList)
myList.insert(2,"Cobol")
print(myList)
newSub=["Mathematics","Biology","Chemistry","Physics","English"]
print(newSub)
newSub.pop(-1)
print(newSub)
newSub.append("Kiswahili")
print(newSub)
newSub.remove("Kiswahili")
print(newSub)
#Reverse
newSub.reverse()
print(newSub)
myList=["C++","Java","Python","Cobol"]
print(myList)
myList.sort()
print(myList)
myList.sort(reverse=True)
print(myList)



































