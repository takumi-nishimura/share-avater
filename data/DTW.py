from dtaidistance import dtw_ndim
import numpy as np
from numpy.core.arrayprint import _extendLine_pretty
import pandas as pd

def import_data(path):
	data = pd.read_csv(path)
	return data

def get_data(d):
	x = d['x']
	y = d['y']
	z = d['z']
	x1 = d['x1']
	y1 = d['y1']
	z1 = d['z1']
	x2 = d['x2']
	y2 = d['y2']
	z2 = d['z2']
	robot_lsit = np.array([x,y,z])
	begginer_list = np.array([x1,y1,z1])
	expert_lsit = np.array([x2,y2,z2])
	return robot_lsit,begginer_list,expert_lsit

def dtw_n(d1,d2):
	dtw_n = dtw_ndim.distance(d1,d2)
	return dtw_n

if __name__ == '__main__':
	data = import_data(path='/Users/sprout/OneDrive - 名古屋工業大学/学校/研究室/実験/予備実験/第4回ゼミ用/fusion/20211112_tsuruoka_tanada_woFB_2.csv')
	robot,begginer,expert = get_data(data)
	dtw = dtw_n(begginer,expert)
	print(dtw)
	