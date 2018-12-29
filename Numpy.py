import numpy as np

numbers=[10,20,30]
print(numbers)

arr= np.array([10,20])
print(arr)
print(type(arr))

arr2=np.array((10,20))
print(arr2)
print(type(arr2))

arr3= np.array({'a':10,'b':20})
print(arr3)
print(type(arr3))

# 3-D
arr4= np.array([[[1,2,3],[4,5,6],[7,8,9]],[[1,2,3],[4,5,6],[7,8,9]]])
print(arr4)
print(type(arr4))
print(arr4.shape)