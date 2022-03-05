from tkinter import *
from PIL import Image,ImageTk
import time
import os

class MENTAL_DISTANCE:
	def __init__(self) -> None:
		self.value = 1
	
	def main(self):
		self.md = self.MD()
		self.r = {'MD_r':[self.md]}
		print(self.r)
		return self.r

	def MD(self):
		self.root = Tk()
		self.root.title('Mental Distance')
		self.root.geometry('1200x550')

		self.image = Image.open(os.path.join('2021','questionnaire','we-mode.png'))
		self.w_size = int(self.image.width/4)
		self.h_size = int(self.image.height/4)

		self.canvas = Canvas(width=self.w_size, height=self.h_size)
		self.tk_image = ImageTk.PhotoImage(image=self.image.resize((self.w_size,self.h_size)))
		self.canvas.create_image(10, 0, anchor=NW, image=self.tk_image)

		self.radio_value = IntVar(value = 1)

		self.radio1 = Radiobutton(self.root, 
						text = "1",
						command = self.radio_click,
						variable = self.radio_value,
						value = 1)
		self.radio2 = Radiobutton(self.root, 
						text = "2",
						command = self.radio_click,
						variable = self.radio_value,
						value = 2)
		self.radio3 = Radiobutton(self.root, 
						text = "3",
						command = self.radio_click,
						variable = self.radio_value,
						value = 3)
		self.radio4 = Radiobutton(self.root, 
						text = "4",
						command = self.radio_click,
						variable = self.radio_value,
						value = 4)
		self.radio5 = Radiobutton(self.root, 
						text = "5",
						command = self.radio_click,
						variable = self.radio_value,
						value = 5)
		self.radio6 = Radiobutton(self.root, 
						text = "6",
						command = self.radio_click,
						variable = self.radio_value,
						value = 6)
		self.radio7 = Radiobutton(self.root, 
						text = "7",
						command = self.radio_click,
						variable = self.radio_value,
						value = 7)

		self.button_e = Button(
			self.root,
			text='終了')

		def end():
			time.sleep(0.5)
			self.root.destroy()

		self.button_e.config(command=end)
		self.button_e.place(x=600,y=510)

		self.canvas.pack()
		self.radio1.pack()
		self.radio2.pack()
		self.radio3.pack()
		self.radio4.pack()
		self.radio5.pack()
		self.radio6.pack()
		self.radio7.pack()
		self.r_p = 450
		self.radio1.place(x=self.r_p,y=480)
		self.radio2.place(x=self.r_p+50,y=480)
		self.radio3.place(x=self.r_p+100,y=480)
		self.radio4.place(x=self.r_p+150,y=480)
		self.radio5.place(x=self.r_p+200,y=480)
		self.radio6.place(x=self.r_p+250,y=480)
		self.radio7.place(x=self.r_p+300,y=480)
		self.root.mainloop()

		return self.value

	def radio_click(self):
			self.value = self.radio_value.get()