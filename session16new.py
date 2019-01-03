import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

table = pd.read_csv("Citytemps.csv",index_col='Month')
table1=table[:12]
table1=table1.drop('Year',axis=1)
print(table1)
print(type(table1))

table1.plot()
plt.ylabel("Temps in City")
plt.show()