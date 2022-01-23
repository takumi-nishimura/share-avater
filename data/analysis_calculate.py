import pandas as pd
import os
import glob
from analysis_DTW import DTW

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

	def main(self):
		self.dtw = DTW()
		self.participant_l()
		for self.participant in self.participant_list:
			print(self.participant)
			self.read()
			# for i, j in enumerate(['A','B','C']):
			# 	if j == 'A':
			# 		for k in range(3):
			# 			print(self.df_A_1_dict[str(k+1)])
			# 			# self.dtw.main(self.df_A_r_dict[str(k+1)],self.df_A_1_dict[str(k+1)],self.df_A_2_dict[str(k+1)])
			# 	elif j == 'B':
			# 		for k in range(3):
			# 			print(self.df_B_1_dict[str(k+1)])
			# 			# self.dtw.main(self.df_B_r_dict[str(k+1)],self.df_B_1_dict[str(k+1)],self.df_B_2_dict[str(k+1)])
			# 	elif j == 'C':
			# 		for k in range(3):
			# 			print(self.df_C_1_dict[str(k+1)])
			# 			# self.dtw.main(self.df_C_r_dict[str(k+1)],self.df_C_1_dict[str(k+1)],self.df_C_2_dict[str(k+1)])

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
		self.participant_list = ['Kusaka','Ebina','Nakamura']

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
				self.df_B_r_dict[str(j+1)] = self.df_B_r
			elif 'Participant_1' in i:
				k += 1
				self.df_B_1 = pd.read_csv(i)
				self.df_B_1_dict[str(j+1)] = self.df_B_1
			elif 'Participant_2' in i:
				l += 1
				self.df_B_2 = pd.read_csv(i)
				self.df_B_2_dict[str(j+1)] = self.df_B_2
		j = 0
		k = 0
		l = 0
		for i in self.d_C_list:
			if 'endEffector' in i:
				j += 1
				self.df_C_r = pd.read_csv(i)
				print(i)
				print(self.df_C_r)
				self.df_C_r_dict[str(j+1)] = self.df_C_r
			elif 'Participant_1' in i:
				k += 1
				self.df_C_1 = pd.read_csv(i)
				print(i)
				print(self.df_C_1)
				self.df_C_1_dict[str(j+1)] = self.df_C_1
			elif 'Participant_2' in i:
				l += 1
				self.df_C_2 = pd.read_csv(i)
				print(i)
				print(self.df_C_2)
				self.df_C_2_dict[str(j+1)] = self.df_C_2
		self.d_A_list.clear()
		self.d_B_list.clear()
		self.d_C_list.clear()

if __name__ in '__main__':
	calculate = DATACALCULATE()
	calculate.main()