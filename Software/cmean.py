from math import *
from tkinter import *

class cmean():
    n = 0
    mean = 0
    uinput = ""
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
                        
            mean = sum(fval)/n
            print(mean)
            Label(self, text=mean,anchor=W, foreground="#00a", font="Bold").place(x=10,y=80, width=300, height=20)

        calculate = Button(self, text="Calculate", command=calc_mean)
        calculate.place(x=10,y=100,width=300, height=20)
        exit = Button(self, text="exit", command=self.quit)
        exit.place(x=10,y=130,width=300, height=20)

        self.mainloop()