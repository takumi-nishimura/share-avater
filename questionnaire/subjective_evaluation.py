from tkinter import *
import time

class SUBJECTIVE_EVALUATION:
	def __init__(self) -> None:
		self.q = [0] * 5

	def main(self):
		self.se = self.SE()
		self.r = {'SE_r':self.se}
		print(self.r)
		return self.r

	def SE(self):
		self.root = Tk()
		self.root.title('Subjective Evaluation')
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

		def p(n):
			self.q = [self.q1.get(),self.q2.get(),self.q3.get(),self.q4.get(),self.q5.get()]

		self.l1 = Label(self.root,text='Q1. どれだけ操作しやすかったですか？')
		self.l1l = Label(self.root,text='低い')
		self.l1r = Label(self.root,text='高い')
		self.s1 = Scale(self.root, orient = 'h',
				from_ = 0, to = 100, variable = self.q1,
				command = p, showvalue=False)
		self.l2 = Label(self.root,text='Q2. 自分がどれだけ作業に貢献しましたか？')
		self.l2l = Label(self.root,text='低い')
		self.l2r = Label(self.root,text='高い')
		self.s2 = Scale(self.root, orient = 'h',
				from_ = 0, to = 100, variable = self.q2,
				command = p, showvalue=False)
		self.l3 = Label(self.root,text='Q3. 自分の運動がどれだけ反映されていましたか？')
		self.l3l = Label(self.root,text='0%')
		self.l3r = Label(self.root,text='100%')
		self.s3 = Scale(self.root, orient = 'h',
				from_ = 0, to = 100, variable = self.q3,
				command = p, showvalue=False)
		self.l4 = Label(self.root,text='Q4. 相手の動きをどれだけ理解できましたか？')
		self.l4l = Label(self.root,text='低い')
		self.l4r = Label(self.root,text='高い')
		self.s4 = Scale(self.root, orient = 'h',
				from_ = 0, to = 100, variable = self.q4,
				command = p, showvalue=False)
		self.l5 = Label(self.root,text='Q5. ロボットの動きをどれだけ理解できましたか？')
		self.l5l = Label(self.root,text='低い')
		self.l5r = Label(self.root,text='高い')
		self.s5 = Scale(self.root, orient = 'h',
				from_ = 0, to = 100, variable = self.q5,
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
		self.button_e.grid(column=0,columnspan=2,row=16,pady=10)

		self.root.mainloop()

		return self.q