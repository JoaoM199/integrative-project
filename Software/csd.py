from math import *
from tkinter import *
import numpy as np

class csd():
    n = 0
    mean = 0
    val = 0
    s = 0

    def __init__(self):
        self = Tk()
        self.title("SD")
        self.geometry("500x400")
        
        Label(self, text = "Enter comma-separated values (','): ", anchor=W).place(x=10,y=10, width=300, height=20)
        uentry = Entry(self)
        uentry.place(x=10,y=30,width=300, height=20)

        def calc_sd():
            # Get Mean
            rval = uentry.get()
            val = rval.split(',')
            fval = [float(i) for i in val]
            n = len(fval)
            mean = np.mean(fval)

            # Standard Deviation
            sd = np.std(fval)

            # Relative Standard Deviation
            rsd = (sd/mean)*100

            Label(self, text='x = {}'.format(val), anchor=W).place(x=10, y=130, width=300, height=20)
            Label(self, text='n = {}'.format(n), anchor=W).place(x=10,y=150, width=300, height=20)
            Label(self, text='mean = {}'.format(mean), anchor=W).place(x=10,y=170,width=300, height=20)

            # Values
            Label(self, text='The Standard Deviation is equal to', anchor=W).place(x=10,y=190, width=300, height=20)
            Label(self, text=sd, anchor=W, foreground='#00a', font={'bold'}).place(x=10,y=210, width=300, height=20)
            Label(self, text='The Relative Standard Detation os equal to', anchor=W).place(x=10,y=230, width=300, height=20)
            Label(self, text=rsd, anchor=W, foreground='#00a', font={'bold'}).place(x=10,y=250, width=300, height=20)



            '''
            Normal: Label(self, text='x = {}'.format(val),anchor=W).place(x=10,y=50, width=300, height=20)
            Destaque: Label(self, text='sd = {}'.format(desv),anchor=W, foreground="#00a", font="Bold").place(x=10,y=130, width=300, height=20)
            '''

        calculate = Button(self, text="Calculate", command=calc_sd)
        calculate.place(x=10,y=110,width=300, height=20)

        self.mainloop()