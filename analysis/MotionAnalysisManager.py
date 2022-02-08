# -----------------------------------------------------------------------
# Author:   Takumi Nishimura (Haptics Lab)
# Created:  2022/02/02
# Summary:  Motion analysis manager
# -----------------------------------------------------------------------

import os
import glob
import pandas as pd
import numpy as np
from Figure.figure_manager import FIG
from MotionAnalysisDTW import DTW
from MotionAnalysisJRK import JRK
from MotionAnalysisCoT import CoT

class MOTIONAN_ALYSIS:
	def __init__(self) -> None:
		print('--- import --- : Motion Analysis')

		self.dtw = DTW()
		self.jrk = JRK()
		self.cot = CoT()

		self.main()

	def main(self):
		print('--- start --- : Motion Analysis')
		
		self.get_metadata()

		self.export_df = pd.DataFrame(columns=['Participant','Condition','Cycle','Evaluation','Score'])

		self.participant_list = ['Ebina','Hijikata']
		for self.name in self.participant_list:
			for self.condition in self.condition_list:
				for self.cycle in self.cycle_list:
					self.read_csv()
					print('participant: '+self.name+'  condition: '+self.condition+'  cycle: '+self.cycle)
					self.dtw_s = self.dtw.DTW_C(self.d_1,self.d_2)
					self.export_df = self.export_df.append({'Participant':self.name,'Condition':self.condition,'Cycle':self.cycle,'Evaluation':'dtw','Score':self.dtw_s},ignore_index=True)
					self.jrk_s = self.jrk.JRK_C(self.d_r)
					self.export_df = self.export_df.append({'Participant':self.name,'Condition':self.condition,'Cycle':self.cycle,'Evaluation':'jrk','Score':self.jrk_s},ignore_index=True)
					self.cot_s = self.cot.CoT_C(self.d_r,self.d_1,self.d_2)
					self.export_df = self.export_df.append({'Participant':self.name,'Condition':self.condition,'Cycle':self.cycle,'Evaluation':'cot','Score':self.cot_s},ignore_index=True)

		self.export_df.to_excel('Analysis/ExData/Motion/CutData/Analysis_Result.xlsx')

		print('--- finish --- : Motion Analysis')

	def get_metadata(self):
		self.file_list = []
		self.participant_list = []
		self.condition_list = []
		self.cycle_list = []
		self.dir = os.path.join('analysis','ExData','Motion','CutData')
		self.files = sorted(glob.glob(os.path.join(self.dir, '*.csv')))
		for self.filename_s in self.files:
			self.filename_split = self.filename_s.split('_')
			self.participant_list.append(self.filename_split[1])
			self.condition_list.append(self.filename_split[2])
			self.cycle_list.append(self.filename_split[3])
		self.participant_list = sorted(set(self.participant_list),key=self.participant_list.index)
		self.condition_list = sorted(set(self.condition_list),key=self.condition_list.index)
		self.cycle_list = sorted(set(self.cycle_list),key=self.cycle_list.index)

	def read_csv(self):
		self.read_list = [i for i in self.files if self.name in i and self.condition+'_'+self.cycle in i]
		for i in self.read_list:
			if 'Participant1' in i:
				self.d_1 = pd.read_csv(i)
			elif 'Participant2' in i:
				self.d_2 = pd.read_csv(i)
			elif 'endEffector' in i:
				self.d_r = pd.read_csv(i)

