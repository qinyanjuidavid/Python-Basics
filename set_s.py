#A set is an ordered bag of unique values
a_set={1,2}
print(a_set)
print(type(a_set))
a_list=["a","b","mpilgrim",True,False,42,"a"]
a_set=set(a_list)
print(a_set)
a_set.add("New")
print(a_set)
print(len(a_set))
#Modifying a set
a_set1={1,2}
a_set1.add(4)
print(a_set1)
a_set1.add(3)
print(a_set1)
a_set1.add(3)
# a_set1.add({'a','b'})Takes only one argument
print(a_set1)
a_set2={1,2,3}
print(a_set2)
a_set2.update({2,6,10})

print(a_set2)
a_set2.update({3,4,6},{1,2,3,5,8})
print(a_set2)
a_set2.update([1,5,10,15])
print(a_set2)
#Removing Items From a set
a_set={'a',"b","c","d","e"}
print(a_set)
a_set.discard("e")
print(a_set)
a_set.discard("e")
print(a_set)
a_set.add("z")
print(a_set)
import fractions
a_set.update({"k","l","M","n",fractions.Fraction(2,3)})
print(a_set)
a_set.remove("l")
print(a_set)
a_set.remove(fractions.Fraction(2,3))
print(a_set)
try:
    pass
    # a_set.remove(21) Trying to remove a value that does not exsist raise an error
except ValueError:
    print(a_set)
a_set.pop()
print(a_set)
# Common set operations
a_set={2,4,5,6,7 ,8,9}
print(a_set)
print(2 in a_set)
a_setb={2,8,7,9,10,"C"}
print(a_set.union(a_setb))
print(a_set.intersection(a_setb))
print(a_set.difference(a_setb))
print(a_set.symmetric_difference(a_setb))







