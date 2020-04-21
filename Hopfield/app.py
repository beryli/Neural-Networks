import hopfield as hf
import tkinter as tk
import tkinter.ttk as ttk
import numpy as np
import pandas as pd
import sys
import os
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn.utils import shuffle

def leftbtn():
	path_train = "Hopfield/"+cb.get()+"_Training.txt"
	path_test  = "Hopfield/"+cb.get()+"_Testing.txt"
	data, row, col, width = hf.load(path_train)
	wgt, theta = hf.train(data, row, col)
	output = data
	# load traing data, and train
	data, row, col, width  = hf.load(path_test)
	output = np.append(output, data)
	data = hf.recall(data, row, wgt, theta, int(var1.get()))
	# load traing data, and recall
	output = np.append(output, data)
	hf.image(output, row, width, 3)
	# show reault

def righttbn():
	path_train = "Hopfield/"+cb.get()+"_Training.txt"
	path_test  = "Hopfield/"+cb.get()+"_Testing.txt"
	data, row, col, width = hf.load(path_train)
	wgt, theta = hf.train(data, row, col)
	output = data
	# load traing data, and train
	data, row, col, width  = hf.load(path_train)
	data = hf.noise(data, float(var2.get()))
	output = np.append(output, data)
	data = hf.recall(data, row, wgt, theta, int(var1.get()))
	# load traing data, and recall
	output = np.append(output, data)
	hf.image(output, row, width, 3)
	# show reault



box=["Basic", "Bonus"]
text_font = ('Helvetica', '20', 'bold')
# variable

window = tk.Tk()
window.title('Neural Networks_HW3_Hopfield')
window.geometry('660x300')
window.configure(background='#364862')

top_frame = tk.Frame(window)
top_frame.pack(pady=(20, 0))
top_frame.configure(background='#364862')

style = ttk.Style()
style.configure("TLabel", foreground="#FFFFFF", background = '#364862')

l1 = ttk.Label(top_frame, text="Select", font=text_font)
l1.grid(row=0, column=0, padx=20, pady=10)

cb = ttk.Combobox(top_frame, justify="center", state="readonly"
	, values=box, width=20, font=text_font)
window.option_add('*TCombobox*Listbox.font', text_font)
cb.current(0)
cb.grid(row=0, column=1, padx=20, pady=10)
# print(cb.current(), cb.get())

l2 = ttk.Label(top_frame, text="Epoch", font=text_font)
l2.grid(row=1, column=0, padx=20, pady=10)

var1=tk.StringVar()
var1.set(3)
l3 = tk.Entry(top_frame, justify="center", textvariable=var1
	, width=21, font=text_font)
l3.grid(row=1, column=1, padx=20, pady=10)


l4 = ttk.Label(top_frame, text="Noise", font=text_font)
l4.grid(row=2, column=0, padx=20, pady=10)

var2=tk.StringVar()
var2.set(0.1)
l5 = tk.Entry(top_frame, justify="center", textvariable=var2
	, width=21, font=text_font)
l5.grid(row=2, column=1, padx=20, pady=10)
# window, top_frame, l1, l2, l3, cb, l4, l5

btn_frame = tk.Frame(window)
btn_frame.pack(pady=20)
btn_frame.configure(background='#364862')
btn1 = tk.Button(btn_frame, text='directly', activebackground='#2887D8', activeforeground='#FFFFFF'
	, font=text_font, width=12, height=1, command=leftbtn, bg='#5BBAFA', fg='#FFFFFF')
btn1.grid(row=0, column=0, padx=20)

btn2 = tk.Button(btn_frame, text='with noise', activebackground='#C0910D', activeforeground='#FFFFFF'
	, font=text_font, width=12, height=1, command=righttbn, bg='#F2C40F', fg='#FFFFFF')
btn2.grid(row=0, column=1, padx=20)
# btn_frame, btn1, btn2

window.mainloop()
