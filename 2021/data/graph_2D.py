import numpy as np
import pandas as pd
from scipy import signal
import matplotlib.pyplot as plt
import seaborn as sns
import os
from statistics import mean

class GRAPH2D:
	def __init__(self) -> None:
		pass

	def main(self, time:list=[], pos:list=[]):
		self.move = self.get_speed_list(time,pos)

		self.vel_norm = self.get_norm(self.vy1_filt,self.vy2_filt,self.vy3_filt)

		self.solox_graph(time,self.vy1_filt,'vx',self.vy2_filt,'vy',self.vy3_filt,'vz',self.vel_norm,'v')

	def make_list(self, p):
		print('aaa')
		print((p['x']))
		self.x = []
		self.y = []
		self.z = []
		for i in range(len(p)):
			self.x.append(p[i][0])
			self.y.append(p[i][1])
			self.z.append(p[i][2])
		self.pos = pd.DataFrame({'x':self.x,'y':self.y,'z':self.z})
		return self.pos

	def getSpeed(self,t,g1):
		self.mean_dt = mean(np.diff(t))
		self.speed = []
		for i in range(len(t)):
			if i == 0:
				self.speed.append(0)
			elif i == len(t)-1:
				self.speed.append(0)
			else:
				self.speed.append((g1[i+1]-g1[i-1])/(2*self.mean_dt))
		return self.speed

	def get_norm(self,d1,d2,d3):
		self.d_l = np.c_[d1,d2,d3]
		self.vel_norm = np.linalg.norm(self.d_l,axis=1)
		return self.vel_norm

	def lowpass(self, x, fp, fs):
		self.samplerate = 170
		self.fp = fp
		self.fs = fs
		self.gpass = 5
		self.gstop = 100
		self.x = np.nan_to_num(x)
		self.fn = self.samplerate/2
		self.wp = self.fp/self.fn
		self.ws = self.fs/self.fn
		self.N,self.Wn = signal.buttord(self.wp,self.ws,self.gpass,self.gstop)
		self.b,self.a = signal.butter(self.N,self.Wn,'low')
		self.y = signal.filtfilt(self.b,self.a,self.x)
		return self.y

	def get_speed_list(self, time, pos):
		# self.make_list(pos)
		self.y1_filt = self.lowpass(pos['x'],0.4,5)
		self.y2_filt = self.lowpass(pos['y'],0.4,5)
		self.y3_filt = self.lowpass(pos['z'],0.4,5)
		self.vy1 = self.getSpeed(time,self.y1_filt)
		self.vy2 = self.getSpeed(time,self.y2_filt)
		self.vy3 = self.getSpeed(time,self.y3_filt)
		self.vy1_filt = self.lowpass(self.vy1,1,5)
		self.vy2_filt = self.lowpass(self.vy2,1,5)
		self.vy3_filt = self.lowpass(self.vy3,1,5)
		self.ay1 = self.getSpeed(time,self.vy1_filt)
		self.ay2 = self.getSpeed(time,self.vy2_filt)
		self.ay3 = self.getSpeed(time,self.vy3_filt)
		self.ay1_filt = self.lowpass(self.ay1,1,5)
		self.ay2_filt = self.lowpass(self.ay2,1,5)
		self.ay3_filt = self.lowpass(self.ay3,1,5)
		self.jy1 = self.getSpeed(time,self.ay1_filt)
		self.jy2 = self.getSpeed(time,self.ay2_filt)
		self.jy3 = self.getSpeed(time,self.ay3_filt)
		self.jy1_filt = self.lowpass(self.jy1,1,5)
		self.jy2_filt = self.lowpass(self.jy2,1,5)
		self.jy3_filt = self.lowpass(self.jy3,1,5)
		self.dict_move = pd.DataFrame(data={'vx':self.vy1_filt,'vy':self.vy2_filt,'vz':self.vy3_filt,'ax':self.ay1_filt,'ay':self.ay2_filt,'az':self.ay3_filt,'jx':self.jy1_filt,'jy':self.jy2_filt,'jz':self.jy3_filt})
		return self.dict_move

	def solox_graph(self,x,y1,lb1,y2,lb2,y3,lb3,y4,lb4):
		plt.subplot(4,1,1)
		plt.plot(x,y1,label=lb1,color='r')
		plt.legend()
		plt.subplot(4,1,2)
		plt.plot(x,y2,label=lb2,color='c')
		plt.legend()
		plt.subplot(4,1,3)
		plt.plot(x,y3,label=lb3,color='b')
		plt.legend()
		plt.subplot(4,1,4)
		plt.plot(x,y4,label=lb4,color='y')
		plt.legend()
		plt.show()

	def write_csv(self,cs,ce,t,x,y,z,vx,vy,vz,ax,ay,az,jx,jy,jz,x_1,y_1,z_1,vx_1,vy_1,vz_1,ax_1,ay_1,az_1,jx_1,jy_1,jz_1,x_2,y_2,z_2,vx_2,vy_2,vz_2,ax_2,ay_2,az_2,jx_2,jy_2,jz_2):
		self.name = 'tsuruoka_tanada'
		self.conditions = 'robot'
		self.comment = input('part--> ')
		self.date = '20211112'
		self.folder = '/Users/sprout/OneDrive - ?????????????????????/??????/?????????/??????/????????????/???4???????????????/fusion'
		self.filename = self.folder + '/' + self.date + '_' + self.name + '_' + self.conditions + '_' + self.comment + '.csv'
		check = os.path.isfile(self.filename)
		if check:
			os.remove(self.filename)
			print('remove')
		self.df = pd.DataFrame(data={'time':t,'x':x,'y':y,'z':z,'vx':vx,'vy':vy,'vz':vz,'ax':ax,'ay':ay,'az':az,'jx':jx,'jy':jy,'jz':jz,'x1':x_1,'y1':y_1,'z1':z_1,'vx1':vx_1,'vy1':vy_1,'vz1':vz_1,'ax1':ax_1,'ay1':ay_1,'az1':az_1,'jx1':jx_1,'jy1':jy_1,'jz1':jz_1,'x2':x_2,'y2':y_2,'z2':z_2,'vx2':vx_2,'vy2':vy_2,'vz2':vz_2,'ax2':ax_2,'ay2':ay_2,'az2':az_2,'jx2':jx_2,'jy2':jy_2,'jz2':jz_2})
		self.df_c = pd.DataFrame(self.df[cs:ce])
		self.df_r = self.df_c.reset_index(drop=True)
		self.df_r.to_csv(self.filename)
		print('write csv')

	def fig_3x(self,df):
		self.fig, self.ax1 = plt.subplots()
		self.fig.subplots_adjust(bottom=0.2)
		self.fig.subplots_adjust(right=0.75)
		self.fig.subplots_adjust(left=0.1)
		sns.set_palette('Set2')
		self.ax1.sns.lineplot(data=df,x='Time [s]',y='z [mm]')
		self.ax2 = self.ax1.twinx()
		self.ax2.sns.lineplot(data=df,x='Time [s]',y='Beginner [mm/s]')
		self.ax3 = self.ax1.twinx()
		self.ax3.sns.lineplot(data=df,x='Time [s]',y='Expert [mm/s]')
		plt.tight_layout()
		plt.show()

