import pandas as pd

path = '/Users/sprout/OneDrive - 名古屋工業大学/学校/研究室/コード/data/fusion_20211018_1724.csv'
data = pd.read_csv(path)

column = input('列名を入力してください．-->')
print(column)

column_n = data.columns.get_loc(column)

print(column_n)