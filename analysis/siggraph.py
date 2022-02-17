from Figure import matplotlib_style
import pandas as pd
import numpy as np
import statistics
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_excel('/Users/sprout/OneDrive - 名古屋工業大学/学校/研究室/code/Analysis/ExData/Questionnaire/CutData/SIGGRAPH Asia 2021 - Collaborative Avatar Platform for Collecting Human Expertise（回答）.xlsx')

sns.set_style()
sns.distplot(data.iloc[:,3].values,kde=False,bins=[1, 2, 3, 4, 5, 6, 7, 8])
print(statistics.median(data.iloc[:,3].values))
plt.xticks([1, 2, 3, 4, 5, 6, 7, 8])
plt.xlabel('Sense of body ownership')
plt.ylabel('Count')
plt.savefig('/Users/sprout/OneDrive - 名古屋工業大学/学校/研究室/code/Analysis/Figure/Questionnaire/siggraph_ownership')
plt.close()

sns.distplot(data.iloc[:,4].values,kde=False)
print(statistics.median(data.iloc[:,4].values))
plt.xticks([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
plt.xlabel('Sense of agency [%]')
plt.ylabel('Count')
plt.savefig('/Users/sprout/OneDrive - 名古屋工業大学/学校/研究室/code/Analysis/Figure/Questionnaire/siggraph_agency')
plt.close()

sns.distplot(data.iloc[:,5].values,kde=False,bins=[1, 2, 3, 4, 5, 6, 7, 8])
print(statistics.median(data.iloc[:,5].values))
plt.xticks([1, 2, 3, 4, 5, 6, 7, 8])
plt.xlabel('Task load')
plt.ylabel('Count')
plt.savefig('/Users/sprout/OneDrive - 名古屋工業大学/学校/研究室/code/Analysis/Figure/Questionnaire/siggraph_taskload')
plt.close()

sns.distplot(data.iloc[:,6].values,kde=False,bins=[1, 2, 3, 4, 5, 6, 7, 8])
print(statistics.median(data.iloc[:,6].values))
plt.xticks([1, 2, 3, 4, 5, 6, 7, 8])
plt.xlabel('Controllability')
plt.ylabel('Count')
plt.savefig('/Users/sprout/OneDrive - 名古屋工業大学/学校/研究室/code/Analysis/Figure/Questionnaire/siggraph_controllability')
plt.close()

sns.distplot(data.iloc[:,7].values,kde=False,bins=[1, 2, 3, 4, 5, 6, 7, 8])
print(statistics.median(data.iloc[:,7].values))
plt.xticks([1, 2, 3, 4, 5, 6, 7, 8])
plt.xlabel('Prefer to use')
plt.ylabel('Count')
plt.savefig('/Users/sprout/OneDrive - 名古屋工業大学/学校/研究室/code/Analysis/Figure/Questionnaire/siggraph_prefer')
plt.close()