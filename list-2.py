# q = [1,2,1,2,3,5]
# # for x in range (0,len(q)):
# for x in q:
# #     print(q[x]) when we need number which we given input use this for this range will be used
#     print(x)    when we need index use this and range should not be used in range place inputs will be given


# write a script to print all array values in the console.
# a =[1,2,3,4,5,6]
# print(a)

# For the Given array: [23,34,54,0,4,7] print all the Array values using a for loop. Expected output: 23 34 54 0 4 7
# a = [23,34,54,0,4,7]
# for x in a:
#     print(x)

# print all numbers in an array except the first element. Expected output: 34 54 0 4 7
# a = [23,34,54,0,4,7]
# for x in range (1,len(a)):
#     print(a[x])

# Print all elements in an array except the last element Expected output: 23 34 54 0 4
# a = [23,34,54,0,4,7]
# print(a[0:5])

# Print all the numbers from last index to first index Expected output: 7 4 0 54 34 23
# a = [23,34,54,0,4,7]
# print(a[::-1])

# # Print all the numbers from last index to first index except the first element Expected output: 4 0 54 34 23
# a = [23,34,54,0,4,7]
# print(a[-2::-1])

# # Print all the numbers from last index to first index except the last element Expected output: 7 4 0 54 34
# a = [23,34,54,0,4,7]
# print(a[:0:-1])

# Print only the last 4 elements of an array. Expected output: 54 0 4 7
# a = [23,34,54,0,4,7]
# print(a[2:])

# For the Given array: [23,34,54,10,4,7] print the minimum number in an Array. Expected output: 4
# a = [23,34,54,10,4,7]
# for x in range(len(a)):
#     if (x>3):
#         print(a[x])
# for x in range(len(a)):
#     if (x<5):
#         print(a[x])

# for i in range(len(a)):
#     if (i<len(a)-1):
#         print(a[i])

# for i in range (len(a)-1,-1,-1): first -1 indicates starting point second -1 indicates ending points last -1 indicates steps
#     print(a[i])
# for i in range(len(a)-1,0,-1):
#     print(a[i])
# for i in range(len(a)-2,-1,-1):
#     print(a[i])
# for i in range (len(a)-1,0,-1):
#     print(a[i])

# a = [23,34,54,10,4,7]
# print(max(a))
# print(min(a))
# print(sum(a))
# print(sum(a)//len(a))
# for i in (a):
#     if (i>20):
#         print(i)

# For the Given array: [23,34,54,10,4,7] print all the even numbers in an Array. Expected output: 34,54,10,4
# for i in (a):
#     if (i%2==0):
#         print(i)

# For the Given array: [23,34,54,10,4,7] print all the odd numbers in an Array. Expected output: 23,7
# for i in (a):
#     if (i%2!=0):
#         print(i)

# For the Given array: [23,-34,-54,10,-4,7] print all the positive numbers in an array. Expected output: 23,10,7
# a = [23,-34,-54,10,-4,7]
# for i in (a):
#     if (i >0):
#         print(i)

