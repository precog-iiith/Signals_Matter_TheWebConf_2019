import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import scipy.stats
import scipy.stats as stats

df = pd.read_csv('../data/augmented_combined_df.csv')
percentile = 0.1
thres_impact = np.percentile(df['impact'], 100 - percentile)
thres_views = np.percentile(df['views'], 100 - percentile)
poor_idx = (df['views'] < thres_views) & (df['impact'] < thres_impact)
rich_idx = (df['views'] >= thres_views) & (df['impact'] >= thres_impact)
impactful_idx = (df['views'] < thres_views) & (df['impact'] >= thres_impact)
popular_idx = (df['views'] >= thres_views) & (df['impact'] < thres_impact)

all_badges = ['num_Necromancer_badges']

poor_df = df[poor_idx]
rich_df = df[rich_idx]
impactful_df = df[impactful_idx]
popular_df = df[popular_idx]

for badge in all_badges:
    lim = min(50, df[badge].max())
    bins = np.linspace(-1, lim, lim + 1)

    n, x, _ = plt.hist(poor_df[badge], bins=bins, alpha=0.3, label="poor", weights=np.ones_like(poor_df[badge])/len(poor_df[badge]), histtype='step')
    plt.gcf().clear()
    print(x)
    print(n)
    plt.plot(x[1:], n)
    plt.legend(loc="upper right")
    plt.savefig('hist_' + badge + '.pdf')
