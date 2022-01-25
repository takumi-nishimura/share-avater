import pandas as pd
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

class CoT:
	def __init__(self) -> None:
		pass

	def main(self, robot, begginer, expert, participant, condition, cycle, save:bool=False, input:bool=False):
		if save:
			self.get_data(robot,begginer,expert)
			for i in range(3):
				if i == 0:
					self.max_t_r = self.Contemporaneity_Time(self.v_x_r,self.v_y_r,self.v_z_r,self.tl, participant, condition, cycle,save=True)
				elif i == 1:
					self.max_t_1 = self.Contemporaneity_Time(self.v_x_1,self.v_y_1,self.v_z_1,self.tl, participant, condition, cycle,save=True)
				elif i == 2:
					self.max_t_2 = self.Contemporaneity_Time(self.v_x_2,self.v_y_2,self.v_z_2,self.tl, participant, condition, cycle,save=True)
			self.max_t_l = [self.max_t_r,self.max_t_1,self.max_t_2]
			return self.max_t_l
		if input:
			self.get_data(robot,begginer,expert)
			for i in range(3):
				if i == 0:
					self.max_t_r = self.Contemporaneity_Time(self.v_x_r,self.v_y_r,self.v_z_r,self.tl, participant, condition, cycle)
				elif i == 1:
					self.max_t_1 = self.Contemporaneity_Time(self.v_x_1,self.v_y_1,self.v_z_1,self.tl, participant, condition, cycle)
				elif i == 2:
					self.max_t_2 = self.Contemporaneity_Time(self.v_x_2,self.v_y_2,self.v_z_2,self.tl, participant, condition, cycle)
			self.max_t_l = [self.max_t_r,self.max_t_1,self.max_t_2]
			return self.max_t_l
			pass

	def get_data(self,r,d1,d2):
		self.tl = r['time']
		self.v_x_r = r['vx']
		self.v_y_r = r['vy']
		self.v_z_r = r['vz']
		self.v_x_1 = d1['vx']
		self.v_y_1 = d1['vy']
		self.v_z_1 = d1['vz']
		self.v_x_2 = d2['vx']
		self.v_y_2 = d2['vy']
		self.v_z_2 = d2['vz']

	def Contemporaneity_Time(self,dx,dy,dz,t, participant, condition, cycle, save:bool=False):
		self.d_l = np.c_[dx,dy,dz]
		self.d_norm = np.linalg.norm(self.d_l,axis=1)
		self.maxid = signal.argrelmax(self.d_norm, order=100)
		self.maxid_v = []
		for i in range(len(self.maxid[0])):
			self.maxid_v.append([self.maxid[0][i],self.d_norm[self.maxid[0][i]]])
		self.maxid_v_sort = sorted(self.maxid_v, key=lambda x: x[1])
		self.maxid_v_sort_10 = self.maxid_v_sort[-15:]
		self.maxid_o = []
		for j in range(len(self.maxid_v_sort_10)):
			self.maxid_o.append(self.maxid_v_sort_10[j][0])
		if save:
			plt.subplots()
			plt.plot(t,self.d_norm)
			plt.plot(t[self.maxid_o],self.d_norm[self.maxid_o],'bo')
			self.filename = participant + '_' + condition + '_' + cycle
			plt.title(self.filename)
			plt.savefig('/Users/sprout/OneDrive - 名古屋工業大学/学校/研究室/実験/卒論実験/m_calculate/fig/CoT/'+self.filename+'.png')
			plt.close()
			return self.maxid_o
		else:
			return self.maxid_o