import numpy as np
import scipy as scp
from tkinter import * 

class ttr():
    def __init__(self):
        self = Tk()
        self.title("trust threshold")
        self.geometry("500x400")

        Label(self, text = "Enter comma-separated values (','): ", anchor=W).place(x=10,y=10, width=300, height=20) # Valores inseridos pelo usuário
        uentry = Entry(self)
        uentry.place(x=10,y=30,width=300, height=20)

        Label(self, text="Enter the probability percentage (%): ", anchor=W).place(x=10,y=50, width=50, height=20) # Parâmetro t do limite de confiança
        tinput = Entry(self)
        tinput.place(x=10,y=70,width=50,height=20)

        def calc_ttr():
            rval = uentry.get()
            val = rval.split(',')
            fval = [float(i) for i in val]
            print(fval)
            print(type(fval))
            print('\n')

            rt = tinput.get()
            t = float(rt)
            print(t)
            print(type(t))

            mean = np.mean(fval)
            print(mean)

            sd = np.std(fval)
            print(sd)

            n = len(fval)
            print(n)

            dof = n - 1
            print(dof)

            critical_value = scp.stats.t.ppf((1 + t/100) / 2.0, dof)
            print(critical_value)

            error_margin = critical_value * (sd/np.sqrt(n))
            print(error_margin)

            ttr = (mean - error_margin, mean + error_margin)
            print(ttr)

            Label(self, text='Ttr = {}'.format(ttr), anchor=W, foreground="#00a", font="Bold").place(x=10,y=110, width=450, height=20)

        calculate = Button(self, text="Calculate", command=calc_ttr)
        calculate.place(x=10,y=90,width=300, height=20)



        self.mainloop()