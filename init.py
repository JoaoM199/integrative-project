'''
    Projeto Integrador Transdisciplinar em Ciência da Computação II
    Aluno: João Marcelo Coelho Pacheco
    RGM: 23163054
    Tutores: Thyago Alves Sobreira, Leonardo Akira Teixeira Dantas Kamimura
'''

from tkinter import *
from tkinter import ttk
from math import *
from scipy.optimize import fsolve
import numpy as np
import scipy as scp
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg # Plotar gráfico dentro de uma janela
from matplotlib import figure
            
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
        Label(tab_mean, text='mean = {}'.format(mean),anchor=W, foreground="#00a").place(x=10,y=110, width=300, height=20)

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
        Label(tab_dev, text='mean of d = {}'.format(devitation_mean), anchor=W, foreground='#00a').place(x=10,y=160,width=300, height=20)
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
        Label(tab_csd, text='sd = {}'.format(sd), anchor=W, foreground='#00a').place(x=10,y=170, width=300, height=20)
        Label(tab_csd, text='rsd = {}'.format(rsd), anchor=W, foreground='#00a').place(x=10,y=190, width=300, height=20)

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
        Label(tab_ttr, text='u = {}'.format(u), anchor=W, foreground="#00a").place(x=10,y=140, width=450, height=20)

    calculate = Button(tab_ttr, text="Calculate", command=calc_ttr)
    calculate.place(x=10,y=90,width=300, height=20)
