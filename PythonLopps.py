#While Loop
count=0
while count<9:
    print(f"The count is {count}")
    count+=1
print("Good Bye!!")  

# var=1
# while var ==1:
#     num=
#     print("You entered:",num)
# print("Good Bye!")

#Use else statement with Loops
count=0
while count<5:
    print(f"{count} is less than 5")
    count+=1
else:print(f"{count} is not less than 5")

#For Loop Statements
for var in range(0,100):
    print(var)
for var in range(0,100):
    if var%2==0:
        print(f"{var} is Even.")
    else:
        print(f"{var} is Odd.")
mylist=[1,5,10,"a","b"]

for member in range(len(mylist)):
    print(f"{member}.")

for var in list(range(5)):
    print(var)
mystr="Python"
for letter in mystr:
    print("current letter.",letter,"\n\n")
print("=="*50)
new_list=[1,5,9,45,78]
i=0
for member in new_list:
    print(f" ",member)
    
fruits=["banana","apple","mango"]
for fruit in fruits:
    print(f"I love {fruit}")
fruits=["water Melon","Oranges","Lemon","Apple"]
for index in range(len(fruits)):
    print(f"{index}. This  is a {fruits[index]}.")
numbers=[11,33,55,39,55,75,37,21,23,50,13]
for num in numbers:
    if num%2==0:
        print(f"The list contains an even number -->{num}.")
        break
else:
    print("The list does not contain any even number")

for place in range(len(numbers)):
    print(f"{place}-->{numbers[place]}")
#Nested loops
for i in range(0,10):
    for j in range(i,10):
        print("*",end="")
    print()
# Multiplication table   
for i in range(1,11):
    for j in range(1,11):
        k=i*j
        print(f"{i} * {j}={k}",end=" ")
        print()
    print()
#Loop Control Statements
for letter in "Python":
    if letter =="h":
        break
    print(f"Current Letter: {letter}")
var=10
while var>0:
    print(f"Current variable value: {var}")
    var-=1
    if var ==5:
        break
print("Good Bye!")

#trial
for num in range(0,100):
    if num==50:
        break
    print(num)
#Trial While
num1=0
while num1<100:
    if num1==50:
        break
    print("While",num1)
    num1+=1
    
num1=11
numbers=[11,33,55,39,55,75,37,21,23,41,13]
for num in numbers:
    if num==num1:
        print("Number found in list")
        break
else:
    print("Number not found in list")
#Continue Statement
    
for letters in "Python":
    if letters =="h":
        continue
    print(f"Current letter: {letters}")
print("Good Bye")

var=10
while var>0:
    var-=1
    if var == 5:
        continue
    print("Current variable value:",var)
print("Good Bye!")
#Pass Statement
for letter in "Python":
    if letter =="h":
        pass
        print("This is pass block")
    print("Current letterz",letter)
    
print("Good Bye!")
#Iterators and Generators
list=[2,1,2,3,4,5]
it=iter(list)
print(next(it))









