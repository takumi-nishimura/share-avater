import time
import datetime
import math
import itertools
import random
import csv
from tkinter import *

def main():
	name,job = initial_data_set()

	question = q_list()
	itertools_question = itertools_make_question(question)
	
	PCT(itertools_question)
	q = TLX()
	print(q)

	wwl = WWL(w1,w2,w3,w4,w5,w6,q)

	result(name,job,q,wwl)

def initial_data_set():
	name = input('名前を入力してください--> ')
	job = input('FBを入力してください\nFB無し->A\n相手の速度->B\n相手との速度の差(小)->C\n相手との速度の差(大)->D\n相手の速度＋ロボット->E\n--> ')
	print(name+'さん , FB: '+job)
	return name,job

def q_list():
	question = [[1,"知的・知覚的要求"],[2,"身体的要求"],[3,"タイムプレッシャー"],[4,"作業成績"],[5,"努力"],[6,"フラストレーション"]]
	random.shuffle(question)
	return question

def combinations_count(n,r):
	combinations = math.factorial(n)//(math.factorial(n-r)*math.factorial(r))
	return combinations

def itertools_make_question(question):
	itertools_question = []
	for i in itertools.combinations(question,r=2):
		itertools_question.append(i)
	random.shuffle(itertools_question)
	return itertools_question

def PCT(itertools_question):
	root = Tk()
	root.title('Button')
	root.columnconfigure(0, weight=1)
	root.columnconfigure(1, weight=1)
	root.rowconfigure(0, weight=1)

	label1 = Label(
		root,
		text='今行った作業についてお聞きします．\n下に示す２つの項目のうち，作業負荷・負担に関わりが強いと思う方をクリックしてください．',
		anchor=W)
	label1.grid(row=0, column=0, columnspan=2,pady=5)

	canvas1 = Canvas(root,height=50,bg='cyan')
	canvas1.grid(row=1,column=0)

	canvas2 = Canvas(root,height=50,bg='cyan')
	canvas2.grid(row=1,column=1)

	button_l = Button(
			root,
			text=itertools_question[i][0][1],
			font=('','15'),
			bg='sky blue',
			activebackground='light sky blue')
	button_l.grid(row=1, column=0,sticky=NE+NW+S)

	button_r = Button(
			root,
			text=itertools_question[i][1][1],
			font=('','15'),
			bg='sky blue',
			activebackground='light sky blue')
	button_r.grid(row=1, column=1,sticky=NE+NW+S)
	e1 = Label(
			root,
			text='-知的・知覚的要求-\nどの程度の知的・知覚的活動(考える，決める，計算する，記憶する，見るなど)を必要とするか．課題がやさしいか難しいか，単純か複雑か，正確さが求められるか大さっぱでよいか．')
	e1.grid(row=2,column=0,columnspan=2,pady=10)
	e2 = Label(
			root,
			text='-身体的要求-\nどの程度の身体的活動(押す，引く，回す，操作する等)を必要とするか．作業がラクかキツイか，ゆっくりできるかキビキビやらなければならないか．')
	e2.grid(row=3,column=0,columnspan=2,pady=5)
	e3 = Label(
			root,
			text='-タイムプレッシャー-\n仕事のペースや課題が発生する頻度のために感じる時間的切迫感がどの程度か．ペースはゆっくりとして余裕があるものか，それとも速くて余裕のないものか．')
	e3.grid(row=4,column=0,columnspan=2,pady=5)
	e4 = Label(
			root,
			text='-作業成績-\n作業指示者によって設定された課題の目標をどの程度達成できたと考えるか．目標の達成に関して自分の作業成績にどの程度満足しているか．')
	e4.grid(row=5,column=0,columnspan=2,pady=5)
	e5 = Label(
			root,
			text='-努力-\n作業成績のレベルを達成・維持するために，精神的・身体的にどの程度一生懸命に作業しなければならないか．')
	e5.grid(row=6,column=0,columnspan=2,pady=5)
	e6 = Label(
			root,
			text='-フラストレーション-\n作業中に，不安感，落胆，いらいら，ストレス，悩みをどの程度感じるか．あるいは逆に，安心感，満足感，充足感，楽しさ，リラックスをどの程度感じるか．')
	e6.grid(row=7,column=0,columnspan=2,pady=5)

	def counter_l():
		global w1,w2,w3,w4,w5,w6,i
		if itertools_question[i][0][0] == 1:
			w1 += 1
		elif itertools_question[i][0][0] == 2:
			w2 += 1
		elif itertools_question[i][0][0] == 3:
			w3 += 1
		elif itertools_question[i][0][0] == 4:
			w4 += 1
		elif itertools_question[i][0][0] == 5:
			w5 += 1
		elif itertools_question[i][0][0] == 6:
			w6 += 1
		i += 1
		if i == 15:
			time.sleep(1)
			root.destroy()
		else:
			button_l.config(text=itertools_question[i][0][1])
			button_r.config(text=itertools_question[i][1][1])

	def counter_r():
		global w1,w2,w3,w4,w5,w6,i
		if itertools_question[i][1][0] == 1:
			w1 += 1
		elif itertools_question[i][1][0] == 2:
			w2 += 1
		elif itertools_question[i][1][0] == 3:
			w3 += 1
		elif itertools_question[i][1][0] == 4:
			w4 += 1
		elif itertools_question[i][1][0] == 5:
			w5 += 1
		elif itertools_question[i][1][0] == 6:
			w6 += 1
		i += 1
		if i == 15:
			time.sleep(1)
			root.destroy()
		else:
			button_l.config(text=itertools_question[i][0][1])
			button_r.config(text=itertools_question[i][1][1])

	button_l.config(command=counter_l)
	button_r.config(command=counter_r)

	root.mainloop()

	print(w1,w2,w3,w4,w5,w6)

