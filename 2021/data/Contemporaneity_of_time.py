import numpy as np
import pandas as pd
import  os
from scipy import signal
import matplotlib.pyplot as plt

def contemporaneity_time(d1,d2,d3,i):
	d_l = np.c_[d1,d2,d3]
	d_norm = np.linalg.norm(d_l,axis=1)
	maxid = signal.argrelmax(d_norm, order=100)
	maxid_o = []
	for i in range(len(maxid[0])):
		if d_norm[maxid[0][i]] > 40:
			maxid_o.append(maxid[0][i])
	print(i)
	print(maxid_o)
	max_t = t[maxid_o[1]]
	print(t[maxid_o])
	plt.plot(t,d_norm)
	plt.plot(t[maxid_o],d_norm[maxid_o],'bo')
	plt.show()
	return max_t
	# max_d_norm = d_norm[maxid_o[1]]
	# reaction = max_d_norm * 0.4
	# for reaction_index in range(maxid_o[1],0,-1):
	# 	if reaction >= d_norm[reaction_index]:
	# 		reaction_time = t[reaction_index]
	# 		return reaction_time

def get_data(number,index,o_path):
	n = number + 1
	read_path = o_path + str(n) + '.csv'
	df = pd.read_csv(read_path)
	t_d = df.loc[:,'time']
	if index == 'x':
		vel_x_d = df['vx'].values
		vel_y_d = df['vy'].values
		vel_z_d = df['vz'].values
		return  t_d,vel_x_d,vel_y_d,vel_z_d
	elif index == 'x1':
		vel_x_d = df['vx1'].values
		vel_y_d = df['vy1'].values
		vel_z_d = df['vz1'].values
		return  t_d,vel_x_d,vel_y_d,vel_z_d
	elif index == 'x2':
		vel_x_d = df['vx2'].values
		vel_y_d = df['vy2'].values
		vel_z_d = df['vz2'].values
		return  t_d,vel_x_d,vel_y_d,vel_z_d

def write_csv():
	name = 'tsuruoka_tanada'
	conditions = 'robot'
	date = '20211112'
	folder = '/Users/sprout/OneDrive - 名古屋工業大学/学校/研究室/実験/予備実験/第4回ゼミ用'
	filename = folder + '/' + 'ct_' + date + '_' + name + '_' + conditions + '.csv'
	check = os.path.isfile(filename)
	if check:
		os.remove(filename)
		print('remove')
	df.to_csv(filename)
	print('write csv')

if __name__ == '__main__':
	df = pd.DataFrame(columns=['robot','begginer','expert','diff','percentage'])
	path = '/Users/sprout/OneDrive - 名古屋工業大学/学校/研究室/実験/予備実験/第4回ゼミ用/fusion/20211112_tsuruoka_tanada_woFB_'
	print(os.path.splitext(os.path.basename(path))[0])
	for i in range(5):
		t,vel_x,vel_y,vel_z = get_data(i,'x',path)
		t,vel_x_1,vel_y_1,vel_z_1 = get_data(i,'x1',path)
		t,vel_x_2,vel_y_2,vel_z_2 = get_data(i,'x2',path)
		ct_r = contemporaneity_time(vel_x,vel_y,vel_z,i)
		ct_1 = contemporaneity_time(vel_x_1,vel_y_1,vel_z_1,i)
		ct_2 = contemporaneity_time(vel_x_2,vel_y_2,vel_z_2,i)
		df = df.append({'robot':ct_r,'begginer':ct_2,'expert':ct_1,'diff':ct_2-ct_1,'percentage':(ct_2-ct_1)/ct_1},ignore_index=True)
	# write_csv()