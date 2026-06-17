import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

#Employ salary
salaries =[22,28,35,42,38,55,48,60,72,85,30,45,52,65,28,34,41,58,75,90]
 
#Central Tendency where is the 'centre' of data?

# mean = np.mean(salaries) #Average
# median = np.median(salaries) #middle value when sorted
# mode = stats.mode(salaries, keepdims=True).mode[0]# most frequent

# print(f'Mean (Average): Rs.{mean:.1f}K')
# print(f'Median (Middle value): Rs.{median}K')
# print(f'Mode (Most common): Rs.{mode}K')



#spread - how varied is data
std = np.std(salaries)
var = np.var(salaries)
rng = max(salaries)-min(salaries)
q1 = np.percentile(salaries,25)
q3 = np.percentile(salaries,75)
iqr = q3-q1

print(f'Std Deviation: {std:.2f}k (most imp spead measure)')
print(f'IQR: {iqr}k (Q1={q1}, Q3={q3})')

#outliner direction using IQr
lower = q1 - 1.5*iqr
upper = q3 + 1.5*iqr
outliners = [x for x in salaries if x < lower or x > upper]
print(f'Outliners: {outliners}')
