import os
import glob
import pandas as pd
import numpy as np

class TIME_CALCULATE:
	def __init__(self) -> None:
		self.time_list = []
		self.t_list = []
		self.time_list_A = []
		self.time_list_B = []
		self.time_list_C = []
		self.time_A = []
		self.time_B = []
		self.time_C = []

	def time_c(self, participant:str):
		self.file_list = []
		self.dir = os.path.join('data','ExportData','time_data','')
		self.files = sorted(glob.glob(os.path.join(self.dir, '*.xlsx')))
		for self.data in self.files:
			if participant in self.data:
				self.file_list.append(self.data)
		for i in self.file_list:
			self.d = pd.read_excel(i, index_col=0)
			for i in range(9):
				self.time_list.append([self.d.at['condition',i+1], self.d.at['time',i+1], self.d.at['points',i+1]])
				self.t_list.append(self.d.at['time',i+1])
		for i in range(len(self.time_list)):
			if self.time_list[i][0] == 'A':
				self.time_list_A.append(self.time_list[i])
				self.time_A.append(self.time_list[i][1])
			elif self.time_list[i][0] == 'B':
				self.time_list_B.append(self.time_list[i])
				self.time_B.append(self.time_list[i][1])
			elif self.time_list[i][0] == 'C':
				self.time_list_C.append(self.time_list[i])
				self.time_C.append(self.time_list[i][1])

		self.average_A = np.average(self.time_A)
		self.average_B = np.average(self.time_B)
		self.average_C = np.average(self.time_C)
		self.average_time = [self.average_A,self.average_B,self.average_C]
		self.t_l = []
		for i in range(len(self.t_list)):
			if i < 3:
				self.t_l.append(self.time_A[i])
			elif 3 <= i < 6:
				self.t_l.append(self.time_B[i-3])
			elif 6 <= i < 9:
				self.t_l.append(self.time_C[i-6])

		self.time_list.clear()
		self.time_A.clear()
		self.time_B.clear()
		self.time_C.clear()

		return self.t_l, self.average_time

	def save_time(self):
		self.average_list_A = []
		self.average_list_B = []
		self.average_list_C = []
		self.Export_df = pd.DataFrame(index=['A','B','C'])
		self.participant_l()
		for i in self.participant_list:
			self.time_c(participant=i)
			self.average_list_A.append(self.average_A)
			self.average_list_B.append(self.average_B)
			self.average_list_C.append(self.average_C)
		for i, j in enumerate(self.participant_list):
			self.Export_df[j] = [self.average_list_A[i],self.average_list_B[i],self.average_list_C[i]]
		self.Export_df.to_excel('data/ExportData/time_data/TaskTime/TaskTime.xlsx')

	def participant_l(self):
		self.file_list = []
		self.participant_list = []
		self.dir = os.path.join('data','ExportData','time_data','')
		self.files = sorted(glob.glob(os.path.join(self.dir, '*.xlsx')))

		for self.filename_s in self.files:
			self.filename_split = self.filename_s.split('_')
			self.participant_name = self.filename_split[2]
			if self.participant_name in self.participant_list:
				pass
			else:
				self.participant_list.append(self.participant_name)

if __name__ in '__main__':
	read = TIME_CALCULATE()
	read.time_c(participant='Nakamura')
	read.save_time()