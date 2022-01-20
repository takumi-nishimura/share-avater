import pandas as pd
import datetime
import os
from NASA_TLX import TLX
from minimal_self import MINIMALSELF
from mental_distance import MENTAL_DISTANCE
from subjective_evaluation import SUBJECTIVE_EVALUATION

def initial_data_set():
	# name = input('名前を入力してください--> '
	name = 'Tanada'
	job = input('FBを入力してください\nFB無し->A\n相手の速度->B\nロボットの速度->C\n--> ')
	number = input('サイクル数を入力してください--> ')
	print(name + 'さん , FB: ' + job + ', サイクル数: ' + number)
	return name, job, number

def write(path,data):
	df = pd.DataFrame(data.values(), index=data.keys()).T
	exportPath = path + 'questionnaire_' + '_' + name + '_' + job + '_' + number + '_' + datetime.datetime.now().strftime('%Y%m%d%H%M') + '.csv'
	df.to_csv(exportPath)
				
if __name__ == '__main__':
	name,job, number = initial_data_set()

	TLX_manager = TLX()
	MINIMALSELF_manager = MINIMALSELF()
	MENTALDISTANCE_manager = MENTAL_DISTANCE()
	SUBJECTIVEEVALUATION_manager = SUBJECTIVE_EVALUATION()

	r_tlx = TLX_manager.main()
	r_MS = MINIMALSELF_manager.main()
	r_MD = MENTALDISTANCE_manager.main()
	r_SE = SUBJECTIVEEVALUATION_manager.main()

	r_Q = r_tlx|r_MS|r_MD|r_SE
	write(os.path.join('questionnaire','q_data',''),r_Q)