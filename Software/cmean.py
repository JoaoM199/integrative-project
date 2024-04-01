from math import *
from tkinter import *
import numpy as np

class cmean():
    n = 0
    mean = 0
    val = 0

    def __init__(self):
        self = Tk()
        self.title("Calculate mean")
        self.geometry("500x400")
        
        Label(self, text = "Enter comma-separated values (','): ", anchor=W).place(x=10,y=10, width=300, height=20)
        uentry = Entry(self)
        uentry.place(x=10,y=30,width=300, height=20)

        def calc_mean():
            rval = uentry.get()
            val = rval.split(',')
            fval = [float(i) for i in val]
            
            n = len(fval)
            print(n)
            
            mean = np.mean(fval)
            print(mean)
            
            Label(self, text='x = {}'.format(val),anchor=W).place(x=10,y=50, width=300, height=20)
            Label(self, text='n = {}'.format(n),anchor=W).place(x=10,y=70, width=300, height=20)
            Label(self, text='mean = {}'.format(mean),anchor=W, foreground="#00a", font="Bold").place(x=10,y=90, width=300, height=20)

        calculate = Button(self, text="Calculate", command=calc_mean)
        calculate.place(x=10,y=110,width=300, height=20)

        self.mainloop()