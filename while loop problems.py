"""
# 1.Print numbers 1 to 10 . Use a while loop to print numbers from 1 to 10.

i = 1                       # i=1 ; i=2 ; i=3; i=4 ; i=5 ;i=6 ; i=7 ; i=8 ;i=9 , i=10 , i=11
while i < 11:               # 1<11 :T; 2<11 :T; 3<11:T ; 4<11:T ; 5<11:T; 6<11:T; 7<11:T ; 8<11:T;9<11:T;10<11:T ; 11<11:F(loop ends here)
    print(i)                # 1 ; 2 ; 3 ; 4 ; 5 ; 6 ; 7 ; 8 ; 9 ; 10 -->output
    i = i + 1               # i=1+1=2; 2+1=3 ; 3+1=4; 4+1=5 ;5+1=6; 6+1=7; 7+1=8; 8+1=9 ; 9+1=10 ; 10+1=11



# 2. Sum of first N natural numbers . Input: N , Output: Sum = 1+2+....+N

N=int(input("Enter N : "))         # Enter N:5
i =1                               #i=1; i=2;i=3;i=4;i=5,i=6
sum =0                             #sum=0;sum=1;sum=3;sum=5,sum=10,sum=15
while i<=N:                        # 1<=5:T;2<=5:T;3<=5:T;4<=5:T,5<=5:T;6<=5:F(loop ends here)
    sum = sum +i                   #sum=0+1=1;sum=1+2=3;sum=3+3=6;sum=6+4=10;sum=10+5=15
    i = i +1                       #i=1+1=2;2+1=3;3+1=4;4+1=5;5+1=6
print("Sum = 1+2+....",N,"=",sum)   #out: sum=1+2+....5=15


# 3. Print even numbers upto N. Input: N , Output: Print all even numbers <=N

N = int(input("Enter N: "))         # N:10
i=2                                 # i=2;i=4;i=6;i=8;i=10,i=12
while i<=N:                         # 2<=10:T;4<=10:T;6<=10:T;8<=10:T;10<=10:T;12<=10:F (loop ends here)
    print(i)                        # 2 ; 4; 6 ; 8 ; 10 ->out
    i = i + 2                       #i=2+2=4;4+2=6;6+2=8;8+2=10;10+2=12


# 4.count down timer. Input: n=5 , Output: 5 4 3 2 1 "Finish"

n = int(input("Enter n: "))         # n=5; n=4;n=3;n=2;n=1;n=0
while n>0:                          # 5>0:T;4>0:T;3>0:T;2>0:T;1>0:T;0>0:F (loop ends here)
    print(n,end=' ')                # 5 4 3 2 1 Finish
    n = n - 1                       #n=5-1=4;4-1=3;3-1=2;2-1=1;1-1=0;
print("Finish")

n = int(input("Enter n: "))         # n=5; n=4;n=3;n=2;n=1;n=0
while n>0:                          # 5>0:T;4>0:T;3>0:T;2>0:T;1>0:T;0>0:F (loop ends here)
    print(n,)                       # 5 ;4; 3; 2; 1; Finish (newline format)
    n = n - 1                       #n=5-1=4;4-1=3;3-1=2;2-1=1;1-1=0;
print("Finish")


# 5. Reverse a number. Input: 1234 , output: 4321

num = int(input("Enter a number: "))       # num=1234;num=123;num=12;num=1;num=0
rev = 0                                    # rev=0;rev=4;rev=43;rev=432;rev=4321 -> out:Reversed Number:4321
while num > 0:                             # 1234>0:T;123>0:T;12>0:T;1>0:T;0>0:F(loop ends here)
    digit = num % 10                       # digit=1234%10=4;123%10=3;12%10=2;1%10=1
    rev = rev * 10 + digit                 # rev =0*10+4=4;rev=4*10+3=43;rev=43*10+2=432;rev=432*10+1=4321
    num = num // 10                        # num=1234//10=123;num=123//10=12;num=12//10=1;num=1//10=0
print("Reversed Number:",rev)

# 6. Sum of digits of a number. Input: 5678 , output: 26

num=int(input("Enter a number: "))          #num = 5678; num=567 ; num=56 ; num=5 ; num=0
sum=0                                       #sum=0; sum=8 ; sum =15 ; sum=21; sum =26  ->out:Sum of digits : 26
while num>0:                                # 5678>0:T; 567>0:T; 56>0:T; 5>0:T; 0>0:F(loop ends here)
    digit=num%10                            # digit = 5678%10=8; 567%10=7; 56%10=6;5%10=5
    sum = sum+digit                         # sum = 0+8=8; 8+7=15 ; 15+6=21; 21+5=26
    num = num//10                           # num= 5678//10 =567; 567//10=56; 56//10=5; 5//10=0
print("Sum of digits:",sum)

# 7. Check Palindrome Number : Input: 121, Output: Palindrome ; Input:123 , output: Not a Palindrome


num=int(input("Enter a number: "))      # num=121 , num =12; num=1;num=0
temp = num                              # temp=121 (does not change)
rev =0                                  # rev=0; rev=1; rev =12; rev=121
while num>0:                            # 121>0:T; 12>0:T; 1>0:T; 0>0:F(loop ends here )(after the loop completely ends the if - else block starts to execute
    digit = num%10                      # digit=121%10=1; 12%10 =2; 1%10=1;
    rev = rev*10 + digit                # rev=0*10+1=1; 1*10+2=12; 12*10+1=121
    num = num//10                       # num =121//10=12; 12//10=1; 1//10=0
if temp==rev:                           # 121==121 : out->Palindrome
    print("Palindrome")
else:
    print("Not Palindrome")
    """


