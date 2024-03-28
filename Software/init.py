'''
    Projeto Integrador Transdisciplinar em Ciência da Computação II
    Aluno: João Marcelo Coelho Pacheco
    RGM: 23163054
    Tutor: Thyago Alves Sobreira
'''

from tkinter import *
from math import *
import numpy as np
import scipy as scp
import matplotlib.pyplot as plt
from pHcalc import Acid, Inert, System

# components
from cmean import cmean

# Apagar esta função quando finalizar
def Nulo():
    print("")

app = Tk()
app.title("Advanced Calculator for Quantitative Analytical Calculations")
app.geometry('500x700')

menubar = Menu(app)
mfile = Menu(menubar, tearoff=0)
mfile.add_command(label='Save as', command=Nulo)
mfile.add_command(label='print', command=Nulo)
mfile.add_command(label='print', command=Nulo)
mfile.add_command(label='clear', command=Nulo)
mfile.add_separator()
mfile.add_command(label='exit', command=app.quit)
menubar.add_cascade(label="File",menu=mfile)

mcalc = Menu(menubar, tearoff=0)
m_analytical = Menu(mcalc, tearoff=0)
m_analytical.add_command(label='Mean', command=cmean)
m_analytical.add_command(label='Deviation of a Measurement', command=Nulo)
m_analytical.add_command(label='SD', command=Nulo) # Standard deviation
m_analytical.add_command(label='RSD', command=Nulo) # Relative Standard deviation
m_analytical.add_command(label='trust threshold', command=Nulo) # Limite de confiança
mcalc.add_cascade(label='Analytical',menu=m_analytical)
mcalc.add_command(label="Command", command=Nulo)
menubar.add_cascade(label="Calculate",menu=mcalc)

settings = Menu(menubar, tearoff=0)
settings.add_command(label='Preferences', command=Nulo)
menubar.add_cascade(label='settings', menu=settings)

help = Menu(menubar, tearoff=0)
help.add_command(label='about', command=Nulo)
menubar.add_cascade(label='help', menu=help)

app.config(menu=menubar)
app.mainloop()
