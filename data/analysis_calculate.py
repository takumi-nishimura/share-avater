import pandas as pd
import numpy as np
import os
import glob
import matplotlib.pyplot as plt
import seaborn as sns
from time_calculate import TIME_CALCULATE
from analysis_DTW import DTW
from analysis_Jerk import JERK
from analisis_CoT import CoT

class DATACALCULATE:
	def __init__(self) -> None:
		self.d_A_list = []
		self.d_B_list = []
		self.d_C_list = []
		self.df_A_r_dict = {}
		self.df_A_1_dict = {}
		self.df_A_2_dict = {}
		self.df_B_r_dict = {}
		self.df_B_1_dict = {}
		self.df_B_2_dict = {}
		self.df_C_r_dict = {}
		self.df_C_1_dict = {}
		self.df_C_2_dict = {}

	def main(self, score:bool=True, dtw:bool=False, jrk:bool=False, cot=False):
		self.score = TIME_CALCULATE()
		self.dtw = DTW()
		self.jrk = JERK()
		self.CoT = CoT()
		self.participant_l()
		if score:
			self.score.save_time()
		if dtw:
			self.dtw_c()
		if jrk:
			self.jrk_c()
		if cot:
			self.CoT_s()
			print('save_finish')
			self.CoT_c()
			
	def dtw_c(self):
		self.dtw_A_l = []
		self.dtw_B_l = []
		self.dtw_C_l = []
		self.dict_dtw ={}
		for self.participant in self.participant_list:
			print(self.participant)
			self.read()
			for i, j in enumerate(['A','B','C']):
				print(j)
				if j == 'A':
					for k in range(3):
						self.dtw_A = self.dtw.main(self.df_A_r_dict[str(k+1)],self.df_A_1_dict[str(k+1)],self.df_A_2_dict[str(k+1)],self.participant,j,str(k+1))
						self.dtw_A_l.append(self.dtw_A)
					self.dtw_A_average = np.average(self.dtw_A_l)
				elif j == 'B':
					for k in range(3):
						self.dtw_B = self.dtw.main(self.df_B_r_dict[str(k+1)],self.df_B_1_dict[str(k+1)],self.df_B_2_dict[str(k+1)],self.participant,j,str(k+1))
						self.dtw_B_l.append(self.dtw_B)
					self.dtw_B_average = np.average(self.dtw_B_l)
				elif j == 'C':
					for k in range(3):
						self.dtw_C = self.dtw.main(self.df_C_r_dict[str(k+1)],self.df_C_1_dict[str(k+1)],self.df_C_2_dict[str(k+1)],self.participant,j,str(k+1))
						self.dtw_C_l.append(self.dtw_C)
					self.dtw_C_average = np.average(self.dtw_C_l)
			self.dict_dtw[self.participant] = [self.dtw_A_average,self.dtw_B_average,self.dtw_C_average]
			self.dtw_A_l = []
			self.dtw_B_l = []
			self.dtw_C_l = []
		self.Export_dtw = pd.DataFrame(index=['A','B','C'])
		for key in self.dict_dtw.keys():
			self.Export_dtw[key] = [self.dict_dtw[key][0],self.dict_dtw[key][1],self.dict_dtw[key][2]]
		self.toXlsx(evaluation='DTW_SCORE', df=self.Export_dtw)

	def jrk_c(self):
		self.jrk_A_l = []
		self.jrk_B_l = []
		self.jrk_C_l = []
		self.dict_jrk = {}
		for self.participant in self.participant_list:
			print(self.participant)
			self.read()
			for i, j in enumerate(['A','B','C']):
				print(j)
				if j == 'A':
					for k in range(3):
						self.jrk_A = self.jrk.main(self.df_A_r_dict[str(k+1)])
						self.jrk_A_l.append(self.jrk_A)
					self.jrk_A_average = np.average(self.jrk_A_l)
				elif j == 'B':
					for k in range(3):
						self.jrk_B = self.jrk.main(self.df_B_r_dict[str(k+1)])
						self.jrk_B_l.append(self.jrk_B)
					self.jrk_B_average = np.average(self.jrk_B_l)
				elif j == 'C':
					for k in range(3):
						self.jrk_C = self.jrk.main(self.df_C_r_dict[str(k+1)])
						self.jrk_C_l.append(self.jrk_C)
					self.jrk_C_average = np.average(self.jrk_C_l)
			self.dict_jrk[self.participant] = [self.jrk_A_average,self.jrk_B_average,self.jrk_C_average]
			self.jrk_A_l = []
			self.jrk_B_l = []
			self.jrk_C_l = []
		self.Export_jrk = pd.DataFrame(index=['A','B','C'])
		for key in self.dict_jrk.keys():
			self.Export_jrk[key] = [self.dict_jrk[key][0],self.dict_jrk[key][1],self.dict_jrk[key][2]]
		self.toXlsx(evaluation='JRK_SCORE', df=self.Export_jrk)

	def CoT_s(self):
		self.cot_A_l = []
		self.cot_B_l = []
		self.cot_C_l = []
		for self.participant in self.participant_list:
			print(self.participant)
			self.read()
			for i, j in enumerate(['A','B','C']):
				print(j)
				if j == 'A':
					for k in range(3):
						self.cot_A = self.CoT.main(self.df_A_r_dict[str(k+1)],self.df_A_1_dict[str(k+1)],self.df_A_2_dict[str(k+1)], self.participant, j, str(k+1),save=True)
						self.cot_A_l.append(self.cot_A)
					self.cot_A_average = np.average(self.cot_A_l)
			self.cot_A_l = []

	def CoT_c(self):
		for self.participant in self.participant_list:
			print(self.participant)
			self.read()
			for i, j in enumerate(['A','B','C']):
				print(j)
				if j == 'A':
					for k in range(3):
						self.cot_A = self.CoT.main(self.df_A_r_dict[str(k+1)],self.df_A_1_dict[str(k+1)],self.df_A_2_dict[str(k+1)], self.participant, j, str(k+1),input=True)
						self.cot_A_l.append(self.cot_A)
					self.cot_A_average = np.average(self.cot_A_l)
			self.cot_A_l = []

	def participant_l(self):
		self.file_list = []
		self.participant_list = []
		self.dir = os.path.join('data','ExportData','expt_data','move_data','')
		self.files = sorted(glob.glob(os.path.join(self.dir, '*.csv')))
		for self.filename_s in self.files:
			self.filename_split = self.filename_s.split('_')
			self.participant_name = self.filename_split[3]
			if self.participant_name in self.participant_list:
				pass
			else:
				self.participant_list.append(self.participant_name)
		print(self.participant_list)

	def read(self):
		for self.data in self.files:
			if self.participant in self.data:
				if 'A' in self.data:
					self.d_A_list.append(self.data)
				elif 'B' in self.data:
					self.d_B_list.append(self.data)
				elif 'C' in self.data:
					self.d_C_list.append(self.data)
		j = 0
		k = 0
		l = 0
		for i in self.d_A_list:
			if 'endEffector' in i:
				j += 1
				self.df_A_r = pd.read_csv(i)
				self.df_A_r_dict[str(j)] = self.df_A_r
			elif 'Participant_1' in i:
				k += 1
				self.df_A_1 = pd.read_csv(i)
				self.df_A_1_dict[str(k)] = self.df_A_1
			elif 'Participant_2' in i:
				l += 1
				self.df_A_2 = pd.read_csv(i)
				self.df_A_2_dict[str(l)] = self.df_A_2
		j = 0
		k = 0
		l = 0
		for i in self.d_B_list:
			if 'endEffector' in i:
				j += 1
				self.df_B_r = pd.read_csv(i)
				self.df_B_r_dict[str(j)] = self.df_B_r
			elif 'Participant_1' in i:
				k += 1
				self.df_B_1 = pd.read_csv(i)
				self.df_B_1_dict[str(k)] = self.df_B_1
			elif 'Participant_2' in i:
				l += 1
				self.df_B_2 = pd.read_csv(i)
				self.df_B_2_dict[str(l)] = self.df_B_2
		j = 0
		k = 0
		l = 0
		for i in self.d_C_list:
			if 'endEffector' in i:
				j += 1
				self.df_C_r = pd.read_csv(i)
				self.df_C_r_dict[str(j)] = self.df_C_r
			elif 'Participant_1' in i:
				k += 1
				self.df_C_1 = pd.read_csv(i)
				self.df_C_1_dict[str(k)] = self.df_C_1
			elif 'Participant_2' in i:
				l += 1
				self.df_C_2 = pd.read_csv(i)
				self.df_C_2_dict[str(l)] = self.df_C_2
		self.d_A_list.clear()
		self.d_B_list.clear()
		self.d_C_list.clear()

	def toXlsx(self, evaluation, df):
		self.w_dir = '/Users/sprout/OneDrive - 名古屋工業大学/学校/研究室/実験/卒論実験/m_calculate'
		self.w_name = self.w_dir + '/' + evaluation + '.xlsx'
		df.to_excel(self.w_name)
		print(self.w_name)

