a =  "python is Easy language"
# s = a.capitalize()  -- make the first letter of the sentence into capital and if some letter in capital it will make them small 
# print(s) output -- Python is easy language

# s = a.title() -- it makes first letter of the word into capital in the sentence
# print(s) output --Python Is Easy Language

# s = a.upper()  -- makes all letter of the sentence into capital
# print(s) output - PYTHON IS EASY LANGUAGE

# s = a.lower() -- makes all letter into smaller in the sentence
# print(s) output -- python is easy language

# s = a.startswith("python") -- we can find the starting word of the sentence it will not take second word of the sentence  the output will be true or false
# print(s) output -- true
# s= a.startswith("E")
# print(s) output -- False

# s= a.endswith("y language")  -- it will check the last word of the sentence present or not 
# print(s) output --  True
# s= a.endswith("y")
# print(s) output -- False

# s= a.find("thon") -- it will find the values present in the string or not if it is present it will give the idex value of the searched word 
# if it is not present in the string the output will be -1.
# print(s) output -- 2 
# s= a.find("x")
# print(s) output = -1

# s=a.index("p") -- find and index are but the if the value is not present in the string it will give error in the output 
# but in find it will give -1 in output
# print(s) output = 0
# s= a.index("w")
# print(s)
# output -     s= a.index("w")
#        ^^^^^^^^^^^^
# ValueError: substring not found

# s = a.rfind("e")  -- it will give last word of the  index value of the sentence if search value is not present in the string the output will be -1
# print(s) -- output == -1
# s= a.rindex("y") -- it will give last word of the index value of the sentece if search value (substring) is not present in the string output will be error
# print(s)

# s=a.count("a") -- it will count the letters present in string 
# print(s) -- 3

# x= "sanjai"
# y= "srinath"
# print("the {0} is {1}".format(x,y))

# s = "sanjai"
# a = '/'.join(s)
# print(a)  output -- s,a,n,j,a,i

# str1 = 'sanjai' -- remove the prefix of entered substring
# str2 = str1.removeprefix('sa')
# print(str2) output -- njai

# str3 = "sanjai" -- remove the suffix of enteredd substring
# str4 = str3.removesuffix("i")
# print(str4) output -- sanja


# str1 = 'sanjai' -- it will replace all letters which we entered 
# str2 = str1.replace('a','A') -- 1st is replaced words and 2nd is what to replace
# print(str2) output -- sAnjAi

# a = 'sanjaisrinath'
# b= a.split(',', maxsplit=3)
# print(b)

a = 'hello    '
b= a.strip() -- remove the white space 
print(b)
print(len(b))

