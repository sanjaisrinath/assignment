# for forloop we use range do we have to keep one extra number ie: we need 1 to 10 so we have to give range 1 to 11 the only we get 1 to 10
#for loop always move in positive direction so when we need a reverse order we have to use negative int in range ie; Write a program to print 10 to 1 numbers using a for loop
# for the above question we have to add -1 in a range for a in range (10,0,-1):
#  Write a program to print 1 to 10 numbers using a for loop

# for a in range (1,11):
#     print(a)

# Write a program to print 10 to 1 numbers using a for loop
# for a in range (10,0,-1):
#     print(a)

#write a program to print all numbers from 1 to a given number
# a = int(input("enter the number"))
# for a in range (1,a+1):
#     print(a)

# Write a program to print 1 to 10 even numbers using a for loop
# for a in range(1,11):
#     if a%2==0:
#         print(a)

# Write a program to print 1 to 10 odd numbers using a for loop
# for a in range (1,11):
#     if a%3==0:
#         print(a)

# Write a program to print first 10 multiples of 3 using a for loop
# a = 1
# for a in range(1,11):
#     print(a*3)

# Write a program to print multiplication table of 6 using a for loop
# a =1
# for a in range(1,10):
#     print("6 x",a,"=",a*6)

# Write a program to print all the factors of a given number (if we need to count the factor we need to add count =0 in starting and count = count+1)
# a =1
# for a in range(1,11):
#     print(a ,"factor is", a**a)

# num = int(input("enter the number"))
# for x in range (1,num+1):
#     if num%x==0:
#         print(x)

#a program to read 5 numbers and print the maximum and minimum number
# to print min and maximum we have to use float('-inf')--- max value it is a reserved str,, float(inf)---- min value 
# a = float('-inf')
# for x in range(5):
#     num = int(input("enter the number"))
#     if num>a:
#         a = num

# print(a)


# b = float('inf')
# for x in range (3):
#     num = int(input("enter the number"))
#     if num<b:
#         b=num
# print(b)

# a program to read 5 numbers and print only the even numbers

# for x in range(5):
#     a = int(input(f"enter the number{x+1}:"))
#     if a%2==0:
#         print(a)
#     else:
#         print("no")

# Print all the digits of a given number
# num = int(input("enter the number :"))
# while num>0:
#     a = num%10
#     print(a)
#     num= num//10

# Write a program to print only even digits of a given number The output should be 4,2,6 Ex. Let us take 154256
# num =int(input("enter the number:"))
# while num>0:
#     a = num%10
#     if num%2==0:
#         print(a)
#     num = num//10

#Write a program to print only odd digits of a given number Ex. Let us take 1542763 The output should be 1,5,7,3
# num = int(input("enter the number: "))
# while num>0:
#     a = num%10
#     if num%2!=0:
#         print(a)
#     num= num//10

# Write a program to print the number at 1’s place
# num = int(input("enter the number:"))
# a = num%10
# print(a)

# write the program to print the number at 10's place
# num = int(input("enter the number"))
# a = (num//10)%10
# print(a)
 
# Write a program to print the number at 100’s place
# num = int(input("enter the number: "))
# a = (num//100)%10
# print(a)

# Write a program to print the number at 1000’s place
# num = int(input("enter the number: "))
# a = (num//1000)%10
# print(a)
