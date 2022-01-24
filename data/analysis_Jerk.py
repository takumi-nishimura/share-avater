import pandas as pd
import numpy as np

class JERK:
	def __init__(self) -> None:
		pass

	def main(self,d):
		self.get_data(data=d)
		self.Jerk = self.Ahmad_2016()
		return self.Jerk

	def Ahmad_2016(self):
		self.jrk_sq_list = []
		for i in range(len(self.j_x)):
			self.jrk_sq = self.j_x[i]**2 + self.j_y[i]**2 + self.j_z[i]**2
			self.jrk_sq_list.append(self.jrk_sq)
		self.sum_jrk = np.sum(self.jrk_sq_list)
		self.dt = self.tl[len(self.tl)-1] - self.tl[0]
		self.vel_sq_list = []
		for i in range(len(self.v_x)):
			self.vel_sq = np.sqrt(self.v_x[i]**2 + self.v_y[i]**2 + self.v_z[i]**2)
			self.vel_sq_list.append(self.vel_sq)
		self.sum_vel = np.sum(self.vel_sq_list)
		self.normalized_Jrk_index = self.sum_jrk * self.dt**5 / (self.sum_vel**2)
		print('Ahmad_2016 : ','{:.5g}'.format(self.normalized_Jrk_index))
		return self.normalized_Jrk_index

	def get_data(self,data):
		self.tl = data['time']
		self.v_x = data['vx']
		self.v_y = data['vz']
		self.v_z = data['vz']
		self.j_x = data['jx']
		self.j_y = data['jz']
		self.j_z = data['jz']