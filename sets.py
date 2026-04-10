# I) SETS

# eg:

a= {'apple','mango','orange'}
print(a)
print(type(a))

# sets are used to store multiple values in a single variable
# a set is a collection which is unordered,unchangeable and unindexed , do not allow duplicate values

# unchangeable - we cannot change the items after the set has been created

# set list is unordered which means they will appear in random order

b={ 'lily','sunflower','roses'}
print(b)


# ii) duplicates not allowed

c = {'lily','sunflower','roses','lily','jasmine'}
print(c)


# in sets True and 1 are considered as the same value so it will print either one of them and not both
# same goes for False and 0

d ={'lily','sunflower','roses','lily','jasmine',True,False,4,54,2,1,3,True,0}
print(d) # 1 is not printed and 0 is also not printed


# iii) get the length of the set

print(len(d))

# iv) set items - datatypes -> string, boolean,int

e = {'lily','sunflower','roses','lily','jasmine',True,False,4,54,2,1,3,True,0} # everything is present here

# v) the set() constructor - to make a set()

# use double round brackets

x= set(('apple','mango','orange'))
print(x)


# II) ACCESS SET ITEMS

# access items - you cannot access items using index or a key but you can do by using loop  -> for loop by using in keyword

# eg: loop through the set and print the values

f = {'apple','mango','orange'}
for x in f:
    print(x)


# eg : check if banana is present in the set

g = {'apple','mango','orange'}
print('banana' in g) # false becaause banana is not present

# eg : check if banana is not present in the set

print('banana' not in g) # True coz it is not present

# ii) change items - once set is created you cannot change items but you can add new items



# III) ADD SET ITEMS

# i) once set is created you cannot change items but you can add new items - use add() method

h = {'apple','mango','orange'}
h.add('banana')
print(h)

# ii) add sets - update () method

# to add items from another set to current set use update () metgod

flowers ={'lily','sunflower','roses','jasmine'}
fruits = {'apple','mango','orange','banana'}
flowers.update(fruits)
print(flowers)


# add any iterable it can be list,tuple
flowers1 = {'lily','sunflower','roses','jasmine'}
fruits1 = ['kiwi','mango']
flowers1.update(fruits1)
print(flowers1)


# IV) REMOVE SET ITEMS

# i) to remove an item in the set use - discard() or remove() method

# eg : remove banana using remove() method and mango using discard method


fruits2 = {'apple','mango','orange','banana'}
fruits2.remove('banana')
fruits2.discard('mango')
print(fruits2)

# if the item is not present the one which we are asking to remove in remove() method it will raise an error

"""fruits2.remove('kiwi')
print(fruits2) # error"""

# whereas in discard() method it will not raise an error
fruits2.discard('kiwi')
print(fruits2) # no error in discard method


# clear() method empties the set

fruits2.clear()
print(fruits2)  # out is set()

# del() method will delete the set entirely

"""del fruits2
print(fruits2) # error
"""


# V) LOOP SETS

# VI) JOIN SETS - there are several ways to join two sets in python

#The union() and update() methods joins all items from both sets.
#The intersection() method keeps ONLY the duplicates.
#The difference() method keeps the items from the first set that are not in the other set(s).
#The symmetric_difference() method keeps all items EXCEPT the duplicates.



#i) union() -method returns a new set with all items from both sides

set1 = {1,2,3}
set2 = {'a','b','c'}
set3 = set1.union(set2)
print(set3)

# use | operator instead of writing union

set3 = set1 | set2
print(set3)

# join multiple sets

set1 = {1,2,3}
set2 = {'a','b','c'}
set3 = {'apple','mango','orange'}
set4 = {'lily','sunflower','roses','jasmine'}

set5= set1.union(set2,set3,set4)
print(set5)

set5 = set1 | set2 | set3 | set4
print(set5)


# join a set and tuple using union() and | operator will not allow you to add different datatypes like tuple,list

set1 = {1,2,3}
set2 = ['a','b','c']
set3 = set1.union(set2)
print(set3)


# ii) update() - inserts all items from one set to another and changes the original set does not return a new set

set1 = {1,2,3}
set2 = {'a','b','c'}
set1.update(set2)
print(set1)

# both union () and update () will exclude the duplicate items


# iii) intersection - keep only duplicates

# this method will return a new set, that will contains the items that are present in both the sets

set1 = {'apple','mango','orange',}
set2 = {'guava','lily','orange','apple','lotus'}
set3 = set1.intersection(set2)
print(set3)

# use & opeartor instead of writing intersection ()

set3 = set1 & set2
print(set3)


# instersection_update() - method will only keep duplicates but it will chnage the original set instead of returning a  new set

# eg : keep the items that exists in both set1, set2

set3 = set1.intersection_update(set2)
print(set1)


# true , false , 0,1

set1 = {'apple','mango','orange',0,False,True}
set2 = {'guava','lily','orange','apple','lotus',1,False}
set3 = set1.intersection(set2)
print(set3)


# iv) Difference() - method will return a new set that will contain only the items from the first set that are not present in the other set.

set3 = set1.difference(set2)
print(set3)

# - operator

set3 = set1 - set2
print(set3)


# The difference_update() method will also keep the items from the first set that are not in the other set,
# but it will change the original set instead of returning a new set.

set1.difference_update(set2)
print(set1)


# v) symmetric differences

# the symmetric difference method will keep only the elements that are not presemt in both sets

set3 = set2.symmetric_difference(set1)
print(set2)

# use ^ operator

set3 = set1 ^ set2
print(set1)

set3 = set2 ^ set1
print(set2)

# The symmetric_difference_update() method will also keep all but the duplicates, but it will change the original set instead of returning a new set.

set2.symmetric_difference_update(set1)
print(set2) # doubt


# VII) FROZENSET

#frozenset is an immutable version of a set.
#Like sets, it contains unique, unordered, unchangeable elements.
#Unlike sets, elements cannot be added or removed from a frozenset.

# i) craeting a frozenset

# use frozenset() constructor to create a frozenset from any iterable

x = frozenset(('apple','mango','orange'))
y=frozenset({'lily','sunflower','roses','jasmine'})
z=frozenset([1,2,3])
print(x)
print(type(x))
print(y)
print(z)


# ii) frozenset methods

# VIII) SET METHODS