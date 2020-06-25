var1=1
var2=10
print(var1,var2)
del var1
try:
    print(var1)
except:
    print("Var 1 is not Found!")
#Complex
comp=3+45j
print(type(comp))
print(comp.real)#Real Number
print(comp.imag)#Imaginary number
#Numbers Operations
print(abs(-45))#Absolute Value
print(pow(2,2))#Power
print(max(1,15,20,89,12,33))#Maximum Value
list=[4,5,6,1]
print(max(list))
print(min(23,56,12,98))
from fractions import Fraction
a=Fraction(23,54)
print(a)
print(round(23.55998,3))
import math
print(math.sqrt(49))


#Random Numbers Function
#Choice
from random  import choice

print(choice(range(100)))
list=[1,2,3,5,9]
print(choice(list))
name="Hello World"
print(choice(name))
#RandRange
from random import randrange
print(randrange(0,100,2))
print(randrange(100))
#Random Method
from random import random
list=[1,2,3]
print(random())
#Seed
from random import seed
print(seed(2))
#Shuffle
from random import shuffle
list=[1,2,3,6,4,5]
shuffle(list)
print(list)
#Uniform method
from random import uniform
print(uniform(5,10))
print(uniform(6,6))







































