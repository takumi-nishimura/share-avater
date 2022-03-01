from datetime import datetime
import random
import pandas as pd
import itertools

class random_condition:
	def __init__(self) -> None:
		self.condition_list = []
		self.condition = ['A','B','C']

	def export(self):
		self.p = list(itertools.permutations(self.condition))
		self.r = random.sample(self.p, 6)
		print(self.r)

if __name__ == '__main__':
	# randomcondition = random_condition()
	# randomcondition.export()

	print(random.sample(range(1,5), k=4))