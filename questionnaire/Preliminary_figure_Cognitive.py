import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib_style
import seaborn as sns

path = '/Users/sprout/OneDrive - 名古屋工業大学/学校/研究室/実験/予備実験/20211108/fusion_tsuruoka_tanada_20211112_2.xlsx'
data = pd.read_excel(path)

def fig(index:str,ylabel:str,min:int=9999,max:int=9999,participant:str=1):
	figx = 12
	figy = 7

	ddd = data[index].values
	dddd = []
	for i in range(4):
		dddd.append(ddd[3*i+participant])
	condition = ['without feedback','with feedback','partner velocity','robot velocity','partner + robot velocity']
	dddd = [dddd[0],np.mean(dddd[1:4]),dddd[1],dddd[2],dddd[3]]
	dddd_df = pd.DataFrame({'condition':condition,ylabel:dddd})

	sns.set_palette('Set3')
	plt.figure(figsize=(figx, figy))
	ax = sns.barplot(x='condition',y=ylabel,data=dddd_df)
	if not min == 9999 and not max==9999:
		plt.ylim(min,max)
	elif not max == 9999:
		plt.ylim(0,max)
	plt.xticks(rotation=45)
	plt.savefig('questionnaire/graph/Preliminary experiment/'+ylabel+'.jpg',dpi=300, format='jpg', bbox_inches='tight')

	print('finish   :   ' + ylabel)

def fig_MS(ylabel:str,level:str,min:int=9999,max:int=9999,participant:str=1):
	figx = 12
	figy = 7

	dddd = []
	ms = []
	condition = []
	ddddd = []

	for j in ['owner-ship','ownership-control','agency','agency-control']:
		ddd = data[j].values
		for i in range(4):
			dddd.append(ddd[3*i+participant])
		for k in range(5):
			ms.append(j)
			if k == 0:
				condition.append('without feedback')
				ddddd.append(dddd[0])
			elif k == 1:
				condition.append('with feedback')
				ddddd.append(np.mean(dddd[1:4]))
			elif k == 2:
				condition.append('partner velocity')
				ddddd.append(dddd[1])
			elif k == 3:
				condition.append('robot velocity')
				ddddd.append(dddd[2])
			elif k == 4:
				condition.append('partner + robot velocity')
				ddddd.append(dddd[3])
		dddd = []
	dddd_df = pd.DataFrame({'condition':condition,ylabel:ddddd,'':ms})

	sns.set_palette('Paired')
	plt.figure(figsize=(figx, figy))
	ax = sns.barplot(x='condition',y=ylabel,hue='',data=dddd_df)
	if not min == 9999 and not max==9999:
		plt.ylim(min,max)
	elif not max == 9999:
		plt.ylim(0,max)
	plt.xticks(rotation=45)
	lg = plt.legend(loc='upper right', bbox_to_anchor=(0.75, 0.5, 0.5, .100), borderaxespad=0.,)
	plt.savefig('questionnaire/graph/Preliminary experiment/' + level +ylabel+'.jpg',dpi=300, format='jpg', bbox_extra_artists=(lg,), bbox_inches='tight')

	print('finish   :   ' + level + ylabel)
	

accuracy = fig(index='accuracy-score',ylabel='accuracy score',min=0,max=5)
tasktime = fig(index='TaskTime',ylabel='task time [s]',max=14)
tlx_b = fig(index='TLX-SCORE',ylabel='Beginner WWL',max=100)
tlx_e = fig(index='TLX-SCORE',ylabel='Expert WWL',max=100,participant=2)
ios_b = fig(index='we-mode-score',ylabel='Beginner Inclusion of Other in the Self',max=7.8)
ios_e = fig(index='we-mode-score',ylabel='Expert Inclusion of Other in the Self',max=7.8,participant=2)
ms_b = fig_MS(ylabel='Rating Score',level='Beginner ')
ms_e = fig_MS(ylabel='Rating Score',level='Expert ',participant=2)