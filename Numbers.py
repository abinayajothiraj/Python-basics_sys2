# three numeric types - int,float,complex

x=1
y=4.5
z=3j

print(type(x))
print(type(y))
print(type(z))

#complex

a=2+5j
print(type(a))
b=5j
print(type(b))
c=-5j
print(type(c))

#Type conversion

x=float(x)
y=int(y)
z=complex(x)

print(x) # int to float
print(y) # float to int
print(z) # int to complex

print(type(x))
print(type(y))
print(type(z))

#random number

import random
#print(random.random())
print(random.randrange(1,10))