import pandas as pd
import numpy as np
import os
from dtaidistance import dtw,dtw_ndim,dtw_visualisation as dtwvis
from scipy.spatial.distance import euclidean
from fastdtw import fastdtw
import matplotlib.pyplot as plt

class DTW:
	def __init__(self) -> None:
		pass

	def main(self, robot, begginer, expert, participant, condition, cycle):
		self.robot, self.begginer, self.expert = self.get_data(robot,begginer,expert)
		self.result = self.f_dtw(self.begginer, self.expert, participant, condition, cycle, show=False, save=False)
		return self.result

	def get_data(self,d_r,d_1,d_2):
		self.x = d_r['x']
		self.y = d_r['y']
		self.z = d_r['z']
		self.x1 = d_1['x']
		self.y1 = d_1['y']
		self.z1 = d_1['z']
		self.x2 = d_2['x']
		self.y2 = d_2['y']
		self.z2 = d_2['z']
		self.x = self.x - self.x[0]
		self.y = self.y - self.y[0]
		self.z = self.z - self.z[0]
		self.x1 = self.x1 - self.x1[0]
		self.y1 = self.y1 - self.y1[0]
		self.z1 = self.z1 - self.z1[0]
		self.x2 = self.x2 - self.x2[0]
		self.y2 = self.y2 - self.y2[0]
		self.z2 = self.z2 - self.z2[0]
		self.robot_lsit = pd.DataFrame(data=np.c_[self.x,self.y,self.z],columns=['x','y','z'])
		self.begginner_list = pd.DataFrame(data=np.c_[self.x1,self.y1,self.z1],columns=['x1','y1','z1'])
		self.expert_lsit = pd.DataFrame(data=np.c_[self.x2,self.y2,self.z2],columns=['x2','y2','z2'])
		return self.robot_lsit, self.begginner_list, self.expert_lsit

	def f_dtw(self,d1,d2, participant, condition, cycle, show:bool=False, save:bool=False):
		self.a1 = np.array(d1)
		self.a2 = np.array(d2)
		dtw_c,dtw_p = fastdtw(self.a1,self.a2,dist=euclidean)
		print(dtw_c)

		if show:
			fig = plt.figure()
			ax = plt.gca(projection='3d')
			for i, j in dtw_p:
				ax.plot([self.a1[i][0],self.a2[j][0]],[self.a1[i][1],self.a2[j][1]],[self.a1[i][2],self.a2[j][2]],color='gray', linestyle='dashdot',linewidth = 0.3)
			ax.plot(self.begginer['x1'],self.begginer['y1'],self.begginer['z1'],label='begginer')
			ax.plot(self.expert['x2'],self.expert['y2'],self.expert['z2'],label='expert')
			ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0, fontsize=9)
			ax.view_init(elev=50, azim=13)
			filename = participant + '_' + condition + '_' + cycle
			plt.title(filename)

			if save:
				plt.savefig('/Users/sprout/OneDrive - 名古屋工業大学/学校/研究室/実験/卒論実験/m_calculate/fig/dtw/'+filename+'.png')
			if show:
				plt.show()
			
			ax.close()

		if save:
			fig = plt.figure()
			ax = plt.gca(projection='3d')
			for i, j in dtw_p:
				ax.plot([self.a1[i][0],self.a2[j][0]],[self.a1[i][1],self.a2[j][1]],[self.a1[i][2],self.a2[j][2]],color='gray', linestyle='dashdot',linewidth = 0.3)
			ax.plot(self.begginer['x1'],self.begginer['y1'],self.begginer['z1'],label='begginer')
			ax.plot(self.expert['x2'],self.expert['y2'],self.expert['z2'],label='expert')
			ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0, fontsize=9)
			ax.view_init(elev=50, azim=13)
			filename = participant + '_' + condition + '_' + cycle
			plt.title(filename)
			plt.savefig('/Users/sprout/OneDrive - 名古屋工業大学/学校/研究室/実験/卒論実験/m_calculate/fig/dtw/'+filename+'.png')

			ax.close

		return dtw_c