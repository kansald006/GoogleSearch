import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

table=pd.read_csv("Cuntries.csv")
# print(table.describe())
table1 = table.loc[:,["Country", "LandArea"]]
# table1== table1.index.rename('Country',inplace=True)
print(table1)
list1=[]
for row in table1.itertuples():
    if row[2] > 2000:
        print(row)
        list1.append(row[1:])
print()
print(list1)
print(type(list1))
X,Y= zip(*list1)
plt.plot(X, Y)
plt.show()
# for i, key in enumerate(row):
#     # print(i, key)
#     plt.bar(i, row[key])
# X = np.arange(len(row))
# plt.xticks(X, row.keys())
#
# plt.show()