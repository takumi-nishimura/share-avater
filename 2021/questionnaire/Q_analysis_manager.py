import pandas as pd
import numpy as np
import os
import glob
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib_style

class Q_AVERAGE:
	def __init__(self) -> None:
		self.q_A_list = []
		self.q_B_list = []
		self.q_C_list = []
		self.df_A_dict = {}
		self.df_B_dict = {}
		self.df_C_dict = {}
		self.q_average_list = {}
		self.tlx_A1_l = []
		self.tlx_A2_l = []
		self.tlx_A3_l = []
		self.tlx_B1_l = []
		self.tlx_B2_l = []
		self.tlx_B3_l = []
		self.tlx_C1_l = []
		self.tlx_C2_l = []
		self.tlx_C3_l = []
		self.Q1_A1_l = []
		self.Q1_A2_l = []
		self.Q1_A3_l = []
		self.Q1_B1_l = []
		self.Q1_B2_l = []
		self.Q1_B3_l = []
		self.Q1_C1_l = []
		self.Q1_C2_l = []
		self.Q1_C3_l = []
		self.Q2_A1_l = []
		self.Q2_A2_l = []
		self.Q2_A3_l = []
		self.Q2_B1_l = []
		self.Q2_B2_l = []
		self.Q2_B3_l = []
		self.Q2_C1_l = []
		self.Q2_C2_l = []
		self.Q2_C3_l = []
		self.Q3_A1_l = []
		self.Q3_A2_l = []
		self.Q3_A3_l = []
		self.Q3_B1_l = []
		self.Q3_B2_l = []
		self.Q3_B3_l = []
		self.Q3_C1_l = []
		self.Q3_C2_l = []
		self.Q3_C3_l = []

	def main(self):
		self.participant_l()

		for self.participant in self.participant_list:
			print(self.participant)
			self.read()
			self.TLX_c()
			self.MS_c()
			self.MD_c()
			self.SE_c()
			self.ALL_TLX_c()
			self.ALL_Q1_c()
			self.ALL_Q2_c()
			self.ALL_Q3_c()
			self.make_l()
		
		self.write()

	def write(self):
		self.TLX_w()
		self.MS_w()
		self.MD_w()
		self.SE_w()

	def participant_l(self):
		self.file_list = []
		self.participant_list = []
		self.dir = os.path.join('questionnaire','q_data','')
		self.files = sorted(glob.glob(os.path.join(self.dir, '*.csv')))

		for self.filename_s in self.files:
			self.filename_split = self.filename_s.split('_')
			self.participant_name = self.filename_split[2]
			if self.participant_name in self.participant_list:
				pass
			else:
				self.participant_list.append(self.participant_name)

	def read(self):
		for self.data in self.files:
			if self.participant in self.data:
				if 'A' in self.data:
					self.q_A_list.append(self.data)
				elif 'B' in self.data:
					self.q_B_list.append(self.data)
				elif 'C' in self.data:
					self.q_C_list.append(self.data)

		for i in range(len(self.q_A_list)):
			self.df_A = pd.read_csv(self.q_A_list[i])
			self.df_A_dict[str(i+1)] = self.df_A
		for i in range(len(self.q_B_list)):
			self.df_B = pd.read_csv(self.q_B_list[i])
			self.df_B_dict[str(i+1)] = self.df_B
		for i in range(len(self.q_C_list)):
			self.df_C = pd.read_csv(self.q_C_list[i])
			self.df_C_dict[str(i+1)] = self.df_C

		self.q_A_list.clear()
		self.q_B_list.clear()
		self.q_C_list.clear()

	def TLX_c(self):
		self.TLX_A = []
		self.TLX_B = []
		self.TLX_C = []
		for i in range(len(self.df_A_dict)):
			self.TLX_A.append(((self.df_A_dict[str(i+1)])['TLX_awwl'])[0]/21)
		for i in range(len(self.df_B_dict)):
			self.TLX_B.append(((self.df_B_dict[str(i+1)])['TLX_awwl'])[0]/21)
		for i in range(len(self.df_C_dict)):
			self.TLX_C.append(((self.df_C_dict[str(i+1)])['TLX_awwl'])[0]/21)
		self.TLX_average_A = pd.DataFrame({self.participant:np.average(self.TLX_A)}, index=['TLX_awwl'])
		self.TLX_average_B = pd.DataFrame({self.participant:np.average(self.TLX_B)}, index=['TLX_awwl'])
		self.TLX_average_C = pd.DataFrame({self.participant:np.average(self.TLX_C)}, index=['TLX_awwl'])
		self.TLX_average = {'A':self.TLX_average_A,'B':self.TLX_average_B,'C':self.TLX_average_C}

	def MS_c(self):
		self.MS_A = []
		self.MS_B = []
		self.MS_C = []
		for i in range(len(self.df_A_dict)):
			self.MS_A.append(((self.df_A_dict[str(i+1)])['MS_score'])[0:4])
		for i in range(len(self.df_B_dict)):
			self.MS_B.append(((self.df_B_dict[str(i+1)])['MS_score'])[0:4])
		for i in range(len(self.df_C_dict)):
			self.MS_C.append(((self.df_C_dict[str(i+1)])['MS_score'])[0:4])
		self.MS_average_A = pd.DataFrame({self.participant:np.average(self.MS_A, axis=0)}, index=['ownership','ownership_control','agency','agency_control'])
		self.MS_average_B = pd.DataFrame({self.participant:np.average(self.MS_B, axis=0)}, index=['ownership','ownership_control','agency','agency_control'])
		self.MS_average_C = pd.DataFrame({self.participant:np.average(self.MS_C, axis=0)}, index=['ownership','ownership_control','agency','agency_control'])
		self.MS_average = {'A':self.MS_average_A,'B':self.MS_average_B,'C':self.MS_average_C}

	def MD_c(self):
		self.MD_A = []
		self.MD_B = []
		self.MD_C = []
		for i in range(len(self.df_A_dict)):
			self.MD_A.append(((self.df_A_dict[str(i+1)])['MD_r'])[0])
		for i in range(len(self.df_B_dict)):
			self.MD_B.append(((self.df_B_dict[str(i+1)])['MD_r'])[0])
		for i in range(len(self.df_C_dict)):
			self.MD_C.append(((self.df_C_dict[str(i+1)])['MD_r'])[0])
		self.MD_average_A = pd.DataFrame({self.participant:np.average(self.MD_A)}, index=['MD_score'])
		self.MD_average_B = pd.DataFrame({self.participant:np.average(self.MD_B)}, index=['MD_score'])
		self.MD_average_C = pd.DataFrame({self.participant:np.average(self.MD_C)}, index=['MD_score'])
		self.MD_average = {'A':self.MD_average_A,'B':self.MD_average_B,'C':self.MD_average_C}

	def SE_c(self):
		self.SE_A = []
		self.SE_B = []
		self.SE_C = []
		for i in range(len(self.df_A_dict)):
			self.SE_A.append(((self.df_A_dict[str(i+1)])['SE_r'])[0:5])
		for i in range(len(self.df_B_dict)):
			self.SE_B.append(((self.df_B_dict[str(i+1)])['SE_r'])[0:5])
		for i in range(len(self.df_C_dict)):
			self.SE_C.append(((self.df_C_dict[str(i+1)])['SE_r'])[0:5])
		self.SE_average_A = pd.DataFrame({self.participant:np.average(self.SE_A, axis=0)}, index=['Q1','Q2','Q3','Q4','Q5'])
		self.SE_average_B = pd.DataFrame({self.participant:np.average(self.SE_B, axis=0)}, index=['Q1','Q2','Q3','Q4','Q5'])
		self.SE_average_C = pd.DataFrame({self.participant:np.average(self.SE_C, axis=0)}, index=['Q1','Q2','Q3','Q4','Q5'])
		self.SE_average = {'A':self.SE_average_A,'B':self.SE_average_B,'C':self.SE_average_C}

	def ALL_TLX_c(self):
		self.TLX_A = []
		self.TLX_B = []
		self.TLX_C = []
		for i in range(len(self.df_A_dict)):
			self.TLX_A.append(((self.df_A_dict[str(i+1)])['TLX_awwl'])[0]/21)
		for i in range(len(self.df_B_dict)):
			self.TLX_B.append(((self.df_B_dict[str(i+1)])['TLX_awwl'])[0]/21)
		for i in range(len(self.df_C_dict)):
			self.TLX_C.append(((self.df_C_dict[str(i+1)])['TLX_awwl'])[0]/21)
		self.tlx_A1_l.append(self.TLX_A[0])
		self.tlx_A2_l.append(self.TLX_A[1])
		self.tlx_A3_l.append(self.TLX_A[2])
		self.tlx_B1_l.append(self.TLX_B[0])
		self.tlx_B2_l.append(self.TLX_B[1])
		self.tlx_B3_l.append(self.TLX_B[2])
		self.tlx_C1_l.append(self.TLX_C[0])
		self.tlx_C2_l.append(self.TLX_C[1])
		self.tlx_C3_l.append(self.TLX_C[2])
		self.tlx_1_df = pd.DataFrame({'A':self.tlx_A1_l,'B':self.tlx_B1_l,'C':self.tlx_C1_l})
		self.tlx_2_df = pd.DataFrame({'A':self.tlx_A2_l,'B':self.tlx_B2_l,'C':self.tlx_C2_l})
		self.tlx_3_df = pd.DataFrame({'A':self.tlx_A3_l,'B':self.tlx_B3_l,'C':self.tlx_C3_l})
		with pd.ExcelWriter('/Users/sprout/OneDrive - 名古屋工業大学/学校/研究室/実験/卒論実験/q_calculate/ALL_TLX_COST.xlsx') as writer:
			self.tlx_1_df.to_excel(writer, sheet_name='1')
			self.tlx_2_df.to_excel(writer, sheet_name='2')
			self.tlx_3_df.to_excel(writer, sheet_name='3')

	def ALL_Q1_c(self):
		self.Q1_A = []
		self.Q1_B = []
		self.Q1_C = []
		for i in range(len(self.df_A_dict)):
			self.Q1_A.append(((self.df_A_dict[str(i+1)])['SE_r'])[0])
		for i in range(len(self.df_B_dict)):
			self.Q1_B.append(((self.df_B_dict[str(i+1)])['SE_r'])[0])
		for i in range(len(self.df_C_dict)):
			self.Q1_C.append(((self.df_C_dict[str(i+1)])['SE_r'])[0])
		self.Q1_A1_l.append(self.Q1_A[0])
		self.Q1_A2_l.append(self.Q1_A[1])
		self.Q1_A3_l.append(self.Q1_A[2])
		self.Q1_B1_l.append(self.Q1_B[0])
		self.Q1_B2_l.append(self.Q1_B[1])
		self.Q1_B3_l.append(self.Q1_B[2])
		self.Q1_C1_l.append(self.Q1_C[0])
		self.Q1_C2_l.append(self.Q1_C[1])
		self.Q1_C3_l.append(self.Q1_C[2])
		self.Q1_1_df = pd.DataFrame({'A':self.Q1_A1_l,'B':self.Q1_B1_l,'C':self.Q1_C1_l})
		self.Q1_2_df = pd.DataFrame({'A':self.Q1_A2_l,'B':self.Q1_B2_l,'C':self.Q1_C2_l})
		self.Q1_3_df = pd.DataFrame({'A':self.Q1_A3_l,'B':self.Q1_B3_l,'C':self.Q1_C3_l})
		with pd.ExcelWriter('/Users/sprout/OneDrive - 名古屋工業大学/学校/研究室/実験/卒論実験/q_calculate/ALL_Q1.xlsx') as writer:
			self.Q1_1_df.to_excel(writer, sheet_name='1')
			self.Q1_2_df.to_excel(writer, sheet_name='2')
			self.Q1_3_df.to_excel(writer, sheet_name='3')

	def ALL_Q2_c(self):
		self.Q2_A = []
		self.Q2_B = []
		self.Q2_C = []
		for i in range(len(self.df_A_dict)):
			self.Q2_A.append(((self.df_A_dict[str(i+1)])['SE_r'])[1])
		for i in range(len(self.df_B_dict)):
			self.Q2_B.append(((self.df_B_dict[str(i+1)])['SE_r'])[1])
		for i in range(len(self.df_C_dict)):
			self.Q2_C.append(((self.df_C_dict[str(i+1)])['SE_r'])[1])
		self.Q2_A1_l.append(self.Q2_A[0])
		self.Q2_A2_l.append(self.Q2_A[1])
		self.Q2_A3_l.append(self.Q2_A[2])
		self.Q2_B1_l.append(self.Q2_B[0])
		self.Q2_B2_l.append(self.Q2_B[1])
		self.Q2_B3_l.append(self.Q2_B[2])
		self.Q2_C1_l.append(self.Q2_C[0])
		self.Q2_C2_l.append(self.Q2_C[1])
		self.Q2_C3_l.append(self.Q2_C[2])
		self.Q2_1_df = pd.DataFrame({'A':self.Q2_A1_l,'B':self.Q2_B1_l,'C':self.Q2_C1_l})
		self.Q2_2_df = pd.DataFrame({'A':self.Q2_A2_l,'B':self.Q2_B2_l,'C':self.Q2_C2_l})
		self.Q2_3_df = pd.DataFrame({'A':self.Q2_A3_l,'B':self.Q2_B3_l,'C':self.Q2_C3_l})
		with pd.ExcelWriter('/Users/sprout/OneDrive - 名古屋工業大学/学校/研究室/実験/卒論実験/q_calculate/ALL_Q2.xlsx') as writer:
			self.Q2_1_df.to_excel(writer, sheet_name='1')
			self.Q2_2_df.to_excel(writer, sheet_name='2')
			self.Q2_3_df.to_excel(writer, sheet_name='3')

	def ALL_Q3_c(self):
		self.Q3_A = []
		self.Q3_B = []
		self.Q3_C = []
		for i in range(len(self.df_A_dict)):
			self.Q3_A.append(((self.df_A_dict[str(i+1)])['SE_r'])[2])
		for i in range(len(self.df_B_dict)):
			self.Q3_B.append(((self.df_B_dict[str(i+1)])['SE_r'])[2])
		for i in range(len(self.df_C_dict)):
			self.Q3_C.append(((self.df_C_dict[str(i+1)])['SE_r'])[2])
		self.Q3_A1_l.append(self.Q3_A[0])
		self.Q3_A2_l.append(self.Q3_A[1])
		self.Q3_A3_l.append(self.Q3_A[2])
		self.Q3_B1_l.append(self.Q3_B[0])
		self.Q3_B2_l.append(self.Q3_B[1])
		self.Q3_B3_l.append(self.Q3_B[2])
		self.Q3_C1_l.append(self.Q3_C[0])
		self.Q3_C2_l.append(self.Q3_C[1])
		self.Q3_C3_l.append(self.Q3_C[2])
		self.Q3_1_df = pd.DataFrame({'A':self.Q3_A1_l,'B':self.Q3_B1_l,'C':self.Q3_C1_l})
		self.Q3_2_df = pd.DataFrame({'A':self.Q3_A2_l,'B':self.Q3_B2_l,'C':self.Q3_C2_l})
		self.Q3_3_df = pd.DataFrame({'A':self.Q3_A3_l,'B':self.Q3_B3_l,'C':self.Q3_C3_l})
		with pd.ExcelWriter('/Users/sprout/OneDrive - 名古屋工業大学/学校/研究室/実験/卒論実験/q_calculate/ALL_Q3.xlsx') as writer:
			self.Q3_1_df.to_excel(writer, sheet_name='1')
			self.Q3_2_df.to_excel(writer, sheet_name='2')
			self.Q3_3_df.to_excel(writer, sheet_name='3')

	def make_l(self):
		self.q_average = pd.DataFrame(data={'TLX_awwl':self.TLX_average,'MS_score':self.MS_average,'MD':self.MD_average,'SE':self.SE_average})

		self.q_average_list[self.participant] = self.q_average

	def TLX_w(self):
		self.TLX_list = pd.DataFrame(index=['A','B','C'])
		for i in self.participant_list:
			self.TLX_list[i] = [((self.q_average_list[i])['TLX_awwl'])['A'].loc['TLX_awwl',i],((self.q_average_list[i])['TLX_awwl'])['B'].loc['TLX_awwl',i],((self.q_average_list[i])['TLX_awwl'])['C'].loc['TLX_awwl',i]]
		self.toXlsx(evaluation='TLX_AWWL', df=self.TLX_list)

	def MS_w(self):
		self.MS_A_list = pd.DataFrame(index=['ownership','ownership_control','agency','agency_control'])
		self.MS_B_list = pd.DataFrame(index=['ownership','ownership_control','agency','agency_control'])
		self.MS_C_list = pd.DataFrame(index=['ownership','ownership_control','agency','agency_control'])
		for i in self.participant_list:
			self.MS_A_list[i] = [((self.q_average_list[i])['MS_score'])['A'].loc['ownership',i],((self.q_average_list[i])['MS_score'])['A'].loc['ownership_control',i],((self.q_average_list[i])['MS_score'])['A'].loc['agency',i],((self.q_average_list[i])['MS_score'])['A'].loc['agency_control',i]]
			self.MS_B_list[i] = [((self.q_average_list[i])['MS_score'])['B'].loc['ownership',i],((self.q_average_list[i])['MS_score'])['B'].loc['ownership_control',i],((self.q_average_list[i])['MS_score'])['B'].loc['agency',i],((self.q_average_list[i])['MS_score'])['B'].loc['agency_control',i]]
			self.MS_C_list[i] = [((self.q_average_list[i])['MS_score'])['C'].loc['ownership',i],((self.q_average_list[i])['MS_score'])['C'].loc['ownership_control',i],((self.q_average_list[i])['MS_score'])['C'].loc['agency',i],((self.q_average_list[i])['MS_score'])['C'].loc['agency_control',i]]
		self.MS_list = [self.MS_A_list,self.MS_B_list,self.MS_C_list]
		self.toXlsx_list(evaluation='MINIMAL_SELF', df_l=self.MS_list)

	def MD_w(self):
		self.MD_list = pd.DataFrame(index=['A','B','C'])
		for i in self.participant_list:
			self.MD_list[i] = [((self.q_average_list[i])['MD'])['A'].loc['MD_score',i],((self.q_average_list[i])['MD'])['B'].loc['MD_score',i],((self.q_average_list[i])['MD'])['C'].loc['MD_score',i]]
		self.toXlsx(evaluation='MD_SCORE', df=self.MD_list)

	def SE_w(self):
		self.SE_A_list = pd.DataFrame(index=['Q1','Q2','Q3','Q4','Q5'])
		self.SE_B_list = pd.DataFrame(index=['Q1','Q2','Q3','Q4','Q5'])
		self.SE_C_list = pd.DataFrame(index=['Q1','Q2','Q3','Q4','Q5'])
		for i in self.participant_list:
			self.SE_A_list[i] = [((self.q_average_list[i])['SE'])['A'].loc['Q1',i],((self.q_average_list[i])['SE'])['A'].loc['Q2',i],((self.q_average_list[i])['SE'])['A'].loc['Q3',i],((self.q_average_list[i])['SE'])['A'].loc['Q4',i],((self.q_average_list[i])['SE'])['A'].loc['Q5',i]]
			self.SE_B_list[i] = [((self.q_average_list[i])['SE'])['B'].loc['Q1',i],((self.q_average_list[i])['SE'])['B'].loc['Q2',i],((self.q_average_list[i])['SE'])['B'].loc['Q3',i],((self.q_average_list[i])['SE'])['B'].loc['Q4',i],((self.q_average_list[i])['SE'])['B'].loc['Q5',i]]
			self.SE_C_list[i] = [((self.q_average_list[i])['SE'])['C'].loc['Q1',i],((self.q_average_list[i])['SE'])['C'].loc['Q2',i],((self.q_average_list[i])['SE'])['C'].loc['Q3',i],((self.q_average_list[i])['SE'])['C'].loc['Q4',i],((self.q_average_list[i])['SE'])['C'].loc['Q5',i]]
		self.SE_list = [self.SE_A_list,self.SE_B_list,self.SE_C_list]
		self.toXlsx_list(evaluation='SUBJECTIVE_EVALUATION', df_l=self.SE_list)

	def toXlsx(self, evaluation, df):
		self.w_dir = '/Users/sprout/OneDrive - 名古屋工業大学/学校/研究室/実験/卒論実験/q_calculate'
		self.w_name = self.w_dir + '/' + evaluation + '.xlsx'
		df.to_excel(self.w_name)
		print(self.w_name)
	
	def toXlsx_list(self, evaluation, df_l):
		self.w_name = self.w_dir + '/' + evaluation + '.xlsx'
		with pd.ExcelWriter(self.w_name) as writer:
			for i, df in enumerate(df_l):
				if i == 0:
					df.to_excel(writer, sheet_name="A")
				elif i == 1:
					df.to_excel(writer, sheet_name="B")
				elif i == 2:
					df.to_excel(writer, sheet_name="C")
		print(self.w_name)

