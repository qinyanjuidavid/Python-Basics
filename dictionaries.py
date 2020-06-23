# A dictionary is unordered set of key-value pairs.
a_dict={
    "server":"local host",
    "database":"Postgresql"
}
print(a_dict)
print(type(a_dict))
print(a_dict["server"])
print(a_dict['database'])
print(a_dict.items())
print(a_dict.keys())
print(a_dict.values())
# Modifying a dictionary
a_dict["database"]="MySql"
print(a_dict)
a_dict["Super User"]="Day"
print(a_dict)
print(a_dict["Super User"])
suffixes={
    1000:["kb","MB","Gb","Tb","PB","EB","ZB","YB"],
    1024:["KiB","MiB","GiB","TiB","PiB","EiB","ZiB","YiB"]
          }
print(suffixes)
print(1000 in suffixes)
print(suffixes[1000])
print(suffixes[1000][3])
print(len(suffixes[1000]))

# Dictionaries in a Boolean Context
def is_it_true(anything):
    """

    :param anything:
    :return:
    """
    if anything:
        print("yes, it\'s True.")
    else:
        print("No, it\'s False.")
if __name__=="__main__":
    is_it_true({})
    is_it_true({'a':1})
    is_it_true({"0":False})
def DictComprehension():
    """

    :return:
    """
    a_dict={"a":1,"b":2,"c":3}
    print(a_dict.items())
    for key,value in a_dict.items():
        print("Key",key)
        print("value",value)


if __name__=="__main__":
    DictComprehension()