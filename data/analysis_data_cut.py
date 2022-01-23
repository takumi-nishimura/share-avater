import pandas as pd
import os
import glob
from homogeneous_transformation import HOMOGENEOUS
from graph_3D import GRAPH3D
from graph_2D import GRAPH2D
from time_calculate import TIME_CALCULATE

class DATA_READ:
	def __init__(self) -> None:
		pass

	def read(self, participant:str, condition:str, cycle:int):
		self.file_list = []
		self.dir = os.path.join('data','ExportData','expt_data','')
		self.files = sorted(glob.glob(os.path.join(self.dir, '*.csv')))
		for self.data in self.files:
			if participant in self.data:
				if condition in self.data:
					self.file_list.append(self.data)
		if len(self.file_list) == 9:
			self.cycle_1 = self.file_list[0:3]
			self.cycle_2 = self.file_list[3:6]
			self.cycle_3 = self.file_list[6:9]
			if cycle == 1:
				for self.read_data in self.cycle_1:
					if 'Participant_1' in self.read_data:
						self.d_1 = pd.read_csv(self.read_data)
					if 'Participant_2' in self.read_data:
						self.d_2 = pd.read_csv(self.read_data)
					if 'endEffector' in self.read_data:
						self.d_r = pd.read_csv(self.read_data)
			elif cycle == 2:
				for self.read_data in self.cycle_2:
					if 'Participant_1' in self.read_data:
						self.d_1 = pd.read_csv(self.read_data)
					if 'Participant_2' in self.read_data:
						self.d_2 = pd.read_csv(self.read_data)
					if 'endEffector' in self.read_data:
						self.d_r = pd.read_csv(self.read_data)
			elif cycle == 3:
				for self.read_data in self.cycle_3:
					if 'Participant_1' in self.read_data:
						self.d_1 = pd.read_csv(self.read_data)
					if 'Participant_2' in self.read_data:
						self.d_2 = pd.read_csv(self.read_data)
					if 'endEffector' in self.read_data:
						self.d_r = pd.read_csv(self.read_data)
			return self.d_r, self.d_1, self.d_2
		else:
			print('Not enough files')

	def make_list(self, p):
		self.x = []
		self.y = []
		self.z = []
		for i in range(len(p)):
			self.x.append(p[i][0])
			self.y.append(p[i][1])
			self.z.append(p[i][2])
		self.xyz = pd.DataFrame(data={'x':self.x,'y':self.y,'z':self.z})
		return self.xyz

	def Compile_Organiz(self, participant:str='',condition:str=''):
		self.participant = participant
		self.condition = condition
		self.dictPos = {}
		self.dictHomogeneous = {}
		self.start_end_l = []
		self.dictExport = {}

		print(participant,condition)

		self.t_lsit, self.average_list = time_cal.time_c(participant=participant)

		for i in range(3):
			self.d_r, self.d_1, self.d_2 = data_reader.read(participant,condition,i+1)
			self.dictPos[str(i+1)] = [self.d_r,self.d_1,self.d_2]
			self.pos_r, self.rot_r = homogeneous.main(self.d_r)
			self.pos_1, self.rot_1 = homogeneous.main(self.d_1)
			self.pos_2, self.rot_2 = homogeneous.main(self.d_2)
			self.pos_r_l = self.make_list(self.pos_r)
			self.pos_1_l = self.make_list(self.pos_1)
			self.pos_2_l = self.make_list(self.pos_2)
			self.dictHomogeneous[str(i+1)] = [self.pos_r_l,self.pos_1_l,self.pos_2_l]

		for i in range(3):
			self.r_flag = 0
			while self.r_flag == 0:
				graph2d.main(time=((self.dictPos[str(i+1)])[0])['time'],pos=((self.dictHomogeneous[str(i+1)])[1]))

				self.dictMove_r = graph2d.get_speed_list(((self.dictPos[str(i+1)])[0])['time'],((self.dictHomogeneous[str(i+1)])[0]))
				self.dictMove_1 = graph2d.get_speed_list(((self.dictPos[str(i+1)])[0])['time'],((self.dictHomogeneous[str(i+1)])[1]))
				self.dictMove_2 = graph2d.get_speed_list(((self.dictPos[str(i+1)])[0])['time'],((self.dictHomogeneous[str(i+1)])[2]))

				self.start = input('start : ')
				# self.end = input('end: ')
				if self.condition == 'A':
					print('task time : ',self.t_lsit[i])
					self.end = round(float(self.start) + self.t_lsit[i],1)
				elif self.condition == 'B':
					print('task time : ',self.t_lsit[i+3])
					self.end = round(float(self.start) + self.t_lsit[i+3],1)
				elif self.condition == 'C':
					print('task time : ',self.t_lsit[i+6])
					self.end = round(float(self.start) + self.t_lsit[i+6],1)
				print('end : ', self.end)

				graph3d.main(start=float(self.start), end=float(self.end),time=((self.dictPos[str(i+1)])[0])['time'], position_r=((self.dictHomogeneous[str(i+1)])[0]), position_1=((self.dictHomogeneous[str(i+1)])[1]), position_2=((self.dictHomogeneous[str(i+1)])[2]))

				self.perfect = input('切り出しを行いますか？ : y/n   ')

				if self.perfect == 'y':
					self.start_end_l.append([float(self.start),float(self.end)])
					for j in range(3):
						if j == 0:
							self.dictExport['endEffector'] = [((self.dictPos['1'])[0])['time'],(self.dictHomogeneous[str(j+1)])[i],self.dictMove_r]
						elif j == 1:
							self.dictExport['participant'+str(j)] = [((self.dictPos['1'])[0])['time'],(self.dictHomogeneous[str(j+1)])[j],self.dictMove_1]
						elif j == 2:
							self.dictExport['participant'+str(j)] = [((self.dictPos['1'])[0])['time'],(self.dictHomogeneous[str(j+1)])[j],self.dictMove_2]
					self.key_l = self.dictExport.keys()
					for k, key in enumerate(self.key_l):
						if k == 0:
							self.list_e = self.dictExport[key]
							self.list_e_time = pd.DataFrame({'time':self.list_e[0]})
							self.dict_e = self.list_e_time.join([self.list_e[1],self.list_e[2]])
						elif k == 1:
							self.list_1 = self.dictExport[key]
							self.list_1_time = pd.DataFrame({'time':self.list_1[0]})
							self.dict_1 = self.list_1_time.join([self.list_1[1],self.list_1[2]])
						elif k == 2:
							self.list_2 = self.dictExport[key]
							self.list_2_time = pd.DataFrame({'time':self.list_2[0]})
							self.dict_2 = self.list_2_time.join([self.list_2[1],self.list_2[2]])

					self.filename_e = 'data/ExportData/expt_data/move_data/Cut_' + self.participant + '_' + self.condition + '_' + str(i+1) + '_endEffector.csv'
					self.filename_1 = 'data/ExportData/expt_data/move_data/Cut_' + self.participant + '_' + self.condition + '_' + str(i+1) + '_Participant_1.csv'
					self.filename_2 = 'data/ExportData/expt_data/move_data/Cut_' + self.participant + '_' + self.condition + '_' + str(i+1) + '_Participant_2.csv'
					self.dict_e.to_csv(self.filename_e)
					self.dict_1.to_csv(self.filename_1)
					self.dict_2.to_csv(self.filename_2)
					self.r_flag = 1
				else:
					print('!!! もう一度 !!!')
		print('!!!finish!!!')

if __name__ == '__main__':
	data_reader = DATA_READ()
	homogeneous = HOMOGENEOUS()
	graph3d = GRAPH3D()
	graph2d = GRAPH2D()
	time_cal = TIME_CALCULATE()

	data_reader.Compile_Organiz(participant='Kusaka',condition='C')

	# count = 1

	# d_r, d_1, d_2 = data_reader.read('Katagiri','A',count)

	# pos_r, rot_r = homogeneous.main(d_r)
	# pos_1, rot_1 = homogeneous.main(d_1)
	# pos_2, rot_2 = homogeneous.main(d_2)

	# graph2d.main(time=d_r['time'],pos=d_r)

	# start = input('start: ')
	# end = input('end: ')

	# dict_pos_r = data_reader.make_list(pos_r)
	# dict_pos_1 = data_reader.make_list(pos_1)
	# dict_pos_2 = data_reader.make_list(pos_2)

	# graph3d.main(start=int(start), end=int(end),time=d_r['time'], position_r=dict_pos_r, position_1=dict_pos_1, position_2=dict_pos_2)