#Exception
import os
print(os.getcwd())
os.chdir("/Users/david/PycharmProjects/Mastering/FilesIO/")
try:
    Exception=open("exception Handling.txt","w")
    Exception.write("This File is meant for testing Exception Handling in my code")
except:
    print("The File is already opened")
else:
    print("Content written successfully")
    Exception.close()
#Example II
try:
    Exception=open("exception Handling.txt","r+")
    p=Exception.read()
    print(p)
except:
    print("Could not Find The file specified")
    
else:
    print("File was successfully Read")
    Exception.close()
#Example III
try:
    fh=open("testIII.txt","w")
    fh.write("This file is meant to test the finally exception handling tactic")
finally:
    print("Cant create the file")
    fh.close()
#Raising an exception
def FunctionName(level):
    if level<1:
        raise Exception(level)
    print(level)
    return level
if __name__=="__main__":
    try:
        FunctionName(10)
        FunctionName(1)
#         FunctionName(-100)This line results to an error
    except Exception as e:
        print("Error in the argument")






















