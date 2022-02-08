# -----------------------------------------------------------------------
# Author:   Takumi Nishimura (Haptics Lab)
# Created:  2022/02/02
# Summary:  Motion data processing
# -----------------------------------------------------------------------

import os
import glob
import re
import  matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy import signal
from decimal import Decimal, ROUND_HALF_UP
from MotionHomogeneous import HOMOGENEOUS
from Figure.figure_manager import FIG
import Figure.matplotlib_style

class MOTION_PROCESSING:
	def __init__(self,participant) -> None:
		print('--- import --- : Motion Data Processing')

		self.name = participant

		self.performance_p = PERFORMANCE_PROCESSING()
		self.homogeneous = HOMOGENEOUS()
		self.fig = FIG()

		self.participant = []
		self.condition = []
		self.cycle = []
		self.evaluation = []
		self.data = []
		self.number = []

		self.main()

	def main(self):
		print('--- start --- : Motion Data Processing')

		self.get_metadata()
		self.pf_df = self.performance_p.time_l(self.name)
		print(self.pf_df)

		for self.cut_condition in self.condition:
			for self.cut_cycle in self.cycle:
				self.read_csv(self.cut_condition,self.cut_cycle)
				self.pos_r, self.rot_r = self.homogeneous.homogeneous(self.d_r)
				self.pos_1, self.rot_1 = self.homogeneous.homogeneous(self.d_1)
				self.pos_2, self.rot_2 = self.homogeneous.homogeneous(self.d_2)
				self.pos_r_l = self.make_list(self.pos_r)
				self.pos_1_l = self.make_list(self.pos_1)
				self.pos_2_l = self.make_list(self.pos_2)
				self.dictMove_r = self.getSpeed_list(self.d_r['time'],self.pos_r_l)
				self.dictMove_1 = self.getSpeed_list(self.d_1['time'],self.pos_1_l)
				self.dictMove_2 = self.getSpeed_list(self.d_2['time'],self.pos_2_l)
				self.n_l = np.c_[self.dictMove_r['vx'],self.dictMove_r['vy'],self.dictMove_r['vz']]
				self.v_n = pd.DataFrame({'v':np.linalg.norm(self.n_l,axis=1)})

				self.r_flag = 0
				while self.r_flag == 0:
					self.fig.subplot_graph(self.dictMove_r['time'],vx=self.dictMove_r['vx'],vy=self.dictMove_r['vy'],vz=self.dictMove_r['vz'],v=self.v_n)

					self.start_0 = input('start : ')
					self.start_t, self.start_i = self.get_start_time(Decimal(str(self.start_0)).quantize(Decimal('0.01')),self.dictMove_r['time'])
					self.end_t = self.start_t + self.pf_df[(self.pf_df['condition']==self.cut_condition)&(self.pf_df['cycle']==int(self.cut_cycle))]['time'].values[0]
					self.end_i = self.search_index(self.dictMove_r['time'],Decimal(str(self.end_t)).quantize(Decimal('0.01')),'0.01')

					self.fig.make_3dPlot(self.start_i,self.end_i,self.dictMove_r,self.dictMove_1,self.dictMove_2)

					self.complete = input('切り出しを行いますか? : y/n   ')

					self.exportDir = 'Analysis/ExData/Motion/CutData/'
					if self.complete == 'y':
						self.dict_cut_r = self.dictMove_r.iloc[self.start_i:self.end_i+1]
						self.dict_cut_1 = self.dictMove_1.iloc[self.start_i:self.end_i+1]
						self.dict_cut_2 = self.dictMove_2.iloc[self.start_i:self.end_i+1]
						self.dict_cut_r = self.dict_cut_r.reset_index(drop=True)
						self.dict_cut_1 = self.dict_cut_1.reset_index(drop=True)
						self.dict_cut_2 = self.dict_cut_2.reset_index(drop=True)
						self.dict_cut_r.to_csv(self.exportDir+'Cut_'+self.name+'_'+self.cut_condition+'_'+self.cut_cycle+'_endEffector'+'.csv')
						self.dict_cut_1.to_csv(self.exportDir+'Cut_'+self.name+'_'+self.cut_condition+'_'+self.cut_cycle+'_Participant1'+'.csv')
						self.dict_cut_2.to_csv(self.exportDir+'Cut_'+self.name+'_'+self.cut_condition+'_'+self.cut_cycle+'_Participant2'+'.csv')
						print('write')
						self.r_flag = 1
					else:
						print('!!! もう一度 !!!')
			
		print('--- finish --- : Motion Data Processing')

	def get_metadata(self):
		self.file_list = []
		self.dir = os.path.join('analysis','ExData','Motion','RawData')
		self.files = sorted(glob.glob(os.path.join(self.dir,'*.csv')))
		for i in self.files:
			self.filename_split = re.split('_|/',i)
			self.participant.append(self.filename_split[4])
			self.condition.append(self.filename_split[5])
			self.cycle.append(self.filename_split[6])
		self.participant = sorted(set(self.participant),key=self.participant.index)
		self.condition = sorted(set(self.condition),key=self.condition.index)
		self.cycle = sorted(set(self.cycle),key=self.cycle.index)

	def read_csv(self,condition,cycle):
		self.read_list = [i for i in self.files if self.name in i and condition+'_'+cycle in i]
		print(self.read_list)
		self.d_1 = pd.read_csv(self.read_list[0])
		self.d_2 = pd.read_csv(self.read_list[1])
		self.d_r = pd.read_csv(self.read_list[2])

	def make_list(self,p):
		self.x = []
		self.y = []
		self.z = []
		for i in range(len(p)):
			self.x.append(p[i][0])
			self.y.append(p[i][1])
			self.z.append(p[i][2])
		self.xyz = pd.DataFrame(data={'x':self.x,'y':self.y,'z':self.z})
		return self.xyz

	def lowpass(self,x,fp,fs):
		self.samplerate = 235
		self.gpass = 5
		self.gstop = 50
		self.x = np.nan_to_num(x)
		self.fn = self.samplerate/2
		self.wp = fp/self.fn
		self.ws = fs/self.fn
		self.N,self.Wn = signal.buttord(self.wp,self.ws,self.gpass,self.gstop)
		self.b,self.a = signal.butter(self.N,self.Wn,'low')
		self.y = signal.filtfilt(self.b,self.a,self.x)
		return self.y

	def getSpeed(self,t,g1):
		self.mean_dt = np.mean(np.diff(t))
		self.speed = []
		for i in range(len(t)):
			if i == 0:
				self.speed.append(0)
			elif i == len(t)-1:
				self.speed.append(0)
			else:
				self.speed.append((g1[i+1]-g1[i-1])/(2*self.mean_dt))
		return self.speed

	def getSpeed_list(self,time,pos):
		self.y1_filt = self.lowpass(pos['x'],0.5,5)
		self.y2_filt = self.lowpass(pos['y'],0.5,5)
		self.y3_filt = self.lowpass(pos['z'],0.5,5)
		self.vy1 = self.getSpeed(time,self.y1_filt)
		self.vy2 = self.getSpeed(time,self.y2_filt)
		self.vy3 = self.getSpeed(time,self.y3_filt)
		self.ay1 = self.getSpeed(time,self.vy1)
		self.ay2 = self.getSpeed(time,self.vy2)
		self.ay3 = self.getSpeed(time,self.vy3)
		self.ay1[1] = 0
		self.ay2[1] = 0
		self.ay3[1] = 0
		self.jy1 = self.getSpeed(time,self.ay1)
		self.jy2 = self.getSpeed(time,self.ay2)
		self.jy3 = self.getSpeed(time,self.ay3)
		self.jy1[1:3] = [0,0]
		self.jy2[1:3] = [0,0]
		self.jy3[1:3] = [0,0]
		self.dict_move = pd.DataFrame(data={'time':time,'x':self.y1_filt,'y':self.y2_filt,'z':self.y3_filt,'vx':self.vy1,'vy':self.vy2,'vz':self.vy3,'ax':self.ay1,'ay':self.ay2,'az':self.ay3,'jx':self.jy1,'jy':self.jy2,'jz':self.jy3})
		return self.dict_move

	def get_start_time(self,start,time):
		self.start_index = self.search_index(time,start,'0.01')
		self.maxid = signal.argrelmax(self.v_n['v'].values[self.start_index:],order=200)
		self.minid = signal.argrelmin(self.v_n['v'].values[self.start_index:],order=10)
		for i in range(len(self.maxid[0])):
			self.maxid[0][i] = self.maxid[0][i] + self.start_index
		for j in range(len(self.minid[0])):
			self.minid[0][j] = self.minid[0][j] + self.start_index
		self.start_vel_max = self.v_n['v'].values[self.maxid[0][0]]
		self.start_vel = self.start_vel_max * 0.1
		self.v_n_r = []
		for k in reversed(self.v_n['v'].values[:self.maxid[0][0]]):
			self.v_n_r.append(k)
		self.start_per_i =self.search_index(pd.DataFrame({'time':self.v_n_r}),Decimal(str(self.start_vel)).quantize(Decimal('0.001')),'0.001')
		self.start_vel_index = self.maxid[0][0]-self.start_per_i
		if self.start_vel_index < self.minid[0][0]:
			self.start_vel_index = self.minid[0][0]
		if self.start_vel_index == self.maxid[0][0]:
			self.start_vel_index = self.minid[0][0]
		plt.plot(time,self.v_n['v'].values)
		plt.plot(time[self.maxid[0]],self.v_n['v'].values[self.maxid[0]],'bo')
		plt.plot(time[self.minid[0]],self.v_n['v'].values[self.minid[0]],'bo')
		plt.plot(time[self.start_vel_index],self.v_n['v'].values[self.start_vel_index],'x')
		plt.show()
		return round(time[self.start_vel_index],2), self.start_index

	def search_index(self,d,s,r):
		self.df_time = pd.DataFrame(data=d)
		self.s_flag = 0
		ddd = []
		for self.s_row_counter in range(len(self.df_time)):
			if self.s_flag == 0:
				ddd.append(Decimal(str(self.df_time.at[self.df_time.index[self.s_row_counter],'time'])).quantize(Decimal(r), rounding=ROUND_HALF_UP))
				if s == Decimal(str(self.df_time.at[self.df_time.index[self.s_row_counter],'time'])).quantize(Decimal(r), rounding=ROUND_HALF_UP):
					start = self.s_row_counter
					print('start',start)
					print('start time',self.df_time.iloc[start,0])
					self.s_flag = 1
				elif self.s_row_counter == len(self.df_time)-1:
					start = 0
					print('Start not matched!!!')
					print('start time',self.df_time.iloc[start,0])
		return start

class PERFORMANCE_PROCESSING:
	def __init__(self) -> None:
		print('--- import --- : Performance Data Processing')

	def time_l(self,name):
		self.file_list = []
		self.dir = os.path.join('analysis','ExData','Performance','RawData','')
		self.files = sorted(glob.glob(os.path.join(self.dir,'*.xlsx')))
		for self.data in self.files:
			if name in self.data:
				self.read_file = self.data
		self.d = pd.read_excel(self.read_file,index_col=0)
		self.d_T = self.d.T
		self.cycle_l = []
		for i in range(3):
			for j in range(3):
				self.cycle_l.append(i+1)
		self.d_T['cycle'] = self.cycle_l
		return self.d_T	

if __name__ in '__main__':
	dataProcessing = MOTION_PROCESSING(participant='Yamashita')