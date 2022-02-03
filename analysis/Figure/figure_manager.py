# -----------------------------------------------------------------------
# Author:   Takumi Nishimura (Haptics Lab)
# Created:  2022/02/02
# Summary:  figure manager
# -----------------------------------------------------------------------

from cProfile import label
import matplotlib.pyplot as plt
import seaborn as sns
import Figure.matplotlib_style

class FIG:
	def __init__(self) -> None:
		print('--- import --- : FIG_MEAN')

	def MeanBoxPlot(self,df,ylabel:str='Questionnaire rating',filename:str='',min:float=999,max:float=999):
		sns.set_palette('Set2')
		self.ax = sns.boxplot(x='Condition', y='Score', data=df)
		plt.ylabel(ylabel,labelpad=8)
		plt.xlabel('Condition',labelpad=10)
		plt.subplots_adjust(left=0.15,bottom=0.15)
		if not min == 999 and not max == 999:
			plt.ylim(min,max)
		self.filename = 'Analysis/Figure/Questionnaire/' + filename + '.jpg'
		plt.savefig(self.filename, dpi=600, format='jpg')
		plt.close()

	def CycleBoxPlot(self,df,ylabel:str='Questionnaire rating',filename:str='',min:float=999,max:float=999):
		sns.set_palette('Set2')
		self.ax = sns.boxplot(x='Cycle', y='Score', hue='Condition',data=df)
		plt.ylabel(ylabel,labelpad=5)
		plt.xlabel('Cycle',labelpad=10)
		if not min == 999 and not max == 999:
			plt.ylim(min,max)
		self.lg = plt.legend(loc='upper right', bbox_to_anchor=(0.95, 0.5, 0.5, .100), borderaxespad=0.,)
		self.filename = 'Analysis/Figure/Questionnaire/' + filename + '.jpg'
		plt.savefig(self.filename, dpi=600, format='jpg', bbox_extra_artists=(self.lg,), bbox_inches='tight')
		plt.close()
