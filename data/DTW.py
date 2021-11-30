from dtaidistance import dtw_ndim
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

def import_data(path):
	data = pd.read_csv(path)
	return data,path

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
	x = x - x[0]
	y = y - y[0]
	z = z - z[0]
	x1 = x1 - x1[0]
	y1 = y1 - y1[0]
	z1 = z1 - z1[0]
	x2 = x2 - x2[0]
	y2 = y2 - y2[0]
	z2 = z2 - z2[0]
	robot_lsit = np.array([x,y,z])
	expert_list = np.array([x1,y1,z1])
	begginner_lsit = np.array([x2,y2,z2])
	return robot_lsit,expert_list,begginner_lsit

def dtw_n(d1,d2):
	dtw_n = dtw_ndim.distance(d1,d2)
	return dtw_n

def plot_3d():
	fig = plt.figure()
	ax = plt.gca(projection='3d')
	ax.set_xlabel("X-axis")
	ax.set_ylabel("Y-axis")
	ax.set_zlabel("Z-axis")
	ax.plot(robot[0],robot[1],robot[2],label='robot')
	ax.plot(begginer[0],begginer[1],begginer[2],label='begginer')
	ax.plot(expert[0],expert[1],expert[2],label='expert')
	ax.legend(loc="upper right",bbox_to_anchor=(1.1,1.1))
	ax.set_box_aspect((1,1,1))
	filename = os.path.splitext(os.path.basename(path))[0]
	plt.title(filename)
	plt.show()

if __name__ == '__main__':
	data,path = import_data(path='/Users/sprout/OneDrive - 名古屋工業大学/学校/研究室/実験/予備実験/第4回ゼミ用/fusion/20211112_tsuruoka_tanada_partner+robot_5.csv')
	robot,expert,begginer = get_data(data)
	dtw = dtw_n(expert,begginer)
	print(dtw)
	plot_3d()