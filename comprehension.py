# comprehension is used in real world 

# list comprehension is used to write code effectively.

# a = [2,3,4,5,6]
# b = [z*2 for z in a]
# b = [c*2 for c in range(0,6)]
# print(b)

# set comprehension 
# sett = {a for a in "sanjai" if a not in "srinath"}
# print(sett)

# dictoniery  comprehension
# dic = {a:a**3 for a in range(1,10) if a>2}  a refers to key not values
# print(dic)

# zip format 
a  = ["Name","college","Age"]
b =["sanjai","FAU",24]
for k,v in zip(a,b):
    print(" {0}  {1}".format(k,v))