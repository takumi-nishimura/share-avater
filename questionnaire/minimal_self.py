import time
import datetime
import csv
import random
from tkinter import *

class MINIMALSELF:
	def __init__(self) -> None:
		self.q = [50] * 8

	def main(self):
		self.qa = self.MS()
		self.score = self.SCORE(self.qa)
		self.r = {'MS_q':self.qa,'MS_score':self.score}
		print(self.r)
		return self.r

	def initial_data_set(self):
		self.name = input('名前を入力してください--> ')
		self.job = input('FBを入力してください\nFB無し->A\n相手の速度->B\n相手との速度の差(小)->C\n相手との速度の差(大)->D\n相手の速度＋ロボット->E\n--> ')
		print(self.name+'さん , FB: '+self.job)
		return self.name,self.job

	def MS(self):
		self.root = Tk()
		self.root.title('Minimal Self')
		self.root.columnconfigure(0, weight=1)
		self.root.rowconfigure(0, weight=1)

		self.q1 = IntVar()
		self.q1.set(50)
		self.q2 = IntVar()
		self.q2.set(50)
		self.q3 = IntVar()
		self.q3.set(50)
		self.q4 = IntVar()
		self.q4.set(50)
		self.q5 = IntVar()
		self.q5.set(50)
		self.q6 = IntVar()
		self.q6.set(50)
		self.q7 = IntVar()
		self.q7.set(50)
		self.q8 = IntVar()
		self.q8.set(50)
		self.q9 = IntVar()
		self.q9.set(50)
		self.q10 = IntVar()
		self.q10.set(50)

		self.question = [[1,'ロボットアームが自分の腕のように感じた．'],\
			[2,'ロボットアームが物を掴んでいるのを見たとき，物をつかんでいるのは自分の手だと感じた．'],\
			[3,'本物の手がロボットになっているように感じた'],\
			[4,'腕が複数あるように感じた．'],\
			[5,'ロボットアームは，まるで自分の意思に従うかのように，思い通りに動いた．'],\
			[6,'ロボットアームの動きを自分でコントロールしているような感覚を覚えた．'],\
			[7,'ロボットアームの動きが自分の動きを制御しているように感じた．'],\
			[8,'ロボットアームには独自の意思があるように感じた．']]

		def p(n):
			self.q = [self.q1.get(),self.q2.get(),self.q3.get(),self.q4.get(),self.q5.get(),self.q6.get(),self.q7.get(),self.q8.get()]

		random.shuffle(self.question)

		self.l1 = Label(self.root,text=self.question[0][1])
		self.l1l = Label(self.root,text='全くそう思わない')
		self.l1r = Label(self.root,text='非常にそう思う')
		self.s1 = Scale(self.root, orient = 'h',
				from_ = 0, to = 100, variable = self.q1,
				command = p, showvalue=False)
		self.l2 = Label(self.root,text=self.question[1][1])
		self.l2l = Label(self.root,text='全くそう思わない')
		self.l2r = Label(self.root,text='非常にそう思う')
		self.s2 = Scale(self.root, orient = 'h',
				from_ = 0, to = 100, variable = self.q2,
				command = p, showvalue=False)
		self.l3 = Label(self.root,text=self.question[2][1])
		self.l3l = Label(self.root,text='全くそう思わない')
		self.l3r = Label(self.root,text='非常にそう思う')
		self.s3 = Scale(self.root, orient = 'h',
				from_ = 0, to = 100, variable = self.q3,
				command = p, showvalue=False)
		self.l4 = Label(self.root,text=self.question[3][1])
		self.l4l = Label(self.root,text='全くそう思わない')
		self.l4r = Label(self.root,text='非常にそう思う')
		self.s4 = Scale(self.root, orient = 'h',
				from_ = 0, to = 100, variable = self.q4,
				command = p, showvalue=False)
		self.l5 = Label(self.root,text=self.question[4][1])
		self.l5l = Label(self.root,text='全くそう思わない')
		self.l5r = Label(self.root,text='非常にそう思う')
		self.s5 = Scale(self.root, orient = 'h',
				from_ = 0, to = 100, variable = self.q5,
				command = p, showvalue=False)
		self.l6 = Label(self.root,text=self.question[5][1])
		self.l6l = Label(self.root,text='全くそう思わない')
		self.l6r = Label(self.root,text='非常にそう思う')
		self.s6 = Scale(self.root, orient = 'h',
				from_ = 0, to = 100, variable = self.q6,
				command = p, showvalue=False)
		self.l7 = Label(self.root,text=self.question[6][1])
		self.l7l = Label(self.root,text='全くそう思わない')
		self.l7r = Label(self.root,text='非常にそう思う')
		self.s7 = Scale(self.root, orient = 'h',
				from_ = 0, to = 100, variable = self.q7,
				command = p, showvalue=False)
		self.l8 = Label(self.root,text=self.question[7][1])
		self.l8l = Label(self.root,text='全くそう思わない')
		self.l8r = Label(self.root,text='非常にそう思う')
		self.s8 = Scale(self.root, orient = 'h',
				from_ = 0, to = 100, variable = self.q8,
				command = p, showvalue=False)

		self.button_e = Button(
			self.root,
			text='終了')

		def end():
			time.sleep(0.5)
			self.root.destroy()

		self.button_e.config(command=end)

		self.l1.grid(column=0,columnspan=2,row=0)
		self.l1l.grid(column=0,row=1,sticky=W)
		self.l1r.grid(column=1,row=1,sticky=E)
		self.s1.grid(column=0,columnspan=2,row=3,sticky=NE+NW+S)
		self.l2.grid(column=0,columnspan=2,row=4)
		self.l2l.grid(column=0,row=5,sticky=W)
		self.l2r.grid(column=1,row=5,sticky=E)
		self.s2.grid(column=0,columnspan=2,row=6,sticky=NE+NW+S)
		self.l3.grid(column=0,columnspan=2,row=7)
		self.l3l.grid(column=0,row=8,sticky=W)
		self.l3r.grid(column=1,row=8,sticky=E)
		self.s3.grid(column=0,columnspan=2,row=9,sticky=NE+NW+S)
		self.l4.grid(column=0,columnspan=2,row=10)
		self.l4l.grid(column=0,row=11,sticky=W)
		self.l4r.grid(column=1,row=11,sticky=E)
		self.s4.grid(column=0,columnspan=2,row=12,sticky=NE+NW+S)
		self.l5.grid(column=0,columnspan=2,row=13)
		self.l5l.grid(column=0,row=14,sticky=W)
		self.l5r.grid(column=1,row=14,sticky=E)
		self.s5.grid(column=0,columnspan=2,row=15,sticky=NE+NW+S)
		self.l6.grid(column=0,columnspan=2,row=16)
		self.l6l.grid(column=0,row=17,sticky=W)
		self.l6r.grid(column=1,row=17,sticky=E)
		self.s6.grid(column=0,columnspan=2,row=18,sticky=NE+NW+S)
		self.l7.grid(column=0,columnspan=2,row=19)
		self.l7l.grid(column=0,row=20,sticky=W)
		self.l7r.grid(column=1,row=20,sticky=E)
		self.s7.grid(column=0,columnspan=2,row=21,sticky=NE+NW+S)
		self.l8.grid(column=0,columnspan=2,row=22)
		self.l8l.grid(column=0,row=23,sticky=W)
		self.l8r.grid(column=1,row=23,sticky=E)
		self.s8.grid(column=0,columnspan=2,row=24,sticky=NE+NW+S)

		self.button_e.grid(column=0,columnspan=2,row=34,pady=10)

		self.root.mainloop()

		self.q_n = [self.question[0][0],self.question[1][0],self.question[2][0],self.question[3][0],self.question[4][0],self.question[5][0],self.question[6][0],self.question[7][0]]

		for i in range(len(self.q_n)):
			if self.q_n[i] == 1:
				self.q1a = self.q[i]
			elif self.q_n[i] == 2:
				self.q2a = self.q[i]
			elif self.q_n[i] == 3:
				self.q3a = self.q[i]
			elif self.q_n[i] == 4:
				self.q4a = self.q[i]
			elif self.q_n[i] == 5:
				self.q5a = self.q[i]
			elif self.q_n[i] == 6:
				self.q6a = self.q[i]
			elif self.q_n[i] == 7:
				self.q7a = self.q[i]
			elif self.q_n[i] == 8:
				self.q8a = self.q[i]
		self.qa = [self.q1a,self.q2a,self.q3a,self.q4a,self.q5a,self.q6a,self.q7a,self.q8a]

		return self.qa

	def SCORE(self,q):
		self.ownership = (q[0]+q[1])/2
		self.ownership_control = (q[2]+q[3])/2
		self.agency = (q[4]+q[5])/2
		self.agency_control = (q[6]+q[7])/2
		self.score = [self.ownership,self.ownership_control,self.agency,self.agency_control]
		return self.score

	def result(self,name,fb,q,score):
		self.now = datetime.datetime.now()
		self.path = '/Users/sprout/OneDrive - 名古屋工業大学/学校/研究室/CODE/questionnaire/'
		self.filename = self.path + 'MS_' + name + '_' + fb + '_' + self.now.strftime('%Y%m%d') + '.csv'
		self.f = open(self.filename,'w',newline='')
		self.writer = csv.writer(self.f,lineterminator='\n')
		self.writer.writerow(['w1','w2','w3','w4','w5','w6','w7','w8','ownership','ownership_control','agency','agency_control'])
		self.data = [q[0],q[1],q[2],q[3],q[4],q[5],q[6],q[7],score[0],score[1],score[2],score[3]]
		print(self.data)
		self.writer.writerow(self.data)
		self.f.close()