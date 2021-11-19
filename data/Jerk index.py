import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

path = '/Users/sprout/OneDrive - 名古屋工業大学/学校/研究室/実験/予備実験/第4回ゼミ用/fusion/20211112_tsuruoka_tanada_partner_1.csv'
df = pd.read_csv(path)
filename = os.path.splitext(os.path.basename(path))[0]
print("file:",filename)

if 'x' in df.columns:
	tf = df.loc[:,'time'].sum()
	x = df.loc[:,'x']
	y = df.loc[:,'y']
	z = df.loc[:,'z']
	dx = np.diff(x,axis=0)
	dy = np.diff(y,axis=0)
	dz = np.diff(z,axis=0)
	pos_d = np.c_[dx,dy,dz]
	norm = np.linalg.norm(pos_d,axis=1)
	d = np.sum(norm)

	jrk_x = df['jx'].values
	jrk_y = df['jy'].values
	jrk_z = df['jz'].values
	jrk_d = np.c_[jrk_x,jrk_y,jrk_z]
	jrk = np.linalg.norm(jrk_d,axis=1)
	jrk_sq = np.power(jrk,2)
	all_jrk_sq = np.sum(jrk_sq)

	Jerk_index = tf**5/(d**2)*all_jrk_sq/2
	print('robot :','{:.5g}'.format(Jerk_index))

if 'x1' in df.columns:
	tf = df.loc[:,'time'].sum()
	x = df.loc[:,'x1']
	y = df.loc[:,'y1']
	z = df.loc[:,'z1']
	dx = np.diff(x,axis=0)
	dy = np.diff(y,axis=0)
	dz = np.diff(z,axis=0)
	pos_d = np.c_[dx,dy,dz]
	norm = np.linalg.norm(pos_d,axis=1)
	d = np.sum(norm)

	jrk = df['j1'].values
	jrk_sq = np.power(jrk,2)
	all_jrk_sq = np.sum(jrk_sq)

	Jerk_index = tf**5/(d**2)*all_jrk_sq/2
	print('p_1 :','{:.5g}'.format(Jerk_index))

if 'x2' in df.columns:
	tf = df.loc[:,'time'].sum()
	x = df.loc[:,'x2']
	y = df.loc[:,'y2']
	z = df.loc[:,'z2']
	dx = np.diff(x,axis=0)
	dy = np.diff(y,axis=0)
	dz = np.diff(z,axis=0)
	pos_d = np.c_[dx,dy,dz]
	norm = np.linalg.norm(pos_d,axis=1)
	d = np.sum(norm)

	jrk = df['j2'].values
	jrk_sq = np.power(jrk,2)
	all_jrk_sq = np.sum(jrk_sq)

	Jerk_index = tf**5/(d**2)*all_jrk_sq/2
	print('p_2 :','{:.5g}'.format(Jerk_index))