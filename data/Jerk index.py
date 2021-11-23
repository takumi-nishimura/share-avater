import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

def Teulings_1997(tl,xl,yl,zl,j_x,j_y,j_z):
	sum_t = sum(tl)
	dx = np.diff(xl,axis=0)
	dy = np.diff(yl,axis=0)
	dz = np.diff(zl,axis=0)
	pos_d = np.c_[dx,dy,dz]
	norm = np.linalg.norm(pos_d,axis=1)
	d = np.sum(norm)
	jrk_d = np.c_[j_x,j_y,j_z]
	jrk = np.linalg.norm(jrk_d,axis=1)
	jrk_sq = np.power(jrk,2)
	all_jrk_sq = np.sum(jrk_sq)
	Jerk_index = np.sqrt(1/2*all_jrk_sq*sum_t**5/d**2)
	return Jerk_index

def search_data(number,o_path):
	n = number + 1
	read_path = o_path + str(n) + '.csv'
	df = pd.read_csv(read_path)
	filename = os.path.splitext(os.path.basename(read_path))[0]
	print(filename)
	if 'x' in df.columns:
		t = df.loc[:,'time']
		x = df.loc[:,'x']
		y = df.loc[:,'y']
		z = df.loc[:,'z']

		jrk_x = df['jx'].values
		jrk_y = df['jy'].values
		jrk_z = df['jz'].values
	return  t,x,y,z,jrk_x,jrk_y,jrk_z

if __name__ == '__main__':
	for i in range(5):
		t,x,y,z,jrk_x,jrk_y,jrk_z = search_data(i,'/Users/sprout/OneDrive - 名古屋工業大学/学校/研究室/実験/予備実験/第4回ゼミ用/fusion/20211112_tsuruoka_tanada_partner+robot_')
		Jrk_index = Teulings_1997(t,x,y,z,jrk_x,jrk_y,jrk_z)
		print('robot :','{:.5g}'.format(Jrk_index))