#
# # 8. Find the maximum element in a list (without using max()) . Input:[11,7,23,5] , Output: 23
#
#
# """
# pesudo code:
# 1:  declare temp wid the first element in list
# 2: iterate over all elements using len() of list
# 3: compare between temp and iterable element
# 4: if i greater
#    replace temp wid i
# """
#
# num = [11,7,23,5]
# temp=num[0]             # temp=11;temp=11;temp=11;temp=23;
# i=0                     # i=0;i=1;i=2;i=3
# while i < len(num):     # 0<4=T;1<4=T;2<4=T;3<4=T;4<4=F( loop ends here)
#     if num[i] > temp:   # 11>11=F;7>11=F;23>11=T;5>23=F;
#      temp = num[i]      # temp=11;temp=11;temp=23;temp=23
#     i = i + 1           # i=0+1=1;i=2;i=3;i=4
# print("Maximum num = ",temp) # temp =23
#
#
#
# # 9. Count even and odd numbers in a list : Input = [1,2,3,4,5] , Output : Even = 2 , odd = 3
#
#
# """
# 1 declare two var, even and odd
# 2 iterate
# 3 div the item by 2
# 4 increment if it is even and if it is odd to each variable
#
# """
#
#
# numbers = [1, 2, 3, 4, 5]
# even = 0                                            #even=0;even=0;even=1;even=1;even=2;even=2
# odd = 0                                             #odd=0;odd=1;odd=1;odd=2;odd=2;odd=3
# i = 0                                               #i=0;i=1;i=2;i=3;i=4;i=5
# while i < len(numbers):                             #0<5:T;1<5:T; 2<5:T; 3<5:T;4<5:T;5<5:F(loop ends here)
#     if numbers[i] % 2 == 0:                         #1%2==0 =>F; 2%2==0 =>T; 3%2==0 =>F ;4%2==0 =>T; 5%2==0 =>F
#         even += 1                                   #no; even=0+1=1;no;even=1+1=2;no
#     else:                                           #yes;no;yes;no;yes
#         odd += 1                                    #odd=0+1=1;no; odd=1+1=2;no;odd=2+1=3
#     i += 1                                          #i=0+1=1;i=2;i=3;i=4;i=5
# print("Total Even Numbers =", even, ",Total Odd Numbers =", odd)        #even = 2 ; odd =3
#
#
# # 10 . Reverse a list using while . Input = [1,2,3,4] , Output = [4,3,2,1]
#
#
# """
# 1 declare a temp list
# 2 iterate from last element and append it ,in the temp list
#
# """
#
# numbers = [1, 2, 3, 4]
# reversed_list = []                          #r=[];r=[4];r=[4,3];r=[4,3,2];r=[4,3,2,1]
# i = len(numbers) - 1                        # i=4-1=3;i=2;i=1;i=0;i=-1
# while i >= 0:                               # 3>=0 :T; 2>=0:T;1>=0:T;0>=0:T;-1>=0:F(loop ends here)
#     reversed_list.append(numbers[i])        # r=[4];r=[4,3];r=[4,3,2];r=[4,3,2,1]
#     i -= 1                                  # i=3-1=2;i=2-1=1;i=1-1=0; i=0-1=-1
# print("Reversed list:", reversed_list)      #r=[4,3,2,1]
#
#
# # 11 . Remove duplicates manually using while loop. Input = [1,2,2,3,1]
#
# '''
# 1 create a temp list(empty list)
# 2 check there is already element is there, if it is not append it to temp list
# '''
#
# numbers = [1, 2, 2, 3, 1]
# lists = []                                               #l=[];l=[1];l=[1,2];l=[1,2];l=[1,2,3];l=[1,2,3]
# i = 0                                                   #i=0;i=1;i=2;i=3;i=4;i=5
# while i < len(numbers):                                 #0<5:T;1<5:T;2<5:T;3<5:T;4<5:T;5<5:F(loop ends here)
#     if numbers[i] not in lists:                          # yes;yes;no;yes;no
#         lists.append(numbers[i])                         #l=[1];l=[1,2];l=[1,2];l=[1,2,3];l=[1,2,3]
#     i += 1                                              # i=0+1=1;i=1+1=2;i=2+1=3;i=3+1=4;i=4+1=5;
# print("List without duplicates:", lists)                 #l=[1,2,3]
#
#
# # 12. convert tuple to list normally using while loop. Input : (5,10,15) , Output: [5,10,15]
#
#
#
# """
# pseudo code:
# 1.create a temp list(empty list)
# 2. append it to the temp list
# """
#
# numbers =(5,10,15,20,25,30)
# temp_list =[]
# i=0
# while i < len(numbers):
#      temp_list.append(numbers[i])
#      i=i+1
# print("Converted List:",temp_list)
#
#
#
# # 13. Find the length of a tuple without using len() . Input: (7,8,9,10) , Output: 4
#
#
# numbers =(7,8,9,10,7,4,6,522,54,357,85,47,22)
# i=0
# count=0
#
#
# while i < len(numbers):
#    count += 1
#    #print(count,numbers[i])
#    i=i+1
# print("length of tuple:",count)
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# # 14. Sum all values in a dictionary     Input: {"x": 10, "y": 20, "z": 30} Output: 60
#
# x = {"x":10,"y":20,"z":30}
#
# y=list(x.values())
# #print(y)
#
# i=0
# sum=0
# while i < len(y):
#     sum = sum + y[i]
#     i=i+1
# print("Sum of digits:",sum)
#
#
#
#
# # 15. Count how many values are greater than a threshold. Input : {"a" : 5 , "b" : 10 , "c" : 15} , threshold = 8 , output: 2
#
# my_dict ={"a":5, "b":10, "c":15}
# my_list=list(my_dict.values())
# threshold=(int(input("Enter a threshold value:")))
#
# i=0
# count=0
# while i < len(my_dict):
#     if my_list[i] > threshold:
#         count=count+1
#     i=i+1
# print("Count of digits:",count)



