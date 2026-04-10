# I) DICTIONARY

a= {
    "Germany": "Berlin",
    "Australia" : "canberra",
    "England" : " London"
}

print(a)
print(type(a))

# dictionaries are stored data in key value pairs
# ordered,changeable,do not allow duplicates

# i) dictionary items - are represented in key value pairs and can be reffered to by using the key name

b = a["Germany"]
print(b)

# ii) ordered or unordered , changeable

# according to 3.6 it is unordered and to  3.7 it is ordered
# it is changeable meaning that we can change, add or remove items fromm the dictionary

# iii) duplicates not allowed

# dictionaries cannot have two items with same key.

#eg: duplicates will overwrite existing values

a = {
    "Germany": "Berlin",
    "Australia" : "canberra",
    "England" : " London",
    "England" : "UK"
}

print(a)

# iv) dictionary length

print(len(a))

# v) datatypes - can be of any (list,int, boolean)

b= {
    "age" : 20,
    "City" : False,
    "country" : ["Australia","Japan" , "Korea"]
}

print(b)
print(type(b))

#  vi) dict() constructor

c = dict(name="John", age=17, city="London")
print(c)
print(type(c))


# II) ACCESS ITEMS

#i) access the items of a dictionary by referring to its key name, inside square brackets

b=b["age"]
print(b)

# get () method


b= {
    "age" : 20,
    "City" : "Birmingham",
    "country" : ["Australia","Japan" , "Korea"]
}
d = b.get("City")
print(d)

# ii) Get keys - keys() method will return a list of all the keys in a dictionary

e = b.keys()
print(e)



# III) CHANGE ITEMS

# i) change values

b["age"] = 17
print(b)

# ii) update dictionary

c= {
    "age" : 20,
    "City" : "Birmingham",
    "country" : ["Australia","Japan" , "Korea"]
}
c.update({"city":"Kerala"}) # doubt
c.update({"age":25})
print(c)

# IV) ADD ITEMS

c["fruits"] = "Apple"
print(c)


# V) REMOVE ITEMS

#i) Removing items

# pop() method

c.pop("age")
print(c)

# popitem() - removes the last inserted item

c.popitem()
print(c)

# del keywprd


d= {
    "Germany": "Berlin",
    "Australia" : "canberra",
    "England" : " London"
}

del d["Australia"]
print(d)

"""del d
print(d)""" #error

# clear() method empties the dictionary

d.clear()
print(d)


#V) LOOP DICTIONARIES

# VI) COPY DICTIONARIES

#i) copy () method


c= {
    "age" : 20,
    "City" : "Birmingham",
    "country" : ["Australia","Japan" , "Korea"]
}

x = c.copy()
print(x)


#ii) dict() method

mydict = dict (c)
print(mydict)


# VII) NESTED DICTIONARIES

# i ) create a dictionary that contain three dictionaries

countries = {
    "Asia" :{
        "India":"Bollywood",
        "Korea":"k-pop Idols"
    }
    ,
    "Europe" :{
        "Germany":"Berlin",
        "UK":"London"
    },
    "Island":{
        "Indian":"Andaman",
        "korea":"jeju island"
    }
}

print(countries)

# ii) access items in dictionaries

print(countries["Asia"]["Korea"])





