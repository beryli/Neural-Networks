import tkinter as tk
import numpy as np
import pandas as pd
import sys
import os
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn.utils import shuffle
from random import seed
from random import random

# data=[]
# col = 0 # dimension
# row = 1 # number of input
# width = 0 # number of elemnet in a row of image
# row * col = number of element in data[]


def load(path):
	d =[]
	r = 1
	w = 0
	file=open(path,"r")
	line=file.readlines()
	file.close()
	for x in line:
		if x != "\n":
			w = len(x.split("\n")[0])
			for i in range(len(x.split("\n")[0])):
				if (x.split("\n")[0][i] == '1'):
					d.append(1)
				else:
					d.append(-1)
		else:
			r+=1
	d = np.array(d)
	d = np.reshape(d, (r, -1))
	c = d.shape[1]
	return d, r, c, w
	# load in data

def train(d, r, c):
	w = np.zeros((c, c))
	for i in range(r):
		w += np.dot(d[i][:, np.newaxis], d[i][:, np.newaxis].T)
	w = w/r
	for i in range(c):
		w[i][i] = 0
	# train weight
	t = np.zeros((c, 1))
	for i in range(c):
		t += w[i][:, np.newaxis]
	# train theta
	return w, t

def recall(d, r, w, t, epoch):
	for i in range(r):
		for j in range(epoch):
			output = (np.dot(w, d[i][:, np.newaxis])-t)
			for k in range(len(output)):
				output[k] = sign(output[k])
			if np.array_equal(output, d[i][:, np.newaxis]):
				break
			else:
				d[i][:, np.newaxis] = output
	return d

def noise(d, p):
	for i in range(len(d)):
		for j in range(len(d[i])):
			value = random()
			if value < p:
				d[i][j] = -1*d[i][j]
	return d

def image(d, row, width, col):
	title = ['Training data', 'Testing data', 'recall']
	d = d.reshape(col, row, -1, width)
	fig, ax = plt.subplots(nrows=1, ncols=col)

	count = 1
	for i in range(col):
		for j in range(row):
			fig.add_subplot(row, col, count)
			plt.imshow(d[i][j])
			plt.gca().axes.get_xaxis().set_visible(False)
			plt.gca().axes.get_yaxis().set_visible(False)
			count += 3
		count = count - row*3 + 1
		ax[i].set_xticks([])
		ax[i].set_yticks([])
		ax[i].spines['top'].set_visible(False)
		ax[i].spines['right'].set_visible(False)
		ax[i].spines['bottom'].set_visible(False)
		ax[i].spines['left'].set_visible(False)

	for ax, col in zip(ax, title):
		ax.set_title(col)
	plt.gcf().canvas.set_window_title('Result')
	plt.show()

def draw(d, w):
	for i in range(len(d)):
		for j in range(len(d[i])):
			if (d[i][j] == 1):
				print("% 2d" %(d[i][j]), end = "")
			else:
				print("  ", end = "")
			if ((j+1) % w == 0):
				print()
		print()

def sign(z):  
    if z > 0:
        return 1
    elif z < 0:
        return -1
    else:
    	return z



