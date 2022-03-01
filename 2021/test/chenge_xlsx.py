import pandas as pd

data = pd.read_excel('/Users/sprout/OneDrive - 名古屋工業大学/学校/研究室/code/test/3_Q4s.xlsx')

woFB = data[data['Condition']=='without feedback']['Score'].values
pv = data[data['Condition']=='partner velocity']['Score'].values
rv = data[data['Condition']=='robot velocity']['Score'].values

exdf = pd.DataFrame(data={'woFB':woFB,'pv':pv,'rv':rv})

exdf.to_excel('test/t_31_MD.xlsx')