class Q_IMAGE:
	def __init__(self) -> None:
		pass

	def main(self):
		self.fig_MS()
		self.fig_SE()
		self.fig_TLX()
		self.fig_MD()
		self.fig_ALL_TLX()
		self.fig_ALL_Q1()
		self.fig_ALL_Q2()
		self.fig_ALL_Q3()

	def fig_MS(self):
		self.condition = []
		self.item = []
		self.value = []
		self.path = '/Users/sprout/OneDrive - 名古屋工業大学/学校/研究室/実験/卒論実験/q_calculate/MINIMAL_SELF.xlsx'
		self.data = pd.read_excel(self.path, sheet_name=None, index_col=0)
		self.keys = []
		for i in self.data.keys():
			self.keys.append(i)
		self.index = self.data[self.keys[0]].index.values
		for key in self.keys:
			for index in self.index:
				self.i = self.data[key].loc[index]
				for name in range(len(self.i)):	
					if key == 'A':
						self.condition.append('without feedback')
					elif key == 'B':
						self.condition.append('partner velocity')
					elif key == 'C':
						self.condition.append('robot velocity')
					if index == 'ownership':
						self.item.append('Ownership')
					elif index == 'ownership_control':
						self.item.append('Ownership Control')
					elif index == 'agency':
						self.item.append('Agency')
					elif index == 'agency_control':
						self.item.append('Agency Control')
					self.value.append(self.i[name])
		self.MS_df = pd.DataFrame({'condition':self.condition,'':self.item,'Questionnaire rating':self.value})
		sns.set_palette('Paired')
		
		self.ax = sns.boxplot(x='condition', y='Questionnaire rating', hue='', data=self.MS_df)
		self.ax.legend([],['Ownership','Ownership Control','Agency','Agency Control'])
		self.lg = plt.legend(loc='upper right', bbox_to_anchor=(0.97, 0.5, 0.5, .100), borderaxespad=0.,)
		plt.savefig('questionnaire/graph/MINIMAL_SELF.png', dpi=300, format='png', bbox_extra_artists=(self.lg,), bbox_inches='tight')
		plt.figure()

	def fig_SE(self):
		self.condition_1 = []
		self.condition_2 = []
		self.condition_3 = []
		self.condition_4 = []
		self.condition_5 = []
		self.item_1 = []
		self.item_2 = []
		self.item_3 = []
		self.item_4 = []
		self.item_5 = []
		self.value_1 = []
		self.value_2 = []
		self.value_3 = []
		self.value_4 = []
		self.value_5 = []
		self.path = '/Users/sprout/OneDrive - 名古屋工業大学/学校/研究室/実験/卒論実験/q_calculate/SUBJECTIVE_EVALUATION.xlsx'
		self.data = pd.read_excel(self.path, sheet_name=None, index_col=0)
		self.keys = []
		for i in self.data.keys():
			self.keys.append(i)
		self.index = self.data[self.keys[0]].index.values
		for key in self.keys:
			for index in self.index:
				if index == 'Q1':
					self.i_1 = self.data[key].loc[index]
					for name in range(len(self.i)):
						if key == 'A':
							self.condition_1.append('without feedback')
						elif key == 'B':
							self.condition_1.append('partner velocity')
						elif key == 'C':
							self.condition_1.append('robot velocity')
						self.item_1.append(index)
						self.value_1.append(self.i_1[name])
				elif index == 'Q2':
					self.i_2 = self.data[key].loc[index]
					for name in range(len(self.i)):
						if key == 'A':
							self.condition_2.append('without feedback')
						elif key == 'B':
							self.condition_2.append('partner velocity')
						elif key == 'C':
							self.condition_2.append('robot velocity')
						self.item_2.append(index)
						self.value_2.append(self.i_2[name])
				elif index == 'Q3':
					self.i_3 = self.data[key].loc[index]
					for name in range(len(self.i)):
						if key == 'A':
							self.condition_3.append('without feedback')
						elif key == 'B':
							self.condition_3.append('partner velocity')
						elif key == 'C':
							self.condition_3.append('robot velocity')
						self.item_3.append(index)
						self.value_3.append(self.i_3[name])
				elif index == 'Q4':
					self.i_4 = self.data[key].loc[index]
					for name in range(len(self.i)):
						if key == 'A':
							self.condition_4.append('without feedback')
						elif key == 'B':
							self.condition_4.append('partner velocity')
						elif key == 'C':
							self.condition_4.append('robot velocity')
						self.item_4.append(index)
						self.value_4.append(self.i_4[name])
				elif index == 'Q5':
					self.i_5 = self.data[key].loc[index]
					for name in range(len(self.i)):
						if key == 'A':
							self.condition_5.append('without feedback')
						elif key == 'B':
							self.condition_5.append('partner velocity')
						elif key == 'C':
							self.condition_5.append('robot velocity')
						self.item_5.append(index)
						self.value_5.append(self.i_5[name])

		self.SE_df_1 = pd.DataFrame({'condition':self.condition_1,'':self.item_1,'Questionnaire rating':self.value_1})
		sns.set_palette('Set2')
		self.ax = sns.boxplot(x='condition', y='Questionnaire rating', data=self.SE_df_1)
		plt.savefig('questionnaire/graph/SUBJECTIVE_EVALUATION_1.png', dpi=300, format='png')
		plt.figure()
		self.SE_df_2 = pd.DataFrame({'condition':self.condition_2,'':self.item_2,'Questionnaire rating':self.value_2})
		sns.set_palette('Set2')
		self.ax = sns.boxplot(x='condition', y='Questionnaire rating', data=self.SE_df_2)
		plt.savefig('questionnaire/graph/SUBJECTIVE_EVALUATION_2.png', dpi=300, format='png')
		plt.figure()
		self.SE_df_3 = pd.DataFrame({'condition':self.condition_3,'':self.item_3,'Questionnaire rating':self.value_3})
		sns.set_palette('Set2')
		self.ax = sns.boxplot(x='condition', y='Questionnaire rating', data=self.SE_df_3)
		plt.savefig('questionnaire/graph/SUBJECTIVE_EVALUATION_3.png', dpi=300, format='png')
		plt.figure()
		self.SE_df_4 = pd.DataFrame({'condition':self.condition_4,'':self.item_4,'Questionnaire rating':self.value_4})
		sns.set_palette('Set2')
		self.ax = sns.boxplot(x='condition', y='Questionnaire rating', data=self.SE_df_4)
		plt.savefig('questionnaire/graph/SUBJECTIVE_EVALUATION_4.png', dpi=300, format='png')
		plt.figure()
		self.SE_df_5 = pd.DataFrame({'condition':self.condition_5,'':self.item_5,'Questionnaire rating':self.value_5})
		sns.set_palette('Set2')
		self.ax = sns.boxplot(x='condition', y='Questionnaire rating', data=self.SE_df_5)
		plt.savefig('questionnaire/graph/SUBJECTIVE_EVALUATION_5.png', dpi=300, format='png')
		plt.figure()

	def fig_TLX(self):
		self.condition = []
		self.item = []
		self.value = []
		self.path = '/Users/sprout/OneDrive - 名古屋工業大学/学校/研究室/実験/卒論実験/q_calculate/TLX_AWWL.xlsx'
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
						self.condition.append('partner velocity')
					elif index == 'C':
						self.condition.append('robot velocity')
					self.item.append(index)
					self.value.append(self.i[name])
		self.TLX_df = pd.DataFrame({'condition':self.condition,'':self.item,'AWWL':self.value})
		sns.set_palette('Set2')
		self.ax = sns.boxplot(x='condition', y='AWWL', data=self.TLX_df)
		plt.savefig('questionnaire/graph/TLX_AWWL.png', dpi=300, format='png')
		plt.figure()
	
	def fig_MD(self):
		self.condition = []
		self.item = []
		self.value = []
		self.path = '/Users/sprout/OneDrive - 名古屋工業大学/学校/研究室/実験/卒論実験/q_calculate/MD_SCORE.xlsx'
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
						self.condition.append('partner velocity')
					elif index == 'C':
						self.condition.append('robot velocity')
					self.item.append(index)
					self.value.append(self.i[name])
		self.MD_df = pd.DataFrame({'condition':self.condition,'':self.item,'Questionnaire rating':self.value})
		sns.set_palette('Set2')
		self.ax = sns.boxplot(x='condition', y='Questionnaire rating', data=self.MD_df)
		self.ax.set_ylim(0,8)
		plt.savefig('questionnaire/graph/MD_SCORE.png', dpi=300, format='png')
		plt.figure()

	def fig_ALL_TLX(self):
		self.condition = []
		self.cycle = []
		self.value = []
		self.path = '/Users/sprout/OneDrive - 名古屋工業大学/学校/研究室/実験/卒論実験/q_calculate/ALL_TLX_COST.xlsx'
		self.data = pd.read_excel(self.path, sheet_name=None, index_col=0)
		self.keys = []
		self.condition = []
		for i in self.data.keys():
			self.keys.append(i)
		for key in self.keys:
			for k, l in enumerate(self.data[self.keys[0]].columns.values):
				for j in range(len(self.data[key][l].values)):
					self.value.append(self.data[key][l].values[j])
					self.cycle.append(key)
					if l == 'A':
						self.condition.append('without feedback')
					elif l == 'B':
						self.condition.append('partner velocity')
					elif l == 'C':
						self.condition.append('robot velocity')
		self.ALLDTW_df = pd.DataFrame({'condition':self.condition,'AWWL':self.value,'Cycle':self.cycle})
		sns.set_palette('Set2')
		self.ax = sns.boxplot(x='Cycle',y='AWWL',hue='condition',data=self.ALLDTW_df)
		self.ax.legend([],['without feedback','partner velocity','robot velocity'])
		self.lg = plt.legend(loc='upper right', bbox_to_anchor=(0.95, 0.5, 0.5, .100), borderaxespad=0.,)
		plt.savefig('questionnaire/graph/ALL_TLX_SCORE.png',dpi=300, format='png', bbox_extra_artists=(self.lg,), bbox_inches='tight')
		plt.figure()

	def fig_ALL_Q1(self):
		self.condition = []
		self.cycle = []
		self.value = []
		self.path = '/Users/sprout/OneDrive - 名古屋工業大学/学校/研究室/実験/卒論実験/q_calculate/ALL_Q1.xlsx'
		self.data = pd.read_excel(self.path, sheet_name=None, index_col=0)
		self.keys = []
		self.condition = []
		for i in self.data.keys():
			self.keys.append(i)
		for key in self.keys:
			for k, l in enumerate(self.data[self.keys[0]].columns.values):
				for j in range(len(self.data[key][l].values)):
					self.value.append(self.data[key][l].values[j])
					self.cycle.append(key)
					if l == 'A':
						self.condition.append('without feedback')
					elif l == 'B':
						self.condition.append('partner velocity')
					elif l == 'C':
						self.condition.append('robot velocity')
		self.ALLQ1_df = pd.DataFrame({'condition':self.condition,'Questionnaire rating':self.value,'Cycle':self.cycle})
		sns.set_palette('Set2')
		self.ax = sns.boxplot(x='Cycle',y='Questionnaire rating',hue='condition',data=self.ALLQ1_df)
		self.ax.legend([],['without feedback','partner velocity','robot velocity'])
		self.lg = plt.legend(loc='upper right', bbox_to_anchor=(0.95, 0.5, 0.5, .100), borderaxespad=0.,)
		plt.savefig('questionnaire/graph/ALL_Q1.png',dpi=300, format='png', bbox_extra_artists=(self.lg,), bbox_inches='tight')
		plt.figure()

	def fig_ALL_Q2(self):
		self.condition = []
		self.cycle = []
		self.value = []
		self.path = '/Users/sprout/OneDrive - 名古屋工業大学/学校/研究室/実験/卒論実験/q_calculate/ALL_Q2.xlsx'
		self.data = pd.read_excel(self.path, sheet_name=None, index_col=0)
		self.keys = []
		self.condition = []
		for i in self.data.keys():
			self.keys.append(i)
		for key in self.keys:
			for k, l in enumerate(self.data[self.keys[0]].columns.values):
				for j in range(len(self.data[key][l].values)):
					self.value.append(self.data[key][l].values[j])
					self.cycle.append(key)
					if l == 'A':
						self.condition.append('without feedback')
					elif l == 'B':
						self.condition.append('partner velocity')
					elif l == 'C':
						self.condition.append('robot velocity')
		self.ALLQ2_df = pd.DataFrame({'condition':self.condition,'Questionnaire rating':self.value,'Cycle':self.cycle})
		sns.set_palette('Set2')
		self.ax = sns.boxplot(x='Cycle',y='Questionnaire rating',hue='condition',data=self.ALLQ2_df)
		self.ax.legend([],['without feedback','partner velocity','robot velocity'])
		self.lg = plt.legend(loc='upper right', bbox_to_anchor=(0.95, 0.5, 0.5, .100), borderaxespad=0.,)
		plt.savefig('questionnaire/graph/ALL_Q2.png',dpi=300, format='png', bbox_extra_artists=(self.lg,), bbox_inches='tight')
		plt.figure()

	def fig_ALL_Q3(self):
		self.condition = []
		self.cycle = []
		self.value = []
		self.path = '/Users/sprout/OneDrive - 名古屋工業大学/学校/研究室/実験/卒論実験/q_calculate/ALL_Q3.xlsx'
		self.data = pd.read_excel(self.path, sheet_name=None, index_col=0)
		self.keys = []
		self.condition = []
		for i in self.data.keys():
			self.keys.append(i)
		for key in self.keys:
			for k, l in enumerate(self.data[self.keys[0]].columns.values):
				for j in range(len(self.data[key][l].values)):
					self.value.append(self.data[key][l].values[j])
					self.cycle.append(key)
					if l == 'A':
						self.condition.append('without feedback')
					elif l == 'B':
						self.condition.append('partner velocity')
					elif l == 'C':
						self.condition.append('robot velocity')
		self.ALLQ3_df = pd.DataFrame({'condition':self.condition,'Questionnaire rating':self.value,'Cycle':self.cycle})
		sns.set_palette('Set2')
		self.ax = sns.boxplot(x='Cycle',y='Questionnaire rating',hue='condition',data=self.ALLQ3_df)
		self.ax.legend([],['without feedback','partner velocity','robot velocity'])
		self.lg = plt.legend(loc='upper right', bbox_to_anchor=(0.95, 0.5, 0.5, .100), borderaxespad=0.,)
		plt.savefig('questionnaire/graph/ALL_Q3.png',dpi=300, format='png', bbox_extra_artists=(self.lg,), bbox_inches='tight')
		plt.figure()

if __name__ in '__main__':
	q_read = Q_AVERAGE()
	q_graph = Q_IMAGE()
	q_read.main()
	q_graph.main()