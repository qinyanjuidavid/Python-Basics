var1=100
if var1:
    print(var1)
#Blank Variables are always False
myStr=""
if myStr:
    print("That is a String")
var2=0
if var2:
    print("This statement is True")
else:
    print("Good Bye cruel world!")
amount=600
if amount<1000:
    discount=amount*0.05
    print(f"You got a discount of {discount} Kshs.")
else:
    discount=amount*0.10
    print(f"You got a discount of {discount} Kshs.")
PayableAmount=amount-discount
print(f"The amount Payable is {PayableAmount}")

amount=2000
if amount<1000:
    discount=amount*0.05
    print(f"You got a discount of {discount} Kshs.")
elif amount<5000:
    discount=amount*0.10
    print(f"You got a discount of {discount} Kshs.")
else:
    discount=amount*0.15
    print(f"You got a discount of {discount} Kshs.")
print(f"The net payble is {amount-discount} Kshs.")
#Nested If statement
num=30
if num%2==0:
    if num%3==0:
        print("The number is divisible by both 2 and 3.")
    else:
        print("The number is not divisible by 2 and 3")
else:
    if num%3==0:
        print("The number is divisible by 3 but not divisible by 2")
    else:
        print("The number is not divisible by both 2 and 3")











