import matplotlib.pyplot as plt
import pandas as pd
import pickle

df = pd.read_csv('../data/augmented_small_df.csv')
percent = 0.1

df = df.sort_values(['views'],ascending = 0)
y_line = df.iloc[int(percent*0.01*df.shape[0]-1)]["views"]

df = df.sort_values(['impact'],ascending = 0)
x_line = df.iloc[int(percent*0.01*df.shape[0]-1)]["impact"]

df = df[df.views<25000]
df = df[df.impact<20000000]

year_08 = []
year_11 = []
year_13 = []
year_15 = []
year_17 = []

for index,row in df.iterrows():
    t = []
    t.append(row["impact"])
    t.append(row["views"])
    if row["creation_date"] == 2008:
        year_08.append(t)
    elif row["creation_date"] == 2011:
        year_11.append(t)
    elif row["creation_date"] == 2013:
        year_13.append(t)
    elif row["creation_date"] == 2015:
        year_15.append(t)
    elif row["creation_date"] == 2017:
        year_17.append(t)

years = [year_08, year_11, year_13, year_15, year_17]

fig = plt.figure(figsize=(6,5))
plt.rcParams.update({'font.size': 10})
ax = fig.add_subplot(1, 1, 1)

colors = ["#f4320c","#FF81C0","#0343df","#028f1e","#ff9408"]
for i in range(len(years)):
    plt.plot([idx[0]/float(1000000) for idx in years[i]], [idx[1] for idx in years[i]],linestyle='None',markersize=3, marker='o', color=colors[i], alpha = 0.6)

plt.axvline(x = x_line/float(1000000),color="black", linewidth=1)
plt.axhline(y = y_line,color="black", linewidth=1)

leg = ax.legend(['2008-2010','2011-2012','2013-2014','2015-2016','2017-2018'], fancybox=True,frameon=1, loc=1,markerscale=2)
w = 1
leg.get_frame().set_linewidth(w)
leg.get_frame().set_edgecolor('black')

axes = plt.gca()
ax.set_xscale('linear')
ax.set_xlabel('Impact Score (x $10^6$)')
ax.set_ylabel('Popularity Score')
ax.tick_params(direction='in')

fname = "plot_latest_reversed.png"
plt.savefig(fname, dpi=1000)
