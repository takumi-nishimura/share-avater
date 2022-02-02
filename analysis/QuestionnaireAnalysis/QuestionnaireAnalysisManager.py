# -----------------------------------------------------------------------
# Author:   Takumi Nishimura (Haptics Lab)
# Created:  2022/02/02
# Summary:  Questionnaire analysis manager
# -----------------------------------------------------------------------

import os
import glob
from aem import con
import pandas as pd
import numpy as np

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

		data = pd.read_excel(readname, index_col=0)

		tlx_d = data[data['evaluation'] == 'TLX_q']
		print(tlx_d[tlx_d['number']==1])

		print('--- finish --- : Questionnaire Analysis')

if __name__ in '__main__':
	questionnaireAnalysisExport = QUESTIONNAIRE_Export('AllQuestionnaireData_20220202.xlsx')
	questionnaireAnalysis = QUESTIONNAIRE_Analysis('/Users/sprout/OneDrive - 名古屋工業大学/学校/研究室/code/Analysis/ExData/Questionnaire/CutData/AllQuestionnaireData_20220202.xlsx')