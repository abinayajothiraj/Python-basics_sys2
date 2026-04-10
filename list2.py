# V) REMOVE LIST ITEMS:

# i) remove() method - removes the specified item
#if there are more than one item then it removes the first occurrence alone

a= ["Apple","Banana","Cherry","Banana","Cherry"]
a.remove("Cherry")
print(a)

#ii) Remove specified index - pop() method removes the specified index
# eg: remove the second item

b=["apple","banana","cherry","mango","strawberry"]
b.pop(0)
print(b)

# if you do not specify the index the pop() method removes the last item

c=["apple","banana","cherry"]
c.pop()
print(c)

#the del keyword also removes the specified index

# remove the first ittem

d = ["apple","banana","cherry"]
del d[1]
print(d)

# the del keyword can also remove the list completely

"""e = ["apple","banana","cherry"]
del e
print(e)"""

# iii) clear the list - clear () method  empties the list
# the list still remains but it has no content

f=["apple","banana","cherry"]
f.clear()
print(f)


# VI) LOOP LISTS

# i) we can loop through a list of items using - for loop

#eg: Print all the items in the list one by one
thislist = ["apple","banana","cherry"]
for x in thislist:
    print(x)

# ii) Loop through the index numbers - use range() and len() functions to create a suitable iterable

#eg: print all items referring to index number

thislist1 = ["apple","banana","cherry"]
for i in range(len(thislist1)):
    print(thislist1[i])


#  iii) Using a while loop



# iv) Looping using list comprehension - offers shortest syntax
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

#VII) LIST COMPREHENSION

# VIII) SORT LISTS

#i) sort() - method that will sort alphanumerically, ascending

g= ["apple","cherry",'mango',"banana",'strawberry','lemon','blueberry','kiwi']
g.sort()
print(g)

#eg : sort list numerically

h = [748,23,734,232,998,12,9,34]
h.sort()
print(h)

#ii) sort descending - use keyword argument -> reverse= True

g.sort(reverse=True)
print(g)

#iii) customize sort Function


#iv) Case Insensitive sort

# by default the sort() method is case sensitive , so all capital letters are sorted first before lower letters

i=["banana","Lemon","Kiwi","apple","orange","Mango"]
i.sort()
print(i)

#Luckily we can use built-in functions as key functions when sorting a list.
#So if you want a case-insensitive sort function, use str.lower as a key function:

#eg: Perform a case-insensitive sort of the list

i.sort(key=str.lower)
print(i)


# v) Reverse order - reverse() method

g= ["apple","cherry",'mango',"banana",'strawberry','lemon','blueberry','kiwi']
g.reverse()
print(g)



# IX) PYTHON - COPY LISTS

#i)  copy a list - You cannot copy a list simply by typing list2 = list1, because: list2 will only be a reference to list1, and changes made in list1 will automatically also be made in list2.

# copy() - method which is a built - in method to copy a list

k= ["apple","cherry",'mango',"banana",'strawberry','lemon','blueberry','kiwi']
thislist = k.copy()
print(thislist)


# ii) Another way to copy a list is to use list() method

# list() - method

l= ["apple","banana","cherry"]
hi=list(l)
print(hi)

# iii) use the slice operator

m=["apple","banana","cherry",'mango']
hello = m[:]
print(hello)


# X) JOIN LISTS

#i) using + operator

# eg: join two list

n=['apple','banana','cherry']
o=[1,54,78,34,95]

hooo= n + o
print(hooo)

#ii) using extend method

n.extend(o)
print(n)