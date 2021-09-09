"""
TSF GRIP September 2021
Author : Harshit Tyagi
Scores Prediction Based on study hours per day
"""
import math
import seaborn as sb
import pandas as pd
import numpy as np
import matplotlib.pyplot as mpt
import word2number.w2n
from openpyxl.workbook import Workbook
from scipy import stats
from sklearn import linear_model

#Score prediction

df4 = pd.read_csv('Tsf Dataset.csv', index_col=False)
#df4.set_index('Hours', inplace=True)
print(df4.to_markdown())
mpt.xlabel('Study (hours/day)')
mpt.ylabel('Score')
mpt.title('Student Progress Graph')

#plotting scatter plot graph of given dataset.
mpt.scatter(df4.Hours, df4.Scores, marker="+", color='g')
#creating regression object
reg = linear_model.LinearRegression()
reg.fit(df4[['Hours']], df4.Scores)
print("\n\nThe predicted score for the student who study for 9.25 hrs/day is ", float(reg.predict([[9.25]])))
mpt.show()
