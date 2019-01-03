import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

df=pd.read_csv("Fulldata.csv")
# print(df)
# print(df.head(5))
#
#  plt.figure(figsize=(30,20))
# # plt.savefig("")
#
# sns.countplot(y=df.Nationality, palette="Set2")
# plt.show()
#
# plt.figure(figsize=(30, 20))
# sns.countplot(x="Age", palette="Set2")
a=0.5
b=1
c=1.5
d=2
e=3
df['GK_Shot-Stopper']=(a*df.GK_Positioning+b*df.GK_Diving+c*df.GK_Kicking+d*df.GK_Handling+e*df.GK_Reflexes)
print(df['GK_Shot-Stopper'])
sortedDF= df.sort_values('GK_Shot-Stopper')
top5=sortedDF.tail(5)
print(top5)

X=np.array(list(top5['Name']))
Y=np.array(list(top5['GK_Shot-Stopper']))
# df1=df[['GK_Handling','GK_Diving']]
# print(df1)
sns.barplot(X, Y, palette="colorblind")
plt.ylabel("Shot Stopper Score")

plt.show()