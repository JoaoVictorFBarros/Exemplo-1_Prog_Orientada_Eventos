import tkinter as tk
import time as tm

# Referência: https://docs.python.org/3/library/tkinter.html

begining = tm.time()
running = True

#Funções 
def resetBegining (event):
	global begining
	begining = tm.time()
	update()

def run ():
	global running
	if running:
		running = False
	else:
		running = True
	control.config(text=upText())

def upText():
	if running:
		return "Stop"
	else:
		return "Start"	

def update ():
	global begining
	aux = int(tm.time() - begining)
	m = int(aux/60)
	s = int(aux%60)
	setText(m,s)

def setText(m,s):
	global begining

	ms = str(m)
	ss = str(s)

	if (m < 10):
		ms = "0" + ms
	if (s < 10):
		ss = "0" + ss

	if (running):
		displayText = ms + " : " + ss
		timer.config(text=displayText)
	else:
		begining = begining + 1

	timer.after(1000,update)

def addtime(event):
	global begining
	begining = begining - 10

backupm = -1
backups = -1

def readFile():
	global begining
	global backups
	global backupm
	f = open("exemplo.txt","r")

	if (f.readline() == "upd\n"):
		
		m = int(f.readline())
		s = int(f.readline())
		if (backupm != m or backups != s):
			begining = tm.time() - (60*m + s)
			backupm = m
			backups = s
			setText(m,s)
	f.close()
	window.after(1000,readFile)


#Inicio da execução

window = tk.Tk()

window.title("Exemplo Programação Orientada a eventos")
window.geometry("450x550")
window.configure(bg="#333333")

timer = tk.Label(window,text="00 : 00",font=("Helvetica",48),height=5,width=10)
timer.configure(bg="#bbbbbb")

timer.pack(pady=10)
timer.after(1000,update)

timer.bind("<Enter>", func=lambda e: timer.config(background="#4444ff"))  
timer.bind("<Leave>", func=lambda e: timer.config(background="#bbbbbb"))


control = tk.Button(window,text=upText(),height=5,width=20,command=run)
control.configure(bg="#666666",fg="#ffffff",font=40,bd=0,cursor="hand2")

control.bind("<Enter>", func=lambda e: control.config(background="#ff4444"))  
control.bind("<Leave>", func=lambda e: control.config(background="#666666"))

window.after(1000,readFile)

window.bind('<r>',resetBegining)
window.bind('<a>',addtime)

control.pack()

window.mainloop()