def TLX():
	root = Tk()
	root.title('NASA TLX-Score')
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

	def p(n):
		global q
		q = [q1.get(),q2.get(),q3.get(),q4.get(),q5.get(),q6.get()]

	l1 = Label(root,text='-知的・知覚的要求-\nどの程度の知的・知覚的活動(考える，決める，記憶するなど)を必要としましたか．\n課題はやさしかったですか難しかったですか，単純でしたか複雑でしたか，正確さが求められましたか大雑把でよかったですか．')
	l1l = Label(root,text='低い')
	l1r = Label(root,text='高い')
	s1 = Scale(root, orient = 'h',
			from_ = 1, to = 100, variable = q1,
			command = p, showvalue=False)
	l2 = Label(root,text='-身体的要求-\nどの程度の身体的活動(押す，引く，回す，制御する，動き回るなど)を必要としましたか．\n作業はラクでしたかキツかったですか，ゆっくりできましたかキビキビやらなければなりませんでしたか，休み休みできましたか働きづめでしたか．')
	l2l = Label(root,text='低い')
	l2r = Label(root,text='高い')
	s2 = Scale(root, orient = 'h',
			from_ = 1, to = 100, variable = q2,
			command = p, showvalue=False)
	l3 = Label(root,text='-タイムプレッシャー-\n仕事のペースや課題が発生する頻度のために感じる時間的切迫感はどの程度でしたか．\nペースはゆっくりとして余裕があるものでしたか，それとも速くて余裕のないものでしたか．')
	l3l = Label(root,text='低い')
	l3r = Label(root,text='高い')
	s3 = Scale(root, orient = 'h',
			from_ = 1, to = 100, variable = q3,
			command = p, showvalue=False)
	l4 = Label(root,text='-作業成績-\n作業指示者によって設定された課題の目標をどの程度達成できたと思いますか．目標の達成に関して自分の作業成績にどの程度満足していますか．')
	l4l = Label(root,text='良い')
	l4r = Label(root,text='悪い')
	s4 = Scale(root, orient = 'h',
			from_ = 1, to = 100, variable = q4,
			command = p, showvalue=False)
	l5 = Label(root,text='-努力-\n作業成績のレベルを達成・維持するために，精神的・身体的にどの程度一生懸命に作業しなければなりませんでしたか．')
	l5l = Label(root,text='低い')
	l5r = Label(root,text='高い')
	s5 = Scale(root, orient = 'h',
			from_ = 1, to = 100, variable = q5,
			command = p, showvalue=False)
	l6 = Label(root,text='-フラストレーション-\n作業中に，不安感，落胆，いらいら，ストレス，悩みをどの程度感じましたか．あるいは逆に，安心感，満足感，充足感，楽しさ，リラックスをどの程度感じましたか．')
	l6l = Label(root,text='低い')
	l6r = Label(root,text='高い')
	s6 = Scale(root, orient = 'h',
			from_ = 1, to = 100, variable = q6,
			command = p, showvalue=False)

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
	button_e.grid(column=0,columnspan=2,row=19,pady=10)

	root.mainloop()
	return q

def WWL(w1,w2,w3,w4,w5,w6,q):
	wwl = (w1*q[0]+w2*q[1]+w3*q[2]+w4*q[3]+w5*q[4]+w6*q[5])/15
	print(wwl)
	return wwl

def result(name,job,q,wwl):
	now = datetime.datetime.now()
	path = '/Users/sprout/OneDrive - 名古屋工業大学/学校/研究室/実験/予備実験/第4回ゼミ用/'
	filename = path + 'PCT_TLX_' + name + '_' + job + '_' + now.strftime('%Y%m%d') + '.csv'
	f = open(filename,'w',newline='')
	writer = csv.writer(f,lineterminator='\n')
	writer.writerow(['w1','w2','w3','w4','w5','w6','q1','q2','q3','q4','q5','q6','wwl'])
	data = [w1,w2,w3,w4,w5,w6,q[0],q[1],q[2],q[3],q[4],q[5],wwl]
	writer.writerow(data)
	f.close()

if __name__ == "__main__":
	i = 0
	w1 = 0
	w2 = 0
	w3 = 0
	w4 = 0
	w5 = 0
	w6 = 0
	q = [0] * 6

	main()