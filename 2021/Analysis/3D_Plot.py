from Figure.figure_manager import FIG
import numpy as np
import pandas as pd

path1 = '/Users/sprout/OneDrive - 名古屋工業大学/学校/研究室/code/Analysis/ExData/Motion/CutData/Cut_Hijikata_C_3_Participant1.csv'
path2 = '/Users/sprout/OneDrive - 名古屋工業大学/学校/研究室/code/Analysis/ExData/Motion/CutData/Cut_Hijikata_C_3_Participant2.csv'

d1 = pd.read_csv(path1)
d2 = pd.read_csv(path2)

figure = FIG()

figure.make_3dPlot(0,9999,d1,d2,d2)