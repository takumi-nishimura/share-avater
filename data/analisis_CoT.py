import pandas as pd
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

class CoT:
	def __init__(self) -> None:
		pass

	def main(self, robot, begginer, expert):
		self.get_data(robot,begginer,expert)
		for i in range(3):
			if i == 0:
				self.max_t_r = self.Contemporaneity_Time(self.v_x_r,self.v_y_r,self.v_z_r,self.tl)
			elif i == 1:
				self.max_t_1 = self.Contemporaneity_Time(self.v_x_1,self.v_y_1,self.v_z_1,self.tl)
			elif i == 2:
				self.max_t_2 = self.Contemporaneity_Time(self.v_x_2,self.v_y_2,self.v_z_2,self.tl)
		self.max_t_l = [self.max_t_r,self.max_t_1,self.max_t_2]
		return self.max_t_l

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

	def Contemporaneity_Time(self,dx,dy,dz,t):
		self.d_l = np.c_[dx,dy,dz]
		self.d_norm = np.linalg.norm(self.d_l,axis=1)
		self.maxid = signal.argrelmax(self.d_norm, order=100)
		self.maxid_v = []
		for i in range(len(self.maxid[0])):
			self.maxid_v.append([self.maxid[0][i],self.d_norm[self.maxid[0][i]]])
		self.maxid_v_sort = sorted(self.maxid_v, key=lambda x: x[1])
		self.maxid_v_sort_10 = self.maxid_v_sort[-10:]
		self.maxid_o = []
		for j in range(len(self.maxid_v_sort_10)):
			self.maxid_o.append(self.maxid_v_sort_10[j][0])
		print(self.maxid_o)
		plt.plot(t,self.d_norm)
		plt.plot(t[self.maxid_o],self.d_norm[self.maxid_o],'bo')
		plt.show()
		return self.maxid_o