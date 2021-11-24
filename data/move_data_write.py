import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy import signal
import os
from statistics import mean
from scipy import fftpack

def main():
	start,end,column = read(data,'time',0,10000.0)
	x,y1,y2,y3 = get_data(start,end,column,'x','y','z')
	x_1,y1_1,y2_1,y3_1 = get_data(start,end,column,'x1','y1','z1')
	x_2,y1_2,y2_2,y3_2 = get_data(start,end,column,'x2','y2','z2')

	y1_filt = lowpass(y1,0.3,5)
	y2_filt = lowpass(y2,0.3,5)
	y3_filt = lowpass(y3,0.3,5)
	vy1 = getSpeed(x,y1_filt)
	vy1_filt = lowpass(vy1,1,5)
	vy2 = getSpeed(x,y2_filt)
	vy2_filt = lowpass(vy2,1,5)
	vy3 = getSpeed(x,y3_filt)
	vy3_filt = lowpass(vy3,1,5)
	ay1 = getSpeed(x,vy1_filt)
	ay1_filt = lowpass(ay1,1,5)
	ay2 = getSpeed(x,vy2_filt)
	ay2_filt = lowpass(ay2,1,5)
	ay3 = getSpeed(x,vy3_filt)
	ay3_filt = lowpass(ay3,1,5)
	jy1 = getSpeed(x,ay1_filt)
	jy1_filt = lowpass(jy1,1,5)
	jy2 = getSpeed(x,ay2_filt)
	jy2_filt = lowpass(jy2,1,5)
	jy3 = getSpeed(x,ay3_filt)
	jy3_filt = lowpass(jy3,1,5)

	y1_1_filt = lowpass(y1_1,0.4,5)
	y2_1_filt = lowpass(y2_1,0.4,5)
	y3_1_filt = lowpass(y3_1,0.4,5)
	vy1_1 = getSpeed(x_1,y1_1_filt)
	vy1_1_filt = lowpass(vy1_1,1,5)
	vy2_1 = getSpeed(x_1,y2_1_filt)
	vy2_1_filt = lowpass(vy2_1,1,5)
	vy3_1 = getSpeed(x_1,y3_1_filt)
	vy3_1_filt = lowpass(vy3_1,1,5)
	ay1_1 = getSpeed(x_1,vy1_1_filt)
	ay1_1_filt = lowpass(ay1_1,1,5)
	ay2_1 = getSpeed(x_1,vy2_1_filt)
	ay2_1_filt = lowpass(ay2_1,1,5)
	ay3_1 = getSpeed(x_1,vy3_1_filt)
	ay3_1_filt = lowpass(ay3_1,1,5)
	jy1_1 = getSpeed(x_1,ay1_1_filt)
	jy1_1_filt = lowpass(jy1_1,1,5)
	jy2_1 = getSpeed(x_1,ay2_1_filt)
	jy2_1_filt = lowpass(jy2_1,1,5)
	jy3_1 = getSpeed(x_1,ay3_1_filt)
	jy3_1_filt = lowpass(jy3_1,1,5)

	y1_2_filt = lowpass(y1_2,0.4,5)
	y2_2_filt = lowpass(y2_2,0.4,5)
	y3_2_filt = lowpass(y3_2,0.4,5)
	vy1_2 = getSpeed(x_2,y1_2_filt)
	vy1_2_filt = lowpass(vy1_2,1,5)
	vy2_2 = getSpeed(x_2,y2_2_filt)
	vy2_2_filt = lowpass(vy2_2,1,5)
	vy3_2 = getSpeed(x_2,y3_2_filt)
	vy3_2_filt = lowpass(vy3_2,1,5)
	ay1_2 = getSpeed(x_2,vy1_2_filt)
	ay1_2_filt = lowpass(ay1_2,1,5)
	ay2_2 = getSpeed(x_2,vy2_2_filt)
	ay2_2_filt = lowpass(ay2_2,1,5)
	ay3_2 = getSpeed(x_2,vy3_2_filt)
	ay3_2_filt = lowpass(ay3_2,1,5)
	jy1_2 = getSpeed(x_2,ay1_2_filt)
	jy1_2_filt = lowpass(jy1_2,1,5)
	jy2_2 = getSpeed(x_2,ay2_2_filt)
	jy2_2_filt = lowpass(jy2_2,1,5)
	jy3_2 = getSpeed(x_2,ay3_2_filt)
	jy3_2_filt = lowpass(jy3_2,1,5)
	
	cs,ce,column_c = read(data,'time',236,250)
	write_csv(cs,ce,x,y1,y2,y3,vy1,vy2,vy3,ay1,ay2,ay3,jy1,jy2,jy3,y1_1,y2_1,y3_1,vy1_1,vy2_1,vy3_1,ay1_1,ay2_1,ay3_1,jy1_1,jy2_1,jy3_1,y1_2,y2_2,y3_2,vy1_2,vy2_2,vy3_2,ay1_2,ay2_2,ay3_2,jy1_2,jy2_2,jy3_2)

