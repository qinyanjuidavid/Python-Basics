a=21
b=10
c=0
c=a+b
print(c)
c=a*b
print(c)
c=a-b
print(c)
c=a/b
print(c)
c=a//b
print(c)
c=a%b
print(c)
# Python Comparison Operators
a=21
b=10
if a==b:
    print(f"{a} is equal to {b}.")
else:
    print(f"{a} is not equal to {b}.")

if a!=b:
    print(f"{a} is not equal to {b}.")
else:
    print(f"{a} is equal to {b}.")

if a<b:
    print(f"{a} is less than {b}.")
else:
    print(f"{a} is greater than {b}.")
    
if a>b:
    print(f"{a} is greater than {b}.")
else:
    print(f"{a} is less than {b}.")
if a>=b:
    print(f"{a} is greater or equal to {b}.")
else:
    print(f"{a} is less or equal to {b}.")

if a<=b:
    print(f"{a} is less or equal to {b}.")
else:
    print(f"{a} is greater or equal to {b}.")
#Python Assignment Operators
a=21
b=10
c=0
c+=a
print(c)
c*=a
print(c)
c/=a
print(c)
c%=a
print(c)
c**=a
print(c)
#Binary ~~Bit Wise
c=21
print(bin(c))
b=56
print(bin(b))
#Python membership Operators
def CheckMembership():
    a=10
    b=20
    list=[1,2,3,4,5]
    if a in list:
        print(f"{a} is in the list.")
    else:
        print(f"{a} is not in the list.")
    
    if b not in list:
        print(f"{b} is not in the list.")
    else:
        print(f"{b} is in the list.")  

if __name__=="__main__":
    CheckMembership()
# Python Identity Operators
a=20
b=56
if a is b:
    print(f"{a} is similar to b.")
else:
    print(f"{a} is not similar to b")
a=20
b=20
print(id(a))
print(id(b))
if id(a) == id(b):
    print("a has the same identity as b.")
else:
    print("a does not have similar identity as b.")












