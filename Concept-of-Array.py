# Concept of Array 
#different types of array
import numpy as np
array=np.array([12,3,4,5,66,6,])
print(array)

# 2d Array Concept in Numpy

import numpy as np
array=np.array([[1,2,3],
                [11,22,33],
                [22,33,44]])
print(array)


import numpy as np

# Array banana
arr = np.array([10, 20, 30, 40, 50])

print("Array:", arr)
print("Sum:", np.sum(arr))
print("Average:", np.mean(arr))
print("Max:", np.max(arr))
print("Min:", np.min(arr))

import numpy as np
array=np.array([[1,2,3],
[1,2,3],
[1,2,3]])

print(array)  

# Common Array Creation Functions

# zeros
import numpy as np
print(np.zeros(4))


import numpy as np
a = np.array([10, 20, 30])
print(np.zeros((2,3)))

# ones

import numpy as np
print([np.ones(4)]) 


import numpy as np
a = np.array([10, 20, 30])
print(np.ones((2,3)))

# full

import numpy as np

print(np.full((2,3),7))


import numpy as np
a = np.array([10, 20, 30])
print(np.full((2,3),7))


# eyes

import numpy as np
data=np.array([12,13,1414,155])

print((np.eye(3)))

# Array Properties

import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6]])

print(arr.shape)
print(arr.size)
print(arr.dtype)

# Mathematical Operations

import numpy as np
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(a + b)
print(a * b)
print(a ** 2)


# Statistical Functions

import numpy as np
data = np.array([10, 20, 30, 40])

print(np.mean(data))
print(np.sum(data))
print(np.max(data))
print(np.min(data))