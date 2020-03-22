 
# data: https://ourworldindata.org/coronavirus-source-data
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style="whitegrid")

df22m = pd.read_csv(
"~/Documents/BigData/datasets/SARS-CoV-2/data.europa.eu/full_data_21Mar.csv")

print("Number ofcountries affected: ",len(countries)) # 176

df_nor = df22m[df22m['location']=='Norway']

# data since 31st Jan 2019, 0 values til 26th Feb 2020

# replace 0 with NaN
df_nor2 = df_nor.replace(0,np.nan)

# reseting index from 0 int
df_nor3 = df_nor2.reset_index(drop=True)

# creating MultiIndex for 'date' and 'location' columns:
df_nor4 = df_nor3.set_index(['date','location'])

# removing all NaN values (not from index)
df_nor5 = df_nor4.dropna(how='all', axis=0)

# now the dates start from 27th of Feb
# replace NaN with 0s:
df_nor6 = df_nor5.replace(np.nan, 0)

# convert MultiIndex back to columns:
df_nor6.reset_index(level=df_nor6.index.names ,inplace=True)
#df_nor6.drop(['level_0'],axis=1, inplace=True)
#df_nor6.drop(['index'],axis=1, inplace=True)

# vizualization code:
fig, ax = plt.subplots(figsize=(12, 6))
barwidth=0.5

posit = list(range(len(df_nor6['total_cases']))) 
plt.bar(posit,df_nor6['total_cases'],barwidth,alpha=0.5,
        color='blue', label=df_nor6['date'])

plt.bar([p + barwidth for p in posit], df_nor6['total_deaths'],
        barwidth,alpha=0.5,color='#e33232',
       label=df_nor6['date'])

plt.legend(['total_cases','total_deaths'], loc=10)
ax.set_xticks([p + 1.5 * barwidth for p in posit])
ax.set_xticklabels(df_nor6['date'],rotation=300)
plt.show()
