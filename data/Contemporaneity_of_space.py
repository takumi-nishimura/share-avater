from dtaidistance import dtw,dtw_ndim,dtw_visualisation as dtwvis
from scipy.spatial.distance import euclidean
from fastdtw import fastdtw
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import matplotlib_style

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
	dtw_c,dtw_p = dtw_ndim.warping_paths(a1,a2)
	print(dtw_c)
	return dtw_c

def f_dtw(d1,d2,show:bool=False,save:bool=False):
	a1 = np.array(d1)
	a2 = np.array(d2)
	dtw_c,dtw_p = fastdtw(a1,a2,radius=5,dist=euclidean)
	print(dtw_c)

	fig = plt.figure()
	ax = plt.gca(projection='3d')
	for i, j in dtw_p:
		ax.plot([a1[i][0],a2[j][0]],[a1[i][1],a2[j][1]],[a1[i][2],a2[j][2]],color='gray', linestyle='dashdot',linewidth = 0.3)
	ax.plot(begginer['x2'],begginer['y2'],begginer['z2'],label='begginer')
	ax.plot(expert['x1'],expert['y1'],expert['z1'],label='expert')
	ax.legend(bbox_to_anchor=(0.95, 0.8), loc='upper left', borderaxespad=0, fontsize=12)
	ax.view_init(elev=50, azim=13)
	filename = os.path.splitext(os.path.basename(path))[0]
	plt.title(filename)

	if save:
		plt.savefig('fig/f_dtw/'+filename+'.png')
	if show:
		plt.show()

def norm_cost(d1,d2,show:bool=False,save:bool=False):
	a1 = np.array(d1)
	a2 = np.array(d2)
	diff_list = np.c_[expert['x1']-begginer['x2'],expert['y1']-begginer['y2'],expert['z1']-begginer['z2']]
	norm = np.linalg.norm(diff_list,axis=1)
	sum_norm = np.sum(norm)
	print(sum_norm)

	fig = plt.figure()
	ax = plt.gca(projection='3d')
	for i in range(len(norm)):
		ax.plot([a1[i][0],a2[i][0]],[a1[i][1],a2[i][1]],[a1[i][2],a2[i][2]],color='gray', linestyle='dashdot',linewidth = 0.3)
	ax.plot(begginer['x2'],begginer['y2'],begginer['z2'],label='begginer')
	ax.plot(expert['x1'],expert['y1'],expert['z1'],label='expert')
	ax.legend(bbox_to_anchor=(0.95, 0.8), loc='upper left', borderaxespad=0, fontsize=12)
	ax.view_init(elev=50, azim=13)
	filename = os.path.splitext(os.path.basename(path))[0]
	plt.title(filename)

	if save:
		plt.savefig('fig/f_dtw/'+filename+'.png')
	if show:
		plt.show()

def path_norm(participants):
	if participants == 'begginner':
		dx1 = np.diff(begginer['x2'],axis=0)
		dy1 = np.diff(begginer['y2'],axis=0)
		dz1 = np.diff(begginer['z2'],axis=0)
		pos_d1 = np.c_[dx1,dy1,dz1]
		norm = np.linalg.norm(pos_d1,axis=1)
		d = np.sum(norm)
		print(d)
	elif participants == 'expert':
		dx1 = np.diff(expert['x1'],axis=0)
		dy1 = np.diff(expert['y1'],axis=0)
		dz1 = np.diff(expert['z1'],axis=0)
		pos_d1 = np.c_[dx1,dy1,dz1]
		norm = np.linalg.norm(pos_d1,axis=1)
		d = np.sum(norm)
		print(d)

def plot_3d():
	fig = plt.figure()
	ax = plt.gca(projection='3d')
	ax.set_xlabel("X-axis")
	ax.set_ylabel("Y-axis")
	ax.set_zlabel("Z-axis")
	ax.plot(begginer['x2'],begginer['y2'],begginer['z2'],label='begginer')
	ax.plot(expert['x1'],expert['y1'],expert['z1'],label='expert')
	ax.view_init(elev=13, azim=13)
	ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0, fontsize=12)
	ax.set_box_aspect((1,1,1))
	filename = os.path.splitext(os.path.basename(path))[0]
	plt.title(filename)
	# plt.savefig('fig/'+filename+'.png')
	plt.show()

if __name__ == '__main__':
	for i in range(1):
		data,path = import_data(number=i,path='/Users/sprout/OneDrive - 名古屋工業大学/学校/研究室/実験/予備実験/20211108/fusion/20211112_tsuruoka_tanada_woFB_')
		robot,expert,begginer = get_data(data)

		# dtw_n(expert,begginer)
		f_dtw(expert,begginer,show=True,save=False)
		norm_cost(expert,begginer,show=True,save=False)
		# path_norm(participants='begginner')

		# plot_3d()