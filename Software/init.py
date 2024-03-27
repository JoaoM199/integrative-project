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

def main():
    app = Tk()
    gui = main_window(app)
    gui.app.mainloop()
    return None

class main_window:
    def Nulo():
        print("")

    def __init__(self, app, menubar):
        self.app = app
        self.app.title("Advanced Calculator for Quantitative Analytical Calculations")
        self.app.geometry('500x700')
        self.app(Menu = menubar)

    def menu(self, app, Nulo):
        menubar = Menu(self.app)
        mfile = Menu(menubar, tearoff=0)
        mfile.add_command(label='New',command=Nulo)
        mfile.add_command(label='Save as',command=Nulo)
        mfile.add_command(label='Clear',command=Nulo)
        mfile.add_command(label='Print',command=Nulo)
        mfile.add_separator()
        mfile.add_command(label='exit',command=self.app.quit)

main()
