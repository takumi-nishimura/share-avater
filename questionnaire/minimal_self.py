import time
import datetime
import csv
import random
from tkinter import *

def main():
	name,job = initial_data_set()

	qa = TLX()
	
	score = SCORE(qa)

	result(name,job,qa,score)

def initial_data_set():
	name = input('名前を入力してください--> ')
	job = input('FBを入力してください\nFB無し->A\n相手の速度->B\n相手との速度の差(小)->C\n相手との速度の差(大)->D\n相手の速度＋ロボット->E\n--> ')
	print(name+'さん , FB: '+job)
	return name,job

def TLX():
	root = Tk()
	root.title('Minimal Self')
	root.columnconfigure(0, weight=1)
	root.rowconfigure(0, weight=1)

	q1 = IntVar()
	q1.set(0)
	q2 = IntVar()
	q2.set(0)
	q3 = IntVar()
	q3.set(0)
	q4 = IntVar()
	q4.set(0)
	q5 = IntVar()
	q5.set(0)
	q6 = IntVar()
	q6.set(0)
	q7 = IntVar()
	q7.set(0)
	q8 = IntVar()
	q8.set(0)
	q9 = IntVar()
	q9.set(0)
	q10 = IntVar()
	q10.set(0)

	question = [[1,'ロボットアームが自分の腕のように感じた．'],\
			[2,'ロボットアームが物を掴んでいるのを見たとき，物をつかんでいるのは自分の手だと感じた．'],\
			[3,'本物の手がロボットになっているように感じた'],\
			[4,'腕が複数あるように感じた．'],\
			[5,'ロボットアームは，まるで自分の意思に従うかのように，思い通りに動いた．'],\
			[6,'ロボットアームの動きを自分でコントロールしているような感覚を覚えた．'],\
			[7,'ロボットアームの動きが自分の動きを制御しているように感じた．'],\
			[8,'ロボットアームには独自の意思があるように感じた．']]

	def p(n):
		global q
		q = [q1.get(),q2.get(),q3.get(),q4.get(),q5.get(),q6.get(),q7.get(),q8.get()]

	random.shuffle(question)
	# print(question)
	
	l1 = Label(root,text=question[0][1])
	l1l = Label(root,text='全くそう思わない')
	l1r = Label(root,text='非常にそう思う')
	s1 = Scale(root, orient = 'h',
			from_ = 1, to = 100, variable = q1,
			command = p, showvalue=False)
	l2 = Label(root,text=question[1][1])
	l2l = Label(root,text='全くそう思わない')
	l2r = Label(root,text='非常にそう思う')
	s2 = Scale(root, orient = 'h',
			from_ = 1, to = 100, variable = q2,
			command = p, showvalue=False)
	l3 = Label(root,text=question[2][1])
	l3l = Label(root,text='全くそう思わない')
	l3r = Label(root,text='非常にそう思う')
	s3 = Scale(root, orient = 'h',
			from_ = 1, to = 100, variable = q3,
			command = p, showvalue=False)
	l4 = Label(root,text=question[3][1])
	l4l = Label(root,text='全くそう思わない')
	l4r = Label(root,text='非常にそう思う')
	s4 = Scale(root, orient = 'h',
			from_ = 1, to = 100, variable = q4,
			command = p, showvalue=False)
	l5 = Label(root,text=question[4][1])
	l5l = Label(root,text='全くそう思わない')
	l5r = Label(root,text='非常にそう思う')
	s5 = Scale(root, orient = 'h',
			from_ = 1, to = 100, variable = q5,
			command = p, showvalue=False)
	l6 = Label(root,text=question[5][1])
	l6l = Label(root,text='全くそう思わない')
	l6r = Label(root,text='非常にそう思う')
	s6 = Scale(root, orient = 'h',
			from_ = 1, to = 100, variable = q6,
			command = p, showvalue=False)
	l7 = Label(root,text=question[6][1])
	l7l = Label(root,text='全くそう思わない')
	l7r = Label(root,text='非常にそう思う')
	s7 = Scale(root, orient = 'h',
			from_ = 1, to = 100, variable = q7,
			command = p, showvalue=False)
	l8 = Label(root,text=question[7][1])
	l8l = Label(root,text='全くそう思わない')
	l8r = Label(root,text='非常にそう思う')
	s8 = Scale(root, orient = 'h',
			from_ = 1, to = 100, variable = q8,
			command = p, showvalue=False)
	# l9 = Label(root,text=question[7])
	# l9l = Label(root,text='全くそう思わない')
	# l9r = Label(root,text='非常にそう思う')
	# s9 = Scale(root, orient = 'h',
	# 		from_ = 1, to = 100, variable = q9,
	# 		command = p, showvalue=False)
	# l10 = Label(root,text=question[8])
	# l10l = Label(root,text='全くそう思わない')
	# l10r = Label(root,text='非常にそう思う')
	# s10 = Scale(root, orient = 'h',
	# 		from_ = 1, to = 100, variable = q10,
	# 		command = p, showvalue=False)

	button_e = Button(
			root,
			text='終了')
	def end():
		time.sleep(0.5)
		root.destroy()
	button_e.config(command=end)

	l1.grid(column=0,columnspan=2,row=0)
	l1l.grid(column=0,row=1,sticky=W)
	l1r.grid(column=1,row=1,sticky=E)
	s1.grid(column=0,columnspan=2,row=3,sticky=NE+NW+S)
	l2.grid(column=0,columnspan=2,row=4)
	l2l.grid(column=0,row=5,sticky=W)
	l2r.grid(column=1,row=5,sticky=E)
	s2.grid(column=0,columnspan=2,row=6,sticky=NE+NW+S)
	l3.grid(column=0,columnspan=2,row=7)
	l3l.grid(column=0,row=8,sticky=W)
	l3r.grid(column=1,row=8,sticky=E)
	s3.grid(column=0,columnspan=2,row=9,sticky=NE+NW+S)
	l4.grid(column=0,columnspan=2,row=10)
	l4l.grid(column=0,row=11,sticky=W)
	l4r.grid(column=1,row=11,sticky=E)
	s4.grid(column=0,columnspan=2,row=12,sticky=NE+NW+S)
	l5.grid(column=0,columnspan=2,row=13)
	l5l.grid(column=0,row=14,sticky=W)
	l5r.grid(column=1,row=14,sticky=E)
	s5.grid(column=0,columnspan=2,row=15,sticky=NE+NW+S)
	l6.grid(column=0,columnspan=2,row=16)
	l6l.grid(column=0,row=17,sticky=W)
	l6r.grid(column=1,row=17,sticky=E)
	s6.grid(column=0,columnspan=2,row=18,sticky=NE+NW+S)
	l7.grid(column=0,columnspan=2,row=19)
	l7l.grid(column=0,row=20,sticky=W)
	l7r.grid(column=1,row=20,sticky=E)
	s7.grid(column=0,columnspan=2,row=21,sticky=NE+NW+S)
	l8.grid(column=0,columnspan=2,row=22)
	l8l.grid(column=0,row=23,sticky=W)
	l8r.grid(column=1,row=23,sticky=E)
	s8.grid(column=0,columnspan=2,row=24,sticky=NE+NW+S)
	# l9.grid(column=0,columnspan=2,row=25)
	# l9l.grid(column=0,row=26,sticky=W)
	# l9r.grid(column=1,row=26,sticky=E)
	# s9.grid(column=0,columnspan=2,row=27,sticky=NE+NW+S)
	# l10.grid(column=0,columnspan=2,row=28)
	# l10l.grid(column=0,row=29,sticky=W)
	# l10r.grid(column=1,row=29,sticky=E)
	# s10.grid(column=0,columnspan=2,row=30,sticky=NE+NW+S)
	button_e.grid(column=0,columnspan=2,row=34,pady=10)

	root.mainloop()

	q_n = [question[0][0],question[1][0],question[2][0],question[3][0],question[4][0],question[5][0],question[6][0],question[7][0]]
	# print('q_n',q_n)
	for i in range(len(q_n)):
		if q_n[i] == 1:
			q1a = q[i]
		elif q_n[i] == 2:
			q2a = q[i]
		elif q_n[i] == 3:
			q3a = q[i]
		elif q_n[i] == 4:
			q4a = q[i]
		elif q_n[i] == 5:
			q5a = q[i]
		elif q_n[i] == 6:
			q6a = q[i]
		elif q_n[i] == 7:
			q7a = q[i]
		elif q_n[i] == 8:
			q8a = q[i]
	qa = [q1a,q2a,q3a,q4a,q5a,q6a,q7a,q8a]

	return qa

def SCORE(q):
	ownership = (q[0]+q[1])/2
	ownership_control = (q[2]+q[3])/2
	agency = (q[4]+q[5])/2
	agency_control = (q[6]+q[7])/2
	score = [ownership,ownership_control,agency,agency_control]
	return score

def result(name,fb,q,score):
	now = datetime.datetime.now()
	path = '/Users/sprout/OneDrive - 名古屋工業大学/学校/研究室/実験/予備実験/第4回ゼミ用/'
	filename = path + 'MS_' + name + '_' + fb + '_' + now.strftime('%Y%m%d') + '.csv'
	f = open(filename,'w',newline='')
	writer = csv.writer(f,lineterminator='\n')
	writer.writerow(['w1','w2','w3','w4','w5','w6','w7','w8','ownership','ownership_control','agency','agency_control'])
	data = [q[0],q[1],q[2],q[3],q[4],q[5],q[6],q[7],score[0],score[1],score[2],score[3]]
	print(data)
	writer.writerow(data)
	f.close()

if __name__ == '__main__':
	q = [0] * 8

	main()