import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy import signal
import os
from statistics import mean
from scipy import fftpack

def main():
	start,end,column = read(data,'time',0,10000.0)
	x,y1,y2,y3,y4,y5,y6 = get_data(start,end,column,'x','y','z','z','z','z')
	dt_mean = np.mean(np.diff(x))
	fs_mean = round(1/dt_mean)
	y1_filt = lowpass(y1,0.4,5)
	y2_filt = lowpass(y2,0.4,5)
	y3_filt = lowpass(y3,0.4,5)
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
	fft_data = np.abs(np.fft.rfft(y1))
	freqList = np.fft.rfftfreq(len(y1), 1.0 / fs_mean)
	fft_data_filt = np.abs(np.fft.rfft(y1_filt))
	freqList_filt = np.fft.rfftfreq(len(y1_filt), 1.0 / fs_mean)
	# fft_data_a1 = np.abs(np.fft.rfft(a1))
	# freqList_a1 = np.fft.rfftfreq(len(a1), 1.0 / fs_mean)
	# fft_data_j1 = np.abs(np.fft.rfft(j1))
	# freqList_j1 = np.fft.rfftfreq(len(j1), 1.0 / fs_mean)
	# y4 = np.rad2deg(y4)
	# y5 = np.rad2deg(y5)
	fb_vel_r = y1+y4*0.8
	fb_vel_1 = y2+y5*0.8
	fb_vel_2 = y3+y6*0.8
	data_out_1 = fb_vel_1
	data_out_2 = fb_vel_2
	mean_jrk(jy1,jy2,jy3)
	# solox_log_graph(freqList,fft_data,freqList_filt,fft_data_filt)
	# solox_graph(x,y3,'z',vy3,'vz',vy3,'az',jy3,'jz')
	# solox_graph(x,y3,'data_out_1',y4,'data_out_2',y5,'data_out_3',y6,'data_out_4')
	# twinx_graph(x,v1,'v1',a1,'a1',y1,'j1',y1,'x')

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

def get_data(start,end,column,c1,c2,c3,c4,c5,c6):
	x = data.loc[start:end,column]
	y1 = data.loc[start:end,c1]
	y2 = data.loc[start:end,c2]
	y3 = data.loc[start:end,c3]
	y4 = data.loc[start:end,c4]
	y5 = data.loc[start:end,c5]
	y6 = data.loc[start:end,c6]
	x = x.reset_index(drop=True)
	y1 = y1.reset_index(drop=True)
	y2 = y2.reset_index(drop=True)
	y3 = y3.reset_index(drop=True)
	y4 = y4.reset_index(drop=True)
	y5 = y5.reset_index(drop=True)
	y6 = y6.reset_index(drop=True)
	return x,y1,y2,y3,y4,y5,y6

def getSpeed(t,g1):
	# get = pd.DataFrame(list(zip(t,g1)))
	# diff = get.diff()
	# speed = diff[1]/diff[0]
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

def mean_jrk(jx,jy,jz):
	jrk_norm_list = []
	for i in range(len(jx)):
		jrk_list = np.array([jx[i],jy[i],jz[i]])
		jrk_norm = np.linalg.norm(jrk_list)
		jrk_norm_list.append(jrk_norm)
	jrk_mean = mean(jrk_norm_list)
	print(jrk_mean)
	return(jrk_norm_list)

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
	filename = os.path.splitext(os.path.basename(path))[0]
	plt.title(filename)
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

if __name__ == "__main__":
	# path = '/Users/sprout/OneDrive - 名古屋工業大学/学校/研究室/実験/予備実験/第4回ゼミ用/fusion/fusion_20211112_1545.csv'
	path = '/Users/sprout/OneDrive - 名古屋工業大学/学校/研究室/実験/予備実験/第4回ゼミ用/fusion/20211112_tsuruoka_tanada_partner+robot_5.csv'
	data = pd.read_csv(path)
	main()