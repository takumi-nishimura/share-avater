# -----------------------------------------------------------------------
# Author:   Takumi Nishimura (Haptics Lab)
# Created:  2022/02/02
# Summary:  figure manager
# -----------------------------------------------------------------------

from cProfile import label
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import Figure.matplotlib_style

class FIG:
	def __init__(self) -> None:
		print('--- import --- : FIG')

	def MeanBoxPlot(self,df,dir:str='Questionnaire',ylabel:str='Questionnaire rating',filename:str='',min:float=999,max:float=999):
		sns.set_palette('Set2')
		self.ax = sns.boxplot(x='Condition', y='Score', data=df)
		plt.ylabel(ylabel,labelpad=8)
		plt.xlabel('Condition',labelpad=10)
		plt.subplots_adjust(left=0.15,bottom=0.15)
		if not min == 999 and not max == 999:
			plt.ylim(min,max)
		self.filename = 'Analysis/Figure/' + dir + '/' + filename + '.jpg'
		plt.savefig(self.filename, dpi=600, format='jpg')
		plt.close()

	def CycleBoxPlot(self,df,dir:str='Questionnaire',ylabel:str='Questionnaire rating',filename:str='',min:float=999,max:float=999):
		sns.set_palette('Set2')
		self.ax = sns.swarmplot(x='Cycle', y='Score', hue='Condition',data=df, dodge=True)
		plt.ylabel(ylabel,labelpad=5)
		plt.xlabel('Cycle',labelpad=10)
		if not min == 999 and not max == 999:
			plt.ylim(min,max)
		self.lg = plt.legend(loc='upper right', bbox_to_anchor=(0.95, 0.5, 0.5, .100), borderaxespad=0.,)
		self.filename = 'Analysis/Figure/' + dir + '/' + filename + '.jpg'
		plt.savefig(self.filename, dpi=600, format='jpg', bbox_extra_artists=(self.lg,), bbox_inches='tight')
		plt.close()

	def ScatterPlot(self,df,dir:str='Questionnaire',ylabel:str='Questionnaire rating',filename:str='',min:float=999,max:float=999):
		sns.set_palette('Set2')
		self.ax = sns.scatterplot(x='Time', y='Points',hue='Condition', data=df)
		plt.ylabel('Task points',labelpad=8)
		plt.xlabel('Task time [s]',labelpad=10)
		self.ax.legend([],['without feedback','partner velocity','robot velocity'])
		self.lg = plt.legend(loc='upper right', bbox_to_anchor=(0.93, 0.5, 0.5, .100), borderaxespad=0.,)
		plt.subplots_adjust(left=0.15,bottom=0.15)
		if not min == 999 and not max == 999:
			plt.ylim(min,max)
		self.filename = 'Analysis/Figure/' + dir + '/' + filename + '.jpg'
		plt.savefig(self.filename, dpi=600, format='jpg', bbox_extra_artists=(self.lg,), bbox_inches='tight')
		plt.close()

	def filt_setting(self,x,vy1,vy1_filt):
		dt_mean = np.mean(np.diff(x))
		fs_mean = round(1/dt_mean)
		fft_data = np.abs(np.fft.rfft(vy1))
		freqList = np.fft.rfftfreq(len(vy1), 1.0 / fs_mean)
		fft_data_filt = np.abs(np.fft.rfft(vy1_filt))
		freqList_filt = np.fft.rfftfreq(len(vy1_filt), 1.0 / fs_mean)
		plt.subplot(2,1,1)
		plt.loglog(freqList, 10 * np.log(fft_data))
		plt.subplot(2,1,2)
		plt.loglog(freqList_filt, 10 * np.log(fft_data_filt))
		plt.show()

	def subplot_graph(self,x,**y):
		cmap = plt.get_cmap("tab10")
		for n, k in enumerate(y.keys()):
			plt.subplot(len(y),1,n+1)
			plt.plot(x,y[k],label=k,color=cmap(n))
			plt.legend(bbox_to_anchor=(1, 1), loc='upper right', borderaxespad=0, fontsize=12)
		plt.show()

	def make_3dPlot(self,start,end,p_r,p_1,p_2):
		self.fig = plt.figure()
		self.ax = plt.gca(projection='3d')
		self.ax.set_xlabel("X-axis")
		self.ax.set_ylabel("Y-axis")
		self.ax.set_zlabel("Z-axis")
		self.ax.plot(p_r['x'][start:end],p_r['y'][start:end],p_r['z'][start:end],label='robot')
		self.ax.plot(p_1['x'][start:end],p_1['y'][start:end],p_1['z'][start:end],label='1')
		self.ax.plot(p_2['x'][start:end],p_2['y'][start:end],p_2['z'][start:end],label='2')
		self.ax.set_box_aspect((1,1,1))
		self.ax.legend(loc="upper right",bbox_to_anchor=(1.1,1.1))
		plt.show()