import matplotlib.pyplot as plt
import numpy as np

# X1=np.random.randn(100,100)
#
# print(X)
# plt.hist(X,100)
A=[1,2,3]
B=[10,2,3]

sales={"2015":50, "2016":120, "2017":30}
# plt.bar(0, sales["2015"])
for i , key in enumerate(sales):
    plt.bar(i,sales[key])

plt.show()