import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
os.chdir("C:/Users/11877/Desktop/IBI/Practical")
covid_data = pd.read_csv("full_data.csv")

print(covid_data.iloc[0:11:2,0:5])

my_column = [False,False,False,False,True,False]
row = []
for i in covid_data.iloc[0: ,1]:
    if i == "Afghanistan":
        row.append(True)
    else:
        row.append(False)
print(covid_data.iloc[row,my_column])

my_column = [False,False,True,False,False,False]
row = []
for i in covid_data.iloc[0: ,1]:
    if i == "World":
        row.append(True)
    else:
        row.append(False)
world_new_cases = covid_data.iloc[row,my_column]
print(world_new_cases.mean())
print(world_new_cases.median())

my_column = [True,False,True,True,False,False]
world_cases = covid_data.iloc[row,my_column]
plt.boxplot(world_cases.loc[0:, "new_cases"],vert=True,whis=1.5)
plt.title('new cases worldwide')
plt.ylabel('number')
plt.xticks([])
plt.show()

plt.plot(world_cases.loc[0:, "date"],world_cases.loc[0:,"new_cases"],"r")
plt.plot(world_cases.loc[0:, "date"],world_cases.loc[0:,"new_deaths"],"b")
plt.xticks(world_cases.iloc[0:len(world_cases):4,0],rotation=-90) #plt.xticks(world_cases.iloc[0:91:4,0],rotation=-90) is ok
plt.ylabel('number')
plt.xlabel('date')
plt.title('new cases and new deaths worldwide')
plt.show()

row = []
for i in covid_data.iloc[0: ,0]:
    if i == "2020-03-14":
        row.append(True)
    else:
        row.append(False)
task = covid_data.iloc[row,4]
plt.boxplot(task,patch_artist=True)
plt.title('total case numbers on 14 March 2020')
plt.ylabel('number')
plt.xticks([])
plt.show()
