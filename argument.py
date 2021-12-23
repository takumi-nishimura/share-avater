import time

class Graph_2D:
	def __init__(self,n=1) -> None:
		self.x_list = []
		self.y_list = [[] for _ in range(n)]
	def make_list(self,x,*y):
		self.x_list.append(x)
		for i in range(len(y)):
				self.y_list[i].append(y[i])
		return self.x_list,self.y_list
	def soloy_graph(self):
		import matplotlib.pyplot as plt
		for i in range(len(self.y_list)):
			plt.plot(self.x_list,self.y_list[i])
		plt.show()

if __name__ == '__main__':
	Graph2DManager = Graph_2D(n=4)
	t_flag = 0
	try:
		while True:
			if t_flag == 0:
				start = time.perf_counter()
				t_flag = 1
			elif t_flag == 1:
				past_time = time.perf_counter()-start
				y1 = 2*past_time
				y2 = pow(past_time,2)
				y3 = pow(past_time,3)
				y4 = pow(past_time,4)
				print(past_time)
				Graph2DManager.make_list(past_time,y1,y2,y3,y4)
	except KeyboardInterrupt:
		print('stop')
		Graph2DManager.soloy_graph()
		