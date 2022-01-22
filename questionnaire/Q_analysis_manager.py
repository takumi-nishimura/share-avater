import pandas as pd
import numpy as np
import os
import glob
import matplotlib.pyplot as plt
import seaborn as sns

class Q_AVERAGE:
	def __init__(self) -> None:
		self.q_A_list = []
		self.q_B_list = []
		self.q_C_list = []
		self.df_A_dict = {}
		self.df_B_dict = {}
		self.df_C_dict = {}
		self.q_average_list = {}

	def main(self):
		self.participant_l()

		for self.participant in self.participant_list:
			self.read()
			self.TLX_c()
			self.MS_c()
			self.MD_c()
			self.SE_c()
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
			self.TLX_A.append(((self.df_A_dict[str(i+1)])['TLX_awwl'])[0])
		for i in range(len(self.df_B_dict)):
			self.TLX_B.append(((self.df_B_dict[str(i+1)])['TLX_awwl'])[0])
		for i in range(len(self.df_C_dict)):
			self.TLX_C.append(((self.df_C_dict[str(i+1)])['TLX_awwl'])[0])
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
		self.w_dir = '/Users/sprout/OneDrive - 名古屋工業大学/学校/研究室/実験/卒論実験/q_calcurate'
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

	def fig_MS(self):
		self.condition = []
		self.item = []
		self.value = []
		self.path = '/Users/sprout/OneDrive - 名古屋工業大学/学校/研究室/実験/卒論実験/q_calcurate/MINIMAL_SELF.xlsx'
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
						self.condition.append('companion speed')
					elif key == 'C':
						self.condition.append('robot speed')
					self.item.append(index)
					self.value.append(self.i[name])
		self.MS_df = pd.DataFrame({'condition':self.condition,'':self.item,'Questionnaire rating':self.value})
		sns.set_palette('Paired')
		
		self.ax = sns.boxplot(x='condition', y='Questionnaire rating', hue='', data=self.MS_df)
		self.lg = plt.legend(loc='upper right', bbox_to_anchor=(0.9, 0.5, 0.5, .100), borderaxespad=0.,)
		plt.savefig('MINIMALSELF.png', 
            dpi=300, 
            format='png', 
            bbox_extra_artists=(self.lg,), 
            bbox_inches='tight')

if __name__ in '__main__':
	q_read = Q_AVERAGE()
	q_graph = Q_IMAGE()
	q_read.main()
	q_graph.main()