def read(data,columns,s,e):
	search_start = s
	search_end = e
	search_column = columns
	search_column_n = data.columns.get_loc(search_column)
	s_flag = 0
	for s_row_counter in range(len(data)):
		if s_flag == 0:
			if search_start == round(data.at[data.index[s_row_counter], search_column],1):
				start = s_row_counter
				print('start',start)
				print('start time',data.iloc[start,search_column_n])
				s_flag = 1
			elif s_row_counter == len(data)-1:
				print('Start not matched.')
				start = 0
				print('start time',data.iloc[start,search_column_n])
	for e_row_counter in range(len(data)):
		if search_end == round(data.at[data.index[e_row_counter], search_column],1):
			end = e_row_counter
			print('end',end)
			print('end time',data.iloc[end,search_column_n])
			return start,end,search_column
		elif e_row_counter == len(data)-1:
			print('End not matched.')
			end = e_row_counter
			print('end',end)
			print('end time',data.iloc[end,search_column_n])
			return start,end,search_column

def get_data(start,end,column,c1,c2,c3):
	x = data.loc[start:end,column]
	y1 = data.loc[start:end,c1]
	y2 = data.loc[start:end,c2]
	y3 = data.loc[start:end,c3]
	x = x.reset_index(drop=True)
	y1 = y1.reset_index(drop=True)
	y2 = y2.reset_index(drop=True)
	y3 = y3.reset_index(drop=True)
	return x,y1,y2,y3

def getSpeed(t,g1):
	mean_dt = mean(np.diff(t))
	speed = []
	for i in range(len(t)):
		if i == 0:
			speed.append(0)
		elif i == len(t)-1:
			speed.append(0)
		else:
			speed.append((g1[i+1]-g1[i-1])/(2*mean_dt))
	return speed

def lowpass(x,fp,fs):
	samplerate = 170
	fp = fp # 通過域端周波数[Hz]
	fs = fs # 阻止域端周波数[Hz]
	gpass = 5 # 通過域端最大損失[dB]
	gstop = 100 # 阻止域端最小損失[dB]
	x = np.nan_to_num(x)
	fn = samplerate/2
	wp = fp/fn
	ws = fs/fn
	N,Wn = signal.buttord(wp,ws,gpass,gstop)
	b,a = signal.butter(N,Wn,'low')
	y = signal.filtfilt(b,a,x)
	return y

def solox_graph(x,y1,lb1,y2,lb2,y3,lb3,y4,lb4):
	plt.subplot(4,1,1)
	plt.plot(x,y1,label=lb1,color='r')
	plt.legend()
	plt.subplot(4,1,2)
	plt.plot(x,y2,label=lb2,color='c')
	plt.legend()
	plt.subplot(4,1,3)
	plt.plot(x,y3,label=lb3,color='b')
	plt.legend()
	plt.subplot(4,1,4)
	plt.plot(x,y4,label=lb4,color='y')
	plt.legend()
	filename = os.path.splitext(os.path.basename(path))[0]
	# plt.title(filename)
	plt.show()

