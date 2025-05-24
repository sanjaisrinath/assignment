import numpy as np



a = np.array([(1,2,3,4,5),(9,5,56,6,7),(2,4,5,6,7)],dtype=float)
print (a.shape)
print (type(a))
print(a)

#zeros in starting array
z = np.zeros((2,4))
print(z)

# ones in starting array
x = np.ones((3,3))
print(x)

 #array of evenly spaced values ------ specifying the number of steps required
e = np.arange(20,50,3)
print(e)
