#1. multiline strings
text="""
python is easy 
and very powerful
language
"""
print(text)

# 2.check if a word exists in a string (use in keyword)
txt="The best things in life are free"
print("free" in txt) # true
print("hii" in txt)  # false
print("hi" in txt) # true  coz in things we have hi so it is true( it checks s sequence of charcacters not as words)

# 3.to check if a word is not in a string use(not in ) keyword
print("expensive" not in txt) # true
print("expensive" in txt) # false

#4. if we want as whole word only means:

txt="The best things in life are free"
words= txt.split()
print("hi" in words) # false
print("hii" in words) # false
print("things" in words) # true

# note: "hi" in txt.split() -> checks full word
#        "hi" in txt -> checks inside anywhere




"""
1. count vowels
2. count consonants
3. Reverse a string 
    i) reverse a string without slicing
4.Check Palindrome
5.count characters ( without space)
6.find first non- repeating character

"""




#1.Take a string from the user and count how many vowels are present in it.
#Vowels = a, e, i, o, u

find_vowels= input("Enter a string: ")
count = 0
for i in find_vowels:
    if i in "aeiou":
        count += 1
print( count)



"""
i) use islower():  for both AEIOU AND aeiou 
find_vowels= input("Enter a string: ")
count = 0
for i in find_vowels:
    if i.isalpha() and i.lower() in "aeiou":
        count += 1
print( count)


ii)

find_vowels= input("Enter a string: ")
count = 0
for i in find_vowels:
    if i in "aeiouAEIOU"":
        count += 1
print( count)

"""


#2. Take a string from the user and count how many consonants are present
# check : 1.character is alphabet 2.and not a vowel

find_consonants= input("Enter a string:")
count = 0
for i in find_consonants:
    if i.isalpha() and i.lower() not in "aeiou":
        count += 1

print("The number of consonants is: ",count)

# isalpha -> ignores numbers,spaces, symbols
# i.lower()-> converts the uppercase letters to lowercase


#3. Reverse a string - use step in slicing[::step]


reverse_string = input("Enter a string: " )
print(reverse_string[::-1])




# 3.i) Reverse a string without slicing


reversed_string1 = input("Enter a string: " )









# slicing:
"""

1️⃣ Reverse Only First Half
Input: "abcdef"
Output: "cbadef"

👉 Reverse first half, keep rest same

2️⃣ Remove First and Last Character
Input: "Python"
Output: "ytho"
3️⃣ Palindrome Check (Using Slicing)
Input: "madam"
Output: True
4️⃣ Swap First and Last Characters
Input: "hello"
Output: "oellh"
5️⃣ Middle Character(s)
Input: "abcde" → "c"
Input: "abcd"  → "bc"




"""


#1. Reverse Only First Half
#Input: "abcdef"
#Output: "cbadef"

"""
break into parts-> first half="abc" , second half="def"

"""
x= "abcdef"
first_half =(x[:3])
print(first_half) # first half: abc
print(first_half[::-1]) # reverse first half: cba

second_half=(x[3:])
print(second_half) #second half: def

#combine:

x= "abcdef"
first_half =x[:3] [::-1]
second_half = x[3:]
result = first_half + second_half
print(result)  # cbadef

# shortcut version:

x="abcdef"
print(x[:3][::-1] + x[3:])  #  cbadef



#2. input: " abcdefgh"
#   output: " dcbahgfe"

a="abcdefgh"
first_half =a[:4][::-1] # dcba
second_half = a[4:][::-1] # hgfe
result = first_half + second_half
print(result)  # dcbahgfe

# 3. o/p: dcbaefgh

b="abcdefgh"
first_half =b[:4][::-1]
second_half = b[4:]
result = first_half + second_half
print(result)


#4.o/P: fedcba

o="abcdef"
first_half =o[3:][::-1]
second_half = o[:3][::-1]
result = first_half + second_half
print(result)

"""
2️⃣ Remove First and Last Character
Input: "Python"
Output: "ytho"
"""

m= "Python"
n="Hello World"
#print(m[1:5]) -> wrong coz it does not work for all inputs

print(m[1:-1])
print(n[1:-1])





"""
3️⃣ Palindrome Check (Using Slicing)
Input: "madam"
Output: True
"""

x="madam"
print(x == x[::-1]) # true
if x == x[::-1]:
    print("It is a palindrome")

# other way

x= "hello"
print(x == x[::-1]) # false



"""
5.
Input: "abcde" → Output: "c"
Input: "abcd"  → Output: "bc"

👉 Find middle character(s) using slicing

"""

x="abcde"
print(x[-3::3]) # hardcode -> ill become wrong if i/p changes

y="abcd"
print(y[1:3])  # hardcode -> ill become wrong if i/p changes




# 1. string methods - using tuple [ if any one matches true ]

txt="Hi,Welcome"
print(txt.startswith(("Hello","Hi"))) #true


# 2.[ startswith,start,end ]
txt = "Hello, welcome to my world."

x = txt.startswith("wel", 7, 20)
print(x)

# 3. Joins()

myTuple = ("John" , "Ken" , "Lara")
x= "#" . join(myTuple)
print(x)