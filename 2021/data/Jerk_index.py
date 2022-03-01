import pandas as pd
import numpy as np
import os

def Teulings_1997(tl,xl,yl,zl,j_x,j_y,j_z):
	dt = tl[len(tl)-1] - tl[0]
	dx = np.diff(xl,axis=0)
	dy = np.diff(yl,axis=0)
	dz = np.diff(zl,axis=0)
	pos_d = np.c_[dx,dy,dz]
	norm = np.linalg.norm(pos_d,axis=1)
	d = np.sum(norm)
	jrk_d = np.c_[j_x,j_y,j_z]
	jrk_norm = np.linalg.norm(jrk_d,axis=1)
	jrk_sq = np.power(jrk_norm,2)
	sum_jrk_sq = np.sum(jrk_sq)
	Jerk_index = np.sqrt(1/2*sum_jrk_sq*dt**5/d**2)
	print('Teulings_1997 : ','{:.5g}'.format(Jerk_index))
	return Jerk_index

def Ahmad_2016(tl,v_x,v_y,v_z,j_x,j_y,j_z):
	jrk_sq_list = []
	for i in range(len(j_x)):
		jrk_sq = j_x[i]**2 + j_y[i]**2 + j_z[i]**2
		jrk_sq_list.append(jrk_sq)
	sum_jrk = np.sum(jrk_sq_list)
	dt = tl[len(tl)-1] - tl[0]
	vel_sq_list = []
	for i in range(len(v_x)):
		vel_sq = np.sqrt(v_x[i]**2 + v_y[i]**2 + v_z[i]**2)
		vel_sq_list.append(vel_sq)
	sum_vel = np.sum(vel_sq_list)
	normalized_Jrk_index = sum_jrk * dt**5 / (sum_vel**2)
	print('Ahmad_2016 : ','{:.5g}'.format(normalized_Jrk_index))
	return normalized_Jrk_index

def _Ahmad_2016(tl,v_x,v_y,v_z,j_x,j_y,j_z):
		jrk_sq_list = []
		for i in range(len(j_x)):
			jrk_sq = j_x[i]**2 + j_y[i]**2 + j_z[i]**2
			jrk_sq_list.append(jrk_sq)
		sum_jrk = np.sum(jrk_sq_list)
		dt = tl.values[-1] - tl.values[0]
		vel_sq_list = []
		for i in range(len(v_x)):
			vel_sq = np.sqrt(v_x[i]**2 + v_y[i]**2 + v_z[i]**2)
			vel_sq_list.append(vel_sq)
		sum_vel = np.sum(vel_sq_list)
		normalized_Jrk_index = sum_jrk * dt**5 / (sum_vel**2)
		print('Ahmad_2016 : ','{:.5g}'.format(normalized_Jrk_index))
		return normalized_Jrk_index

def mean_jrk(j_x,j_y,j_z):
	jrk_norm_list = []
	for i in range(len(j_x)):
		jrk_list = np.array([j_x[i],j_y[i],j_z[i]])
		jrk_norm = np.linalg.norm(jrk_list)
		jrk_norm_list.append(jrk_norm)
	jrk_mean = np.mean(jrk_norm_list)
	print('mean_jerk : ','{:.5g}'.format(jrk_mean))
	return jrk_mean

def search_data(number,o_path):
	n = number + 1
	read_path = o_path + str(n) + '.csv'
	df = pd.read_csv(read_path)
	filename = os.path.splitext(os.path.basename(read_path))[0]
	print(filename)
	if 'x' in df.columns:
		t_d = df.loc[:,'time']
		x_d = df.loc[:,'x']
		y_d = df.loc[:,'y']
		z_d = df.loc[:,'z']

		vel_x_d = df['vx'].values
		vel_y_d = df['vy'].values
		vel_z_d = df['vz'].values

		jrk_x_d = df['jx'].values
		jrk_y_d = df['jy'].values
		jrk_z_d = df['jz'].values
	return  t_d,x_d,y_d,z_d,vel_x_d,vel_y_d,vel_z_d,jrk_x_d,jrk_y_d,jrk_z_d

if __name__ == '__main__':
	for i in range(5):
		t,x,y,z,vel_x,vel_y,vel_z,jrk_x,jrk_y,jrk_z = search_data(i,'/Users/sprout/OneDrive - 名古屋工業大学/学校/研究室/実験/予備実験/20211108/solo/20211112_tsuruoka_solo_')
		# mean_jerk = mean_jrk(jrk_x,jrk_y,jrk_z)
		# Jrk_index = Teulings_1997(t,x,y,z,jrk_x,jrk_y,jrk_z)
		Normlized_Jrk_index = _Ahmad_2016(t,vel_x,vel_y,vel_z,jrk_x,jrk_y,jrk_z)