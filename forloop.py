#1. print numbers from 1 to 10.

for i in range(1,11):
    print(i)

# to print it in one line:

print(*range(1,11))

# explanation for why *

"""
Simple analogy 

Think of a box :
  i)range(1,11) → a box of numbers
  ii)*range(1,11) → emptying the box and giving numbers directly to print()
"""


# 2. Sum of first N natural numbers => 5=1+2+3+4+5=15

N = int(input("2.Enter N: "))
sum=0
for i in range(1,N+1):
    sum=sum+i
print(sum)

#3.Print even numbers upto N. Input: N , Output: Print all even numbers <=N

a= int(input("3.Enter N: "))
for i in range(1, a + 1):
    if i % 2 == 0:
        print(i, end=" ")
