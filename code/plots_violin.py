# Run on Python 3
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import csv,os

debugPrinting=True

# Part 1 - Get a subset of the data, which is to be used
if not os.path.exists('augmented_3_8mil_distribution_df.csv'):
	fname = "../data/augmented_small_df.csv"
	df = pd.read_csv(fname)

	source_df = df[['num_Necromancer_badges','num_Populist_badges','num_Good_Answer_badges','num_Enlightened_badges','num_Revival_badges','views','impact']]
	source_df.to_csv('augmented_3_8mil_distribution_df.csv')
	if debugPrinting:
		print("Done generating augmented_3_8mil_distribution_df.csv")

# Part 2 - Convert this in plottable format 
if not os.path.exists('popularity_to_plot.csv'):
	fname = "augmented_3_8mil_distribution_df.csv"
	df = pd.read_csv(fname)

	df['log_views'] = (df['views'] + 1).apply(np.log)
	df['log_impact'] = (df['impact'] + 1).apply(np.log)

	y_s = ['impact','popularity']

	col=['yFactor','Has_bool','Badge']
	data_popularity = []
	data_impact = []
	counter=0
	counter_m=0
	for index, row in df.iterrows():
		counter_m+=1
		try:
			yf = row['log_views']
			yf_2 = row['log_impact']

			if(row['num_Populist_badges']>0):
				data_popularity.append([yf,'True','Populist'])
			else:
				data_popularity.append([yf,'False','Populist'])

			if(row['num_Revival_badges']>0):
				data_impact.append([yf_2,'True','Revival'])
			else:
				data_impact.append([yf_2,'False','Revival'])

			if(row['num_Enlightened_badges']>0):
				data_popularity.append([yf,'True','Enlightened'])
				data_impact.append([yf_2,'True','Enlightened'])
			else:
				data_popularity.append([yf,'False','Enlightened'])
				data_impact.append([yf_2,'False','Enlightened'])

			if(row['num_Necromancer_badges']>0):
				data_popularity.append([yf,'True','Necromancer']) 
				data_impact.append([yf_2,'True','Necromancer']) 
			else:
				data_popularity.append([yf,'False','Necromancer'])
				data_impact.append([yf_2,'False','Necromancer'])

			if(row['num_Good_Answer_badges']>0):
				data_popularity.append([yf,'True','Good Answer'])
				data_impact.append([yf_2,'True','Good Answer'])
			else:
				data_popularity.append([yf,'False','Good Answer'])
				data_impact.append([yf_2,'False','Good Answer'])
			
		except:
			counter+=1

	print("Counter of fail "+str(counter)+" percentage: "+str(counter/counter_m))
	df = pd.DataFrame(data_popularity, columns=col)
	df.to_csv('popularity_to_plot.csv')

	df = pd.DataFrame(data_impact, columns=col)
	df.to_csv('impact_to_plot.csv')

	if debugPrinting:
		print("Done generating popularity_to_plot.csv and impact_to_plot.csv")

# Part 3 - Plot
def plot(output,whichy,xlabels=None):
	df = pd.read_csv(whichy+"_to_plot.csv")

	if(debugPrinting==True):
		print(df)

	cpalette=["#ff9408","#028f1e"]
	sns.set_palette(cpalette)

	fig, ax = plt.subplots(figsize=(20,10))

	ax = sns.violinplot(x="Badge", y="yFactor", hue="Has_bool",data=df, split=True)

	s=30
	if(whichy=="popularity"):
	  ax.set_ylabel('Popularity Score (log)', fontsize=s)
	else:
	  ax.set_ylabel('Impact Score (log)', fontsize=s)
	ax.set_xlabel('')
	plt.xticks(size=s)
	plt.yticks(size=s)

	plt.setp(ax.collections, alpha=.8)
	if(whichy=="popularity"):
		new_xticklabels = ['Populist\nBadge', 'Enlightened\nBadge', 'Necromancer\nBadge', 'Good Answer\nBadge']
	else:
		new_xticklabels = ['Revival\nBadge', 'Enlightened\nBadge', 'Necromancer\nBadge', 'Good Answer\nBadge']

	ax.set_xticklabels(new_xticklabels)

	#Making Legend Opaque
	leg = ax.legend(fancybox=True,frameon=1, loc='upper center', fontsize=s, bbox_to_anchor=(0,1.03,1,0.2))
	leg.get_frame().set_alpha(1.0)
	leg.get_frame().set_linewidth(1)
	leg.get_frame().set_edgecolor('black')

	# Rect -> left, bottom, right top
	fig.tight_layout(rect=[0, 0 , 1, 0.85])

	#Saving the Plot
	plt.savefig('plots_'+str(output)+'.pdf')
	plt.close('all')

if __name__=='__main__':
	plot("impact_violin","impact")
	plot("popularity_violin","popularity")
