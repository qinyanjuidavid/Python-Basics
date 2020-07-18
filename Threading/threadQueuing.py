import queue
import threading
import time

 class myThread(threading.Thread):
     def __init__(self,threadID,name,q):
         threading.Thread.__init__(self)
         self.threadID=threadID
         self.name=name
         self.q=q
    def run(self):
        print(f"Starting {self.name}")
        process_data(self.name,self.q)
        print(f"Ex