class MOTION_FIG:
	def __init__(self) -> None:
		print('--- import --- : Motion Figure')

		self.main()

	def main(self):
		print('--- start --- : Motion Figure')

		self.figure = FIG()

		self.data = pd.read_excel('/Users/sprout/OneDrive - 名古屋工業大学/学校/研究室/code/Analysis/ExData/Motion/CutData/Analysis_Result.xlsx',index_col=0)

		self.partisipant_list = list(dict.fromkeys(self.data['Participant'].values))
		self.condition_list = list(dict.fromkeys(self.data['Condition'].values))
		self.cycle_list = list(dict.fromkeys(self.data['Cycle'].values))

		self.A_dtw()
		self.A_jrk()
		self.A_cot()

	def make_df(self,df,key:str=''):
		self.ex_df = pd.DataFrame(columns=['Participant','Condition','Cycle','Score'])
		self.e_flag = 0
		self.mean_l = []
		self.diff_l = []
		for i in self.partisipant_list:
			for j in self.condition_list:
				for k in self.cycle_list:
					self.d_c = df[(df['Participant']==i) & (df['Condition']==j) & (df['Cycle']==k)]['Score'].values
					if key == 'all':
						self.score = self.d_c[0]
						self.e_flag = 1
					elif key == 'mean':
						self.mean_l.append(self.d_c[0])
						if len(self.mean_l) == self.cycle_list[-1]:
							self.score = np.average(self.mean_l)
							k = 'mean'
							self.mean_l = []
							self.e_flag = 1
					elif key == '3-1':
						self.diff_l.append(self.d_c[0])
						if len(self.diff_l) == 3:
							self.score = self.diff_l[2]-self.diff_l[0]
							k = '3-1'
							self.e_flag = 1
							self.diff_l = []
					if self.e_flag == 1:
						self.ex_df = self.ex_df.append({'Participant':i,'Condition':j,'Cycle':k,'Score':self.score},ignore_index=True)
					self.e_flag = 0
		self.ex_df.replace({'A':'without feedback','B':'partner velocity','C':'robot velocity'},inplace=True)
		return self.ex_df

	def A_dtw(self):
		self.dtw = self.data[self.data['Evaluation']=='dtw']

		# --- exportExcel --- #
		self.dtw_df = self.make_df(self.dtw,key='all')
		self.dtw_mean_df = self.make_df(self.dtw,key='mean')
		self.dtw_31_df = self.make_df(self.dtw,key='3-1')
		self.dtw_df.to_excel('Analysis/ExData/Motion/CutData/All_DTW.xlsx')
		self.dtw_mean_df.to_excel('Analysis/ExData/Motion/CutData/Mean_DTW.xlsx')
		self.dtw_31_df.to_excel('Analysis/ExData/Motion/CutData/31_DTW.xlsx')

		# --- figure --- #
		self.figure.MeanBoxPlot(self.dtw_mean_df,dir='Motion',ylabel='DTW Score',filename='DTW_MEAN')

		self.figure.CycleBoxPlot(self.dtw_df,dir='Motion',ylabel='DTW Score',filename='DTW_CYCLE')

		self.figure.MeanBoxPlot(self.dtw_31_df,dir='Motion',ylabel='DTW Score\nbetween the third and the first time',filename='DTW_31')

	def A_jrk(self):
		self.jrk = self.data[self.data['Evaluation']=='jrk']

		# --- exportExcel --- #
		self.jrk_df = self.make_df(self.jrk,key='all')
		self.jrk_mean_df = self.make_df(self.jrk,key='mean')
		self.jrk_31_df = self.make_df(self.jrk,key='3-1')
		self.jrk_df.to_excel('Analysis/ExData/Motion/CutData/All_JRK.xlsx')
		self.jrk_mean_df.to_excel('Analysis/ExData/Motion/CutData/Mean_JRK.xlsx')
		self.jrk_31_df.to_excel('Analysis/ExData/Motion/CutData/31_JRK.xlsx')

		# --- figure --- #
		self.figure.MeanBoxPlot(self.jrk_mean_df,dir='Motion',ylabel='Jerk Index',filename='JRK_MEAN')

		self.figure.CycleBoxPlot(self.jrk_df,dir='Motion',ylabel='Jerk Index',filename='JRK_CYCLE')

		self.figure.MeanBoxPlot(self.jrk_31_df,dir='Motion',ylabel='Jerk Index\nbetween the third and the first time',filename='JRK_31')

	def A_cot(self):
		self.cot = self.data[self.data['Evaluation']=='cot']

		# --- exportExcel --- #
		self.cot_df = self.make_df(self.cot,key='all')
		self.cot_mean_df = self.make_df(self.cot,key='mean')
		self.cot_31_df = self.make_df(self.cot,key='3-1')
		self.cot_df.to_excel('Analysis/ExData/Motion/CutData/All_COT.xlsx')
		self.cot_mean_df.to_excel('Analysis/ExData/Motion/CutData/Mean_COT.xlsx')
		self.cot_31_df.to_excel('Analysis/ExData/Motion/CutData/31_COT.xlsx')

		# --- figure --- #
		self.figure.MeanBoxPlot(self.cot_mean_df,dir='Motion',ylabel='Difference Time [s]',filename='COT_MEAN')

		self.figure.CycleBoxPlot(self.cot_df,dir='Motion',ylabel='Difference Time [s]',filename='COT_CYCLE')

		self.figure.MeanBoxPlot(self.cot_31_df,dir='Motion',ylabel='Difference Time [s]\nbetween the third and the first time',filename='COT_31')

if __name__ in '__main__':
	# motionAnalysis = MOTIONAN_ALYSIS()
	motionFig = MOTION_FIG()