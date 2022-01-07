import pandas as pd
import datetime
import os
from NASA_TLX import TLX
from minimal_self import MINIMALSELF
from mental_distance import MENTAL_DISTANCE

def initial_data_set():
	name = input('名前を入力してください--> ')
	job = input('FBを入力してください\nFB無し->A\n相手の速度->B\nロボットの速度->C\n相手の速度＋ロボットの速度->D\n--> ')
	print(name + 'さん , FB: ' + job)
	return name, job

def write(path,data):
	df = pd.DataFrame(data.values(), index=data.keys()).T
	exportPath = path + 'questionnaire_' + datetime.datetime.now().strftime('%Y%m%d%H%M') + '_' + name + '_' + job + '.csv'
	df.to_csv(exportPath)
				
if __name__ == '__main__':
	name,job = initial_data_set()

	TLX_manager = TLX()
	MINIMALSELF_manager = MINIMALSELF()
	MENTALDISTANCE_manager = MENTAL_DISTANCE()

	r_tlx = TLX_manager.main()
	r_MS = MINIMALSELF_manager.main()
	r_MD = MENTALDISTANCE_manager.main()

	r_Q = r_tlx|r_MS|r_MD
	write(os.path.join('questionnaire','q_data',''),r_Q)