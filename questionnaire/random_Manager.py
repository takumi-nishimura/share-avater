from datetime import datetime
import random
import pandas as pd
import datetime

class random_condition:
	def __init__(self) -> None:
		self.condition_list = []
		self.condition = ['A','B','C']

	def export(self):
		for i in range(3):
			self.r_list = random.sample(self.condition,len(self.condition))
			self.condition_list.append(self.r_list)
		print(self.condition_list)

if __name__ == '__main__':
	randomcondition = random_condition()
	randomcondition.export()

	print(random.sample(range(1,6), k=5))