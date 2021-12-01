from dtaidistance import dtw_ndim
from dtaidistance import dtw_visualisation as dtwvis
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

def import_data(number,path):
	n = number + 1
	read_path = path + str(n) + '.csv'
	data = pd.read_csv(read_path)
	filename = os.path.splitext(os.path.basename(read_path))[0]
	print(filename)
	return data,read_path

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
	robot_lsit = pd.DataFrame(data=np.c_[x,y,z],columns=['x','y','z'])
	expert_list = pd.DataFrame(data=np.c_[x1,y1,z1],columns=['x1','y1','z1'])
	begginner_lsit = pd.DataFrame(data=np.c_[x2,y2,z2],columns=['x2','y2','z2'])
	return robot_lsit,expert_list,begginner_lsit

def dtw_n(d1,d2):
	a1 = np.array(d1)
	a2 = np.array(d2)
	dtw_n = dtw_ndim.distance(a1,a2)
	print(dtw_n)
	return dtw_n

def norm_cost():
	diff_list = np.c_[expert['x1']-begginer['x2'],expert['y1']-begginer['y2'],expert['z1']-begginer['z2']]
	norm = np.linalg.norm(diff_list,axis=1)
	sum_norm = np.sum(norm)
	print(sum_norm)

def plot_3d():
	fig = plt.figure()
	ax = plt.gca(projection='3d')
	ax.set_xlabel("X-axis")
	ax.set_ylabel("Y-axis")
	ax.set_zlabel("Z-axis")
	ax.plot(begginer['x2'],begginer['y2'],begginer['z2'],label='begginer')
	ax.plot(expert['x1'],expert['y1'],expert['z1'],label='expert')
	ax.view_init(elev=60, azim=45)
	ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0, fontsize=9)
	ax.set_box_aspect((1,1,1))
	filename = os.path.splitext(os.path.basename(path))[0]
	plt.title(filename)
	plt.savefig('fig/'+filename+'.png')

if __name__ == '__main__':
	for i in range(5):
		data,path = import_data(number=i,path='/Users/sprout/OneDrive - 名古屋工業大学/学校/研究室/実験/予備実験/第4回ゼミ用/fusion/20211112_tsuruoka_tanada_woFB_')
		robot,expert,begginer = get_data(data)
		norm_cost()
		# dtw_n(expert,begginer)
		plot_3d()