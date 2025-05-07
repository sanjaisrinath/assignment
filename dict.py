'''dictoniary has been written in {}
it has key and values eg : "first" : "sanjai"
it is muteable we can change data 
"in" operation is also can be used and "not" operation also used 
dictoniary can be written in 2 ways for this "dict" property is used 
'''
'''s = dict([("first","san"),("last","see")])
print(s)
output = {'first': 'san', 'last': 'see'}
# another type
a = dict(f='sss',s="eee",d="www")
print(a)
output = {'f': 'sss', 's': 'eee', 'd': 'www'}
set = {
    "firstname" :"sanjai",
    "age" : 34,
    "last" : 'sri',
    "color" : "red"
}
'''
'''# to change some value of key syntax  set["firstname"] = "srinath"
# set["firstname"] = "srinath"
# print(set)
# output = {'firstname': 'srinath', 'age': '34', 'last': 'sri'}
# to add some keys we use syntax set['address'] = tn
set['address'] = "TN"
# print(set)
# output = {'firstname': 'sanjai', 'age': '34', 'last': 'sri', 'address': 'TN'}

# to delete some value syntax del set["age"]
del set["age"]
print(set)
output = {'firstname': 'sanjai', 'last': 'sri', 'address': 'TN'}

# to sort the values first we have to create an empty variable it will sort only key no values syntax sorted(set)
set2 = sorted(set)
print(set2)
output = ['address', 'firstname', 'last']

for loop also be used for that "item" is used  syntax  k means key and v means value'''
# for k,v in set.items():
#     # print(k)
# # output = firstname
# # age
# # last
#     print(v)
# output = sanjai
# 34
# sri

# enumerate also can be used 
# for k,v in enumerate(set):
#     print(k)

# person = {
#             "firstName" : "Harry",
#             "lastName" : "Potter",
#             "age":30,
#             "gender": "male",
#             "skill" : "ReactJS",                                
#             "expertise": "Beginner"
# }
# # Print the firstname.
# # Print the lastname.
# # Print the fullname("Harry Potter").
# # If the age is less than 18, then print "false". If the age is more than 18, then print "true".
# print(person["firstName"])
# print(person['lastName'])
# print(f'{person["firstName"]} {person['lastName']}')

# if person["age"] >  18:
#     print("true")
# else:
#     print("false")


marks = {
    "maths" : 34,
    "english" : 56,
    "science": 32,
    "hindi" : 75,
    "social science": 65
}
                        
'''Print the marks of all the subjects.
Print the names of all the subjects from the given object.
Count the number of subjects from the given object.
Print the percentage of the marks of the student.
Print only those subjects where the student scored more than 35.
Print the pass/fail status of the subjects provided 35 is the pass mark.
Print only the passed subjects.
Count the number of passed subjects.
Print only the failed subjects.
Count the number of failed subjects.
Print the least scored subject.
Print the highest scored subject.
Check whether the student has passed in all the subjects or not.
Take the subject name from the student through prompt box and print the subject marks and pass/fail status.'''

# Print the marks of all the subjects.
# count =0
# for k,v in marks.items():
#     print(f"{k}:{v}")
      
# Print the names of all the subjects from the given object
# Count the number of subjects from the given object.
# for k,v in marks.items():
#     print(k)
#     count = count+1
# print(f"total subject :{count}")


# Print only those subjects where the student scored more than 35.
# for k,v in marks.items():
#     if (v >35):
#         print(v)

# Print the pass/fail status of the subjects provided 35 is the pass mark.
for k,v in marks.items():
    if v > 35:
        print(f" pass in {k}:{v}")
    else:
        print(f'fail in {k}:{v}')




    



