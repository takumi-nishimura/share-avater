import matplotlib.pyplot as plt
import seaborn as sns
import Figure.matplotlib_style

class FIG_MEAN:
	def __init__(self) -> None:
		print('--- import --- : FIG_MEAN')

	def BoxPlot(self,df,x,y,hue:str='',filename:str=''):
		if hue:
			print('hue')
		self.ax = sns.boxplot(x=x,y=y,data=df)
		self.ax.legend([],['without feedback','partner velocity','robot velocity'])
		self.lg = plt.legend(loc='upper right', bbox_to_anchor=(0.95, 0.5, 0.5, .100), borderaxespad=0.,)
		plt.savefig(filename,dpi=300, format='jpg', bbox_extra_artists=(self.lg,), bbox_inches='tight')