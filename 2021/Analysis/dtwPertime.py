import numpy as np
import pandas as pd

d_d = pd.read_excel('/Users/sprout/OneDrive - 名古屋工業大学/学校/研究室/実験/卒論実験/test/All_DTW.xlsx')
d_t = pd.read_excel('/Users/sprout/OneDrive - 名古屋工業大学/学校/研究室/実験/卒論実験/test/All_TIME.xlsx')

d_l = []

for i in range(len(d_d)):
	d = d_d['Score'][i]/d_t['Score'][i]
	d_l.append(d)

d_d['Score'] = d_l
d_d.to_excel('/Users/sprout/OneDrive - 名古屋工業大学/学校/研究室/code/Analysis/ExData/Performance/CutData/All_DTWperTIME.xlsx')