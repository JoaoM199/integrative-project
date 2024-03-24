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
    gui = window(app)
    gui.app.mainloop()
    return None

class window:
    def __init__(self, app):
        self.app = app
        self.app.title("Título")
        self.app.geometry('400x700')

main()
