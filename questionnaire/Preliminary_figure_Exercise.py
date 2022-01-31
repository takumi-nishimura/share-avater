from itertools import cycle
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib_style
import seaborn as sns

def fig_CoT():
	path = '/Users/sprout/OneDrive - 名古屋工業大学/学校/研究室/実験/予備実験/20211108/Contemporaneity_of_time2.xlsx'
	data = pd.read_excel(path)
	woFB = data['Unnamed: 4'].values[1:6]
	partner = data['Unnamed: 9'].values[1:6]
	robot = data['Unnamed: 14'].values[1:6]
	p_r = data['Unnamed: 19'].values[1:6]
	d = []
	condition = []
	for i in range(len(woFB)):
		d.append(woFB[i])
		condition.append('without feedback')
	for i in range(5):
		d.append(partner[i])
		d.append(robot[i])
		d.append(p_r[i])
	for i in range(len(woFB)*3):
		condition.append('with feedback')
	for i in range(len(partner)):
		d.append(partner[i])
		condition.append('partner velocity')
	for i in range(len(robot)):
		d.append(robot[i])
		condition.append('robot velocity')
	for i in range(len(p_r)):
		d.append(p_r[i])
		condition.append('partner + robot velocity')
	
	CoT_df = pd.DataFrame({'condition':condition,'Diff Time [s]':d})
	figx = 12
	figy = 7
	sns.set_palette('Set3')
	plt.figure(figsize=(figx, figy))
	sns.barplot(x='condition',y='Diff Time [s]',data=CoT_df)
	plt.xticks(rotation=45)
	plt.savefig('questionnaire/graph/Preliminary experiment/' + 'CoT.jpg',dpi=300, format='jpg', bbox_inches='tight')

	print('finish   :   CoT')

def fig_JRK():
	path = '/Users/sprout/OneDrive - 名古屋工業大学/学校/研究室/実験/予備実験/20211108/jrk_cost_20211112.xlsx'
	data = pd.read_excel(path)
	
	beginner = data['begginer'].values[10:15]
	expert = data['expert'].values[10:15]
	woFB = data['woFB'].values[10:15]
	partner = data['partner'].values[10:15]
	robot = data['robot'].values[10:15]
	p_r = data['partner+robot'].values[10:15]
	
	d = []
	condition = []
	for i in range(len(beginner)):
		d.append(beginner[i])
		condition.append('beginner')
	for i in range(len(expert)):
		d.append(expert[i])
		condition.append('expert')
	for i in range(len(woFB)):
		d.append(woFB[i])
		condition.append('without feedback')
	for i in range(5):
		d.append(partner[i])
		d.append(robot[i])
		d.append(p_r[i])
	for i in range(len(woFB)*3):
		condition.append('with feedback')
	for i in range(len(partner)):
		d.append(partner[i])
		condition.append('partner velocity')
	for i in range(len(robot)):
		d.append(robot[i])
		condition.append('robot velocity')
	for i in range(len(p_r)):
		d.append(p_r[i])
		condition.append('partner + robot velocity')

	JRK_df = pd.DataFrame({'condition':condition,'Jerk Index':d})

	figx = 12
	figy = 7
	sns.set_palette('Set3')
	plt.figure(figsize=(figx, figy))
	sns.boxplot(x='condition',y='Jerk Index',data=JRK_df)
	plt.xticks(rotation=45)
	plt.savefig('questionnaire/graph/Preliminary experiment/' + 'JRK.jpg',dpi=300, format='jpg', bbox_inches='tight')

	print('finish   :   JRK')

def fig_DTW():
	path = '/Users/sprout/OneDrive - 名古屋工業大学/学校/研究室/実験/予備実験/20211108/dtw_data.xlsx'
	data = pd.read_excel(path,sheet_name=None)
	data = data['fast_dtw']
	woFB = data['wo FB'].values[0:5]
	partner = data['partner'].values[0:5]
	robot = data['robot'].values[0:5]
	p_r = data['partner+robot'].values[0:5]

	d = []
	condition = []
	for i in range(len(woFB)):
		d.append(woFB[i])
		condition.append('without feedback')
	for i in range(5):
		d.append(partner[i])
		d.append(robot[i])
		d.append(p_r[i])
	for i in range(len(woFB)*3):
		condition.append('with feedback')
	for i in range(len(partner)):
		d.append(partner[i])
		condition.append('partner velocity')
	for i in range(len(robot)):
		d.append(robot[i])
		condition.append('robot velocity')
	for i in range(len(p_r)):
		d.append(p_r[i])
		condition.append('partner + robot velocity')

	DTW_df = pd.DataFrame({'condition':condition,'DTW Score':d})

	figx = 12
	figy = 7
	sns.set_palette('Set3')
	plt.figure(figsize=(figx, figy))
	sns.boxplot(x='condition',y='DTW Score',data=DTW_df)
	plt.xticks(rotation=45)
	plt.savefig('questionnaire/graph/Preliminary experiment/' + 'DTW.jpg',dpi=300, format='jpg', bbox_inches='tight')

	print('finish   :   DTW')

