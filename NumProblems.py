import numpy as np

arr = np.loadtxt("data.txt")
print(arr)
print(arr.shape)
print()

r=len(arr)
c=len(arr[0])
sum=0
for i in range(r):
    for j in range(c):
        if (i == 0):
            sum += arr[i][j]
            print(sum)
            print()
        elif (j == 0):
            sum += arr[i][j]
            print("it",sum)
        elif (j == c - 1):
            sum += arr[i][j]
            print("i", sum)
        elif (i == r- 1):
            sum += arr[i][j]
            print("sum",sum)
            print()
print("Total sum:",sum)