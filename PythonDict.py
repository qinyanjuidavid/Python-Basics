#Dictionaries are just key value elements
dict={
    "Name":"Day",
    "Age":23,
    "Class":"Lazy Class",
    "Hobby":"Watching"
    }
print(dict["Name"])
print(dict["Age"])
print(dict["Class"])
print(dict.get("Hobby"))
#Updating Dictionary
dict["Hobby"]="Doing Nothing"
print(dict)
del dict["Hobby"]
print(dict)
dict.pop("Age")
print(dict)
#In a Dictionary the last element always wins,ie on duplication
dict={
    "Name":"Day",
    "Age":23,
    "Name":"Qinyanjui"#This one won
    }
print(dict)
#Built in Dictionary Functions
dict={
    "Name":"David",
    "Age":23,
    "Class":"Lazy Class"
    }
print(dict)
#Copy
print(dict.copy())
print(dict.keys())
print(dict.values())
print(dict.items())
print(dict.get("Name"))
dict2={
    "Hobby":"Doing Nothing",
    "Talent":"Sleeping"
    }
dict.update(dict2)#Updating an existing Dictionary,ie by adding more values
print(dict)


