if __name__ in '__main__':
	g_r = GRAPH2D()
	g_1 = GRAPH2D()
	g_2 = GRAPH2D()
	data = pd.read_csv('/Users/sprout/OneDrive - ?????????????????????/??????/?????????/??????/????????????/20211108/fusion/20211112_tsuruoka_tanada_woFB_5.csv')
	pos_r = pd.DataFrame({'x':data['x'],'y':data['y'],'z':data['z']})
	pos_1 = pd.DataFrame({'x':data['x1'],'y':data['y1'],'z':data['z1']})
	pos_2 = pd.DataFrame({'x':data['x2'],'y':data['y2'],'z':data['z2']})
	g_r.get_speed_list(time=data['time'],pos=pos_r)
	g_1.get_speed_list(time=data['time'],pos=pos_1)
	g_2.get_speed_list(time=data['time'],pos=pos_2)
	vel_r_norm = g_r.get_norm(g_r.vy1_filt,g_r.vy2_filt,g_r.vy3_filt)
	vel_1_norm = g_1.get_norm(g_1.vy1_filt,g_1.vy2_filt,g_1.vy3_filt)
	vel_2_norm = g_2.get_norm(g_2.vy1_filt,g_2.vy2_filt,g_2.vy3_filt)
	vel_df = pd.DataFrame({'Time [s]':data['time'],'z [mm]':data['y'],'Robot velocity [mm/s]':vel_r_norm,'Beginner [mm/s]':vel_2_norm,'Expert [mm/s]':vel_1_norm})
	g_r.fig_3x(df=vel_df)	