#mkdir() method
import os
try:
    os.mkdir("FilesIO")
except:
    print("This directory already exists")
#Chdir used for changing Directory
os.chdir("/Users/david/PycharmProjects/Mastering/")
#Gettign The Current Working Directory cwd
print(os.getcwd())
os.chdir("/Users/david/PycharmProjects/Mastering/FilesIO/")
print(os.getcwd())
try:
    os.mkdir("Test1")
except:
    print("Directory already exists")
#rmdir() this method is used to delete the directories
try:
    os.rmdir("Test1")
except:
    print("The directory was printed")
#Files And Directory Related methods
#file close() method
#This method closes an opened file
#A closed File cannot be read or written any more
print(os.getcwd())
test=open("test.txt","w")
test.write("This is Show casing the python close method")
test.close()
#File Flush method
test1=open("test1.txt","w")
test1.write("This is for show casing the flush method")
print(test1.name)
print(test1.mode)
print(test1.closed)
test1.flush()
test1.close()
test1=open("test1.txt","w")
test1.write("I love Python")
print(test1.tell())
print(test1.fileno())
test1.close()
test2=open("test2.txt","w")
test2.write("I am using this to showcase the fileno method.")
test2.fileno()
test2.close()
file1=open("file1.txt","w")
file1.write("Show casing the read method")
file1.close()
fileRead=open("file1.txt","r+")
line=fileRead.read()
print(line)
fileRead.close()
#256
#Python FilesIo methods





















