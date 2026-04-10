#strings - surrounded by single quotation or double quotation

#1.display string literal with 'print' function

print('hi')
print("hi")

#2.quotes inside quotes

print("It's Alright")
print("His name is 'Joe' ")
print('He is called "Alex"')

#3.assign string to variable - variable name followed by an equal sign and a string

a="Hello"
print(a)

#4.multiline string

a=""" Python is dynamically type-checked and garbage-collected.
 It supports multiple programming paradigms, including structured (particularly procedural), object-oriented and functional programming.
Guido van Rossum began working on Python in the late 1980s as a successor to the ABC programming language. 
Python 3.0, released in 2008, was a major revision and not completely backward-compatible with earlier versions.
Recent versions, such as Python 3.12, have added capabilities and keywords for typing (and more; e.g. increasing speed);
helping with (optional) static typing.[35] Currently only versions in the 3.x series are supported."""

print(a) #three double quotes

b= ''' Python is dynamically type-checked and garbage-collected.
 It supports multiple programming paradigms, including structured (particularly procedural), object-oriented and functional programming.
Guido van Rossum began working on Python in the late 1980s as a successor to the ABC programming language. 
Python 3.0, released in 2008, was a major revision and not completely backward-compatible with earlier versions.
Recent versions, such as Python 3.12, have added capabilities and keywords for typing (and more; e.g. increasing speed);
helping with (optional) static typing.[35] Currently only versions in the 3.x series are supported. '''
print(b) # three single quotes



#5.strings are Arrays - [] square brackets can be used to access elements of a string

x= "Hello World!"
print(x[1])
print(x[9])

#6.Looping through a string - since strinbgs are arrays we can loop through the characters with a for loop

for x in 'banana':
    print(x)

#7.String Length - len() function
y='Hello World!'
print(len(y))


#8. Check string - to check if certain phrase or character is present in a string - use in keyword

txt="Everything in this world is free"
print ('free' in txt)  # true
print('hello' in txt)  #false

# use it in an if statement

if 'hello' in txt:
    print('yes, Free is present')
else:
    print('no, Free is not present')


#9. check if NOT - to check if a certain phrase is NOT present in a string , we can use not in keyword

print('hello' not  in txt) # true