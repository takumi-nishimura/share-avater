from ast import Str
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib_style
import seaborn as sns

path = '/Users/sprout/OneDrive - 名古屋工業大学/学校/研究室/実験/予備実験/20211108/fusion_tsuruoka_tanada_20211112_2.xlsx'
data = pd.read_excel(path)

def fig(index:str,ylabel:str,filename:str,min:int=9999,max:int=9999,participant:str=1):
	figx = 12
	figy = 7

	ddd = data[index].values
	dddd = []
	for i in range(4):
		dddd.append(ddd[3*i+participant])
	condition = ['without feedback','partner velocity','robot velocity','partner + robot velocity']
	dddd = [dddd[0],dddd[1],dddd[2],dddd[3]]
	dddd_df = pd.DataFrame({'Condition':condition,ylabel:dddd})

	sns.set_palette('Set2')
	plt.figure(figsize=(figx, figy))
	ax = sns.barplot(x='Condition',y=ylabel,data=dddd_df)
	if not min == 9999 and not max==9999:
		plt.ylim(min,max)
	elif not max == 9999:
		plt.ylim(0,max)
	plt.xticks(rotation=45)
	plt.savefig('questionnaire/graph/Preliminary experiment/'+filename+'.jpg',dpi=300, format='jpg', bbox_inches='tight')

	print('finish   :   ' + ylabel)

def fig_MS(ylabel:str,level:str,filename:str,min:int=9999,max:int=9999,participant:str=1):
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
		for k in range(4):
			ms.append(j)
			if k == 0:
				condition.append('without feedback')
				ddddd.append(dddd[0])
			elif k == 1:
				condition.append('partner velocity')
				ddddd.append(dddd[1])
			elif k == 2:
				condition.append('robot velocity')
				ddddd.append(dddd[2])
			elif k == 3:
				condition.append('partner + robot velocity')
				ddddd.append(dddd[3])
		dddd = []
	dddd_df = pd.DataFrame({'Condition':condition,ylabel:ddddd,'':ms})

	sns.set_palette('Paired')
	plt.figure(figsize=(figx, figy))
	ax = sns.barplot(x='Condition',y=ylabel,hue='',data=dddd_df)
	if not min == 9999 and not max==9999:
		plt.ylim(min,max)
	elif not max == 9999:
		plt.ylim(0,max)
	plt.xticks(rotation=45)
	lg = plt.legend(loc='upper right', bbox_to_anchor=(0.75, 0.5, 0.5, .100), borderaxespad=0.,)
	plt.savefig('questionnaire/graph/Preliminary experiment/' +filename+'.jpg',dpi=300, format='jpg', bbox_extra_artists=(lg,), bbox_inches='tight')

	print('finish   :   ' + level + ylabel)

def fig_map(index:str,ylabel:str,min:int=9999,max:int=9999,participant:str=1):
	ddd = data['TaskTime'].values
	dddd = []
	dddd.append(ddd[22])
	dddd.append(ddd[23])
	for i in range(4):
		dddd.append(ddd[3*i+participant])
	d = data['accuracy-score'].values
	dd = []
	dd.append(d[22])
	dd.append(d[23])
	for i in range(4):
		dd.append(d[3*i+participant])
	condition = ['beginner','expert','without feedback','partner velocity','robot velocity','partner + robot velocity']
	dddd = [dddd[0],dddd[1],dddd[2],dddd[3],dddd[4],dddd[5]]
	dddd_df = pd.DataFrame({'Condition':condition,'Task Time [s]':dddd,'Accuracy Score':dd})

	sns.set_palette('muted')
	plt.figure(figsize=(10, 5))
	sns.scatterplot(x='Task Time [s]',y='Accuracy Score',hue='Condition',data=dddd_df)
	plt.ylim(0,5)
	plt.xlim(0,30)
	lg = plt.legend(loc='upper right', bbox_to_anchor=(0.9, 0.5, 0.5, .100), borderaxespad=0.,)
	plt.savefig('questionnaire/graph/Preliminary experiment/performance.jpg',dpi=300, format='jpg',bbox_extra_artists=(lg,), bbox_inches='tight')

	print('finish   :   performance')

accuracy = fig(index='accuracy-score',ylabel='Accuracy Score',filename='Accuracy_Score',min=0,max=5)
tasktime = fig(index='TaskTime',ylabel='Task Time [s]',filename='TaskTime',max=14)
tlx_b = fig(index='TLX-SCORE',ylabel='Beginner WWL',filename='beginnerTLX',max=100)
tlx_e = fig(index='TLX-SCORE',ylabel='Expert WWL',filename='expertTLX',max=100,participant=2)
ios_b = fig(index='we-mode-score',ylabel='Beginner Inclusion of Other in the Self',filename='beginnerIOS',max=7.8)
ios_e = fig(index='we-mode-score',ylabel='Expert Inclusion of Other in the Self',filename='expertIOS',max=7.8,participant=2)
ms_b = fig_MS(ylabel='Beginner Rating Score',level='Beginner ',filename='beginnerMS')
ms_e = fig_MS(ylabel='Expert Rating Score',level='Expert ',filename='expertMS',participant=2)
performanceMap = fig_map(index='TaskTime',ylabel='Task Time [s]')