# 16. Find the second-largest Element (without using sort() or max())  Input: [10, 4, 7, 12, 9] Output: 10

numbers=[10,4,7,12,10,5,11,9]
largest = -999999
second_largest = -999999
i=0
while i < len(numbers):
    value = numbers[i]

    if value > largest:
        second_largest = largest
        largest = value
    elif value > second_largest and value != largest:
        second_largest = value
    i=i+1

print("Second Largest number:",second_largest)


# 17. Remove All Occurrences of a Given Element  Input: [1, 2, 3, 2, 4, 2], remove 2 Output: [1, 3, 4]
num=[1,2,3,2,4,2]
target =2
i=0
while i < len(num):
    if num[i] == target:
        num.pop(i)
    else:
        i=i+1
print(num)
# 18. Find Element Index Manually Input: (10, 20, 30, 40), find 30 Output: 2

num1=[10,20,30,40]
target= int(input("Enter a number: "))

i=0
found = False
while i < len(num1):
    if num1[i] == target:
      found = True
      break
    i=i+1

if found:
    print("Index of  ",target,"is:" , i)
else:
    print(target,"not found in the list.")


# 19.Check Whether a Number is Prime or Not  Example: Input: 7 Output: Prime number

n = int(input("Enter a value: "))

if n <= 1:
    print("not prime number")
else:
    for i in range(2, (n // 2) + 1):
        if n % i == 0:
            print("not prime number")
            break
    else:
        print("prime number")


# 20. Prime Number Series  Example: Input: N = 10 Output: 2, 3, 5, 7

import math as M

# Function to check if a number is prime
def PrimeNum(num2):
    if num2 <= 1:
        return False  # Always return False for numbers <= 1
    for i in range(2, int(M.sqrt(num2)) + 1):
        if num2 % i == 0:
            return False
    return True

# Input range
start = int(input("Enter the range to begin with: "))
end = int(input("Enter the end of the range: "))

print(f"Prime numbers from {start} to {end} are:", end=" ")

# Loop through the range and print primes
for n in range(start, end + 1):
    if PrimeNum(n):
        print(n, end=" ")
