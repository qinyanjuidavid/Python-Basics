import os
print(os.getcwd())
try:
    os.mkdir("TKinter")
except:
    print("Directory already created")
try:
    os.chdir("/Users/david/PycharmProjects/Mastering/Tkinter/")
except:
    print("The current working directory already created")
print(os.getcwd())


