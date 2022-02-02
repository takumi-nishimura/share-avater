# -----------------------------------------------------------------------
# Author:   Takumi Nishimura (Haptics Lab)
# Created:  2022/02/02
# Summary:  Questionnaire analysis manager
# -----------------------------------------------------------------------

import os
import glob
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from Figure import figure_3mean

class QUESTIONNAIRE_Export:
	def __init__(self,exportname):
		print('--- import --- : Questionnaire Export')

		self.participant = []
		self.condition = []
		self.cycle = []
		self.evaluation = []
		self.data = []
		self.number = []

		self.main(exportname)

	def main(self,exportname):
		print('--- start --- : Questionnaire Export')

		self.participant_l()

		for self.name in self.participant_list:
			self.read()

		self.export(name=exportname)
			
		print('--- finish --- : Questionnaire Export')

	def participant_l(self):
		self.file_list = []
		self.participant_list = []
		self.dir = os.path.join('analysis','ExData','Questionnaire','RawData')
		self.files = sorted(glob.glob(os.path.join(self.dir, '*.csv')))

		for self.filename_s in self.files:
			self.filename_split = self.filename_s.split('_')
			self.participant_name = self.filename_split[1]
			if self.participant_name in self.participant_list:
				pass
			else:
				self.participant_list.append(self.participant_name)

	def read(self):
		for self.filename in self.files:
			if self.name in self.filename:
				self.read_df = pd.read_csv(self.filename, index_col=0)
				self.filename_sp = self.filename.split('_')
				self.make_list(self.name,self.filename_sp[2],self.filename_sp[3])

	def make_list(self,name,condition,cycle):
		for i in self.read_df.columns.values:
				for j,k in enumerate(self.read_df[i].values[~np.isnan(self.read_df[i])]):
					self.participant.append(name)
					self.condition.append(condition)
					self.cycle.append(cycle)
					self.evaluation.append(i)
					self.number.append(j+1)
					self.data.append(k)

	def export(self, name):
		self.export_df = pd.DataFrame({'participant':self.participant,'condition':self.condition,'cycle':self.cycle,'evaluation':self.evaluation,'number':self.number,'score':self.data})
		self.exportPath = 'Analysis/ExData/Questionnaire/CutData/'
		self.exportName = self.exportPath + name
		self.export_df.to_excel(self.exportName)

class QUESTIONNAIRE_Analysis:
	def __init__(self,readname) -> None:
		print('--- import --- : Questionnaire Analysis')

		self.main(readname)

	def main(self,readname):
		print('--- start --- : Questionnaire Analysis')

		self.data = pd.read_excel(readname, index_col=0)

		self.partisipant_list = list(dict.fromkeys(self.data['participant'].values))
		self.condition_list = list(dict.fromkeys(self.data['condition'].values))
		self.cycle_list = list(dict.fromkeys(self.data['cycle'].values))

		self.A_TLX()

		print('--- finish --- : Questionnaire Analysis')

	def A_TLX(self):
		# --- exportExcel --- #
		self.awwl_l = []
		self.awwl_df = pd.DataFrame(columns=['participant','condition','cycle','awwl'])
		self.d_l = self.data[self.data['evaluation'] == 'TLX_q']
		for i in self.partisipant_list:
			for j in self.condition_list:
				for k in self.cycle_list:
					self.d_c = self.d_l[(self.d_l['evaluation']=='TLX_q') & (self.d_l['participant']==i) & (self.d_l['condition']==j) & (self.d_l['cycle']==k)]['score'].values
					self.d_c.sort()
					self.awwl = (self.d_c[0]*1+self.d_c[1]*2+self.d_c[2]*3+self.d_c[3]*4+self.d_c[4]*5+self.d_c[5]*6)/21
					self.awwl_df = self.awwl_df.append({'participant':i,'condition':j,'cycle':k,'awwl':self.awwl},ignore_index=True)
		self.awwl_df.to_excel('Analysis/ExData/Questionnaire/CutData/All_TLX.xlsx')

		# --- figure --- #
		self.awwl_mean_l = []
		self.awwl_mean_df = pd.DataFrame(columns=['participant','condition','AWWL'])
		for i in self.partisipant_list:
			for j in self.condition_list:
				for k in self.cycle_list:
					self.d_awwl = self.awwl_df[(self.awwl_df['participant']==i) & (self.awwl_df['condition']==j) & (self.awwl_df['cycle']==k)]['awwl'].values[0]
					self.awwl_mean_l.append(self.d_awwl)
					if len(self.awwl_mean_l) == self.cycle_list[-1]:
						self.awwl_mean = np.average(self.awwl_mean_l)
						self.awwl_mean_df = self.awwl_mean_df.append({'participant':i,'condition':j,'AWWL':self.awwl_mean},ignore_index=True)
						self.awwl_mean_l = []
		self.awwl_mean_df.to_excel('Analysis/ExData/Questionnaire/CutData/Mean_TLX.xlsx')
		sns.set_palette('Set2')
		self.ax = sns.boxplot(x='condition', y='AWWL', data=self.awwl_mean_df)
		self.ax.set_xticklabels(['without feedback','partner velocity','robot velocity'])
		self.ax.set_xlabel('Condition')
		plt.savefig('Analysis/Figure/Questionnaire/TLX_AWWL_MEAN.jpg', dpi=300, format='jpg')		

if __name__ in '__main__':
	figure = figure_3mean.FIG_MEAN()
	questionnaireAnalysisExport = QUESTIONNAIRE_Export('AllQuestionnaireData_20220202.xlsx')
	questionnaireAnalysis = QUESTIONNAIRE_Analysis('Analysis/ExData/Questionnaire/CutData/AllQuestionnaireData_20220202.xlsx')