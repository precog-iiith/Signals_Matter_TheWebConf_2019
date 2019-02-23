import pandas as pd
from scipy.stats import ttest_ind, ttest_ind_from_stats
import random

df = pd.read_csv('../data/augmented_combined_df.csv')

percent = 0.1

df = df.sort_values(['views'],ascending = 0)
hp_line = df.iloc[int(percent * 0.01 * df.shape[0] - 1)]["views"]

df = df.sort_values(['impact'],ascending = 0)
hi_line = df.iloc[int(percent * 0.01 * df.shape[0] - 1)]["impact"]

categories = []
for index, row in df.iterrows():
    if row["impact"] >= hi_line and row["views"] >= hp_line:
        categories.append(1)

    elif row["impact"] < hi_line and row["views"] >= hp_line:
        categories.append(2)

    elif row["impact"] < hi_line and row["views"] < hp_line:
        categories.append(3)

    elif row["impact"] >= hi_line and row["views"] < hp_line:
        categories.append(4)

df['category'] = categories

rep_HPHI = df.loc[df['category'] == 1]
print(len(rep_HPHI))
rep_HPHI_list = rep_HPHI['reputation'].tolist()

rep_LPLI = df.loc[df['category'] == 3]
print(len(rep_LPLI))
rep_LPLI_list = rep_LPLI['reputation'].tolist()
rep_LPLI_list = random.sample(rep_LPLI_list, len(rep_HPHI_list))

t, p = ttest_ind(rep_HPHI_list, rep_LPLI_list, equal_var=False)
print("ttest_ind:            t = %g  p = %g" % (t, p))

HPLI_feature_list = rep_HPLI[feature].tolist()
LPHI_feature_list = rep_LPHI[feature].tolist()
HPLI_feature_list = random.sample(HPLI_feature_list, len(LPHI_feature_list))
t, p = ttest_ind(LPHI_feature_list, HPLI_feature_list, equal_var=False)
print("ttest_ind:            t = %g  p = %g" % (t, p))
print("Mean LPHI_feature_list  ", np.mean(LPHI_feature_list))
print("Mean HPLI_feature_list  ", np.mean(HPLI_feature_list))
