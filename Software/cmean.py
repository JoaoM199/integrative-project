from math import *
from tkinter import *

val = 0

class show_window():
    def __init__(self):
        mean_window = Tk()
        mean_window.title("Calculate mean")
        mean_window.geometry("500x400")

        mean_window.mainloop()

    '''
    def mean():
        uinput = input("Digite os valores separados por vírgula: ")
        val = [float(i) for i in uinput.split(',')]
        print(type(val))
        print(val)
        
        n = len(val)
        print(n)
        
        mean = sum(val)/n
        print(mean)

    mean()
    '''
show_window()