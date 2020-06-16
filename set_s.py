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