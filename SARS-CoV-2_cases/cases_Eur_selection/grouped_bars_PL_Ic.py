 
# grouped bar chart comparing Poland's and Iceland's 
# number of Coronavirus cases up to 21th March
# data from: https://qap.ecdc.europa.eu/public/extensions/COVID-19/COVID-19.html

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df21m = pd.read_csv(
"~/Documents/BigData/datasets/SARS-CoV-2/data.europa.eu/selected_EURareas.csv")

fig, ax = plt.subplots(figsize=(12, 6))
barwidth=0.3
position = list(range(len(df21m['Iceland']))) 
plt.bar(position,df21m['Iceland'],barwidth,alpha=0.5,color='blue',
       label=df21m['date'])

plt.bar([p + barwidth for p in position], df21m['Poland'],barwidth,
        alpha=0.5,color='red',label=df21m['date'])

plt.legend(['Iceland', 'Poland'], loc=10)
ax.set_xticks([p + 1.5 * barwidth for p in position])
ax.set_xticklabels(df21m['date'],rotation=90)
plt.show()
