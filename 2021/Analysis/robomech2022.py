from turtle import pd
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import Figure.matplotlib_style

d = pd.read_excel('/Users/sprout/OneDrive - 名古屋工業大学/学校/研究室/tex/Robomech_2022/jerk_index.xlsx')
print(d)

sns.set_palette('Set2')
plt.subplots_adjust(left=0.15)
sns.barplot(x='Condition',y='Jerk index [-]',data=d)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('/Users/sprout/OneDrive - 名古屋工業大学/学校/研究室/tex/Robomech_2022/JerkIndex.jpg', dpi=600, format='jpg')
plt.close()

d = pd.read_excel('/Users/sprout/OneDrive - 名古屋工業大学/学校/研究室/tex/Robomech_2022/tasktime.xlsx')
print(d)

sns.set_palette('Set2')
plt.subplots_adjust(left=0.15)
sns.barplot(x='Condition',y='Task time [s]',data=d)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('/Users/sprout/OneDrive - 名古屋工業大学/学校/研究室/tex/Robomech_2022/TaskTime.jpg', dpi=600, format='jpg')
plt.close()

d = pd.read_excel('/Users/sprout/OneDrive - 名古屋工業大学/学校/研究室/tex/Robomech_2022/cot.xlsx')
print(d)

sns.set_palette('Set2')
plt.subplots_adjust(left=0.15)
sns.barplot(x='Condition',y='Diff time [s]',data=d)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('/Users/sprout/OneDrive - 名古屋工業大学/学校/研究室/tex/Robomech_2022/CoT.jpg', dpi=600, format='jpg')
plt.close()