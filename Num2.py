import numpy as np

# arr=np.array([[[1,2,3],[4,5,6],[7,8,9]],[[1,2,3],[4,5,6],[7,8,9]]])
# print(arr[0:2,0:2,0:2])

arr = np.loadtxt("data.txt")
print(arr)
print(arr.shape)


#
# arr1=arr[::-1]
# print(arr1)
# print()
# print(len(arr))

print()
arr2=[]
print(type(arr2))
# for list in arr:
#     for x in list:
#          print (x)


for i in range(2,-1,-1):
     for j in range(0,3,1):
         print(i,j)

         c= arr[i,j]
         arr2.append(c)
         arr3=np.asarray(arr2)
         a1=arr3[0:3]
         a2=arr3[3:6]
         a3 =arr3[6:9]
         a4=np.matrix([a1,a2,a3])
         print(a4)
         print()
         print()
         print(a1)

      #    j-=1
      # i+=1
print(arr2)
print(arr3)
print()
for i in range(0,3,1):
     for j in range(2,-1,-1):
         print(i,j)
