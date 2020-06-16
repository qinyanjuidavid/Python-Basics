import fractions
a_list=['a','b','mpilgrim','z','example']
print(a_list)
print(a_list[0])
print(a_list[-1])
print(a_list[4])
print(a_list[-3])
#Slicing a list
print(a_list)
print(a_list[1:3])
print(a_list[0:-1])
print(a_list[:])
#Adding Items to a list
a_list=['a']
a_list=a_list+[2.0,3]#String Concatination
print(a_list)
a_list.append(fractions.Fraction(2,2))
print(a_list)
a_list.append(True)
print(a_list)
a_list.extend([False,"Five"])
print(a_list)
a_list.insert(0,'First_num')
print(a_list)
#Close Look
new_list=['a','b','c']
print(new_list)
new_list1=['d','e','f']
new_list.extend(new_list1)
print(new_list)
print(len(new_list))
print(len(a_list))
new_list.insert(0,True)
print(new_list)
new_list.append('g')
print(new_list)
print(new_list[-1])
try_list=['h','i','j']
new_list.append(try_list)
print(new_list)
print(new_list[-1])
print(new_list[-1][-1])
try_list2=[1,2,3]
new_list[-1].append(try_list2)
print(new_list)
#Searching For Values In a list
a_list=['a','b','new','mpilgrim','new']