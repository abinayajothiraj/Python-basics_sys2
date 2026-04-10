#1. Divisible by 7 and Multiples of 5
#Write a Python program to find those numbers which are divisible by 7 and multiples of 5, between 1500 and 2700 (both included).


"""nl=[]
for i in range(1500,2701):
    if (i % 7 == 0) and (i % 5 == 0):
        nl.append(str(i))

print(','.join(nl))
"""

def find_numbers():
    nl = []

    for x in range(1500, 2701):
        if (x % 7 == 0) and (x % 5 == 0):
            nl.append(str(x))

    return ','.join(nl)


print(find_numbers())


#2.Write a Python program to list numbers between 1000 and 3000 that are divisible by 7 but not by 5.

num=[]
for i in range(1000,3001):
    if (i % 7 == 0) and (i % 5 != 0):
        num.append(str(i))
print(','.join(num))

# 3.Write a Python program to count how many numbers between 1500 and 2700 are divisible by 7 and also multiples of 5.



def count_numbers():
    count = 0
    for x in range(1500, 2701):
        if (x % 7 == 0) and (x % 5 == 0):
            count = count + 1
    return count

print(count_numbers())

#4. Write a Python program to compute the sum of numbers between 1500 and 2700 that are divisible by 7 and multiples of 5.

def totals():
    total = 0
    for x in range(1500, 2701):
        if (x % 7 == 0) and (x % 5 == 0):
            total = total + x
    return total
print(totals())

#II) Temperature Converter
#Write a Python program to convert temperatures to and from Celsius and Fahrenheit.
#[ Formula : c/5 = f-32/9 [ where c = temperature in celsius and f = temperature in fahrenheit ]
def convert_temperature():
    choice = input("Enter C to convert Celsius to Fahrenheit or F to convert Fahrenheit to Celsius: ")

    if choice == 'C':
        c = float(input("Enter temperature in Celsius: "))
        f = (c * 9/5) + 32
        print("Fahrenheit:", f)

    elif choice == 'F':
        f = float(input("Enter temperature in Fahrenheit: "))
        c = (5/9) * (f - 32)
        print("Celsius:", c)

    else:
        print("Invalid choice")
convert_temperature()


#III)Write a Python program that accepts a word from the user and reverses it.

# using slicing
def reverse_word(word):
    return word[::-1]
print(reverse_word(input("Enter word to reverse: ")))

# using loop
def reverse_word(word):
    rev = ""
    for ch in word:
        rev = ch + rev
    return rev


print(reverse_word(input("Enter word to reverse: ")))

# using for loop

# Prompt the user to input a word
word = input("Input a word to reverse: ")

# Iterate through the characters of the word in reverse order
for char in range(len(word) - 1, -1, -1):
    # Print each character from the word in reverse order without a new line (end="")
    print(word[char], end="")
print("\n")

#IV)


#V)Write a Python program that prints each item and its corresponding type from the following list.Scripting Languages

#Sample List :

datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}]
for item in datalist:
    print("Type of" ,item, "is", type(item) )

#VI) Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.Python statement examples

#Note : Use 'continue' statement.

def print_numbers():
    for i in range(7):
        if i == 3 or i == 6:
            continue
        print(i, end=" ")

print_numbers()
print("\n")

#VII) Fibonacci series: Write a Python program to get the Fibonacci series between 0 and 50.

def fibonacci_series():
    a,b=0,1

    while a <= 50:
        print(a, end=" ")
        a,b = b,a+b
fibonacci_series()


#8)  Two-Dimensional Array (Multiplication Table)

#Write a Python program that takes two digits m (row) and n (column) as input and generates a two-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.
#Note :
#i = 0,1.., m-1
#j = 0,1, n-1.

row_num = int(input("Enter row number: "))
col_num = int(input("Enter column number: "))

multi_list = [[0 for col in range(col_num)] for row in range(row_num)]
for row in range(row_num):
    for col in range(col_num):
        multi_list[row][col] = row * col
print(multi_list)



def create_array(m, n):
    result = []

    for i in range(m):
        row = []
        for j in range(n):
            row.append(i * j)
        result.append(row)

    return result


print(create_array(3, 4))
