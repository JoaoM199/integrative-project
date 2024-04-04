from math import *
from tkinter import *
import numpy as np

class cdevitation():
    def __init__(self):
        self = Tk()
        self.title("SD")
        self.geometry("500x400")
        
        Label(self, text = "Enter comma-separated values (','): ", anchor=W).place(x=10,y=10, width=300, height=20)
        uentry = Entry(self)
        uentry.place(x=10,y=30,width=300, height=20)

        def calc_devitation():
            # Get Mean
            rval = uentry.get()
            val = rval.split(',')
            fval = [float(i) for i in val]
            mean = np.mean(fval)

            devitation_values = np.abs(fval - mean)
            devitation_mean = np.mean(devitation_values)

            Label(self, text='x = {}'.format(val), anchor=W).place(x=10, y=90, width=300, height=20)
            Label(self, text='d = {}'.format(devitation_values), anchor=W).place(x=10,y=120, width=450, height=20)
            Label(self, text='mean of d = {}'.format(devitation_mean), anchor=W, foreground='#00a', font={'bold'}).place(x=10,y=150,width=300, height=20)
        calculate = Button(self, text="Calculate", command=calc_devitation)
        calculate.place(x=10,y=50,width=300, height=20)

        self.mainloop()