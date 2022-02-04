# -----------------------------------------------------------------------
# Author:   Takumi Nishimura (Haptics Lab)
# Created:  2022/02/02
# Summary:  Motion analysis manager
# -----------------------------------------------------------------------

import os
import glob
import pandas as pd
import numpy as np
from Figure.figure_manager import FIG

class MOTIONAN_ALYSIS:
	def __init__(self) -> None:
		print('--- import --- : Motion Analysis')

		self.participant = []
		self.condition = []
		self.cycle = []
		self.evaluation = []
		self.data = []
		self.number = []

	def main(self):
		print('--- start --- : Motion Analysis')

		self.participant_l()

		for self.name in self.participant_list:
			for self.filename in self.files:
				if self.name in self.filename:
					self.read_df = pd.read_csv(self.filename)

		print('--- finish --- : Motion Analysis')

	def participant_l(self):
		self.file_list = []
		self.participant_list = []
		self.dir = os.path.join('analysis','ExData','Motion','RawData')
		self.files = sorted(glob.glob(os.path.join(self.dir, '*.csv')))

		for self.filename_s in self.files:
			self.filename_split = self.filename_s.split('_')
			self.participant_name = self.filename_split[0].split('/')[4]
			if self.participant_name in self.participant_list:
				pass
			else:
				self.participant_list.append(self.participant_name)

if __name__ in '__main__':
	motionAnalysis = MOTIONAN_ALYSIS()
	motionAnalysis.main()