def phc():
    def error_non_numeric():
        Label(tab_ph, text = "ERROR: Non numeric value", anchor=W, foreground='#a00').place(x=100,y=170,width=450,height=20)
    def phc_strong():
        Label(tab_ph, text="Enter the acid volume (mL): ", anchor=W).place(x=10,y=30, width=300, height=20) # Acid volume
        input_Ac_vol = Entry(tab_ph)
        input_Ac_vol.place(x=10,y=50,width=50,height=20)

        Label(tab_ph, text="Enter the Base volume (mL)", anchor=W).place(x=300,y=30, width=300, height=20) # Basic volume
        input_B_vol = Entry(tab_ph)
        input_B_vol.place(x=300,y=50,width=50,height=20)

        Label(tab_ph, text="Enter the acid concentration (N): ", anchor=W).place(x=10,y=70, width=300, height=20) # Acid concentration
        input_Ac_con = Entry(tab_ph)
        input_Ac_con.place(x=10,y=90,width=50,height=20)

        Label(tab_ph, text="Enter the Base concentration (N)", anchor=W).place(x=300,y=70, width=300, height=20) # Basic concentration
        input_B_con = Entry(tab_ph)
        input_B_con.place(x=300,y=90,width=50,height=20)
                

        def calc_ph():
            # Variáveis de entrada
            try:
                # Entrada
                Ac_vol = float(input_Ac_vol.get())
            except ValueError:
                # Erro
                error_non_numeric()

            try:
                # Entrada
                B_vol = float(input_B_vol.get())
            except ValueError:
                # Erro
                error_non_numeric()

            try:
                # Entrada
                Ac_con = float(input_Ac_con.get())
            except ValueError:
                error_non_numeric()

            try:
                # Entrada
                B_con = float(input_B_con.get())
            except ValueError:
                error_non_numeric()

            # Converter volue para litros
            Ac_vol = Ac_vol/1000
            B_vol = B_vol/1000
            # Quantidade de substância
            # n = C * V
            n_Ac = Ac_con * Ac_vol
            n_B = B_con * B_vol

            # Substância em excesso
            if n_Ac > n_B:
                qn = n_Ac - n_B
            else:
                qn = n_B - n_Ac

            # Concentração da espécie em excesso
            n_con = qn/(Ac_vol + B_vol)

            # Calcular pH e pOH
            if n_Ac > n_B:
                pH = -np.log10(n_con)
            else:
                pOH = -np.log10(n_con)

            # Calcular pOH a partir de pH ou vice-versa
            if n_Ac > n_B:
                pOH = 14 - pH
            else:
                pH = 14 - pOH

            # Volumes em equilíbrio
            if Ac_vol == B_vol:
                pH = 7
                pOH = 7
            else:
                pH = pH
                pOH = pOH

            # Imprimindo valores
            Label(tab_ph, text='Volume of acid: {}'.format(Ac_vol*1000), anchor=W).place(x=100,y=170,width=450,height=20)
            Label(tab_ph, text='Volume of base: {}'.format(B_vol*1000), anchor=W).place(x=100,y=190,width=450,height=20)
            Label(tab_ph, text='Concentration of acid: {}'.format(Ac_con), anchor=W).place(x=100,y=210,width=450,height=20)
            Label(tab_ph, text='Concentration of acid: {}'.format(B_con), anchor=W).place(x=100,y=230,width=450,height=20)
            # Resultado
            Label(tab_ph, text = 'pH = {}'.format(pH), anchor=W, foreground='#00a').place(x=100,y=250,width=450,height=20)
            Label(tab_ph, text = 'pOH = {}'.format(pOH), anchor=W, foreground='#00a').place(x=100,y=270,width=450,height=20)
        # Botão
        calculate = Button(tab_ph, text="Calculate", command=calc_ph)
        calculate.place(x=100,y=130,width=300, height=20)
    def phc_weak_acid():
        Label(tab_ph, text="Enter the acid volume (mL): ", anchor=W).place(x=10,y=30, width=300, height=20) # Acid volume
        input_Ac_vol = Entry(tab_ph)
        input_Ac_vol.place(x=10,y=50,width=50,height=20)

        Label(tab_ph, text="Enter the Base volume (mL)", anchor=W).place(x=300,y=30, width=300, height=20) # Basic volume
        input_B_vol = Entry(tab_ph)
        input_B_vol.place(x=300,y=50,width=50,height=20)

        Label(tab_ph, text="Enter the acid concentration (N): ", anchor=W).place(x=10,y=70, width=300, height=20) # Acid concentration
        input_Ac_con = Entry(tab_ph)
        input_Ac_con.place(x=10,y=90,width=50,height=20)

        Label(tab_ph, text="Enter the Base concentration (N)", anchor=W).place(x=300,y=70, width=300, height=20) # Basic concentration
        input_B_con = Entry(tab_ph)
        input_B_con.place(x=300,y=90,width=50,height=20)

        Label(tab_ph, text="Enter acid constaint (Ka):", anchor=W).place(x=100,y=110, width=300, height=20) # Constante do ácido
        Label(tab_ph, text=" * 10^ -", anchor=W).place(x=150,y=130, width=300, height=20)
        input_ka_significant_digits = Entry(tab_ph)
        input_ka_significant_digits.place(x=100,y=130,width=50,height=20)
        input_ka_exponent = Entry(tab_ph)
        input_ka_exponent.place(x=210,y=130,width=50,height=20)

        def calc_ph_wac():
            # Variáveis de entrada
            try:
                # Entrada
                Ac_vol = float(input_Ac_vol.get())
            except ValueError:
                # Erro
                error_non_numeric()

            try:
                # Entrada
                B_vol = float(input_B_vol.get())
            except ValueError:
                # Erro
                error_non_numeric()

            try:
                # Entrada
                Ac_con = float(input_Ac_con.get())
            except ValueError:
                error_non_numeric()

            try:
                # Entrada
                B_con = float(input_B_con.get())
            except ValueError:
                error_non_numeric()

            try:
                # Valores significativos da constante
                ka_sd = float(input_ka_significant_digits.get())
            except ValueError:
                error_non_numeric()

            try:
                # Expoente da constante
                ka_ex = float(input_ka_exponent.get())
            except ValueError:
                error_non_numeric()

            # Valor da constante do ácido
            def get_ka():
                ka = ka_sd * 10 ** (-ka_ex)
                return ka
            ka = get_ka()

            # Converter volume para litros
            Ac_vol = Ac_vol/1000
            B_vol = B_vol/1000
            print(Ac_vol)
            print(B_vol)

            # Calcular número de moles inicial
            init_acid = Ac_con * Ac_vol
            init_base = B_con * B_vol
            print(init_acid)
            print(init_base)

            # Calcular número de moles nal
            final_acid = max(0, init_acid - init_base)
            final_base = max(0, init_base - init_acid)
            print(final_acid)
            print(final_base)

            # Volume final
            final_volume = Ac_vol + B_vol
            print(final_volume)

            # Concentrações finais de ácido e base
            final_Ac_con = final_acid / final_volume
            final_B_con = final_base / final_volume
            print(final_Ac_con)

            # Concentração de H+
            H_con = sqrt(ka * final_Ac_con)
            print(H_con)

            if H_con > 0:
                pH = -log10(H_con)
                pOH = 14 - pH
                # Resultado
                Label(tab_ph, text = 'pH = {}'.format(pH), anchor=W, foreground='#00a').place(x=100,y=300,width=450,height=20)
                Label(tab_ph, text = 'pOH = {}'.format(pOH), anchor=W, foreground='#00a').place(x=100,y=320,width=450,height=20)
            else:
                Label(tab_ph, text = 'The concentratio of hydrogen ions is equals to 0 or is\n a negative value. It is not possible to calculate the pH and pOH', anchor=W, foreground='#a00').place(x=10,y=300,width=500,height=30)

            # Imprimindo valores
            Label(tab_ph, text='Volume of acid: {}'.format(Ac_vol*1000), anchor=W).place(x=100,y=200,width=450,height=20)
            Label(tab_ph, text='Volume of base: {}'.format(B_vol*1000), anchor=W).place(x=100,y=220,width=450,height=20)
            Label(tab_ph, text='Concentration of acid: {}'.format(Ac_con), anchor=W).place(x=100,y=240,width=450,height=20)
            Label(tab_ph, text='Concentration of acid: {}'.format(B_con), anchor=W).place(x=100,y=260,width=450,height=20)
            Label(tab_ph, text='Ka: {}'.format(ka), anchor=W).place(x=100,y=280,width=450,height=20)

        calculate = Button(tab_ph, text="Calculate", command=calc_ph_wac)
        calculate.place(x=100,y=170,width=300, height=20)
    def phc_weak_base():
        Label(tab_ph, text="Enter the acid volume (mL): ", anchor=W).place(x=10,y=30, width=300, height=20) # Acid volume
        input_Ac_vol = Entry(tab_ph)
        input_Ac_vol.place(x=10,y=50,width=50,height=20)

        Label(tab_ph, text="Enter the Base volume (mL)", anchor=W).place(x=300,y=30, width=300, height=20) # Basic volume
        input_B_vol = Entry(tab_ph)
        input_B_vol.place(x=300,y=50,width=50,height=20)

        Label(tab_ph, text="Enter the acid concentration (N): ", anchor=W).place(x=10,y=70, width=300, height=20) # Acid concentration
        input_Ac_con = Entry(tab_ph)
        input_Ac_con.place(x=10,y=90,width=50,height=20)

        Label(tab_ph, text="Enter the Base concentration (N)", anchor=W).place(x=300,y=70, width=300, height=20) # Basic concentration
        input_B_con = Entry(tab_ph)
        input_B_con.place(x=300,y=90,width=50,height=20)

        Label(tab_ph, text="Enter base constaint (Kb):", anchor=W).place(x=100,y=110, width=300, height=20) # Constante do ácido
        Label(tab_ph, text=" * 10^ -", anchor=W).place(x=150,y=130, width=300, height=20)
        input_kb_significant_digits = Entry(tab_ph)
        input_kb_significant_digits.place(x=100,y=130,width=50,height=20)
        input_kb_exponent = Entry(tab_ph)
        input_kb_exponent.place(x=210,y=130,width=50,height=20)

        def calc_ph_wb():
            # Variáveis de entrada
            try:
                # Entrada
                Ac_vol = float(input_Ac_vol.get())
            except ValueError:
                # Erro
                error_non_numeric()

            try:
                # Entrada
                B_vol = float(input_B_vol.get())
            except ValueError:
                # Erro
                error_non_numeric()

            try:
                # Entrada
                Ac_con = float(input_Ac_con.get())
            except ValueError:
                error_non_numeric()

            try:
                # Entrada
                B_con = float(input_B_con.get())
            except ValueError:
                error_non_numeric()

            try:
                # Valores significativos da constante
                kb_sd = float(input_kb_significant_digits.get())
            except ValueError:
                error_non_numeric()

            try:
                # Expoente da constante
                kb_ex = float(input_kb_exponent.get())
            except ValueError:
                error_non_numeric()

            # Valor da constante do ácido
            def get_ka():
                kb = kb_sd * 10 ** (-kb_ex)
                return kb
            kb = get_ka()

            # Converter volume para litros
            Ac_vol = Ac_vol/1000
            B_vol = B_vol/1000

            # Calcular número de moles inicial
            init_acid = Ac_con * Ac_vol
            init_base = B_con * B_vol

            # Calcular número de moles nal
            final_acid = max(0, init_acid - init_base)
            final_base = max(0, init_base - init_acid)

            # Volume final
            final_volume = Ac_vol + B_vol

            # Concentrações finais de ácido e base
            final_Ac_con = final_acid / final_volume
            final_B_con = final_base / final_volume

            # Concentração de H+
            OH_con = sqrt(kb * final_B_con)

            # Calcular pH e pOH
            if OH_con > 0:
                pOH = -log10(OH_con)
                pH = 14 - pOH
                # Resultado
                Label(tab_ph, text = 'pH = {}'.format(pH), anchor=W, foreground='#00a').place(x=100,y=300,width=450,height=20)
                Label(tab_ph, text = 'pOH = {}'.format(pOH), anchor=W, foreground='#00a').place(x=100,y=320,width=450,height=20)
            else:
                Label(tab_ph, text = 'The concentratio of hydroxyl ions is equals to 0 or is\n a negative value. It is not possible to calculate the pOH and pH', anchor=W, foreground='#a00').place(x=10,y=300,width=500,height=30)
                

            # Imprimindo valores
            Label(tab_ph, text='Volume of acid: {}'.format(Ac_vol*1000), anchor=W).place(x=100,y=200,width=450,height=20)
            Label(tab_ph, text='Volume of base: {}'.format(B_vol*1000), anchor=W).place(x=100,y=220,width=450,height=20)
            Label(tab_ph, text='Concentration of acid: {}'.format(Ac_con), anchor=W).place(x=100,y=240,width=450,height=20)
            Label(tab_ph, text='Concentration of acid: {}'.format(B_con), anchor=W).place(x=100,y=260,width=450,height=20)
            Label(tab_ph, text='Kb: {}'.format(kb), anchor=W).place(x=100,y=280,width=450,height=20)

        calculate = Button(tab_ph, text="Calculate", command=calc_ph_wb)
        calculate.place(x=100,y=170,width=300, height=20)
    def phc_wab():
        # Ácido fraco e base fraca
        Label(tab_ph, text="Enter the acid volume (mL): ", anchor=W).place(x=10,y=30, width=300, height=20) # Acid volume
        input_Ac_vol = Entry(tab_ph)
        input_Ac_vol.place(x=10,y=50,width=50,height=20)

        Label(tab_ph, text="Enter the Base volume (mL)", anchor=W).place(x=300,y=30, width=300, height=20) # Basic volume
        input_B_vol = Entry(tab_ph)
        input_B_vol.place(x=300,y=50,width=50,height=20)

        Label(tab_ph, text="Enter the acid concentration (N): ", anchor=W).place(x=10,y=70, width=300, height=20) # Acid concentration
        input_Ac_con = Entry(tab_ph)
        input_Ac_con.place(x=10,y=90,width=50,height=20)

        Label(tab_ph, text="Enter the Base concentration (N)", anchor=W).place(x=300,y=70, width=300, height=20) # Basic concentration
        input_B_con = Entry(tab_ph)
        input_B_con.place(x=300,y=90,width=50,height=20)

        Label(tab_ph, text="Enter acid constaint (Ka):", anchor=W).place(x=100,y=110, width=300, height=20) # Constante do ácido
        Label(tab_ph, text=" * 10^ -", anchor=W).place(x=150,y=130, width=300, height=20)
        input_ka_significant_digits = Entry(tab_ph)
        input_ka_significant_digits.place(x=100,y=130,width=50,height=20)
        input_ka_exponent = Entry(tab_ph)
        input_ka_exponent.place(x=210,y=130,width=50,height=20)

        Label(tab_ph, text="Enter base constaint (Kb):", anchor=W).place(x=100,y=150, width=300, height=20) # Constante do ácido
        Label(tab_ph, text=" * 10^ -", anchor=W).place(x=150,y=170, width=300, height=20)
        input_kb_significant_digits = Entry(tab_ph)
        input_kb_significant_digits.place(x=100,y=170,width=50,height=20)
        input_kb_exponent = Entry(tab_ph)
        input_kb_exponent.place(x=210,y=170,width=50,height=20)

        def calc_ph_wab():
            # Variáveis de entrada
            try:
                # Entrada
                Ac_vol = float(input_Ac_vol.get())
            except ValueError:
                # Erro
                error_non_numeric()

            try:
                # Entrada
                B_vol = float(input_B_vol.get())
            except ValueError:
                # Erro
                error_non_numeric()

            try:
                # Entrada
                Ac_con = float(input_Ac_con.get())
            except ValueError:
                error_non_numeric()

            try:
                # Entrada
                B_con = float(input_B_con.get())
            except ValueError:
                error_non_numeric()

            try:
                # Valores significativos da constante
                ka_sd = float(input_ka_significant_digits.get())
            except ValueError:
                error_non_numeric()

            try:
                # Expoente da constante
                ka_ex = float(input_ka_exponent.get())
            except ValueError:
                error_non_numeric()

            try:
                # Valores significativos da constante
                kb_sd = float(input_kb_significant_digits.get())
            except ValueError:
                error_non_numeric()

            try:
                # Expoente da constante
                kb_ex = float(input_kb_exponent.get())
            except ValueError:
                error_non_numeric()

            # Valor da constante do ácido e da base
            def get_ka():
                ka = ka_sd * 10 ** (-ka_ex)
                return ka
            def get_kb():
                kb = kb_sd * 10 ** (-kb_ex)
                return kb
            ka = get_ka()
            kb = get_kb()

            # Converter volume para litros
            Ac_vol = Ac_vol/1000
            B_vol = B_vol/1000

            # Calcular número de moles inicial
            init_acid = Ac_con * Ac_vol
            init_base = B_con * B_vol

            # Calcular número de moles nal
            final_acid = max(0, init_acid - init_base)
            final_base = max(0, init_base - init_acid)

            # Volume final
            final_volume = Ac_vol + B_vol

            # Concentrações finais de ácido e base
            final_Ac_con = final_acid / final_volume
            final_B_con = final_base / final_volume

            # Realizando equações do equilíbrio
            def eq(vars):
                H, OH = vars
                eq1 = ka - H*(final_Ac_con + H)/(final_B_con + OH)
                eq2 = kb - OH*(final_B_con + OH)/(final_Ac_con + H)
                return [eq1, eq2]
            H, OH = fsolve(eq, (1e-7, 1e-7))

            # Resultado
            Label(tab_ph, text = 'pH = {}'.format(H), anchor=W, foreground='#00a').place(x=100,y=350,width=450,height=20)
            Label(tab_ph, text = 'pOH = {}'.format(OH), anchor=W, foreground='#00a').place(x=100,y=370,width=450,height=20)

            # Imprimindo valores
            Label(tab_ph, text='Volume of acid: {}'.format(Ac_vol*1000), anchor=W).place(x=100,y=230,width=450,height=20)
            Label(tab_ph, text='Volume of base: {}'.format(B_vol*1000), anchor=W).place(x=100,y=250,width=450,height=20)
            Label(tab_ph, text='Concentration of acid: {}'.format(Ac_con), anchor=W).place(x=100,y=270,width=450,height=20)
            Label(tab_ph, text='Concentration of acid: {}'.format(B_con), anchor=W).place(x=100,y=290,width=450,height=20)
            Label(tab_ph, text='Ka: {}'.format(ka), anchor=W).place(x=100,y=310,width=450,height=20)
            Label(tab_ph, text='Kb: {}'.format(kb), anchor=W).place(x=100,y=330,width=450,height=20)

        calculate = Button(tab_ph, text="Calculate", command=calc_ph_wab)
        calculate.place(x=100,y=210,width=300, height=20)
        
    # Opções
    Options_frame = Frame(tab_ph)
    Options_frame.place(x=10,y=10, width=300, height=20, anchor=W)
    Options_list = [
        "Strong acid & strong base",
        "Weak acid & strong base",
        "Strong acid & weak base",
        "Weak acid & weak base"
    ]
    SelOption = StringVar()

    Options = OptionMenu(Options_frame, SelOption, *Options_list)
    Options.pack()
    def clear_tab_ph():
        for widget in tab_ph.winfo_children():
            if widget != Options_frame:
                widget.destroy()
    def option_changed(*args):
        clear_tab_ph()
        if SelOption.get() == "Strong acid & strong base":
            phc_strong()
        elif SelOption.get() == "Weak acid & strong base":
            phc_weak_acid()
        elif SelOption.get() == "Strong acid & weak base":
            phc_weak_base()
        elif SelOption.get() == "Weak acid & weak base":
            phc_wab()

    SelOption.trace("w", option_changed)
    SelOption.set(Options_list[0]) # Valor padrão
