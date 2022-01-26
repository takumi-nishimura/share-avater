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
		self.p_list = []
		self.points_list_A = []
		self.points_list_B = []
		self.points_list_C = []
		self.points_A = []
		self.points_B = []
		self.points_C = []
		self.time_A_l = []
		self.time_B_l = []
		self.time_C_l = []
		self.point_A_l = []
		self.point_B_l = []
		self.point_C_l = []

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
				self.points_A.append(self.time_list[i][2])
			elif self.time_list[i][0] == 'B':
				self.time_list_B.append(self.time_list[i])
				self.time_B.append(self.time_list[i][1])
				self.points_B.append(self.time_list[i][2])
			elif self.time_list[i][0] == 'C':
				self.time_list_C.append(self.time_list[i])
				self.time_C.append(self.time_list[i][1])
				self.points_C.append(self.time_list[i][2])

		self.average_A = np.average(self.time_A)
		self.average_B = np.average(self.time_B)
		self.average_C = np.average(self.time_C)
		self.averageP_A = np.average(self.points_A)
		self.averageP_B = np.average(self.points_B)
		self.averageP_C = np.average(self.points_C)
		self.average_time = [self.average_A,self.average_B,self.average_C]
		self.average_points = [self.averageP_A,self.averageP_B,self.averageP_C]
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
		self.points_A.clear()
		self.points_B.clear()
		self.points_C.clear()

		return self.t_l, self.average_time

	def Alltime_c(self, participant:str):
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
				self.points_A.append(self.time_list[i][2])
				self.time_A_l.append(self.time_list[i][1])
				self.point_A_l.append(self.time_list[i][2])
			elif self.time_list[i][0] == 'B':
				self.time_list_B.append(self.time_list[i])
				self.time_B.append(self.time_list[i][1])
				self.points_B.append(self.time_list[i][2])
				self.time_B_l.append(self.time_list[i][1])
				self.point_B_l.append(self.time_list[i][2])
			elif self.time_list[i][0] == 'C':
				self.time_list_C.append(self.time_list[i])
				self.time_C.append(self.time_list[i][1])
				self.points_C.append(self.time_list[i][2])
				self.time_C_l.append(self.time_list[i][1])
				self.point_C_l.append(self.time_list[i][2])
		self.average_A = np.average(self.time_A)
		self.average_B = np.average(self.time_B)
		self.average_C = np.average(self.time_C)
		self.averageP_A = np.average(self.points_A)
		self.averageP_B = np.average(self.points_B)
		self.averageP_C = np.average(self.points_C)
		self.average_time = [self.average_A,self.average_B,self.average_C]
		self.average_points = [self.averageP_A,self.averageP_B,self.averageP_C]
		self.t_l = []
		for i in range(len(self.t_list)):
			if i < 3:
				self.t_l.append(self.time_A[i])
			elif 3 <= i < 6:
				self.t_l.append(self.time_B[i-3])
			elif 6 <= i < 9:
				self.t_l.append(self.time_C[i-6])
		self.time_list = []
		self.time_A = []
		self.time_B = []
		self.time_C = []
		self.points_A = []
		self.points_B = []
		self.points_C = []

		return self.t_l, self.average_time

	def save_time(self):
		self.average_list_A = []
		self.average_list_B = []
		self.average_list_C = []
		self.averageP_list_A = []
		self.averageP_list_B = []
		self.averageP_list_C = []
		self.participant_l()
		for i in self.participant_list:
			self.time_c(participant=i)
			for j in range(len(self.time_A)):
				self.average_list_A.append(self.time_A[j])
				self.average_list_B.append(self.time_B[j])
				self.average_list_C.append(self.time_C[j])
				self.averageP_list_A.append(self.points_A[j])
				self.averageP_list_B.append(self.points_B[j])
				self.averageP_list_C.append(self.points_C[j])
		self.Export_df = pd.DataFrame({''})
		self.toXlsx_list(evaluation='TASK_TIME', df_l=self.Export_df)

	def ALL_save_time(self):
		self.average_list_A = []
		self.average_list_B = []
		self.average_list_C = []
		self.averageP_list_A = []
		self.averageP_list_B = []
		self.averageP_list_C = []
		self.Export_df_t = pd.DataFrame(index=['A','B','C'])
		self.Export_df_p = pd.DataFrame(index=['A','B','C'])
		self.participant_l()
		for i in self.participant_list:
			self.Alltime_c(participant=i)
		self.time_ll = self.time_A_l + self.time_B_l + self.time_C_l
		self.point_ll = self.point_A_l + self.point_B_l + self.point_C_l
		self.condition = []
		for j in range(len(self.time_A_l)):
			self.condition.append('without feedback')
		for k in range(len(self.time_B_l)):
			self.condition.append('companion speed')
		for l in range(len(self.time_C_l)):
			self.condition.append('robot speed')
		self.Export_df = pd.DataFrame({'time':self.time_ll,'':self.condition,'point':self.point_ll})
		print(self.Export_df)
		self.Export_df.to_excel('/Users/sprout/OneDrive - 名古屋工業大学/学校/研究室/実験/卒論実験/m_calculate/ALL_TIME_POINT.xlsx')

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

	def toXlsx_list(self, evaluation, df_l):
		self.w_dir = '/Users/sprout/OneDrive - 名古屋工業大学/学校/研究室/実験/卒論実験/m_calculate'
		self.w_name = self.w_dir + '/' + evaluation + '.xlsx'
		with pd.ExcelWriter(self.w_name) as writer:
			for i, df in enumerate(df_l):
				if i == 0:
					df.to_excel(writer, sheet_name="Task Time")
				elif i == 1:
					df.to_excel(writer, sheet_name="Points")
		print(self.w_name)

if __name__ in '__main__':
	read = TIME_CALCULATE()
	# read.time_c(participant='Nakamura')
	# read.save_time()
	read.ALL_save_time()