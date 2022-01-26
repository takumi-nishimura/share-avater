import time
import datetime
import math
import itertools
import random
import csv
from tkinter import *

class TLX:
	def __init__(self) -> None:
		self.i = 0
		self.w1 = 0
		self.w2 = 0
		self.w3 = 0
		self.w4 = 0
		self.w5 = 0
		self.w6 = 0
		self.q = [0] * 6

	def main(self):
		# self.question = self.q_list()
		# self.itertools_question = self.itertools_make_question(self.question)
		# self.PCT(self.itertools_question)
		self.q = self.TLX()
		# self.wwl = self.WWL(self.w1,self.w2,self.w3,self.w4,self.w5,self.w6,self.q)
		self.awwl = self.AWWL(self.q)
		self.w_l = [self.w1,self.w2,self.w3,self.w4,self.w5,self.w6]
		# self.r = {'TLX_w':self.w_l,'TLX_q':self.q,'TLX_wwl':[self.wwl]}
		self.r = {'TLX_q':self.q,'TLX_awwl':[self.awwl]}
		print(self.r)
		return self.r

	def initial_data_set(self):
		self.name = input('名前を入力してください--> ')
		self.job = input('FBを入力してください\nFB無し->A\n相手の速度->B\n相手との速度の差(小)->C\n相手との速度の差(大)->D\n相手の速度＋ロボット->E\n--> ')
		print(self.name+'さん , FB: '+self.job)
		return self.name,self.job

	def q_list(self):
		self.question = [[1,"知的・知覚的要求"],[2,"身体的要求"],[3,"タイムプレッシャー"],[4,"作業成績"],[5,"努力"],[6,"フラストレーション"]]
		random.shuffle(self.question)
		return self.question

	def combinations_count(self,n,r):
		self.combinations = math.factorial(n)//(math.factorial(n-r)*math.factorial(r))
		return self.combinations

	def itertools_make_question(self,q):
		self.itertools_question = []
		for i in itertools.combinations(q,r=2):
			self.itertools_question.append(i)
		random.shuffle(self.itertools_question)
		return self.itertools_question

	def PCT(self,i_q):
		self.root = Tk()
		self.root.title('Button')
		self.root.columnconfigure(0, weight=1)
		self.root.columnconfigure(1, weight=1)
		self.root.rowconfigure(0, weight=1)

		self.label1 = Label(self.root,text='今行った作業についてお聞きします．\n下に示す２つの項目のうち，作業負荷・負担に関わりが強いと思う方をクリックしてください．',anchor=W)
		self.label1.grid(row=0, column=0, columnspan=2,pady=5)

		self.canvas1 = Canvas(self.root,height=50,bg='cyan')
		self.canvas1.grid(row=1,column=0)

		self.canvas2 = Canvas(self.root,height=50,bg='cyan')
		self.canvas2.grid(row=1,column=1)

		self.button_l = Button(
			self.root,
			text=i_q[self.i][0][1],
			font=('','15'),
			bg='sky blue',
			activebackground='light sky blue')
		self.button_l.grid(row=1, column=0,sticky=NE+NW+S)

		self.button_r = Button(
			self.root,
			text=i_q[self.i][1][1],
			font=('','15'),
			bg='sky blue',
			activebackground='light sky blue')
		self.button_r.grid(row=1, column=1,sticky=NE+NW+S)

		self.e1 = Label(
			self.root,
			text='-知的・知覚的要求-\nどの程度の知的・知覚的活動(考える，決める，計算する，記憶する，見るなど)を必要とするか．課題がやさしいか難しいか，単純か複雑か，正確さが求められるか大さっぱでよいか．')
		self.e1.grid(row=2,column=0,columnspan=2,pady=10)
		self.e2 = Label(
				self.root,
				text='-身体的要求-\nどの程度の身体的活動(押す，引く，回す，操作する等)を必要とするか．作業がラクかキツイか，ゆっくりできるかキビキビやらなければならないか．')
		self.e2.grid(row=3,column=0,columnspan=2,pady=5)
		self.e3 = Label(
				self.root,
				text='-タイムプレッシャー-\n仕事のペースや課題が発生する頻度のために感じる時間的切迫感がどの程度か．ペースはゆっくりとして余裕があるものか，それとも速くて余裕のないものか．')
		self.e3.grid(row=4,column=0,columnspan=2,pady=5)
		self.e4 = Label(
				self.root,
				text='-作業成績-\n作業指示者によって設定された課題の目標をどの程度達成できたと考えるか．目標の達成に関して自分の作業成績にどの程度満足しているか．')
		self.e4.grid(row=5,column=0,columnspan=2,pady=5)
		self.e5 = Label(
				self.root,
				text='-努力-\n作業成績のレベルを達成・維持するために，精神的・身体的にどの程度一生懸命に作業しなければならないか．')
		self.e5.grid(row=6,column=0,columnspan=2,pady=5)
		self.e6 = Label(
				self.root,
				text='-フラストレーション-\n作業中に，不安感，落胆，いらいら，ストレス，悩みをどの程度感じるか．あるいは逆に，安心感，満足感，充足感，楽しさ，リラックスをどの程度感じるか．')
		self.e6.grid(row=7,column=0,columnspan=2,pady=5)

		def counter_l():
			if i_q[self.i][0][0] == 1:
				self.w1 += 1
			elif i_q[self.i][0][0] == 2:
				self.w2 += 1
			elif i_q[self.i][0][0] == 3:
				self.w3 += 1
			elif i_q[self.i][0][0] == 4:
				self.w4 += 1
			elif i_q[self.i][0][0] == 5:
				self.w5 += 1
			elif i_q[self.i][0][0] == 6:
				self.w6 += 1
			self.i += 1
			if self.i == 15:
				time.sleep(1)
				self.root.destroy()
			else:
				self.button_l.config(text=i_q[self.i][0][1])
				self.button_r.config(text=i_q[self.i][1][1])

		def counter_r():
			if i_q[self.i][0][0] == 1:
				self.w1 += 1
			elif i_q[self.i][0][0] == 2:
				self.w2 += 1
			elif i_q[self.i][0][0] == 3:
				self.w3 += 1
			elif i_q[self.i][0][0] == 4:
				self.w4 += 1
			elif i_q[self.i][0][0] == 5:
				self.w5 += 1
			elif i_q[self.i][0][0] == 6:
				self.w6 += 1
			self.i += 1
			if self.i == 15:
				time.sleep(1)
				self.root.destroy()
			else:
				self.button_l.config(text=i_q[self.i][0][1])
				self.button_r.config(text=i_q[self.i][1][1])

		self.button_l.config(command=counter_l)
		self.button_r.config(command=counter_r)

		self.root.mainloop()


	def TLX(self):
		self.root = Tk()
		self.root.title('NASA TLX-Score')
		self.root.columnconfigure(0,weight=1)
		self.root.rowconfigure(0,weight=1)

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

		def p(n):
			self.q = [self.q1.get(),self.q2.get(),self.q3.get(),self.q4.get(),self.q5.get(),self.q6.get()]

		self.l1 = Label(self.root,text='-知的・知覚的要求-\nどの程度の知的・知覚的活動(考える，決める，記憶するなど)を必要としましたか．\n課題はやさしかったですか難しかったですか，単純でしたか複雑でしたか，正確さが求められましたか大雑把でよかったですか．')
		self.l1l = Label(self.root,text='低い')
		self.l1r = Label(self.root,text='高い')
		self.s1 = Scale(self.root, orient = 'h',
				from_ = 0, to = 100, variable = self.q1,
				command = p, showvalue=False)
		self.l2 = Label(self.root,text='-身体的要求-\nどの程度の身体的活動(押す，引く，回す，制御する，動き回るなど)を必要としましたか．\n作業はラクでしたかキツかったですか，ゆっくりできましたかキビキビやらなければなりませんでしたか，休み休みできましたか働きづめでしたか．')
		self.l2l = Label(self.root,text='低い')
		self.l2r = Label(self.root,text='高い')
		self.s2 = Scale(self.root, orient = 'h',
				from_ = 0, to = 100, variable = self.q2,
				command = p, showvalue=False)
		self.l3 = Label(self.root,text='-タイムプレッシャー-\n仕事のペースや課題が発生する頻度のために感じる時間的切迫感はどの程度でしたか．\nペースはゆっくりとして余裕があるものでしたか，それとも速くて余裕のないものでしたか．')
		self.l3l = Label(self.root,text='低い')
		self.l3r = Label(self.root,text='高い')
		self.s3 = Scale(self.root, orient = 'h',
				from_ = 0, to = 100, variable = self.q3,
				command = p, showvalue=False)
		self.l4 = Label(self.root,text='-作業成績-\n作業指示者によって設定された課題の目標をどの程度達成できたと思いますか．目標の達成に関して自分の作業成績にどの程度満足していますか．')
		self.l4l = Label(self.root,text='良い')
		self.l4r = Label(self.root,text='悪い')
		self.s4 = Scale(self.root, orient = 'h',
				from_ = 0, to = 100, variable = self.q4,
				command = p, showvalue=False)
		self.l5 = Label(self.root,text='-努力-\n作業成績のレベルを達成・維持するために，精神的・身体的にどの程度一生懸命に作業しなければなりませんでしたか．')
		self.l5l = Label(self.root,text='低い')
		self.l5r = Label(self.root,text='高い')
		self.s5 = Scale(self.root, orient = 'h',
				from_ = 0, to = 100, variable = self.q5,
				command = p, showvalue=False)
		self.l6 = Label(self.root,text='-フラストレーション-\n作業中に，不安感，落胆，いらいら，ストレス，悩みをどの程度感じましたか．あるいは逆に，安心感，満足感，充足感，楽しさ，リラックスをどの程度感じましたか．')
		self.l6l = Label(self.root,text='低い')
		self.l6r = Label(self.root,text='高い')
		self.s6 = Scale(self.root, orient = 'h',
				from_ = 0, to = 100, variable = self.q6,
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
		self.button_e.grid(column=0,columnspan=2,row=19,pady=10)

		self.root.mainloop()
		return self.q

	def WWL(self,w1,w2,w3,w4,w5,w6,q):
		self.wwl = (w1*q[0]+w2*q[1]+w3*q[2]+w4*q[3]+w5*q[4]+w6*q[5])/15
		return self.wwl

	def AWWL(self,q):
		self.dict_q = {'q1':q[0],'q2':q[1],'q3':q[2],'q4':q[3],'q5':q[4],'q6':q[5]}
		self.sort_q = sorted(self.dict_q.items(),key=lambda i: i[1])
		print(self.sort_q)
		self.awwl = self.sort_q[0][1]*1+self.sort_q[1][1]*2+self.sort_q[2][1]*3+self.sort_q[3][1]*4+self.sort_q[4][1]*5+self.sort_q[5][1]*6
		return self.awwl
	
	def result(self,name,job,w1,w2,w3,w4,w5,w6,q,wwl):
		self.now = datetime.datetime.now()
		self.path = '/Users/sprout/OneDrive - 名古屋工業大学/学校/研究室/CODE/questionnaire/'
		self.filename = self.path + 'PCT_TLX_' + name + '_' + job + '_' + self.now.strftime('%Y%m%d') + '.csv'
		self.f = open(self.filename,'w',newline='')
		self.writer = csv.writer(self.f,lineterminator='\n')
		self.writer.writerow(['w1','w2','w3','w4','w5','w6','q1','q2','q3','q4','q5','q6','wwl'])
		self.data = [w1,w2,w3,w4,w5,w6,q[0],q[1],q[2],q[3],q[4],q[5],wwl]
		self.writer.writerow(self.data)
		self.f.close()