def tcurve():
    # Ácido forte e base forte
    def error_non_numeric():
        Label(tab_tcurve, text = "ERROR: Non numeric value", anchor=W, foreground='#a00').place(x=100,y=170,width=450,height=20)
    def tcurve_sab():
        Label(tab_tcurve, text="Enter the acid volume (mL): ", anchor=W).place(x=10,y=30, width=300, height=20) # Acid volume
        input_Ac_vol = Entry(tab_tcurve)
        input_Ac_vol.place(x=10,y=50,width=50,height=20)

        Label(tab_tcurve, text="Enter the acid concentration (N): ", anchor=W).place(x=10,y=70, width=300, height=20) # Acid concentration
        input_Ac_con = Entry(tab_tcurve)
        input_Ac_con.place(x=10,y=90,width=50,height=20)

        Label(tab_tcurve, text="Enter the Base concentration (N)", anchor=W).place(x=300,y=70, width=300, height=20) # Base concentration
        input_B_con = Entry(tab_tcurve)
        input_B_con.place(x=300,y=90,width=50,height=20)
                

        def generate_tcurve_sab():
            # Variáveis de entrada
            try:
                # Entrada
                V_acid = float(input_Ac_vol.get())
            except ValueError:
                # Erro
                error_non_numeric()

            try:
                # Entrada
                C_Acid = float(input_Ac_con.get())
            except ValueError:
                error_non_numeric()

            try:
                # Entrada
                C_base = float(input_B_con.get())
            except ValueError:
                error_non_numeric()

            # Volume da base necessário para a neutralização
            V_Base = (C_Acid * V_acid)/C_base
            # Criação de uma lista de volumes da base a serem adicionados
            V_Base_add = np.linspace(0, 2*V_Base, 500)

            # Cálculo de pH para cada volume adicionado
            pH = []
            for V in V_Base_add:
                if V < V_Base:
                    n_Acid = C_Acid - C_base * V
                    V_total = V_acid + V
                    if n_Acid > 0:
                        pH.append(-np.log10(n_Acid/V_total))
                    else:
                        pH.append(0)
                elif V == V_Base:
                    pH.append(7) # Ponto de equivalência
                else:
                    n_base = C_base * V - C_Acid * V_acid
                    V_total = V_acid + V
                    pOH = -np.log10(n_base/V_total)
                    pH.append(14 - pOH)

            # Imprimindo valores inseridos
            Label(tab_tcurve, text='Concentration of acid: {}'.format(C_Acid), anchor=W).place(x=100,y=170,width=450,height=20)
            Label(tab_tcurve, text='Concentration of base: {}'.format(C_base), anchor=W).place(x=100,y=190,width=450,height=20)
            Label(tab_tcurve, text='Volume of acid: {}mL'.format(V_acid), anchor=W).place(x=100,y=210,width=450,height=20)

            # Gerando gráfico
            def show_graph():
                plt.figure(figsize=(8,6))
                plt.plot(V_Base_add, pH, label = 'Titration curve')
                plt.xlabel('Base volume added (mL)')
                plt.ylabel('pH')
                plt.title('Titration curve')
                plt.legend()
                plt.grid(True)
                plt.show()
            
            # Gráfico dentro de janela
            fig = plt.figure(figsize=(8,8))
            plt.plot(V_Base_add, pH, label = 'Titration curve')
            plt.xlabel('Base volume added (mL)')
            plt.ylabel('pH')
            plt.title('Titration curve')
            plt.legend()
            plt.grid(True)
                
            graph = FigureCanvasTkAgg(fig, master=tab_tcurve)
            graph.draw()
            graph.get_tk_widget().place(x=10,y=250, width=600, height=200)
            # Botão para mostrar gráfico mais detalhado
            showmore = Button(tab_tcurve, text="Show more", command=show_graph)
            showmore.place(x=300,y=210,width=100, height=20)
        # Botão para calcular
        calculate = Button(tab_tcurve, text="Calculate", command=generate_tcurve_sab)
        calculate.place(x=100,y=130,width=300, height=20)
    def tcurve_wa():
        pass
    def tcurve_wb():
        pass
    def tcurve_wab():
        pass
    def tcurve_p():
        pass

    
    # Opções
    Options_frame = Frame(tab_tcurve)
    Options_frame.pack()
    Options_list = [
        "titration of strong acid in strong base",
        "titration of weak acid to strong base",
        "titration of weak base to strong acid",
        "titration of strong acid to weak base",
        "precipitation titration"
    ]
    SelOption = StringVar()
    Options = OptionMenu(Options_frame,SelOption,*Options_list)
    Options.pack()

    def clear_tab_tcurve():
        for widget in tab_tcurve.winfo_children():
            if widget != Options_frame:
                widget.destroy()
    def option_changed(*args):
        clear_tab_tcurve()
        if SelOption.get() == "titration of strong acid in strong base":
            tcurve_sab()
        elif SelOption.get() == "titration of weak acid to strong base":
            tcurve_wa()
        elif SelOption.get() == "titration of weak base to strong acid":
            tcurve_wb()
        elif SelOption.get() == "titration of strong acid to weak base":
            tcurve_wab()
        elif SelOption.get() == "precipitation titration":
            tcurve_p()

    SelOption.trace("w", option_changed)
    SelOption.set(Options_list[0])


# Apagar esta função quando finalizar
def Nulo():
    print("")


######################################### Main Window #################################################################
app = Tk()
app.title("Advanced Calculator for Quantitative Analytical Calculations")
app.geometry('700x900')

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

tab_ph = Frame(tabs, width=600, height=600)
tab_ph.pack(fill='both', expand=1)
phc()
tabs.add(tab_ph, text="pH & pOH")

tab_tcurve = Frame(tabs, width=700, height=900)
tab_tcurve.pack(fill="both",expand=1)
tcurve()
tabs.add(tab_tcurve, text="Titration curve")

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