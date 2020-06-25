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