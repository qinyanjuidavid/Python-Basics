#228
if __name__=="__main__":
    a=5
    if 1<=a<=20:
        for num in range(a):
            print(num**2)
def is_leap(year):
    leap=False
    if 1900<=year<=10**5:
        if year%4==0:
            if year%100==0:
                if year%400==0:
                    print(True)
                else:
                    print(False)
            else:
                print(True)
        else:
            print(False)
    return leap
is_leap(year=2000)
#Python Files I/o
#Upening Files
fo=open("python.txt","wb")
print("Name of the file",fo.name)
print("Closed or not",fo.closed)
print("Opening Mode:",fo.mode)
fo.close()
#Trial
LazyClass=open("LazyClass.txt","wb")
print("Name of the opened text File",LazyClass.name)
print("Closed or Not closed:",LazyClass.closed)
print("I know the mode is WB, But let me check-->",LazyClass.mode)
LazyClass.close()
print("Closed or Not Closed-->",LazyClass.closed)
#If a File is closed no more writing can be done
#Python automatically closes the file when the file object is assigned to another file or when close() func is called
fo=open("fo.txt","wb")
print("Name of the file:",fo.name)
fo.close()
#Reading and Writing Files
#Write() method-->The write method writes wtrings to an open file
python=open("python.txt","wb")
print(f"Name: {python.name}")
print(f"Mode: {python.mode}")
print(f"Closed and Not Closed: {python.closed}")
python=open("python1.txt","w")
python.write("Python is a great language.\nYeah! It is a great language.")
python.close()
#Trial
trial=open("day.txt","w")
trial.write("""My name is Day Qinyanjui.
I am 23 years old.
I Love coding.""")
trial.close()
#input
trial=open("trial.txt","w")
# name=input("Enter your Name: ")
name="Day"
age=23
school="TTU"
# age=input("Enter your Age: ")
# school=input("Enter your school: ")
trial.write(f"""{name}
{age}
{school}
""")
trial.close()
#Multiplication Table
mult=open("multiplicationTable.txt","w")
mult.write("\t\tMultiplication Table.\n")
for i in range(1,12):
    for j in range(1,12):
#         print(f"{i}*{j}= {i*j}")
        mult.write(f"""{i}*{j}= {i*j}\n""")
    mult.write("""\n""")
#     print()S
mult.close()
#Pattern
pat=open("Pattern.txt","w")
pat.write("\t\tPattern\n")
for i in range(10):
    for j in range(i,10):
        print("*",end="")
        pat.write(f"{j}")
    print()
pat.close()
#The read() method
#The read method reads a string from an open file
top=open("top.txt","w")
name="Day Qinyanjui"
age=23
hobby="Dancing"
top.write(f"""{name}
{age}
{hobby}""")
top.close()
top=open("top.txt","r+")
details=top.read()#read accepts a slicing parameter
print(details)
top.close()
#Division Table
div=open("division.txt","w")
div.write("\t\tDivision Table.\n")
for i in range(1,12):
    for j in range(1,12):
        division=round(i/j,2)
        div.write(f"""{i} / {j} = {division}\n""")
    div.write("\n")  
div.close()
div=open("division.txt","r+")
details=div.read()
print(details)
div.close()
#File positions
pos=open("position.txt","w")
pos.write("Python is a great language,It was created by Guido van Roussum")
pos.close()
# pos=open("position.txt","r+")
# print(pos.read())
# check=pos.tell()#It returns the length of the file
# print(check)
# # check=pos.seek(0)
# pos=pos.read()
# # print(check)
# pos.close()
#Renaming Files
Test=open("test.txt","w")
Test.write("This is for renaming files")
Test.close()
import os
try:
    os.rename("test.txt","test2.txt")
except:
    print("File already renamed")
#Deleting Files
delTest=open("delTest.txt","w")
delTest.write("This file was deleted")
delTest.close()
import os
os.remove("delTest.txt")




























































