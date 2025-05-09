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
# for k,v in marks.items():
#     if v > 35:
#         print(f" pass in {k}:{v}")
#     else:
#         print(f'fail in {k}:{v}')

# Print only the passed subjects.
# for k, v in marks.items():
#     if (v > 35):
#         print(f'{k}')

# Count the number of passed subjects.
# count =0
# for k, v in marks.items():
#     if (v > 35):
#         count = count+1
# print(f'Total number of passed student :{count}')

# Print only the failed subjects.
# for k, v in marks.items():
#     if (v < 35):
#         print(f'{k}')

# Count the number of failed subjects.
# count = 0
# for k,v in marks.items():
#     if (v<35):
#         count = count +1
# print(f"Total failed subject :{count}")

# Print the least scored subject.
# min_score = 33
# for k,v in marks.items():
#     if (v < min_score):
#         print(k)

# Print the highest scored subject.
max_score = float("-inf")
for v in marks.items():
    if v > max_score:
        max_score = v
print(v)