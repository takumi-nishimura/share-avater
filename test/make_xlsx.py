import pandas as pd

def make(path,filename,sheetname:int=0):
	condition_list = ['A','B','C']
	d = []
	condition = []
	data = pd.read_excel(path,sheet_name =sheetname)
	for i,j in enumerate(condition_list):
		for k in range(len(data.iloc[i,1:].values)):
			d.append(data.iloc[i,1:].values[k])
			condition.append(j)
	df = pd.DataFrame({'condition':condition,'data':d})
	export_name = '/Users/sprout/OneDrive - 名古屋工業大学/学校/研究室/実験/卒論実験/test/' + filename + '.xlsx'
	df.to_excel(export_name)
	print('finish   :   ' + filename)

tlx = make('/Users/sprout/OneDrive - 名古屋工業大学/学校/研究室/実験/卒論実験/q_calculate/TLX_AWWL.xlsx','t_tlx')
md = make('/Users/sprout/OneDrive - 名古屋工業大学/学校/研究室/実験/卒論実験/q_calculate/MD_SCORE.xlsx','t_md')
dtw = make('/Users/sprout/OneDrive - 名古屋工業大学/学校/研究室/実験/卒論実験/m_calculate/DTW_SCORE.xlsx','t_dtw')
jrk = make('/Users/sprout/OneDrive - 名古屋工業大学/学校/研究室/実験/卒論実験/m_calculate/JRK_SCORE.xlsx','t_jrk')
time = make('/Users/sprout/OneDrive - 名古屋工業大学/学校/研究室/実験/卒論実験/m_calculate/TASK_TIME.xlsx','t_time')
point = make('/Users/sprout/OneDrive - 名古屋工業大学/学校/研究室/実験/卒論実験/m_calculate/TASK_TIME.xlsx','t_point',sheetname=1)