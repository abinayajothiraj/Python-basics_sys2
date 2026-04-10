# while loop - is used to repeatedly execute a block of code as long as the specified condition is true

# syntax:

# while condition :
#  i)    code to execute   - if condition is true loop runs , if it is false loop stops

# eg 1:  print i as long as i is less than 6

i = 1
while i < 6:
    print(i)
    i = i +1    # remember to increment i otherwise the loop will continue forever


# eg 2: print x as long as x is less than 9

x = 1
while x < 9:
    print(x)
    x = x +1

# ii) while loop has three statements
            # The break statement
            # The continue statement
            # The else statement

# I) break statement  - stops the loop immediately , even if the condition is true

# eg 1: Exit the loop when i is 3

i = 1
while i < 6:
    print(i)  #  i =1 ; i =2 ; i =2 ; i =3   -> out : 1, 2, 3
    if  i == 3:  # i ==1 F ; i ==2 F ; i == 3 T so the loop stops
        break
    i = i +1    # checks i ==3 which is false so i = 1+1=2; i = 2 +1 = 3



# II) continue statement -  skips the rest of the loop and moves to the next iteration

# eg : continue to the next iteration if i is 3

i = 0                       # i =0; i =1 ; i=2 ; i=3; i=4; i=5; i=6
while i < 6:                # 0 < 6 : T ; 1 <6 : T; 2<6 :T; 3<6:T; 4<6:T;5<6:T ; 6< 6: F (condition fails here so loop has been stopped)
    i = i +1                # i =0+1 =1 ; i = 1+1=2; i=2+1=3;i=3+1=4; 4+1=5; 5+1=6
    if i == 3:              # 1 == 3 :F; 2 == 3:F; 3 == 3 : T; 4 ==3 :F; 5 ==3:F; 6==3: F
        continue
    print(i)                # 1 ; 2 ;skips the loop; 4; 5 ; 6 # -> out : 1,2,4,5,6
    
    
# III) Else statement - runs a block of code when the condition is no longer true

#eg: print a message once the condition is false

i=1
while i < 6:
    print (i)
    i = i + 1
else:
    print("i is no longer less than  6")





# some other examples:

# eg 1:

a =10
while a>0:
    print(a)
    a-=1


# eg 2:

a=10
while a>0:
    a -=1
    if a ==5:
        continue
    print(a)


# eg 3:

a=10
while a>0:
    a -=1
    print(a)
else:
    print("Loop is broken")

# eg 4:

"""while True:
    print("Hello")""" # it is endless loop
