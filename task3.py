# -*- coding: utf-8 -*-
"""
Created on Tue Dec 21 17:23:14 2021

@author: ahmed samir
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.impute import SimpleImputer

##################### 1 #####################
dataset=pd.read_csv("Wuzzuf_Jobs.csv")

##################### 2 #####################
#Display structure by level
dataset.describe()

##################### 3 #####################
dataset.sort_values("Title", inplace = True)
dataset.drop_duplicates(subset = ["Title","Company","Location","Type","Level","YearsExp","Country","Skills"],keep = "first", inplace = True)

X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 7].values

imputer = SimpleImputer(missing_values = "", strategy = 'most_frequent')
imputer = imputer.fit(X[:, 0:7])
X[:, 0:7] = imputer.transform(X[:, 0:7])

##################### 4 #####################
x=dataset['Company'].value_counts()
x

##################### 5 #####################
plt.pie(x)
plt.show() 

##################### 6 #####################
x=dataset['Title'].value_counts()
x
list(x.keys())[0]

##################### 7 #####################
keys = list(x.keys())
values = list(x)
keys
values
# creating the bar plot
plt.bar(keys, values, color ='maroon',width = 0.4)

plt.xlabel("Courses offered")
plt.ylabel("No. of students enrolled")
plt.title("Students enrolled in different courses")
plt.show()

##################### 8 #####################
country_sort=dataset['Country'].value_counts()
country_sort

##################### 9 #####################
keys = list(country_sort.keys())
values = list(country_sort)
keys
values
# creating the bar plot
plt.bar(keys, values, color ='maroon',width = 0.4)

plt.xlabel("Countries")
plt.ylabel("No. of employees in country")
plt.title("employees working in different countries")
plt.show()

#####################  10 #####################
skill_sort=dataset['Skills'].value_counts()
skill_sort


###############################  Finished  #################################


