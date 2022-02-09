# -----------------------------------------------------------------------
# Author:   Takumi Nishimura (Haptics Lab)
# Created:  2022/02/02
# Summary:  Questionnaire analysis manager
# -----------------------------------------------------------------------

import os
import glob
import pandas as pd
import numpy as np
from Figure.figure_manager import FIG

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
			print(self.name)
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
					if condition == 'A':
						condition = 'without feedback'
					elif condition == 'B':
						condition = 'partner velocity'
					elif condition == 'C':
						condition = 'robot velocity'
					self.participant.append(name)
					self.condition.append(condition)
					self.cycle.append(cycle)
					self.evaluation.append(i)
					self.number.append(j+1)
					self.data.append(k)

	def export(self, name):
		self.export_df = pd.DataFrame({'Participant':self.participant,'Condition':self.condition,'Cycle':self.cycle,'Evaluation':self.evaluation,'Number':self.number,'Score':self.data})
		self.exportPath = 'Analysis/ExData/Questionnaire/CutData/'
		self.exportName = self.exportPath + name
		self.export_df.to_excel(self.exportName)

class QUESTIONNAIRE_Analysis:
	def __init__(self,readname) -> None:
		print('--- import --- : Questionnaire Analysis')

		self.figure = FIG()
		self.main(readname)

	def main(self,readname):
		print('--- start --- : Questionnaire Analysis')

		self.data = pd.read_excel(readname, index_col=0)

		self.partisipant_list = list(dict.fromkeys(self.data['Participant'].values))
		self.condition_list = list(dict.fromkeys(self.data['Condition'].values))
		self.cycle_list = list(dict.fromkeys(self.data['Cycle'].values))

		self.A_TLX()
		self.A_MS()
		self.A_MD()
		self.A_SE()

		print('--- finish --- : Questionnaire Analysis')

	def make_df(self,df,key:str=''):
		self.e_flag = 0
		self.mean_l = []
		self.diff_l = []
		self.export_df = pd.DataFrame(columns=['Participant','Condition','Cycle','Score'])
		for i in self.partisipant_list:
			for j in self.condition_list:
				for k in self.cycle_list:
					self.d_c = df[(df['Participant']==i) & (df['Condition']==j) & (df['Cycle']==k)]['Score'].values
					if key == 'tlx':
						self.d_c.sort()
						self.score = (self.d_c[0]*1+self.d_c[1]*2+self.d_c[2]*3+self.d_c[3]*4+self.d_c[4]*5+self.d_c[5]*6)/21
						self.e_flag = 1
					elif key == 'ownership':
						self.score = self.d_c[0]-self.d_c[1]
						self.e_flag = 1
					elif key == 'agency':
						self.score = self.d_c[2]-self.d_c[3]
						self.e_flag = 1
					elif key == 'md':
						self.score = self.d_c[0]
						self.e_flag = 1
					elif key == 'Q1':
						self.score = self.d_c[0]
						self.e_flag = 1
					elif key == 'Q2':
						self.score = self.d_c[1]
						self.e_flag = 1
					elif key == 'Q3':
						self.score = self.d_c[2]
						self.e_flag = 1
					elif key == 'Q4':
						self.score = self.d_c[3]
						self.e_flag = 1
					elif key == 'Q5':
						self.score = self.d_c[4]
						self.e_flag = 1
					elif key == 'mean':
						self.mean_l.append(self.d_c)
						if len(self.mean_l) == self.cycle_list[-1]:
							self.score = np.average(self.mean_l)
							k = 'mean'
							self.e_flag = 1
							self.mean_l = []
					elif key == '3-1':
						self.diff_l.append(self.d_c)
						if len(self.diff_l) == 3:
							self.score = (self.diff_l[2] - self.diff_l[0])[0]
							k = '3-1'
							self.e_flag = 1
							self.diff_l = []
					if self.e_flag == 1:
						self.export_df = self.export_df.append({'Participant':i,'Condition':j,'Cycle':k,'Score':self.score},ignore_index=True)
					self.e_flag = 0
		return self.export_df

	def A_TLX(self):
		self.d_l = self.data[self.data['Evaluation'] == 'TLX_q']
		# --- exportExcel --- #
		self.awwl_df = self.make_df(self.d_l,key='tlx')
		self.awwl_df.to_excel('Analysis/ExData/Questionnaire/CutData/All_TLX.xlsx')

		self.awwl_mean_df = self.make_df(self.awwl_df,key='mean')
		self.awwl_mean_df.to_excel('Analysis/ExData/Questionnaire/CutData/Mean_TLX.xlsx')
		
		# --- figure --- #
		self.figure.MeanBoxPlot(self.awwl_mean_df,ylabel='AWWL',filename='TLX_AWWL_MEAN')

		self.figure.CycleBoxPlot(self.awwl_df,ylabel='AWWL',filename='TLX_AWWL_CYCLE')

	def A_MS(self):
		self.d_l = self.data[self.data['Evaluation'] == 'MS_score']
		# --- exportExcel --- #
		self.ownership_df = self.make_df(self.d_l,key='ownership')
		self.agency_df = self.make_df(self.d_l,key='agency')
		self.ownership_df.to_excel('Analysis/ExData/Questionnaire/CutData/All_Ownership.xlsx')
		self.agency_df.to_excel('Analysis/ExData/Questionnaire/CutData/All_Agency.xlsx')

		self.ownership_mean_df = self.make_df(self.ownership_df,key='mean')
		self.agency_mean_df = self.make_df(self.agency_df,key='mean')
		self.ownership_mean_df.to_excel('Analysis/ExData/Questionnaire/CutData/Mean_Ownership.xlsx')
		self.agency_mean_df.to_excel('Analysis/ExData/Questionnaire/CutData/Mean_Agency.xlsx')

		# --- figure --- #
		self.figure.MeanBoxPlot(df=self.ownership_mean_df,ylabel='Ownership - Ownership Control',filename='OWNERSHIP_MEAN')

		self.figure.MeanBoxPlot(df=self.agency_mean_df,ylabel='Agency - Agency Control',filename='AGENCY_MEAN')

		self.figure.CycleBoxPlot(self.ownership_df,ylabel='Ownership - Ownership Control',filename='OWNERSHIP_CYCLE')

		self.figure.CycleBoxPlot(self.agency_df,ylabel='Agency - Agency Control',filename='AGENCY_CYCLE')

	def A_MD(self):
		self.d_l = self.data[self.data['Evaluation'] == 'MD_r']

		# --- exportExcel --- #
		self.md_df = self.make_df(self.d_l,key='md')
		self.md_df.to_excel('Analysis/ExData/Questionnaire/CutData/All_MD.xlsx')

		self.md_mean_df = self.make_df(self.md_df,key='mean')
		self.md_mean_df.to_excel('Analysis/ExData/Questionnaire/CutData/Mean_MD.xlsx')

		self.md_31_df = self.make_df(self.md_df,key='3-1')
		self.md_31_df.to_excel('Analysis/ExData/Questionnaire/CutData/31_MD.xlsx')

		# --- figure --- #
		self.figure.MeanBoxPlot(self.md_mean_df,ylabel='Mental Distance',filename='MD_MEAN',min=0,max=7.5)

		self.figure.CycleBoxPlot(self.md_df,ylabel='Mendal Distance',filename='MD_CYCLE',min=0,max=7.5)

		self.figure.MeanBoxPlot(self.md_31_df,ylabel='Difference in mental distance\nbetween the third and the first time',filename='MD_31')

	def A_SE(self):
		self.d_l = self.data[self.data['Evaluation'] == 'SE_r']
		# --- exportExcel --- #
		self.SE_Q1_df = self.make_df(self.d_l,key='Q1')
		self.SE_Q1_mean_df = self.make_df(self.SE_Q1_df,key='mean')
		self.SE_Q2_df = self.make_df(self.d_l,key='Q2')
		self.SE_Q2_mean_df = self.make_df(self.SE_Q2_df,key='mean')
		self.SE_Q3_df = self.make_df(self.d_l,key='Q3')
		self.SE_Q3_mean_df = self.make_df(self.SE_Q3_df,key='mean')
		self.SE_Q4_df = self.make_df(self.d_l,key='Q4')
		self.SE_Q4_mean_df = self.make_df(self.SE_Q4_df,key='mean')
		self.SE_Q5_df = self.make_df(self.d_l,key='Q5')
		self.SE_Q5_mean_df = self.make_df(self.SE_Q5_df,key='mean')

		self.SE_Q3_31_df = self.make_df(self.SE_Q3_df,key='3-1')

		self.SE_Q1_df.to_excel('Analysis/ExData/Questionnaire/CutData/All_Q1.xlsx')
		self.SE_Q4_df.to_excel('Analysis/ExData/Questionnaire/CutData/All_Q4.xlsx')
		self.SE_Q5_df.to_excel('Analysis/ExData/Questionnaire/CutData/All_Q5.xlsx')

		self.SE_Q1_mean_df.to_excel('Analysis/ExData/Questionnaire/CutData/Mean_Q1.xlsx')
		self.SE_Q2_mean_df.to_excel('Analysis/ExData/Questionnaire/CutData/Mean_Q2.xlsx')
		self.SE_Q3_mean_df.to_excel('Analysis/ExData/Questionnaire/CutData/Mean_Q3.xlsx')
		self.SE_Q4_mean_df.to_excel('Analysis/ExData/Questionnaire/CutData/Mean_Q4.xlsx')
		self.SE_Q5_mean_df.to_excel('Analysis/ExData/Questionnaire/CutData/Mean_Q5.xlsx')

		self.SE_Q3_31_df.to_excel('Analysis/ExData/Questionnaire/CutData/31_Q3.xlsx')

		# --- figure --- #
		self.figure.MeanBoxPlot(df=self.SE_Q1_mean_df,ylabel='Questionnaire rating',filename='Q1_MEAN')
		self.figure.MeanBoxPlot(df=self.SE_Q2_mean_df,ylabel='Questionnaire rating',filename='Q2_MEAN')
		self.figure.MeanBoxPlot(df=self.SE_Q3_mean_df,ylabel='Questionnaire rating',filename='Q3_MEAN')
		self.figure.MeanBoxPlot(df=self.SE_Q4_mean_df,ylabel='Questionnaire rating',filename='Q4_MEAN')
		self.figure.MeanBoxPlot(df=self.SE_Q5_mean_df,ylabel='Questionnaire rating',filename='Q5_MEAN')

		self.figure.CycleBoxPlot(df=self.SE_Q1_df,ylabel='Questionnaire rating',filename='Q1_CYCLE')
		self.figure.CycleBoxPlot(df=self.SE_Q3_df,ylabel='Questionnaire rating',filename='Q3_CYCLE')
		self.figure.CycleBoxPlot(df=self.SE_Q4_df,ylabel='Questionnaire rating',filename='Q4_CYCLE')
		self.figure.CycleBoxPlot(df=self.SE_Q5_df,ylabel='Questionnaire rating',filename='Q5_CYCLE')

		self.figure.MeanBoxPlot(df=self.SE_Q3_31_df,ylabel='Difference in questionnaire rating\nbetween the third and the first time',filename='Q3_31')

if __name__ in '__main__':
	questionnaireAnalysisExport = QUESTIONNAIRE_Export('AllQuestionnaireData_20220202.xlsx')
	questionnaireAnalysis = QUESTIONNAIRE_Analysis('Analysis/ExData/Questionnaire/CutData/AllQuestionnaireData_20220202.xlsx')