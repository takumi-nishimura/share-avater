# -----------------------------------------------------------------------
# Author:   Takumi Nishimura (Haptics Lab)
# Created:  2022/02/02
# Summary:  Motion analysis manager
# -----------------------------------------------------------------------

from fileinput import filename
import os
import glob
from isort import file
import pandas as pd
import numpy as np
import re
from scipy.stats import spearmanr
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

		for self.name in self.participant_list:
			for self.condition in self.condition_list:
				for self.cycle in self.cycle_list:
					self.read_csv()
					print('participant: '+self.name+'  condition: '+self.condition+'  cycle: '+self.cycle)
					# self.dtw_s = self.dtw.DTW_C(self.d_1,self.d_2)
					# self.export_df = self.export_df.append({'Participant':self.name,'Condition':self.condition,'Cycle':self.cycle,'Evaluation':'dtw','Score':self.dtw_s},ignore_index=True)
					# self.dtw_v = self.dtw.DTW_V(self.d_1,self.d_2)
					# self.export_df = self.export_df.append({'Participant':self.name,'Condition':self.condition,'Cycle':self.cycle,'Evaluation':'dtw_v','Score':self.dtw_v},ignore_index=True)
					self.dtw_n = self.dtw.DTW_N(self.d_1,self.d_2)
					self.export_df = self.export_df.append({'Participant':self.name,'Condition':self.condition,'Cycle':self.cycle,'Evaluation':'dtw_n','Score':self.dtw_n},ignore_index=True)
					self.jrk_s = self.jrk.JRK_C(self.d_r)
					self.export_df = self.export_df.append({'Participant':self.name,'Condition':self.condition,'Cycle':self.cycle,'Evaluation':'jrk','Score':self.jrk_s},ignore_index=True)
					# self.cot_s = self.cot.CoT_C(self.d_r,self.d_1,self.d_2)
					# self.export_df = self.export_df.append({'Participant':self.name,'Condition':self.condition,'Cycle':self.cycle,'Evaluation':'cot','Score':self.cot_s},ignore_index=True)

		self.export_df.to_excel('Analysis/ExData/Motion/CutData/Analysis_Result_notCOT.xlsx')

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

		self.read_performance()

		self.data = pd.read_excel('/Users/sprout/OneDrive - 名古屋工業大学/学校/研究室/code/Analysis/ExData/Motion/CutData/Analysis_Result.xlsx',index_col=0)

		self.partisipant_list = list(dict.fromkeys(self.data['Participant'].values))
		self.condition_list = list(dict.fromkeys(self.data['Condition'].values))
		self.cycle_list = list(dict.fromkeys(self.data['Cycle'].values))

		self.A_performance()
		self.A_time()
		self.A_points()
		self.A_dtw()
		self.A_dtw_N()
		self.A_jrk()
		self.A_cot()
		self.perXjrk()
		# self.perXdtw()
		# self.perXcot()

	def read_performance(self):
		self.performance_df = pd.DataFrame(columns=['Participant','Condition','Cycle','Evaluation','Score'])
		self.A_performance_df = pd.DataFrame(columns=['Participant','Condition','Cycle','Time','Points'])
		self.read_list_pf = []
		self.dir_pf = os.path.join('analysis','ExData','Performance','RawData','')
		self.files_pf = sorted(glob.glob(os.path.join(self.dir_pf,'*.xlsx')))
		for file in self.files_pf:
			self.file_sp = re.split('_',file)
			self.participant = self.file_sp[1]
			self.read_df_pf = pd.read_excel(file,index_col=0)
			for i in range(3):
				for j in range(3):
					self.A_performance_df = self.A_performance_df.append({'Participant':self.participant,'Condition':self.read_df_pf[i*3+j+1][0],'Cycle':i+1,'Time':self.read_df_pf[i*3+j+1][1],'Points':self.read_df_pf[i*3+j+1][2]},ignore_index=True)
					for k in range(2):
						if k == 0:
							self.performance_df = self.performance_df.append({'Participant':self.participant,'Condition':self.read_df_pf[i*3+j+1][0],'Cycle':i+1,'Evaluation':'time','Score':self.read_df_pf[i*3+j+1][1]},ignore_index=True)
						elif k == 1:
							self.performance_df = self.performance_df.append({'Participant':self.participant,'Condition':self.read_df_pf[i*3+j+1][0],'Cycle':i+1,'Evaluation':'points','Score':self.read_df_pf[i*3+j+1][2]},ignore_index=True)
		self.performance_df.to_excel('Analysis/ExData/Performance/CutData/Analysis_Performance.xlsx')

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
					elif key == '3':
						if k == 3:
							self.score = self.d_c[0]
							self.e_flag = 1
					if self.e_flag == 1:
						self.ex_df = self.ex_df.append({'Participant':i,'Condition':j,'Cycle':k,'Score':self.score},ignore_index=True)
					self.e_flag = 0
		self.ex_df.replace({'A':'without feedback','B':'partner velocity','C':'robot velocity'},inplace=True)
		return self.ex_df

	def calculate_pvalues(self,df):
		df = df.dropna()._get_numeric_data()
		dfcols = pd.DataFrame(columns=df.columns)
		correlation = dfcols.transpose().join(dfcols, how='outer')
		pvalues = dfcols.transpose().join(dfcols, how='outer')
		for r in df.columns:
			for c in df.columns:
				correlation[r][c] = spearmanr(df[r], df[c])[0]
				pvalues[r][c] = spearmanr(df[r], df[c])[1]
		return correlation, pvalues

	def A_performance(self):
		self.figure.ScatterPlot(self.A_performance_df,dir='Motion',filename='Performance_Plot')

	def perXjrk(self):
		self.t = pd.read_excel('/Users/sprout/OneDrive - 名古屋工業大学/学校/研究室/code/Analysis/ExData/Performance/CutData/All_TIME.xlsx')
		self.p = pd.read_excel('/Users/sprout/OneDrive - 名古屋工業大学/学校/研究室/code/Analysis/ExData/Performance/CutData/All_POINT.xlsx')
		self.md = pd.read_excel('/Users/sprout/OneDrive - 名古屋工業大学/学校/研究室/code/Analysis/ExData/Questionnaire/CutData/All_MD.xlsx')
		self.tlx = pd.read_excel('/Users/sprout/OneDrive - 名古屋工業大学/学校/研究室/code/Analysis/ExData/Questionnaire/CutData/All_TLX.xlsx')
		self.ag = pd.read_excel('/Users/sprout/OneDrive - 名古屋工業大学/学校/研究室/code/Analysis/ExData/Questionnaire/CutData/All_Agency.xlsx')
		self.ow = pd.read_excel('/Users/sprout/OneDrive - 名古屋工業大学/学校/研究室/code/Analysis/ExData/Questionnaire/CutData/All_Ownership.xlsx')
		self.Q1 = pd.read_excel('/Users/sprout/OneDrive - 名古屋工業大学/学校/研究室/code/Analysis/ExData/Questionnaire/CutData/All_Q1.xlsx')
		self.Q2 = pd.read_excel('/Users/sprout/OneDrive - 名古屋工業大学/学校/研究室/code/Analysis/ExData/Questionnaire/CutData/All_Q2.xlsx')
		self.Q3 = pd.read_excel('/Users/sprout/OneDrive - 名古屋工業大学/学校/研究室/code/Analysis/ExData/Questionnaire/CutData/All_Q3.xlsx')
		self.Q4 = pd.read_excel('/Users/sprout/OneDrive - 名古屋工業大学/学校/研究室/code/Analysis/ExData/Questionnaire/CutData/All_Q4.xlsx')
		self.Q5 = pd.read_excel('/Users/sprout/OneDrive - 名古屋工業大学/学校/研究室/code/Analysis/ExData/Questionnaire/CutData/All_Q5.xlsx')

		self.pair = pd.DataFrame({'Task time':self.t['Score'].values,'Points':self.p['Score'].values,'Jerk Index':self.jrk['Score'].values,'Condition':self.t['Condition'],'DTW Score':self.dtw_n['Score'].values,'Difference Time':self.cot['Score'].values,'Mental Distance':self.md['Score'],'TLX':self.tlx['Score'],'Agency':self.ag['Score'],'Ownership':self.ow['Score'],'Q1':self.Q1['Score'].values,'Q2':self.Q2['Score'].values,'Q3':self.Q3['Score'].values,'Q4':self.Q4['Score'].values,'Q5':self.Q5['Score'].values})
		self.perjrk = pd.DataFrame({'Task time':self.t['Score'].values,'Points':self.p['Score'].values,'Jerk Index':self.jrk['Score'].values,'Condition':self.t['Condition']})
		self.pair_woFB = self.pair[self.pair['Condition']=='without feedback']
		self.pair_partner = self.pair[self.pair['Condition']=='partner velocity']
		self.figure.pairplot(self.pair,dir='Motion',filename='PAIR')
		self.corr = self.pair.corr(method="spearman")
		self.correlation,self.p_value = self.calculate_pvalues(self.pair)
		# print(self.corr['Q1'])
		# print(self.p_value['Q1'])
		# self.figure.heatplot(self.p_value,dir='Motion',filename='pValue_HEAT')
		self.correlation.to_excel('/Users/sprout/OneDrive - 名古屋工業大学/学校/研究室/code/Analysis/ExData/Questionnaire/CutData/correlation.xlsx')
		self.p_value.to_excel('/Users/sprout/OneDrive - 名古屋工業大学/学校/研究室/code/Analysis/ExData/Questionnaire/CutData/p_value.xlsx')
		self.figure.heatplot(self.corr,dir='Motion',filename='PAIR_HEAT')
		self.figure.pairplot(self.pair_woFB,dir='Motion',filename='PAIR_WOFB')
		self.corr = self.pair_woFB.corr()
		self.figure.heatplot(self.corr,dir='Motion',filename='PAIR_HEAT_WOFB')
		self.figure.pairplot(self.pair_partner,dir='Motion',filename='PAIR_PARTNER')
		self.corr = self.pair_partner.corr()
		self.figure.heatplot(self.corr,dir='Motion',filename='PAIR_HEAT_PARTNER')

	def perXdtw(self):
		self.perdtw = pd.DataFrame({'Task time [s]':self.t['Score'].values,'Points':self.p['Score'].values,'DTW Score':self.dtw['Score'].values,'Condition':self.t['Condition']})
		self.figure.pairplot(self.perdtw,dir='Motion',filename='perXdtw')

	def perXcot(self):
		self.percot = pd.DataFrame({'Task time [s]':self.t['Score'].values,'Points':self.p['Score'].values,'Difference Time [s]':self.cot['Score'].values,'Condition':self.t['Condition']})
		self.figure.pairplot(self.percot,dir='Motion',filename='perXcot')
	
	def A_time(self):
		self.time = self.performance_df[self.performance_df['Evaluation']=='time']

		# --- exportExcel --- #
		self.time_df = self.make_df(self.time,key='all')
		self.time_mean_df = self.make_df(self.time,key='mean')
		self.time_31_df = self.make_df(self.time,key='3-1')
		self.time_3_df = self.make_df(self.time,key='3')
		self.time_df.to_excel('Analysis/ExData/Performance/CutData/All_TIME.xlsx')
		self.time_mean_df.to_excel('Analysis/ExData/Performance/CutData/Mean_TIME.xlsx')
		self.time_31_df.to_excel('Analysis/ExData/Performance/CutData/31_TIME.xlsx')
		self.time_3_df.to_excel('Analysis/ExData/Performance/CutData/3_TIME.xlsx')

		# --- figure --- #
		self.figure.MeanBoxPlot(self.time_mean_df,dir='Motion',ylabel='Task time [s]',filename='TIME_MEAN')

		self.figure.CycleBoxPlot(self.time_df,dir='Motion',ylabel='Task time [s]',filename='TIME_CYCLE')

		self.figure.MeanBoxPlot(self.time_31_df,dir='Motion',ylabel='Task time [s]\nbetween the third and the first time',filename='TIME_31')

		self.figure.MeanBoxPlot(self.time_3_df,dir='Motion',ylabel='Task time [s]',filename='TIME_3')

	def A_points(self):
		self.points = self.performance_df[self.performance_df['Evaluation']=='points']

		# --- exportExcel --- #
		self.points_df = self.make_df(self.points,key='all')
		self.points_mean_df = self.make_df(self.points,key='mean')
		self.points_31_df = self.make_df(self.points,key='3-1')
		self.points_3_df = self.make_df(self.points,key='3')
		self.points_df.to_excel('Analysis/ExData/Performance/CutData/All_POINT.xlsx')
		self.points_mean_df.to_excel('Analysis/ExData/Performance/CutData/Mean_POINT.xlsx')
		self.points_31_df.to_excel('Analysis/ExData/Performance/CutData/31_POINT.xlsx')
		self.points_3_df.to_excel('Analysis/ExData/Performance/CutData/3_POINT.xlsx')

		# --- figure --- #
		self.figure.MeanBoxPlot(self.points_mean_df,dir='Motion',ylabel='Task points',filename='POINT_MEAN')

		self.figure.CycleBoxPlot(self.points_df,dir='Motion',ylabel='Task points',filename='POINT_CYCLE')

		self.figure.MeanBoxPlot(self.points_31_df,dir='Motion',ylabel='Task points\nbetween the third and the first points',filename='POINT_31')

		self.figure.MeanBoxPlot(self.points_3_df,dir='Motion',ylabel='Task points',filename='POINT_3')

	def A_dtw_N(self):
		print('aaa')
		self.d = pd.read_excel('/Users/sprout/OneDrive - 名古屋工業大学/学校/研究室/code/Analysis/ExData/Motion/CutData/Analysis_Result_notCOT.xlsx')
		print(self.d)
		self.dtw_n = self.d[self.d['Evaluation']=='dtw_n']

		self.dtw_n_df = self.make_df(self.dtw_n,key='all')
		self.dtw_n_mean_df = self.make_df(self.dtw_n,key='mean')

		self.dtw_n_df.to_excel('Analysis/ExData/Motion/CutData/All_DTW_N.xlsx')
		self.dtw_n_mean_df.to_excel('Analysis/ExData/Motion/CutData/Mean_DTW_N.xlsx')

		self.figure.MeanBoxPlot(self.dtw_n_mean_df,dir='Motion',ylabel='DTW Score',filename='DTW_N_MEAN')
		self.figure.CycleBoxPlot(self.dtw_n_df,dir='Motion',ylabel='DTW Score',filename='DTW_N_CYCLE')

	def A_dtw(self):
		self.dtw = self.data[self.data['Evaluation']=='dtw']

		# --- exportExcel --- #
		self.dtw_df = self.make_df(self.dtw,key='all')
		self.dtw_mean_df = self.make_df(self.dtw,key='mean')
		self.dtw_31_df = self.make_df(self.dtw,key='3-1')
		self.dtw_3_df = self.make_df(self.dtw,key='3')

		self.dtw_time_df = pd.read_excel('/Users/sprout/OneDrive - 名古屋工業大学/学校/研究室/code/Analysis/ExData/Performance/CutData/All_DTWperTIME.xlsx')
		self.dtw_time_mean_df = self.make_df(self.dtw,key='mean')
		self.dtw_time_mean_df.to_excel('/Users/sprout/OneDrive - 名古屋工業大学/学校/研究室/code/Analysis/ExData/Performance/CutData/All_DTWperTIME.xlsx')

		self.dtw_df.to_excel('Analysis/ExData/Motion/CutData/All_DTW.xlsx')
		self.dtw_mean_df.to_excel('Analysis/ExData/Motion/CutData/Mean_DTW.xlsx')
		self.dtw_31_df.to_excel('Analysis/ExData/Motion/CutData/31_DTW.xlsx')
		self.dtw_3_df.to_excel('Analysis/ExData/Motion/CutData/3_DTW.xlsx')

		# --- figure --- #
		self.figure.MeanBoxPlot(self.dtw_mean_df,dir='Motion',ylabel='DTW Score',filename='DTW_MEAN')

		self.figure.CycleBoxPlot(self.dtw_df,dir='Motion',ylabel='DTW Score',filename='DTW_CYCLE')

		self.figure.MeanBoxPlot(self.dtw_31_df,dir='Motion',ylabel='DTW Score\nbetween the third and the first time',filename='DTW_31')

		self.figure.MeanBoxPlot(self.dtw_3_df,dir='Motion',ylabel='DTW Score',filename='DTW_3')

	def A_jrk(self):
		self.jrk = self.data[self.data['Evaluation']=='jrk']

		# --- exportExcel --- #
		self.jrk_df = self.make_df(self.jrk,key='all')
		self.jrk_mean_df = self.make_df(self.jrk,key='mean')
		self.jrk_31_df = self.make_df(self.jrk,key='3-1')
		self.jrk_3_df = self.make_df(self.jrk,key='3')
		self.jrk_df.to_excel('Analysis/ExData/Motion/CutData/All_JRK.xlsx')
		self.jrk_mean_df.to_excel('Analysis/ExData/Motion/CutData/Mean_JRK.xlsx')
		self.jrk_31_df.to_excel('Analysis/ExData/Motion/CutData/31_JRK.xlsx')
		self.jrk_3_df.to_excel('Analysis/ExData/Motion/CutData/3_JRK.xlsx')

		# --- figure --- #
		self.figure.MeanBoxPlot(self.jrk_mean_df,dir='Motion',ylabel='Jerk Index',filename='JRK_MEAN')

		self.figure.CycleBoxPlot(self.jrk_df,dir='Motion',ylabel='Jerk Index',filename='JRK_CYCLE')

		self.figure.MeanBoxPlot(self.jrk_31_df,dir='Motion',ylabel='Jerk Index\nbetween the third and the first time',filename='JRK_31')

		self.figure.MeanBoxPlot(self.jrk_3_df,dir='Motion',ylabel='Jerk Index',filename='JRK_3')

	def A_cot(self):
		self.cot = self.data[self.data['Evaluation']=='cot']

		# --- exportExcel --- #
		self.cot_df = self.make_df(self.cot,key='all')
		self.cot_mean_df = self.make_df(self.cot,key='mean')
		self.cot_31_df = self.make_df(self.cot,key='3-1')
		self.cot_3_df = self.make_df(self.cot,key='3')
		self.cot_df.to_excel('Analysis/ExData/Motion/CutData/All_COT.xlsx')
		self.cot_mean_df.to_excel('Analysis/ExData/Motion/CutData/Mean_COT.xlsx')
		self.cot_31_df.to_excel('Analysis/ExData/Motion/CutData/31_COT.xlsx')
		self.cot_3_df.to_excel('Analysis/ExData/Motion/CutData/3_COT.xlsx')

		# --- figure --- #
		self.figure.MeanBoxPlot(self.cot_mean_df,dir='Motion',ylabel='Difference Time [s]',filename='COT_MEAN')

		self.figure.CycleBoxPlot(self.cot_df,dir='Motion',ylabel='Difference Time [s]',filename='COT_CYCLE')

		self.figure.MeanBoxPlot(self.cot_31_df,dir='Motion',ylabel='Difference Time [s]\nbetween the third and the first time',filename='COT_31')

		self.figure.MeanBoxPlot(self.cot_3_df,dir='Motion',ylabel='Difference Time [s]',filename='COT_3')

if __name__ in '__main__':
	motionAnalysis = MOTIONAN_ALYSIS()
	motionFig = MOTION_FIG()