class M_IMAGE:
	def __init__(self) -> None:
		pass

	def main(self):
		self.fig_dtw()
		self.fig_jrk()
		self.fig_TIME()
		self.fig_POINTS()
		self.fig_POINTS_TIME()

	def fig_dtw(self):
		self.condition = []
		self.item = []
		self.value = []
		self.path = '/Users/sprout/OneDrive - 名古屋工業大学/学校/研究室/実験/卒論実験/m_calculate/DTW_SCORE.xlsx'
		self.data = pd.read_excel(self.path, sheet_name=None, index_col=0)
		self.keys = []
		for i in self.data.keys():
			self.keys.append(i)
		self.index = self.data[self.keys[0]].index.values
		for key in self.keys:
			for index in self.index:
				self.i = self.data[key].loc[index]
				for name in range(len(self.i)):	
					if index == 'A':
						self.condition.append('without feedback')
					elif index == 'B':
						self.condition.append('companion speed')
					elif index == 'C':
						self.condition.append('robot speed')
					self.item.append(index)
					self.value.append(self.i[name])
		self.DTW_df = pd.DataFrame({'condition':self.condition,'':self.item,'Questionnaire rating':self.value})
		sns.set_palette('Set2')
		self.ax = sns.boxplot(x='condition', y='Questionnaire rating', data=self.DTW_df)
		plt.savefig('data/ExportData/graph/DTW_SCORE.png', dpi=300, format='png')
		plt.figure()

	def fig_jrk(self):
		self.condition = []
		self.item = []
		self.value = []
		self.path = '/Users/sprout/OneDrive - 名古屋工業大学/学校/研究室/実験/卒論実験/m_calculate/JRK_SCORE.xlsx'
		self.data = pd.read_excel(self.path, sheet_name=None, index_col=0)
		self.keys = []
		for i in self.data.keys():
			self.keys.append(i)
		self.index = self.data[self.keys[0]].index.values
		for key in self.keys:
			for index in self.index:
				self.i = self.data[key].loc[index]
				for name in range(len(self.i)):	
					if index == 'A':
						self.condition.append('without feedback')
					elif index == 'B':
						self.condition.append('companion speed')
					elif index == 'C':
						self.condition.append('robot speed')
					self.item.append(index)
					self.value.append(self.i[name])
		self.JRK_df = pd.DataFrame({'condition':self.condition,'':self.item,'Questionnaire rating':self.value})
		sns.set_palette('Set2')
		self.ax = sns.boxplot(x='condition', y='Questionnaire rating', data=self.JRK_df)
		plt.savefig('data/ExportData/graph/JRK_SCORE.png', dpi=300, format='png')
		plt.figure()

	def fig_TIME(self):
		self.condition = []
		self.item = []
		self.value = []
		self.path = '/Users/sprout/OneDrive - 名古屋工業大学/学校/研究室/実験/卒論実験/m_calculate/TASK_TIME.xlsx'
		self.data = pd.read_excel(self.path, sheet_name='Task Time', index_col=0)
		self.index = self.data.index.values
		for index in self.index:
			self.i = self.data.loc[index]
			for name in range(len(self.i)):	
				if index == 'A':
					self.condition.append('without feedback')
				elif index == 'B':
					self.condition.append('companion speed')
				elif index == 'C':
					self.condition.append('robot speed')
				self.item.append(index)
				self.value.append(self.i[name])
		self.TIME_df = pd.DataFrame({'condition':self.condition,'':self.item,'Task Time [s]':self.value})
		sns.set_palette('Set2')
		self.ax = sns.boxplot(x='condition', y='Task Time [s]', data=self.TIME_df)
		plt.savefig('data/ExportData/graph/TASK_TIME.png', dpi=300, format='png')
		plt.figure()

	def fig_POINTS(self):
		self.condition = []
		self.item = []
		self.value = []
		self.path = '/Users/sprout/OneDrive - 名古屋工業大学/学校/研究室/実験/卒論実験/m_calculate/TASK_TIME.xlsx'
		self.data = pd.read_excel(self.path, sheet_name=None, index_col=0)
		self.keys = []
		for i in self.data.keys():
			self.keys.append(i)
		self.columns = self.data.columns
		print(self.data)
		for column in self.columns:
			self.i = self.data[self.keys[0]].loc[column]
			print(self.i)
			self.i_2 = self.data[self.keys[1]].loc[column]
			print(self.i)
			for name in range(len(self.i)):	
				if index == 'A':
					self.condition.append('without feedback')
				elif index == 'B':
					self.condition.append('companion speed')
				elif index == 'C':
					self.condition.append('robot speed')
				self.item.append(index)
				self.value.append(self.i[name])
		self.POINTS_df = pd.DataFrame({'condition':self.condition,'':self.item,'Points':self.value})
		sns.set_palette('Set2')
		self.ax = sns.boxplot(x='condition', y='Points', data=self.POINTS_df)
		plt.savefig('data/ExportData/graph/TASK_POINTS.png', dpi=300, format='png')
		plt.figure()

	def fig_POINTS_TIME(self):
		self.condition = []
		self.item = []
		self.value = []
		self.path = '/Users/sprout/OneDrive - 名古屋工業大学/学校/研究室/実験/卒論実験/m_calculate/TASK_TIME.xlsx'
		self.data = pd.read_excel(self.path, sheet_name='Points', index_col=0)
		self.index = self.data.index.values
		for index in self.index:
			self.i = self.data.loc[index]
			for name in range(len(self.i)):	
				if index == 'A':
					self.condition.append('without feedback')
				elif index == 'B':
					self.condition.append('companion speed')
				elif index == 'C':
					self.condition.append('robot speed')
				self.item.append(index)
				self.value.append(self.i[name])
		self.POINTS_df = pd.DataFrame({'condition':self.condition,'':self.item,'Points':self.value})
		sns.set_palette('Set2')
		self.ax = sns.boxplot(x='condition', y='Points', data=self.POINTS_df)
		plt.savefig('data/ExportData/graph/TASK_POINTS.png', dpi=300, format='png')
		plt.figure()

if __name__ in '__main__':
	calculate = DATACALCULATE()
	figure = M_IMAGE()
	# calculate.main(dtw=False, jrk=False, cot=True)
	figure.main()