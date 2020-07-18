import _thread
import time
import os
try:
    os.mkdir("Threading")
except:
    print("Directory already created")
else:
    print("Python is awesome")
os.chdir("/Users/david/PycharmProjects/Mastering/Threading/")
def printTime(threadName,delay):
    count=0
    while count<5:
        time.sleep(delay)
        count+=1
        print(f"{threadName} {time.ctime(time.time())}")
try:
    if __name__=="__main__":
        _thread.start_new_thread(printTime,("Thread1",2))
        _thread.start_new_thread(printTime,("thread2",4))
except:
    print("Error: Unable to start thread")
while 1:
    pass
#Multiplication Table
import _thread
import time
class Table:
    def __init__(self,delay):
        self.delay=delay
    def Multiply(self):
        for i in range(1,12):
            for j in range(1,12):
                time.sleep(self.delay)
                print(f"{i}*{j}= {i*j}",end="\n")
            print("\n")
if __name__=="__main__":
    table1=Table(2)
    _thread.start_new_thread(table1.Multiply())
    
        