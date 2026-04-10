#variables has no type and can also change after setting.
x=80  #type int
x="Welcome!"  #type changed to string
print(x)

#type() func
print(type(x))

#str can be of single quote or double quote
y='yellow'
z="pink"
print(y)
print(z)

#variable names are case-sensitive

a='Apple'
A=2
print(a)
print(A)

#multi-words variable names
"""""
i)camelcase -each word is uppercase except first
ii)pascalcase - eavh word is uppercase
iii)snakecase - each word is separated by underscore
"""
myVariableName='john'
print(myVariableName)
MyVariableName='kee'
print(MyVariableName)
my_variable_name='joe'
print(my_variable_name)

#assign many values to multiple variables

B,C,D='banana','strawberry','blueberry'
print(B)
print(C)
print(D)

#assign one value to multiple variables

E=F=G='Mangoes'
print(E)
print(F)
print(G)

#unpack a collection - collection of values in a list or tuple where python allows yoy to extract values into variables is called unpacking
#unpack a list

series=['TSIP','vampire diaries','originals']
H,I,J=series
print(H)
print(I)
print(J)

#output variables - print() function
# output multiple variables separated by comma
print(H,I,J)

# + operator to output multiple variavles
print(E+F+G)


#Global variables -  created outside the func can be used both inside and outside of func
"""
Q="Awesome"

def myfunc():
  print("Python is " + Q)
myfunc()
"""
Q="Awesome"

def myfunc():
  Q="Fantastic"
  print("Python is " + Q)

myfunc()

print("Python is " + Q)

# THE Global keyword

def myfunc1():
    global k
    k="Popular"

myfunc1()

print("python is " + k)

L="python "
M="is "
N="awesome"
print(L+M+N)


#range () datatype:

x=range(2,10)
print(x)
print(list(x))

# frozenset() datatype
y=frozenset({"apple","mango","cake"})
print(y)

x=None
print(x)
print(type(x))