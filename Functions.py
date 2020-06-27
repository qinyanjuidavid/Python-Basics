def PrintMe(str):
    """This simply
prints a passed string"""
    print(str)
    return
if __name__=="__main__":
    PrintMe("This is my first line")
    PrintMe("This is my second line")

def ChangeMe(mylist):
    """
This changes a passed list"""
    mylist[2]=50
    print(mylist)
    return
if __name__=="__main__":
    ChangeMe([1,2,3,4])

def printMe(str):
    """This prints a simple function"""
    print(str)
if __name__=="__main__":
    printMe(str="My name is Day Qinyanjui")

def printInfo(name,age):
    """Prints the infor"""
    print(f"Name: {name}")
    print(f"Age: {age}")
    
if __name__=="__main__":
    printInfo(name="Day",age=23)
    printInfo(name="Micheal",age=16)
#Default Arguments Functions
def printInfo(name,age=35):
    """Prints the
infor passed on this function"""
    print(f"Name: {name}")
    print(f"Age: {age}")
if __name__=="__main__":
    printInfo(name="Day")
#Args For more arguments
def FunctionName(*args):
    """Prints the info entered on this function as arguments"""
    for arg1 in args:
        print(arg1)
    
if __name__=="__main__":
    FunctionName("BBIT","year 3")
    FunctionName("IT","year 2")
#The Anonymous Functions
#lambda Function
sum=lambda num1,num2:num1+num2
print(sum(20,40))
print(sum(100,200))
multiplication=lambda num1,num2:num1*num2
print(multiplication(20,2))
divide=lambda num1,num2:num1/num2
print(divide(20,3))
Sub=lambda num1,num2:num1-num2
print(Sub(10,3))
#Return Statement
def Sum(arg1,arg2):
    total=arg1+arg2
    print(total)
    return total
if __name__=="__main__":
    Sum(20,30)

def Sub():
    num1,num2=10,20
    total=num1+num2
    print(total)
    return total
if __name__=="__main__":
    Sub()
#Global Variable   
total=0#Global
def sum(arg1,arg2):
    total=arg1+arg2#Local
    print(total)
    return total
sum(10,300)
print(total)

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    



















    
    
    
    
    
    
    
    
    
    
    
    
    
    