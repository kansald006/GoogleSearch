import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

table=pd.read_csv("Cuntries.csv")
# print(table.describe())
table1 = table.loc[:,["Country","GDP"]]
table1=table1.sort_values("GDP")
table1=table1.dropna()
print(table1)
table2=table1.tail(5)
X = np.array(list(table2["Country"]))
Y = np.array(list(table2["GDP"]))
sns.barplot(X, Y, palette="colorblind")
plt.show()