from math import *
from tkinter import *

class operations():
    n = 0
    mean = 0
    uinput = ""
    val = 0

    def mean():
        uinput = input("Digite os valores separados por vírgula: ")
        val = [float(i) for i in uinput.split(',')]
        print(type(val))
        print(val)
            
        n = len(val)
        print(n)
            
        mean = sum(val)/n
        print(mean)

    def md():
        uinput = input("Digite os valores separados por vírgula: ")



    #def sd():


mean_window = Tk()
mean_window.title("Calculate mean")
mean_window.geometry("500x400")

# Inserir

mean_window.mainloop()