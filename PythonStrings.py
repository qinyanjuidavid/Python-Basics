var1="Hello World!"
var2="Monty Python The Flying circus"
print(var1)
print(var2)
print(var1[0])
print(var1[3:9])
print(var1[-1])
# Updating Strings
print(var1+var2,sep=",")
var1=var1[:6]+"Python"
print(var1)
print("""
This is a long string
that is made up of several lines ,
1.This is line one
""")
#Raw Strings
print(r"c:\\This is a raw string\n")
print(r"c:\\Everything will actually look simiral\t")
#String Methods
#Capitilize Function
myStr="this is a python string..."
print(myStr.capitalize())
myStr="this is a string example...wow!"
print(myStr.count("i"))
import base64
myStr="This is an encoded string"
myStr=base64.b64encode(myStr.encode("utf-8","strict"))
print(myStr)
import base64
name="Day Qinyanjui"
name=base64.b64encode(name.encode("utf-",errors="strict"))
print(name)
import base64
lang="Python"
lang=base64.b64encode(lang.encode("utf-8",errors="strict"))
print(lang)
mydict="name Day"

mydict=base64.b64encode(mydict.encode("utf-8",errors="strict"))
print(mydict)
mydict=mydict.decode(encoding="utf-8",errors="strict")
print(mydict)
#Endswith
name="Qinyanjui Day"
print(name.endswith("Day"))
#Finds
print(name.find("D"))
myStr="This is a string example...woow!"
print(myStr.find("exam"))
#index
name="Guido Van Roussum"
print(name.index("V"))
hobby="I love coding"
print(hobby.index("coding"))
# Alphanumeric isalnum()
#This Function Returns true if all the letters are alphanumeric
myStr="tom and jerry was the best cartoon in 2000s"
print(myStr.isalnum())
name="th2eaoiu0"#Spaces and panctuations brings our results to False
print(name.isalnum())
#isalpha Checks whether the string consists of alphabetic characters only
myStr="I like been alone"#Spaces and digits result to 0/false
print(myStr.isalpha())
newStr="AfK"
print(newStr.isalpha())
# isdigit
#This inbuilt function checks whether the string consists of digits only
newStr="Away From Keyboard"
print(newStr.isdigit())#Has No Digit
num="123"
print(num.isdigit())
#islower()
#Checks whether all the letters in a string are lowercase
myStr="this string is in lower case"
print(myStr.islower())
newStr="THIS STRING IS UPPER CASE"
print(newStr.islower())
#isupper()
#Checks whether all the letter in a string are upper cased"
print(myStr.isupper())
print(newStr.isupper())
#isnumeric()
#It checks whether the string is made of numerical characters
numStr="123564"
print(numStr.isnumeric())
newStr="I Dont know what is my talent"
print(newStr.isnumeric())#Incase of letters
#isspace
#This function checks whether the string consists of whitespce
name="I am Day Qinyanjui"
print(name.isspace())#Incase of Strings it returns False
mySpace="       "
print(mySpace.isspace())
#isTitle
myTitle="This Is A Title"
print(myTitle.istitle())
myStr="This is a simple string"
print(myStr.istitle())
#join()
myStr=("I","Am","Diving","into","Python")
seq="%"
print(seq.join(myStr))
start="254"
# phone=eval(input("Enter Phone number"))
phone="0700215667"
print(start.join(phone))
#len()
myStr="this is a string example...wow!"
print(len(myStr))
#lower()
myStr="I love printing"
print(myStr.lower())
#upper()
myStr.upper()
print(myStr)
#lstrip
#The stripped letters are at the bigging
myStr="     this is a string example"
print(myStr.	lstrip())
myHash="########This is my hash #####"
print(myHash.lstrip("#"))
# max() returns the maximum alphabet
myStr="lfjejz"
print(max(myStr))
#min() Returns the minimum alphabet
print(min(myStr))
name="David Qinyanjui"
print(name.replace("David","Day"))
name=name+" Njau"
print(name)
#split()
myStr="this is my string example"
print(myStr.split("i",1))
#isdecimal()
#this in built function checks whether the string consists of decimals characters only
myStr="That is not your name"
print(myStr.isdecimal())
newStr="1256"
print(newStr.isdecimal())











































































