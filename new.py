"""import sys
print(sys.version)"""


"""print("Hello" , end=" ")
print("World")

print("Hello", end="-")
print("carat")

x = 5
xx = "Abi"
print(x)"""


#age = int(input("Enter age: "))
#print(age + 5)

"""

1.Print your name and age

2.Take user input and print it

3.Add two numbers from user input

4.Check if number is even or odd

5.Print numbers from 1 to 10 using loop

"""

#1.Print your name and age

"""name=input("Enter your name: ")
age=int(input("Enter your age: "))

print("Hello" , name)
print("you are", age,"years old")

# using f strings(Improvised version)

x=10
y=20

print(f"The sum of {x} and {y} is {x+y}")

#2&3. Take two numbers from user input and print their sum using f-string.

a=int(input("Enter a number: "))
b=int(input("Enter another number: "))
print(f"The sum of {a} and {b} is {a+b}")

# difference and product as well

print(f"The difference between {a} and {b} is {a-b}")
print(f"The product of {a} and {b} is {a*b}")
"""
#4.Check if number is even or odd

"""num= int(input("Enter a number: "))
if num%2==0:
    print(f"The entered number {num} is even")
else:
    print(f"The entered number {num} is odd")"""


# try and exception - Exception Handling

try:
    num = int(input("Enter a number: "))
    if num % 2 == 0:
        print(f"The entered number {num} is even")
    else:
        print(f"The entered number {num} is odd")
#except ValueError:
 #   print("Please enter a Valid number")

# proffesionalism way

except Exception as e:
    print("Error:" , e)

#2.Will the except block run?

try:
    x=10/0
#except:
 #   print("Error occurred")

except ZeroDivisionError:
    print("You can't divide by zero")

#3.Will except run? Why?

try:
    print("Hello")
except:
    print("Error")

#5.Print numbers from 1 to 10 using loop

for i in range(1,11):
    print(i)

# start,stop,step -> step means it adds that value
"""
1
1+2=3
3+2=5
5+2=7
7+2=9
9+2=11(stops here)

"""
for i in range(1,11,2):
    print(i) # 1,3,5,7,9

# so it will go like
"""
10
10-2=8
8-2=6
6-2=4
4-2=2
2-2=0(stops here)

"""

for i in range(10,0,-2):
    print(i) # 10,8,6,4,2

"""
1.ValueError - correct datatype, wrong value
2.ZeroDivisionError - 10/0
3.TypeError - wrong datatype
4.IndexError
"""

#3. Type Error - occours when the wrong datatype is used
try:
    l="2"
    m=3
    print(l+m)
except:
    print("Error")

# what error will this give?
# - no error coz it supports multiplication which basically gives repititive

x="4"
y=2
print(x*y) #44

#

n="Hi"
m=3
print(n*m)   # HiHiHi

#

print("10"+"20") #1020

#4. IndexError - happens when we are trying to access something outside the range.
# accessing an index that doesnt exist(out of range)
# usually happens in list,tuple,string


#eg1: list
try:
    numbers=[10,20,30]
    print(numbers[3])
except Exception as e:
    print("Error: ", e)

# eg 2: string

try:
    nums="Abi"
    print(nums[6])
except Exception as e:
    print("Error: ", e)


# eg 3: will this give index error

num1=[10,20,30]
for i in range(len(num1)):
    print(num1[i])  #10,20,30->o/p

#4. what will happen here?


num2=[10,20,30]
try:
    for i in range(len(num2) + 1):
        print(num2[i])
except IndexError:
    print("Index out of range")



# GLOBAL VARIABLE

#i)
x=10
def myfunc():
    x=20
    print(x)
myfunc()
print(x)   #20,10

#ii) using global

x=10
def myfunc2():
    global x
    x=20
    print(x)
myfunc2()
print(x) #20,20

#iii) what is o/p?

x=10
def myfunc3():
    x=20
myfunc3()
print(x)  #10



# frozenset - immutable (meaning not changeable)

numm=frozenset([1,2,3])
print(numm)

#set

nummm={2,3,4}
print(nummm)  # set
print(type(nummm))

# frozenset

key = frozenset([1,2,3])

my_dict = {key: "numbers"}
print(my_dict)


#

x = 5
a = float(x)
b = complex(x)

print(a)
print(b)

# we cannot convert complex numbers to int or float

x=2+3j
#int(x)  # type error


# how do you generate random numbers in python
# 1.random.randrange() # 1 to 9
import random
print(random.randrange(1,10))

# 2.random.randint() # 1 to 10

print(random.randint(1,10))

# 3.random. choice() # used to pick random item from the list
fruits=['apple','banana','orange']
print(random.choice(fruits))


print(random.choice("Python")) # possible o/p are [p,y,t,h,o,n] it gives one single output from that

# 4.random.random()  # random decimal between 0 and 1

print(random.random())

# 5. random.shuffle() # used to randomly rearrange elements in a list

num8=[1,2,3,4,5]
random.shuffle(num8)
print(num8)


# generate otp numbers

otp= random.randint(1000,9999)
print("Your otp is: ",otp)

# 6. random.sample
print(random.sample([1,2,3,4,5], 2))

students = ["Abi","Rahul","Priya","Arun","Meena"]

print(random.sample(students,2))

print(len(random.sample([10,20,30,40,],3)))




