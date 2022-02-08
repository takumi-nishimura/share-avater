import pandas as pd
import numpy as np
from fastdtw import fastdtw
from scipy.spatial.distance import euclidean
from Figure.figure_manager import FIG
import matplotlib.pyplot as plt

class DTW:
	def __init__(self) -> None:
		print('--- import --- : Motion Analysis DTW')

	def DTW_C(self,d_1,d_2):
		print('--- calculate --- : Motion Analysis DTW')
		self.begginer, self.expert = self.get_data(d_1,d_2)
		self.dtw = self.f_dtw(self.begginer,self.expert)
		print('dtw : ',self.dtw)
		return self.dtw

	def get_data(self,d_1,d_2):
		self.x1 = d_1['x']
		self.y1 = d_1['y']
		self.z1 = d_1['z']
		self.x2 = d_2['x']
		self.y2 = d_2['y']
		self.z2 = d_2['z']
		self.x1 = self.x1 - self.x1[0]
		self.y1 = self.y1 - self.y1[0]
		self.z1 = self.z1 - self.z1[0]
		self.x2 = self.x2 - self.x2[0]
		self.y2 = self.y2 - self.y2[0]
		self.z2 = self.z2 - self.z2[0]
		self.begginner_list = pd.DataFrame(data=np.c_[self.x1,self.y1,self.z1],columns=['x1','y1','z1'])
		self.expert_lsit = pd.DataFrame(data=np.c_[self.x2,self.y2,self.z2],columns=['x2','y2','z2'])
		return self.begginner_list, self.expert_lsit

	def f_dtw(self,d1,d2):
		self.a1 = np.array(d1)
		self.a2 = np.array(d2)
		dtw_c, dtw_p = fastdtw(self.a1,self.a2,radius=2,dist=euclidean)
		return dtw_c