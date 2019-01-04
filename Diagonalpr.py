import numpy as np

arr= np.loadtxt("data.txt")
print(arr)

r= len(arr)
c= len(arr[0])
list1=[]
list2=[]

for i in range(r):
    for j in range(c):
        if (i==j):
           list1.append(int(arr[i][j]))
        if(i+j==r-1):
            list2.append(int(arr[i][j]))


list3=int(''.join(str(e) for e in list2),2)
print(list3)
list4=int(''.join(str(e) for e in list1),2)
print(list4)
sum=list3+list4
print("Sum of Diagonals is:",sum)