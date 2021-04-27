#By Rameez Mughal
#this program displays how a fourier series better approximates a square wave with an increasing number of terms

#math and graphical tools
import matplotlib.pyplot as plt
import numpy as np
from fractions import Fraction
from scipy import signal
import scipy.integrate as integrate
import scipy.special as special
import tkinter as tk
from tkinter import *

#Here I define the basic square wave and sine wave I use
defaultSquareWave="1+signal.square(x)"
defaultSineWave="np.sin(x)+1"

#genPlot plots a given function on the interval [0,20] with substeps of 0.001
def genPlot(function,domain=np.arange(0.0,20.0,0.001)):
	x=np.array(domain)
	y=eval(function)#parses string containing polynomial and turns it into a useable format
	plt.plot(x,y)
	plt.show(block=False)

#Generates a series based on the default square wave with a given amount of terms	
def genSeries(terms):
	series="1"#initial value in series or a sub 0
	count = int(float(terms))
	#for loop runs for count*2 because only odd values of n are part of the series
	for n in range(1,count*2):
		if n%2 is not 0 or n is 0:
			series = series+"+"+"((4/("+str(n)+"*np.pi))*np.sin("+str(n)+"*"+"x))"
			#nth term of series is hardcoded here. It's only applicable to the default square wave
	return series

#used to refresh or change the visible graphs
def updatePlot(function,terms):
	if terms is 0:
		plt.clf()
		genPlot(function)
	else:
		plt.clf()
		genPlot(genSeries(terms))
		temp=genSeries(terms)
		genPlot(defaultSquareWave)

#function called to get value from entry box
def getTerms():
	r=terms_entry.get()
	updatePlot(defaultSquareWave,r)
	window.update()

#completely clears the graph	
def clearGraph():
	plt.clf()
	plt.show()

#opens initial graph window
genPlot(function=defaultSquareWave)

#Opens control interface
#nothing here is relevant to generating the fourier series, it's all graphical stuff
window=tk.Tk()
window.title("Fourier Series")
controlWindow = tk.Frame(window)
controlWindow.grid(column=0, row=0,sticky=('N','W','E','S'))
controlWindow.columnconfigure(0, weight=1)
controlWindow.rowconfigure(0, weight=1)
terms_entry = tk.Entry(controlWindow,width=7)
terms_entry.grid(column=2, row=1, sticky=(W,E))
terms_entry.insert(END,'0')#sets default terms number to zero
tk.Label(controlWindow,text="Number of Terms").grid(column=1,row=1,sticky=(W,E))
#commands marked with lambda don't run upon the window opening and only activate when the button is pushed
tk.Button(controlWindow, text="Update Graph", command=lambda:getTerms()).grid(column=3,row=1,sticky=E)
tk.Button(controlWindow, text="Clear Graph", command=lambda:clearGraph()).grid(column=4,row=1,sticky=E)
tk.Button(controlWindow, text="Exit", command=lambda:exit()).grid(column=4,row=3,sticky=E)
tk.Button(controlWindow, text="Compare Default Square Wave", command=lambda:genPlot(defaultSquareWave)).grid(column=1,row=2,sticky=W)
tk.Button(controlWindow, text="Compare to Default Sine Wave", command=lambda:genPlot(defaultSineWave)).grid(column=1,row=3,sticky=W)
window.mainloop()