def fig_NORM():
	path = '/Users/sprout/OneDrive - 名古屋工業大学/学校/研究室/実験/予備実験/20211108/dtw_data.xlsx'
	data = pd.read_excel(path,sheet_name=None)
	data = data['path_norm(begginer)']
	woFB_b = data['wo FB'].values[0:5]
	partner_b = data['partner'].values[0:5]
	robot_b = data['robot'].values[0:5]
	p_r_b = data['partner+robot'].values[0:5]
	woFB_e = data['wo-FB'].values[0:5]
	partner_e = data['partner-'].values[0:5]
	robot_e = data['robot-'].values[0:5]
	p_r_e = data['partner+robot-'].values[0:5]

	d = []
	condition = []
	level = []
	cycle = []
	for i in ['Beginner','Expert']:
		if i == 'Beginner':
			for j in woFB_b:
				d.append(j)
				condition.append('without feedback')
				level.append(i)
			for j in range(len(partner_b)):
				d.append(partner_b[j])
				d.append(robot_b[j])
				d.append(p_r_b[j])
			for j in range(len(partner_b)*3):
				condition.append('with feedback')
				level.append(i)
			for j in partner_b:
				d.append(j)
				condition.append('partner velocity')
				level.append(i)
			for j in robot_b:
				d.append(j)
				condition.append('robot velocity')
				level.append(i)
			for j in p_r_b:
				d.append(j)
				condition.append('partner + robot velocity')
				level.append(i)
		elif i == 'Expert':
			for j in woFB_e:
				d.append(j)
				condition.append('without feedback')
				level.append(i)
			for j in range(len(partner_e)):
				d.append(partner_e[j])
				d.append(robot_e[j])
				d.append(p_r_e[j])
			for j in range(len(partner_e)*3):
				condition.append('with feedback')
				level.append(i)
			for j in partner_e:
				d.append(j)
				condition.append('partner velocity')
				level.append(i)
			for j in robot_e:
				d.append(j)
				condition.append('robot velocity')
				level.append(i)
			for j in p_r_e:
				d.append(j)
				condition.append('partner + robot velocity')
				level.append(i)
	NORM_df = pd.DataFrame({'condition':condition,'Norm Path Cost':d,'':level})
	print(NORM_df)

	figx = 12
	figy = 7
	sns.set_palette('Paired')
	plt.figure(figsize=(figx, figy))
	sns.barplot(x='condition',y='Norm Path Cost', hue='',data=NORM_df)
	plt.xticks(rotation=45)
	lg = plt.legend(loc='upper right', bbox_to_anchor=(0.68, 0.5, 0.5, .100), borderaxespad=0.,)
	plt.savefig('questionnaire/graph/Preliminary experiment/' + 'NORM.jpg',dpi=300, format='jpg', bbox_extra_artists=(lg,), bbox_inches='tight')

	print('finish   :   NORM')

def fig_NORM_CYCLE():
	path = '/Users/sprout/OneDrive - 名古屋工業大学/学校/研究室/実験/予備実験/20211108/dtw_data.xlsx'
	data = pd.read_excel(path,sheet_name=None)
	data = data['path_norm(begginer)']
	woFB_b = data['wo FB'].values[0:5]
	partner_b = data['partner'].values[0:5]
	robot_b = data['robot'].values[0:5]
	p_r_b = data['partner+robot'].values[0:5]
	woFB_e = data['wo-FB'].values[0:5]
	partner_e = data['partner-'].values[0:5]
	robot_e = data['robot-'].values[0:5]
	p_r_e = data['partner+robot-'].values[0:5]

	d = []
	condition = []
	level = []
	cycle = []
	for i in ['Beginner','Expert']:
		if i == 'Beginner':
			for j in woFB_b:
				d.append(j)
				condition.append('without feedback')
				level.append(i)
			for j in partner_b:
				d.append(j)
				condition.append('partner velocity')
				level.append(i)
			for j in robot_b:
				d.append(j)
				condition.append('robot velocity')
				level.append(i)
			for j in p_r_b:
				d.append(j)
				condition.append('partner + robot velocity')
				level.append(i)
		elif i == 'Expert':
			for j in woFB_e:
				d.append(j)
				condition.append('without feedback')
				level.append(i)
			for j in partner_e:
				d.append(j)
				condition.append('partner velocity')
				level.append(i)
			for j in robot_e:
				d.append(j)
				condition.append('robot velocity')
				level.append(i)
			for j in p_r_e:
				d.append(j)
				condition.append('partner + robot velocity')
				level.append(i)
	for i in range(20):
		cycle.append(i+1)
	for i in range(20):
		cycle.append(i+1)
	NORM_df = pd.DataFrame({'condition':condition,'Norm Path Cost':d,'':level,'cycle':cycle})
	print(NORM_df)

	figx = 12
	figy = 7
	sns.set_palette('Set2')
	plt.figure(figsize=(figx, figy))
	sns.lineplot(x='cycle',y='Norm Path Cost',hue='',data=NORM_df)
	lg = plt.legend(loc='upper right', bbox_to_anchor=(0.68, 0.5, 0.5, .100), borderaxespad=0.,)
	plt.gca().get_xaxis().set_major_locator(ticker.MaxNLocator(integer=True))
	plt.savefig('questionnaire/graph/Preliminary experiment/' + 'NORM_CYCLE.jpg',dpi=300, format='jpg', bbox_extra_artists=(lg,), bbox_inches='tight')

	print('finish   :   NORM_CYCLE')
	
fig_CoT()
fig_JRK()
fig_DTW()
fig_NORM()
fig_NORM_CYCLE()