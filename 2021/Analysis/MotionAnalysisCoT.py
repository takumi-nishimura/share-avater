from turtle import color
from matplotlib.pyplot import axis
import pandas as pd
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
from sqlalchemy import delete

class CoT:
	def __init__(self) -> None:
		print('--- import --- : Motion Analysis CoT')

	def CoT_C(self,d_r,d_1,d_2):
		print('--- calculate --- : Motion Analysis CoT')

		self.get_data(d_r,d_1,d_2)
		self.cot = self.CoT()
		print('CoT : ',self.cot)
		return self.cot

	def get_data(self,r,d1,d2):
		self.tl = r['time'].values
		self.v_x_r = r['vx']
		self.v_y_r = r['vy']
		self.v_z_r = r['vz']
		self.v_x_1 = d1['vx']
		self.v_y_1 = d1['vy']
		self.v_z_1 = d1['vz']
		self.v_x_2 = d2['vx']
		self.v_y_2 = d2['vy']
		self.v_z_2 = d2['vz']

	def CoT(self):
		self.n_l_r = np.c_[self.v_x_r,self.v_y_r,self.v_z_r]
		self.n_l_1 = np.c_[self.v_x_1,self.v_y_1,self.v_z_1]
		self.n_l_2 = np.c_[self.v_x_2,self.v_y_2,self.v_z_2]
		self.n_r = np.linalg.norm(self.n_l_r,axis=1)
		self.n_1 = np.linalg.norm(self.n_l_1,axis=1)
		self.n_2 = np.linalg.norm(self.n_l_2,axis=1)
		self.maxid_r_l = signal.argrelmax(self.n_r,order=200)[0]
		self.maxid_1_l = signal.argrelmax(self.n_1,order=200)[0]
		self.maxid_2_l = signal.argrelmax(self.n_2,order=200)[0]
		self.minid_r_l = signal.argrelmin(self.n_r,order=130)[0]
		self.minid_1_l = signal.argrelmin(self.n_1,order=130)[0]
		self.minid_2_l = signal.argrelmin(self.n_2,order=130)[0]
		
		self.maxid_r_f = []
		self.maxid_1_f = []
		self.maxid_2_f = []
		self.maxid_r_ff = []
		self.maxid_1_ff = []
		self.maxid_2_ff = []
		self.maxid_r_fff = []
		self.maxid_1_fff = []
		self.maxid_2_fff = []
		self.maxid_r = []
		self.maxid_1 = []
		self.maxid_2 = []
		self.minid_r_f = []
		self.minid_1_f = []
		self.minid_2_f = []
		self.minid_r_ff = []
		self.minid_1_ff = []
		self.minid_2_ff = []
		self.minid_r_fff = []
		self.minid_1_fff = []
		self.minid_2_fff = []
		self.minid_r = []
		self.minid_1 = []
		self.minid_2 = []

		limit = 0.06
		diff = 0.35
		for i in range(len(self.maxid_1_l)):
			if self.n_1[self.maxid_1_l[i]] > limit:
				self.maxid_1_f.append(self.maxid_1_l[i])
		for i in range(len(self.maxid_1_f)):
			if abs(self.tl[self.maxid_1_f[i]]-self.tl[self.maxid_1_f[i-1]]) >= abs(self.tl[self.maxid_1_f[0]]-self.tl[self.maxid_1_f[1]])*diff:
				self.maxid_1_ff.append(self.maxid_1_f[i])
		for i in range(len(self.maxid_1_ff)):
			self.maxid_1_fff.append(self.maxid_1_ff[i])
		for i in range(len(self.maxid_2_l)):
			if self.n_2[self.maxid_2_l[i]] > limit:
				self.maxid_2_f.append(self.maxid_2_l[i])
		for i in range(len(self.maxid_2_f)):
			if abs(self.tl[self.maxid_2_f[i]]-self.tl[self.maxid_2_f[i-1]]) >= abs(self.tl[self.maxid_2_f[0]]-self.tl[self.maxid_2_f[1]])*diff:
				self.maxid_2_ff.append(self.maxid_2_f[i])
		for i in range(len(self.maxid_2_ff)):
			self.maxid_2_fff.append(self.maxid_2_ff[i])

		self.maxid_1 = self.maxid_1_fff
		self.maxid_2 = self.maxid_2_fff
		self.minid_1 = self.minid_1_l
		self.minid_2 = self.minid_2_l

		self.diff_time_l = []

		self.l_flag = 0
		while self.l_flag == 0:
			self.maxid_v_1 = []
			self.maxid_v_2 = []
			for y in range(len(self.maxid_1)):
				self.maxid_v_1.append([self.maxid_1[y],self.n_1[self.maxid_1[y]]])
			self.maxid_v_1_sort = sorted(self.maxid_v_1,key=lambda x:x[1],reverse=True)
			self.maxid_v_1_sort_10 = self.maxid_v_1_sort[0:11]
			for z in range(len(self.maxid_2)):
				self.maxid_v_2.append([self.maxid_2[z],self.n_2[self.maxid_2[z]]])
			self.maxid_v_2_sort = sorted(self.maxid_v_2,key=lambda x:x[1],reverse=True)
			self.maxid_v_2_sort_10 = self.maxid_v_2_sort[0:11]

			self.maxid_1 = []
			self.maxid_2 = []
			for o in range(len(self.maxid_v_1_sort_10)):
				self.maxid_1.append(self.maxid_v_1_sort_10[o][0])
			for o in range(len(self.maxid_v_2_sort_10)):
				self.maxid_2.append(self.maxid_v_2_sort_10[o][0])

			cmap = plt.get_cmap("tab10")
			plt.subplot(2,1,1)
			plt.plot(self.tl,self.n_1,color=cmap(1))
			plt.plot(self.tl[self.maxid_1],self.n_1[self.maxid_1],'bo')
			plt.plot(self.tl[self.minid_1],self.n_1[self.minid_1],'x')
			plt.subplot(2,1,2)
			plt.plot(self.tl,self.n_2,color=cmap(2))
			plt.plot(self.tl[self.maxid_2],self.n_2[self.maxid_2],'bo')
			plt.plot(self.tl[self.minid_2],self.n_2[self.minid_2],'x')
			plt.show()

			self.delete_1 = input('delete 1 : ')
			self.delete_2 = input('delete 2 : ')
			self.maxid_1.sort()
			self.maxid_2.sort()
			if not self.delete_1 == 'f':
				del self.maxid_1[int(self.delete_1)-1]	
			if not self.delete_2 == 'f':
				del self.maxid_2[int(self.delete_2)-1]
			if self.delete_1 == 'f':
				if self.delete_2 == 'f':
					if len(self.maxid_1) == 10:
						if len(self.maxid_2) == 10:
							for i in range(10):
								self.diff_time = abs(self.tl[self.maxid_1[i]]-self.tl[self.maxid_2[i]])
								self.diff_time_l.append(self.diff_time)
							self.diff_mean = np.mean(self.diff_time_l)
							self.l_flag = 1
						else:
							print('error list length')
							self.l_flag = 0
					else:
						print('error list length')
						self.l_flag = 0

		return self.diff_mean