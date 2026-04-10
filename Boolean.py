#boolean values - True or False
from operator import truediv

print(10>9)
print(10<9)
print(10==9)

#using condition statement

a=309
b=89

if b>a:
    print("b is greater than a")
else:
    print("b is not greater than a")


#bool() function - allows you to evaluate any value and give you true or false in return,

x=(bool("Abi"))
y=(bool(223))
z=(bool("")) #false since it is empty string
k=(bool(0))

print(x,y,z,k)

#i) any string is true except empty strings ""
#ii) any number is true except 0
#iii) any list, tuple, dictionary is true except empty sets


R= [1,2,3]
s=[]
t={33,32,33,233}
u={}
v=()
print(bool(R))
print(bool(s))
print(bool(t))
print(bool(u))
print(bool(v))


#Functions can return boolean - we can create fucnctions that can return a booolean value

def myFunction():
    return True

print(myFunction())

#eg 2
def myFunction2():
    return False

if myFunction2():
    print("YES")
else:
    print("NO")

myFunction2()


# isintance() - python has also many built-in functions that can return a boolean value ,
# here we are using isinstance() function - that can be used to find if an object is of a certain datatype

#eg: To check if an object is an integer or not

x=20
print(isinstance (x,int)) #true
print(isinstance (x,str)) #false