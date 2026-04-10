# I) TUPLE - a tuple is a collection which is ordered and unchangeable

# i) tuples are used to store multiple items in a single variable

#eg: create a tuple

a=("apple","banana","cherry",'mango')
print(a)

# ii) ordered, unchangeable and allows duplicates

b = ("apple","banana","cherry",'mango','banana','mango','lemon','pome')
print(b)

# iii) tuple length - len() function

print(len(b))

# iv) tuple datatypes - string, int, boolean datatypes

c =("choco",'chips', 'icecream')
d=(1,2,3)
e = (True,False,False)
print(c)
print(d)
print(e)

# v) a tuple can contain different dataatypes

f = ("apple","banana","cherry",234,True,'mango',23,75,121,False)
print(f)
print(type(f))

# vi) tuple() constructor

g=tuple(("apple",'mango','kiwi'))
print(g)



# II) ACCESS TUPLE ITEMS

#i) by using index number

#eg: print the second item in the tuple

h=('apple','banana','cherry')
print(h[1])

# ii) Negative indexing

#eg: print the last item in the tuple

print(h[-1])

# iii) Range of Indexes

#eg: return the third, fourth, fifth item

i= ('apple','banana','orange','kiwi','cherry','mango')
print(i[2:5])
print(i[2:])
print(i[:2])
print(i[:])
print(i[-3:-2])

# iv) in keyword

if 'apple' in i:
    print('apple')

# III) UPDATE TUPLES

#i) once tuple is created we cannot change, add or remove items
 # but we can convert the tuple into list, change the list, convert the list back into a tuple


#Eg: change tuple values
j=('apple','banana','cherry')
k=list(j)
k[1] = 'mango'
j=tuple(k)
print(j)


# ii) Add Items - since tuples are immutable they do not have a built-in method , but there are ways to  add items to a tuple and there are two steps

# step 1: convert into list
# step 2: Add tuple to a tuple

# eg: convert the tuple into list , add the value 'kiwi ' and convert it back to a tuple

x = ('apple','banana','cherry')
y= list(x)
y.append('kiwi')
x=tuple(y)



# iii) Remove items

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
print(thistuple)

#iv) use del keyword

"""del thistuple
print(thistuple)""" # it will produce error

#IV) UNPACK A TUPLE

# i) when we create a tuple, we normally assign values to it . This is called packing a tuple

flowers = ('sunflower','rose','daisy')
print(flowers)

# but in pythonn we are allowed to extract the values back to variables. This is called unpacking

flowers = ('sunflower','rose','daisy')
(yellow,red,purple) = flowers
print(yellow)
print(red)
print(purple)  # the number of values must match the number of values in the tuple , or we have to use * astreik to collect the remaining values as a list

# ii) using asterisk

# eg : Assign the rest of the values as a list called purple

flowers = ('sunflower','rose','daisy','jasmine','lily','lotus','Tulip')
(yellow,red,*purple) = flowers
print(yellow)
print(red)
print(purple)


#If the asterisk is added to another variable name than the last,
# Python will assign values to the variable until the number of values left matches the number of variables left.

# eg: Add a list of values to red

flowers = ('sunflower','rose','daisy','jasmine','lily','lotus','Tulip')
(yellow,*red,purple) = flowers
print(yellow)
print(red)
print(purple)


# V) LOOP TUPLES


# VI) JOIN TUPLES

# i) join two tuples - + operator

tuple1 = ('apple','banana','cherry')
tuple2 = (1,4,5)
tuple3 = tuple1 + tuple2
print(tuple3)

# ii) multiply tuples

flowers = ('sunflower','rose','daisy')
mytuple = flowers * 3
print(mytuple)


# VII) TUPLE METHODS

# tuple has two in built methods - count() and index()

# i) count() -   returns the number of times a speciiified value occur in a tuple

a = (1,4,3,5,3,6,5,2,5,2,7,2,3,5)
b=a.count(5)
print(b)


# ii) index() - searches the tuple for a sspecified value returns the position of where it is found

#eg: search the first occurrence of 3 and return its position

a=(1,4,3,5,3,6,5,2,5,2,7,2,3,5)
c=a.index(3)
print(c)