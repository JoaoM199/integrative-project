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

# Components
import cmean

def main():
    app = Tk()
    gui = main_window(app)
    gui.app.mainloop()
    return None

class main_window:
    def __init__(self, app):
        self.app = app
        self.app.title("Advanced Calculator for Quantitative Analytical Calculations")
        self.app.geometry('500x700')

class menubar:
    pass

main()
