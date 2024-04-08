'''
    Projeto Integrador Transdisciplinar em Ciência da Computação II
    Aluno: João Marcelo Coelho Pacheco
    RGM: 23163054
    Tutor: Thyago Alves Sobreira
'''

from tkinter import *
from tkinter import ttk
from math import *
import numpy as np
import scipy as scp
import matplotlib.pyplot as plt
#from pHcalc import Acid, Inert, System
            
def cmean():
    Label(tab_mean, text = "Enter comma-separated values (','): ", anchor=W).place(x=10,y=30, width=300, height=20)
    uentry = Entry(tab_mean)
    uentry.place(x=10,y=50,width=300, height=20)

    n = 0
    mean = 0
    val = 0

    def calc_mean():
        rval = uentry.get()
        val = rval.split(',')
        fval = [float(i) for i in val]
                    
        n = len(fval)
        print(n)
                
        mean = np.mean(fval)
        print(mean)
                
        Label(tab_mean, text='x = {}'.format(val),anchor=W).place(x=10,y=70, width=300, height=20)
        Label(tab_mean, text='n = {}'.format(n),anchor=W).place(x=10,y=90, width=300, height=20)
        Label(tab_mean, text='mean = {}'.format(mean),anchor=W, foreground="#00a", font="Bold").place(x=10,y=110, width=300, height=20)

    calculate = Button(tab_mean, text="Calculate", command=calc_mean)
    calculate.place(x=10,y=130,width=300, height=20)
def cdev():        
    Label(tab_dev, text = "Enter comma-separated values (','): ", anchor=W).place(x=10,y=30, width=300, height=20)
    uentry = Entry(tab_dev)
    uentry.place(x=10,y=50,width=300, height=20)

    def calc_devitation():
        # Get Mean
        rval = uentry.get()
        val = rval.split(',')
        fval = [float(i) for i in val]
        mean = np.mean(fval)

        devitation_values = np.abs(fval - mean)
        devitation_mean = np.mean(devitation_values)

        Label(tab_dev, text='x = {}'.format(val), anchor=W).place(x=10, y=110, width=300, height=20)
        Label(tab_dev, text='d = {}'.format(devitation_values), anchor=W).place(x=10,y=130, width=450, height=20)
        Label(tab_dev, text='mean of d = {}'.format(devitation_mean), anchor=W, foreground='#00a', font={'bold'}).place(x=10,y=160,width=300, height=20)
    calculate = Button(tab_dev, text="Calculate", command=calc_devitation)
    calculate.place(x=10,y=90,width=300, height=20)
def csd():
    Label(tab_csd, text = "Enter comma-separated values (','): ", anchor=W).place(x=10,y=10, width=300, height=20)
    uentry = Entry(tab_csd)
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

        Label(tab_csd, text='x = {}'.format(val), anchor=W).place(x=10, y=90, width=300, height=20)
        Label(tab_csd, text='n = {}'.format(n), anchor=W).place(x=10,y=120, width=300, height=20)
        Label(tab_csd, text='mean = {}'.format(mean), anchor=W).place(x=10,y=150,width=300, height=20)

        # Values
        Label(tab_csd, text='The Standard Deviation is equal to', anchor=W).place(x=10,y=170, width=300, height=20)
        Label(tab_csd, text=sd, anchor=W, foreground='#00a', font={'bold'}).place(x=10,y=190, width=300, height=20)
        Label(tab_csd, text='The Relative Standard Detation os equal to', anchor=W).place(x=10,y=210, width=300, height=20)
        Label(tab_csd, text=rsd, anchor=W, foreground='#00a', font={'bold'}).place(x=10,y=230, width=300, height=20)

    calculate = Button(tab_csd, text="Calculate", command=calc_sd)
    calculate.place(x=10,y=50,width=300, height=20)
def ttr():
    Label(tab_ttr, text = "Enter comma-separated values (','): ", anchor=W).place(x=10,y=10, width=300, height=20) # Valores inseridos pelo usuário
    uentry = Entry(tab_ttr)
    uentry.place(x=10,y=30,width=300, height=20)

    Label(tab_ttr, text="Enter the probability percentage (%): ", anchor=W).place(x=10,y=50, width=50, height=20) # Parâmetro t do limite de confiança
    tinput = Entry(tab_ttr)
    tinput.place(x=10,y=70,width=50,height=20)

    def calc_ttr():
        rval = uentry.get()
        val = rval.split(',')
        fval = [float(i) for i in val]

        rt = tinput.get()
        t = float(rt)
        mean = np.mean(fval)
        sd = np.std(fval)
        n = len(fval)
        dof = n - 1

        critical_value = scp.stats.t.ppf((1 + t/100) / 2.0, dof)
        error_margin = critical_value * (sd/np.sqrt(n))
        u = (mean - error_margin, mean + error_margin)

        Label(tab_ttr, text = 'The trust threshold of {},\n with t = {} is equal to:'.format(fval,t/100), anchor=W).place(x=10,y=110,width=450,height=20)
        Label(tab_ttr, text='u = {}'.format(u), anchor=W, foreground="#00a", font="Bold").place(x=10,y=140, width=450, height=20)

    calculate = Button(tab_ttr, text="Calculate", command=calc_ttr)
    calculate.place(x=10,y=90,width=300, height=20)

# Apagar esta função quando finalizar
def Nulo():
    print("")

app = Tk()
app.title("Advanced Calculator for Quantitative Analytical Calculations")
app.geometry('500x700')

'''
mcalc = Menu(menubar, tearoff=0)
m_analytical = Menu(mcalc, tearoff=0)
m_analytical.add_command(label='Mean', command=cmean.cmean)
m_analytical.add_command(label='Deviation of a Measurement', command=cdev.cdevitation)
m_analytical.add_command(label='SD & RSD', command=csd.csd) # Standard deviation
m_analytical.add_command(label='trust threshold', command=ttr.ttr) # Limite de confiança
mcalc.add_cascade(label='Analytical',menu=m_analytical)
mcalc.add_command(label="Command", command=Nulo)
menubar.add_cascade(label="Calculate",menu=mcalc)
'''

# Add tabs
tabs = ttk.Notebook(app)
tabs.pack()

tab_mean = Frame(tabs, width=500, height=300)
tab_mean.pack(fill="both", expand=1)
cmean()
tabs.add(tab_mean, text='Mean')

tab_dev = Frame(tabs, width=500, height=500)
tab_dev.pack(fill="both", expand=1)
cdev()
tabs.add(tab_dev, text="Devitation of a Measument")

tab_csd = Frame(tabs, width=500, height=600)
tab_csd.pack(fill="both")
csd()
tabs.add(tab_csd, text="Standard deviation")

tab_ttr = Frame(tabs, width=500, height=600)
tab_ttr.pack(fill="both", expand=1)
ttr()
tabs.add(tab_ttr, text="trust threshold")

# Menubar
menubar = Menu(app)
mfile = Menu(menubar, tearoff=0)
mfile.add_command(label='Save as', command=Nulo)
mfile.add_command(label='print', command=Nulo)
mfile.add_command(label='print', command=Nulo)
mfile.add_command(label='clear', command=Nulo)
mfile.add_separator()
mfile.add_command(label='exit', command=app.quit)
menubar.add_cascade(label="File",menu=mfile)

settings = Menu(menubar, tearoff=0)
settings.add_command(label='Preferences', command=Nulo)
menubar.add_cascade(label='settings', menu=settings)

help = Menu(menubar, tearoff=0)
help.add_command(label='about', command=Nulo)
menubar.add_cascade(label='help', menu=help)

app.config(menu=menubar)
app.mainloop()
