import pandas as pd
import matplotlib.pyplot as plt
import os

path = '/Users/sprout/OneDrive - 名古屋工業大学/学校/研究室/実験/予備実験/第4回ゼミ用/fusion/20211112_tsuruoka_tanada_woFB_1.csv'
data = pd.read_csv(path)

search_start = 56
search_end = 69.5
if 'time' in data.columns:
	search_column = 'time'
elif 'Time' in data.columns:
	search_column = 'Time'
search_column_n = data.columns.get_loc(search_column)
s_flag = 0
for s_row_counter in range(len(data)):
	if s_flag == 0:
		if search_start == round(data.at[data.index[s_row_counter], search_column],1):
			start = s_row_counter
			print('start',start)
			print('start time',data.iloc[start,search_column_n])
			s_flag = 1
		elif s_row_counter == len(data)-1:
			print('Start not matched.')
			start = 0
			print('start time',data.iloc[start,search_column_n])
for e_row_counter in range(len(data)):
	if search_end == round(data.at[data.index[e_row_counter], search_column],1):
		end = e_row_counter
		print('end',end)
		print('end time',data.iloc[end,search_column_n])
		break
	elif e_row_counter == len(data)-1:
		print('End not matched.')
		end = e_row_counter
		print('end',end)
		print('end time',data.iloc[end,search_column_n])
		break

fig = plt.figure()
ax = plt.gca(projection='3d')

ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")

if 'time' in data.columns:
	time = data.loc[start:end,'time']

if 'Time' in data.columns:
	time  = data.loc[start:end,'Time']

if 'x' in data.columns:
	x = data.loc[start:end,'x']
	y = data.loc[start:end,'y']
	z = data.loc[start:end,'z']
	ax.plot(x,y,z,label='robot')

if 'X' in data.columns:
	x = data.loc[start:end,'X']
	y = data.loc[start:end,'Y']
	z = data.loc[start:end,'Z']
	ax.plot(x,y,z,label='robot')
	# sc = ax.scatter(x, y, z, c=time, alpha=0.3, cmap='jet')
	# fig.colorbar(sc)

if 'x1' in data.columns:
	x1 = data.loc[start:end,'x1']
	y1 = data.loc[start:end,'y1']
	z1 = data.loc[start:end,'z1']
	ax.plot(x1,y1,z1,label='op_A')

if 'x2' in data.columns:
	x2 = data.loc[start:end,'x2']
	y2 = data.loc[start:end,'y2']
	z2 = data.loc[start:end,'z2']
	ax.plot(x2,y2,z2,label='op_B')

ax.legend(loc="upper right",bbox_to_anchor=(1.1,1.1))
ax.set_box_aspect((1,1,1))
filename = os.path.splitext(os.path.basename(path))[0]
plt.title(filename)
plt.show()