def solox_log_graph(y11,y12,y21,y22):
	plt.subplot(2,1,1)
	plt.loglog(y11, 10 * np.log(y12))
	plt.subplot(2,1,2)
	plt.loglog(y21, 10 * np.log(y22))
	# plt.subplot(2,2,3)
	# plt.loglog(y31, 10 * np.log(y32))
	# plt.subplot(2,2,4)
	# plt.loglog(y41, 10 * np.log(y42))
	plt.show()

def twinx_graph(x,y1,lb1,y2,lb2,y3,lb3,y4,lb4):
	fig,ax1 = plt.subplots()
	fig.subplots_adjust(bottom=0.2)
	fig.subplots_adjust(right=0.75)
	fig.subplots_adjust(left=0.1)
	ax1.plot(x,y1,label=lb1,color='r')
	ax2 = ax1.twinx()
	ax2.plot(x,y2,label=lb2,color='c')
	ax3 = ax1.twinx()
	ax3.plot(x,y3,label=lb3,color='b')
	rspine = ax3.spines['right']
	rspine.set_position(('axes', 1.1))
	h1, l1 = ax1.get_legend_handles_labels()
	h2, l2 = ax2.get_legend_handles_labels()
	h3, l3 = ax3.get_legend_handles_labels()
	ax1.legend(h1+h2+h3,l1+l2+l3,loc='upper right')
	ax1.grid(True)
	filename = os.path.splitext(os.path.basename(path))[0]
	plt.title(filename)
	plt.show()

def write_csv(cs,ce,t,x,y,z,vx,vy,vz,ax,ay,az,jx,jy,jz,x_1,y_1,z_1,vx_1,vy_1,vz_1,ax_1,ay_1,az_1,jx_1,jy_1,jz_1,x_2,y_2,z_2,vx_2,vy_2,vz_2,ax_2,ay_2,az_2,jx_2,jy_2,jz_2):
	name = 'tsuruoka_tanada'
	conditions = 'partner+robot'
	comment = input('part--> ')
	date = '20211112'
	folder = '/Users/sprout/OneDrive - 名古屋工業大学/学校/研究室/実験/予備実験/第4回ゼミ用/fusion'
	filename = folder + '/' + date + '_' + name + '_' + conditions + '_' + comment + '.csv'
	check = os.path.isfile(filename)
	if check:
		os.remove(filename)
		print('remove')
	df = pd.DataFrame(data={'time':t,'x':x,'y':y,'z':z,'vx':vx,'vy':vy,'vz':vz,'ax':ax,'ay':ay,'az':az,'jx':jx,'jy':jy,'jz':jz,'x1':x_1,'y1':y_1,'z1':z_1,'vx1':vx_1,'vy1':vy_1,'vz1':vz_1,'ax1':ax_1,'ay1':ay_1,'az1':az_1,'jx1':jx_1,'jy1':jy_1,'jz1':jz_1,'x2':x_2,'y2':y_2,'z2':z_2,'vx2':vx_2,'vy2':vy_2,'vz2':vz_2,'ax2':ax_2,'ay2':ay_2,'az2':az_2,'jx2':jx_2,'jy2':jy_2,'jz2':jz_2})
	df_c = pd.DataFrame(df[cs:ce])
	df_r = df_c.reset_index(drop=True)
	df_r.to_csv(filename)
	print('write csv')

if __name__ == "__main__":
	path = '/Users/sprout/OneDrive - 名古屋工業大学/学校/研究室/実験/予備実験/第4回ゼミ用/fusion/fusion_20211112_1545.csv'
	data = pd.read_csv(path)
	main()