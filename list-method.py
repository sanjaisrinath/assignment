'''list methods -  append Syntax num.append(number to add) it will be added at last
insert - syntax num.insert(where to insert,number to insert)(2,34) it will be inserted at the place
remove - syntax num.remove(number to remove) it will remove the number, when two or more same number is present in list we need to remove that
number means it will remove the one number which is present at first a =[2,2,2,44,4,5,6,7] a.remove(2) 
output = [2,2,44,4,5,6,7]
pop - syntax num.pop() if pop is empty it will automatically remove last element of list  a= [2,2,2,44,4,5,6,7] a.pop()
output = [2,2,2,44,4,5,6]
when we give a specific index number in pop it will remove the specific index number in list  a= [2,2,2,44,4,5,6,7] a.pop(3)
output = [2,2,2,4,5,6,7]
count - syntax num.count (number to count) it will count a specific number how many times it is present
a= [2,2,2,44,4,5,6,7]
t = a.count(2)
print(t)
output = 3
sort - syntax num.sort() it will automatically sort the list into ascending order
a= [2,2,2,44,4,5,6,7]
a.sort()
print(a)
output = [2, 2, 2, 4, 5, 6, 7, 44]
reverse - syntax num.reverse() it will reverse the whole list
a= [2,2,2,44,4,5,6,7]
a.reverse()
print(a)
output = [7, 6, 5, 4, 44, 2, 2, 2]
To get decending order we have to do both sort and reverse
a= [2,2,2,44,4,5,6,7]
a.sort()
a.reverse()
print(a)
output = [44, 7, 6, 5, 4, 2, 2, 2]
The above method change the original list. For not changing the original list there is another method 
we have to decleared the variable syntax a = sorted() 
a= [2,2,2,44,4,5,6,7]
s = sorted(a)
print(s)
output = [2, 2, 2, 4, 5, 6, 7, 44]
for reverse also same syntax num = reverse() it will not change the original list'''
# a= [2,2,2,44,4,5,6,7]
# print(a)
# output = [2, 2, 2, 44, 4, 5, 6, 7]
# a.reverse()
# print(a)
# output = [7, 6, 5, 4, 44, 2, 2, 2]

# To do decending order use these method for not changing the original syntax
a= [2,2,2,44,4,5,6,7]
s = sorted(a)
s.reverse()
print(a)
print(s)