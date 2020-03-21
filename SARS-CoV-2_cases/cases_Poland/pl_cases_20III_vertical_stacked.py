# vertical barplots of current and new cases of 
# contaminated individuals in Poland 
# for 20th March 2020

import pandas as pd
from matplotlib import pyplot as plt
import matplotlib as mpl
import seaborn as sns

plcovdata = pd.read_csv("~/Documents/BigData/datasets/SARS-CoV-2/Poland_cases/pl_cases_csv/pl_cases_20Mar.csv")

plcovdata["total"] = plcovdata.current + plcovdata.new_cases
sns.set_style("whitegrid")
sns.set_context({"figure.figsize": (20, 16)})

sns.barplot(x = plcovdata.date, y = plcovdata.total, color = "#a65332") # reddish
cur_plot = sns.barplot(x = plcovdata.date, y = plcovdata.current, color = "#3a5e85") # blue

curr = plt.Rectangle((0,0),1,1,fc='#3a5e85')
new = plt.Rectangle((0,0),1,1,fc="#a65332")


lgnd = plt.legend([curr, new], ['current', 'new cases'],
                  ncol = 1, loc='center', fontsize='24')
lgnd.draw_frame(False)

sns.despine(left=True)
cur_plot.set_ylabel("number of cases",fontsize=30)
cur_plot.set_xlabel("")

plt.tick_params(labelsize=25)
plt.xticks(rotation=55)
 
