# stacked barplots of current and new cases of 
# contaminated individuals in Poland
# SARS-Cov-2 virus triggers COVID-19 disease

import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

pldata20M = pd.read_csv(
"~/Documents/BigData/datasets/SARS-CoV-2/Poland_cases/pl_cases_csv/pl_cases_20Mar_desc.csv")

f, ax = plt.subplots(figsize=(12, 8))

sns.set(style="whitegrid")
sns.set_color_codes("dark")
sns.barplot(x="current", y="date", data=pldata20M,
            label="so far", color="blue")

sns.set_color_codes("dark")
sns.barplot(x="new_cases", y="date", data=pldata20M,
            label="new", color="orange")

ax.legend(ncol=2, loc="lower right", frameon=True)
ax.set(xlim=(0, 400), ylabel="",
       xlabel="Coronavirus cases in Poland on 20th March 2020")
sns.despine(left=True, bottom=True)
