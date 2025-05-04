# For the Given array: [23,34,54,10,4,7] search if the given number is there in an array or not. Given number: 34, Expected output: true Given number: 26, Expected output: false
# a = [23,34,54,10,4,7]
# print(23 in a)
# print(1 in a)

#For the Given array: [23,34,54,10,34,7,23,10,34] print the total number of times an element found in the array. Given number: 23, Expected output: 2 Given number: 34, Expected output: 3 Given number: 10, Expected output: 2 Given number: 54, Expected output: 1
# a = [23,34,54,10,34,7,23,10,34]
# print(a.count(23))
# print(a.count(34))
# print(a.count(10))
# print(a.count(54))

# For the Given array: [23,34,54,10,34,7,23,10,34] eliminate duplicates in a given array Expected output: 23,34,54,10,7
a = [23,34,54,10,34,7,23,10,34]
for i in enumerate(a):
    print(i)
