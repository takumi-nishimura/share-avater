import pandas as pd
import matplotlib.pyplot as plt

class GRAPH3D:
	def __init__(self) -> None:
		pass

	def main(self, start:float=0, end:float=99999, time:list=[], position_r:list=[], position_1:list=[], position_2:list=[]):
		self.start, self.end = self.search_time(time,start,end)
		self.make_3dGraph(self.start,self.end,position_r,position_1,position_2)

	def search_time(self, time, s, e):
		self.search_start = s
		self.search_end = e
		self.df_time = pd.DataFrame(data=time)
		self.s_flag = 0
		for self.s_row_counter in range(len(self.df_time)):
			if self.s_flag == 0:
				if self.search_start == round(self.df_time.at[self.df_time.index[self.s_row_counter], 'time'],1):
					self.start = self.s_row_counter
					print('start',self.start)
					print('start time',self.df_time.iloc[self.start,0])
					self.s_flag = 1
				elif self.s_row_counter == len(self.df_time)-1:
					print('Start not matched!!!')
					self.start = 0
					print('start time',self.df_time.iloc[self.start,0])
		for self.e_row_counter in range(len(self.df_time)):
			if self.search_end == round(self.df_time.at[self.df_time.index[self.e_row_counter], 'time'],1):
				self.end = self.e_row_counter
				print('end', self.end)
				print('end time', self.df_time.iloc[self.end,0])
				return self.start, self.end
			elif self.e_row_counter == len(self.df_time)-1:
				print('End not matched!!!')
				self.end = self.e_row_counter
				print('end', self.end)
				print('end time', self.df_time.iloc[self.end,0])
				return self.start, self.end

	def make_3dGraph(self, start, end, p_r, p_1, p_2):
		# self.make_list(p_r,p_1,p_2)
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

	def make_list(self, p_r, p_1, p_2):
		self.x = []
		self.y = []
		self.z = []
		self.x1 = []
		self.y1 = []
		self.z1 = []
		self.x2 = []
		self.y2 = []
		self.z2 = []
		for i in range(len(p_r)):
			self.x.append(p_r[i][0])
			self.y.append(p_r[i][1])
			self.z.append(p_r[i][2])
			self.x1.append(p_1[i][0])
			self.y1.append(p_1[i][1])
			self.z1.append(p_1[i][2])
			self.x2.append(p_2[i][0])
			self.y2.append(p_2[i][1])
			self.z2.append(p_2[i][2])