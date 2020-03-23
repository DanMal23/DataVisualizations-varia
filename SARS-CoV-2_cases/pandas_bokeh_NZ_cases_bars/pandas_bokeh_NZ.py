 
# ******* pandas_bokeh library used *********
import pandas as pd
import numpy as np
import pandas_bokeh

df23March = pd.read_csv(
"~/Documents/BigData/datasets/SARS-CoV-2/world_data/full_data.csv")

df_nz = df23March[df23March['location']=='New Zealand']
df_nz

# data has 0 values from 31st Jan 2019 til 27th Feb 2020

# replace 0 with NaN
df_nz2 = df_nz.replace(0,np.nan)

# reseting index from 0 int
df_nz3 = df_nz2.reset_index(drop=True)

# creating Index for 'date' columns:
df_nz4 = df_nz3.set_index(['date','location'])

# removing all NaN values (not form index)
df_nz5 = df_nz4.dropna(how='all', axis=0)

# now the dates start from 28th of Feb
# replace NaN with 0s:
df_nz6 = df_nz5.replace(np.nan, 0)

# convert MultiIndex back to columns:
df_nz7 = df_nz6.reset_index(level=df_nz6.index.names ,inplace=True)
df_nz6

# horizontal grouped bars

p_hbar = df_nz6.plot_bokeh(
kind="barh",
x=df_nz6['date'], # x="date"
xlabel="numbers",
ylabel="",
title="Cases of coronavirus in New Zealand - interactive chart",
alpha=0.6,
legend = "bottom_right")

# stacked horizontal bars:

p_stacked_hbar = df_nz6.plot_bokeh.barh(
x="date",# 'date' is not an index here
stacked=True,
xlabel="number of cases",
ylabel="",
title="New Zealand's cases",
alpha=0.6,
legend = "bottom_right")

# simple grouped bar
df_nz6.plot_bokeh(kind="bar", figsize=(500, 200),
sizing_mode="scale_width",legend = "top_left")
