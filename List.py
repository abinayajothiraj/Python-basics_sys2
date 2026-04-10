#Lists - used to store multiple values in a single variable - created using square brackets []
# used to store collections of data

#eg 1:

a=["apple","mango",'cherry']
print(a)

# ordered, changeable, allow duplicate values

#ordered - will not change the order , the new items will be placed at the end of the list
# changeable - we can change add , remove in a list after being created
# allow duplicates - since lists are indexed they can haave items with samme value

#len() function - to find how many items a list has

print(len(a))

#List items datatypes - it can be of any types
#eg:
#they can be string, int , boolean
x=["a" ,'b','c']
y=[1,2,3,3,4,6,5]
z=[True, False, True, True,False]

print(x)
print(y)
print(z)

#eg2:
# A list can contain different data types

D=[True,"Abi",3545,False,'Apple',7]
print(D)
print(len(D))
print(type(D))

#lists are defined as objects with the data type 'list'
print(type(x)) #<class 'list'>

#The list() constructor

a="Abi"
print(list(a))


# II ACCESS LIST ITEMS

# i)lists are indexed and we can access them by referring to it

A=[23,434,455,787]
print(A[3])

#ii) negative indexing

# -1 refers to last item, -2 refers to second last item
print(A[-3])

# iii) Range of indexes

x=["Apple", " Bananna","Cherry","Mango","Strawberry","Orange","Grapes","Watermelon"]
print(x[2:6])
print(x[4:])
print(x[:5])

# iv) Range of negative indexes

print(x[-4:-2])

# iv) Check if item exits

y=["Apple", " Bananna","Cherry","Mango","Strawberry","Orange","Grapes","Watermelon"]
if "Mango" in y:
    print("Mango is present in y")



# III) CHANGE LIST ITEMS

# i) to change the value of the specific item, refer to the index number

#eg 1: Change the second item in the list

z=["Apple", " Bananna","Cherry","Mango","Strawberry","Orange","Grapes","Watermelon"]
z[1]="Pomegranate"
print(z)

# ii) change a range of Item values

# eg2: Change the values cherry and mango to blackcurrent and kiwi

s=["Apple", " Bananna","Cherry","Mango","Strawberry","Orange","Grapes","Watermelon"]
s[2:4]=["Blackcurrent" , "Kiwi"]
print(s)

# If you insert more items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly
t= ["Apple","Mango","Orange"]
t[1:2]=["Banana","Cherry","Guava","Strawberry"]
print(t)

# If you insert more items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly:

u=["Mango","Orange","cherry"]
u[1:3]=["Watermelon"]
print(u)


# iii) INSERT ITEMS - insert() method is used

# to insert a new item without replacing any of the existing values we use insert() method

# insert() method inserts a specified value at specified position

#eg : Insert "Watermelon"  as the third item

v=["Apple","Mango","Orange","Cherry","pomegranate"]
v.insert(2,"Watermelon")
v.insert(4,"Kiwi")
print(v)


# IV) ADD LIST ITEMS - append() method

#i) Append items - to add an item at the end of the list , use the append() method

b= ["Apple","Mango","Orange","Cherry","pomegranate"]
b.append("Kiwi")
print(b)

#ii) Insert Items - insert() method

#eg: Insert an item in the second position

b.insert(1,"strawberry")
print(b)

#iii) Extend List - to append elements from another list to current list, use extend() method - the elements will be added at the end of the list

thislist=["apple","banana","cherry"]
tropical =["pineapple","papaya","strawberry","pomegranate"]
thislist.extend(tropical)
print(thislist)

#iv) Add any iterable - the extend() method does not have to append lists , you can add any iterable object (tuple,sets,dictionaries)

thislist1=["apple","banana","cherry"]
trop = (1,2,3)
thislist1.extend(trop)
print(thislist1)