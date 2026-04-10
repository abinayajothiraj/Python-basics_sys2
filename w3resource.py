# 1.Write a Python function that takes a sequence of numbers and determines whether all the numbers are different from each other.
# which is basically a unique number.




#2. Write a Python function to find the first duplicate element in a sequence of numbers.

def first_duplicate(nums):
    duplicates = set()
    for num in nums:
        if num in duplicates:
            return num
        duplicates.add(num)

    return "No duplicate found"

print(first_duplicate([1,2,3,4,5,6,5,7,3,2]))
#print(first_duplicate([1,2,3,4,5]))

#3.Write a Python program to extract the longest subsequence from a list in which all numbers are unique.


#4.

#5.

#II) 1.Write a Python program that creates all possible strings using the letters 'a', 'e', 'i', 'o', and 'I'. Ensure that each character is used only once.


import random

char_list=['a','e','i','o','u']
random.shuffle(char_list)
print(''.join(char_list))
print('--'.join(char_list))


# 2.Write a Python program to generate all unique permutations of a given word without repeating any characters.



# III)1. Write a Python program that removes and prints every third number from a list of numbers until the list is empty.

def remove_third(nums):
    index = 0

    while nums:
        index = (index + 2) % len(nums)
        print(nums.pop(index))


remove_third([1, 2, 3, 4, 5, 6, 7, 8, 9])


# IV) 1.