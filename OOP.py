import os
print(os.getcwd())
#Object Oriented rises due to the use of objects and classes
#Creating Classes
class Employee:
    empCount=0
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        Employee.empCount+=1
    def displayCount(self):
        print(f"Total employee: {Employee.empCount}")
    def displayEmployee(self):
        print(f"Name: {self.name}.\nSalary: {self.salary}")
if __name__=="__main__":
    day=Employee("Day",600000)
    day.displayEmployee()
    day.displayCount()
#Trial Creating student
print("==="*100)
class BBIT3:
    student=0
    def __init__(self,name,age):
        self.name=name
        self.age=age
        BBIT3.student+=1
    def displayNumberOfStudents(self):
        print(f"Number of Students: {BBIT3.student}")
    def displayDetails(self):
        print(f"Name: {self.name}.\n{self.age}")
if __name__=="__main__":
    kin=BBIT3("David",23)
    kin.displayNumberOfStudents()
    kin.displayDetails()
    stu=BBIT3("John Doe",32)
    stu.displayNumberOfStudents()
    stu.displayDetails()
#Trial III
class codeRun:
    employee=0
    def __init__(self,name,department):
        self.name=name
        self.department=department
        codeRun.employee+=1
    def numberOfEmployees(self):
        print(f"Number Of Employees: {codeRun.employee}")
    def displayInfor(self):
        print(f"Name: {self.name}.\nDepartment: {self.department}")
        
    
if __name__=="__main__":
    emp1=codeRun("John Doe","IT Department")
    emp1.numberOfEmployees()
    emp1.displayInfor()
    emp2=codeRun("Jane Doe","Sales Department")
    emp2.numberOfEmployees()
    emp2.displayInfor()
    emp3=codeRun("Day Qinyanjui","Marketing Department")
    emp3.numberOfEmployees()
    emp3.displayInfor()
    del emp3.department
    try:
        print(emp3.department)
        print(emp3.name)
    except:
        print(f"Department was deleted {emp3.name}")
#Built in Class Attributes

class Employee:
    """Checking on the in build class attributes."""
    empCount=0
    def __init__(self,name,age):
        self.name=name
        self.age=age
        Employee.empCount+=1
    def displayCount(self):
        print(f"Total Employee {Employee.empCount}")
    def displayEmployee(self):
        print(f"Name: {self.name}.\nAge: {self.age}")
if __name__=="__main__":
    emp1=Employee("John Doe",36)
    emp1.displayCount()
    emp1.displayEmployee()
    print(f"Employee. __doc__: {Employee.__doc__}",)
    print(f"Employee.__name__: {Employee.__name__}")
    print(f"Employee.__module__:{Employee.__module__}")
    print(f"Employee.__bases__:{Employee.__bases__}")
    print(f"Employee.__dict__:{Employee.__dict__}")
#Destroying Objects(Garbage Collection)
class Point:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
    def __del__(self):
        class_name=self.__class__.__name__
        print(class_name,"Destroyed")
if __name__=="__main__":
    pt1=Point()
    pt2=pt1
    pt3=pt1
    print(id(pt1),id(pt2),id(pt3))
    del pt1
    del pt2
    del pt3
#Class Inheritance
#Normally the child class inherits the attributes of its parent class
class Parent:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def displayDetails(self):
        print(f"Name: {self.name}\nAge: {self.age}")
if __name__=="__main__":
    emp1=Parent("day",23)
    emp1.displayDetails()
class Child(Parent):
    def __init__(self,name,age,salary,department):
        Parent.__init__(self,name,age)
        self.salary=salary
        self.department=department
    def displayInfor(self):
        print(f"Salary: {self.salary}\nDepartment: {self.department}")
if __name__=="__main__":
    inf1=Child("Day",23,20000,"IT")
    inf1.displayInfor()
    inf1.displayDetails()
#Class Inheritance Trial I
class Employee:
    def __init__(self,name,age,department,salary):
        self.name=name
        self.age=age
        self.department=department
        self.salary=salary
    def employeeDetails(self):
        print(f"Name: {self.name}.\nAge: {self.age}\nDepartment: {self.department}")
class Salary(Employee):
    def __init__(self,taxRate,commision,name,age,department,salary):
        Employee.__init__(self,name,age,department,salary)
        self.taxRate=taxRate
        self.commision=commision
    def SalaryDetails(self):
        taxableIncome=self.salary+self.commision
        tax=taxableIncome*self.taxRate
        totalSalary=self.salary-tax
        print(f"Name: {self.name}\nAge: {self.age}\nDepartment: {self.department}\nTaxable Income:{taxableIncome}\nTax: {tax}\nSalary:{totalSalary}\n")
        
if __name__=="__main__":
    emp1=Salary(0.04,5000,"John Doe",35,"IT Department",320000)
    emp1.SalaryDetails()
    emp2=Salary(0.04,6000,"Jane Doe",32,"Sales Department",109000)
#Trial
class Measurements:
    def __init__(self,length,width,height):
        self.length=length
        self.height=height
        self.width=width
    def displayMeasurements(self):
        print(self.length,self.width,self.height)
if __name__=="__main__":
    meas1=Measurements(20,10,30)
#     meas1.displayMeasurements()
    
class Volume:
    def __init__(self,length,width,height):
        Measurements.__init__(self, length,width,height)
    def findVolume(self):
        volume=self.length*self.width*self.height
        print(volume)
        print(Measurements.displayMeasurements(self))
if __name__=="__main__":
    vol1=Volume(20,10,30)
    vol1.findVolume()
        
#Data Hiding __variable (Encapsulation)
class Employee:
    __empCount=0
    def __init__(self,name,age):
        self.name=name
        self.age=age
        Employee.__empCount+=1
    def employeeDetails(self):
        print(f"Employee: {Employee.__empCount}\nName: {self.name}\nAge: {self.age}")
if __name__=="__main__":
    emp1=Employee("John Doe",32)
    emp1.employeeDetails()
    emp2=Employee("Jane Doe",35)
    emp2.employeeDetails()
class Measurements:
    def __init__(self,length,width,height):
        self.length=length
        self.width=width
        self.height=height
    def displayMeasurements(self):
        print(f"Length: {self.length}\nWidth: {self.width}\nHeight: {self.height}")
    def Volume(self):
        __volume=self.length*self.width*self.height
        print(f"Volume: {__volume}")

if __name__=="__main__":
    meas1=Measurements(20,10,30)
    meas1.displayMeasurements()
    meas1.Volume()
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    























    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    