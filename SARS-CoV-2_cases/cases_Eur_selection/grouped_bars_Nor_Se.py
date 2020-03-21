 
# grouped bar chart comparing Norway's and Sweden's 
# number of cases
# data from: https://qap.ecdc.europa.eu/public/extensions/COVID-19/COVID-19.html

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df21m = pd.read_csv(
"~/Documents/BigData/datasets/SARS-CoV-2/data.europa.eu/selected_EURareas.csv")

fig, ax = plt.subplots(figsize=(12, 6))
barwidth=0.3
position = list(range(len(df21m['Norway']))) 

plt.bar(position,df21m['Norway'],barwidth,alpha=0.5,color='#592121',
       label=df21m['date'])

plt.bar([p + barwidth for p in position], df21m['Sweden'],
        barwidth,alpha=0.5,color='#e36e07',
       label=df21m['date'])

## optional third country:
# plt.bar([p + barwidth*2 for p in position], 
# df21m['Poland'],barwidth,
#        alpha=0.5,color='#0e8041', label=df21m['date'])
# add 'Poland' to legend:

plt.legend(['Norway','Sweden'], loc=10)
ax.set_xticks([p + 1.5 * barwidth for p in position])
ax.set_xticklabels(df21m['date'],rotation=90)
plt.show()
