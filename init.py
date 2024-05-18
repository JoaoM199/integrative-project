'''
    Projeto Integrador Transdisciplinar em Ciência da Computação II
    Nome do projeto: AQCALC
    Aluno: João Marcelo Coelho Pacheco
    RGM: 23163054
    Tutores: Thyago Alves Sobreira, Leonardo Akira Teixeira Dantas Kamimura
'''
import threading
import webbrowser as web
from tkinter import *
from tkinter import ttk
from math import *
from scipy.optimize import fsolve
import numpy as np
import scipy as scp
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg # Plotar gráfico dentro de uma janela

Versioner = {
    "name":"AQCalc",
    "version":"0.2",
    "status":"beta"
}

def descritive():
    def cmean():
        Label(tab_desc, text = "Enter comma-separated values (','): ", anchor=W).place(x=10,y=30, width=300, height=20)
        uentry = Entry(tab_desc)
        uentry.place(x=10,y=50,width=300, height=20)

        def calc_mean():
            rval = uentry.get()
            val = rval.split(',')
            fval = [float(i) for i in val]
                    
            n = len(fval)
            print(n)
                
            mean = np.mean(fval)
            print(mean)
                
            Label(tab_desc, text='x = {}'.format(val),anchor=W).place(x=10,y=70, width=300, height=20)
            Label(tab_desc, text='n = {}'.format(n),anchor=W).place(x=10,y=90, width=300, height=20)
            Label(tab_desc, text='mean = {}'.format(mean),anchor=W, foreground="#00a").place(x=10,y=110, width=300, height=20)

        calculate = Button(tab_desc, text="Calculate", command=calc_mean)
        calculate.place(x=10,y=130,width=300, height=20)
    def cdev():        
        Label(tab_desc, text = "Enter comma-separated values (','): ", anchor=W).place(x=10,y=30, width=300, height=20)
        uentry = Entry(tab_desc)
        uentry.place(x=10,y=50,width=300, height=20)

        def calc_devitation():
            # Get Mean
            rval = uentry.get()
            val = rval.split(',')
            fval = [float(i) for i in val]
            mean = np.mean(fval)

            devitation_values = np.abs(fval - mean)
            devitation_mean = np.mean(devitation_values)

            Label(tab_desc, text='x = {}'.format(val), anchor=W).place(x=10, y=110, width=300, height=20)
            Label(tab_desc, text='d = {}'.format(devitation_values), anchor=W).place(x=10,y=130, width=450, height=20)
            Label(tab_desc, text='mean of d = {}'.format(devitation_mean), anchor=W, foreground='#00a').place(x=10,y=160,width=300, height=20)
        calculate = Button(tab_desc, text="Calculate", command=calc_devitation)
        calculate.place(x=10,y=90,width=300, height=20)
    def csd():
        Label(tab_desc, text = "Enter comma-separated values (','): ", anchor=W).place(x=10,y=30, width=300, height=20)
        uentry = Entry(tab_desc)
        uentry.place(x=10,y=50,width=300, height=20)

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

            Label(tab_desc, text='x = {}'.format(val), anchor=W).place(x=10, y=90, width=300, height=20)
            Label(tab_desc, text='n = {}'.format(n), anchor=W).place(x=10,y=120, width=300, height=20)
            Label(tab_desc, text='mean = {}'.format(mean), anchor=W).place(x=10,y=150,width=300, height=20)

            # Values
            Label(tab_desc, text='sd = {}'.format(sd), anchor=W, foreground='#00a').place(x=10,y=170, width=300, height=20)
            Label(tab_desc, text='rsd = {}'.format(rsd), anchor=W, foreground='#00a').place(x=10,y=190, width=300, height=20)

        calculate = Button(tab_desc, text="Calculate", command=calc_sd)
        calculate.place(x=10,y=70,width=300, height=20)
    def ttr():
        Label(tab_desc, text = "Enter comma-separated values (','): ", anchor=W).place(x=10,y=30, width=300, height=20) # Valores inseridos pelo usuário
        uentry = Entry(tab_desc)
        uentry.place(x=10,y=60,width=300, height=20)

        Label(tab_desc, text="Enter the probability percentage (%): ", anchor=W).place(x=10,y=90, width=300, height=20) # Parâmetro t do limite de confiança
        tinput = Entry(tab_desc)
        tinput.place(x=10,y=90,width=50,height=20)

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

            Label(tab_desc, text = 'The trust threshold of {}, with t = {} is equal to:'.format(fval,t/100), anchor=W).place(x=10,y=140,width=450,height=20)
            Label(tab_desc, text='u = {}'.format(u), anchor=W, foreground="#00a").place(x=10,y=170, width=450, height=20)
        calculate = Button(tab_desc, text="Calculate", command=calc_ttr)
        calculate.place(x=10,y=110,width=300, height=20)
    Options_frame = Frame(tab_desc)
    Options_frame.pack()
    Options_list = [
        "Mean",
        "Devitation of a Measument",
        "Standard deviation",
        "trust threshold"
    ]
    SelOption = StringVar()
    Options = OptionMenu(Options_frame,SelOption,*Options_list)
    Options.pack()

    def clear_tab_descrive():
        for widget in tab_desc.winfo_children():
            if widget != Options_frame:
                widget.destroy()
    def option_changed(*args):
        clear_tab_descrive()
        if SelOption.get() == "Mean":
            cmean()
        if SelOption.get() == "Devitation of a Measument":
            cdev()
        elif SelOption.get() == "Standard deviation":
            csd()
        elif SelOption.get() == "trust threshold":
            ttr()

    SelOption.trace("w", option_changed)
    SelOption.set(Options_list[0])
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

        Label(tab_ph, text="Enter the acid concentration (mol/L): ", anchor=W).place(x=10,y=70, width=300, height=20) # Acid concentration
        input_Ac_con = Entry(tab_ph)
        input_Ac_con.place(x=10,y=90,width=50,height=20)

        Label(tab_ph, text="Enter the Base concentration (mol/L)", anchor=W).place(x=300,y=70, width=300, height=20) # Basic concentration
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
            # Volume em excesso
            if n_Ac < n_B:
                pH = pH + qn
                pOH = 14 - pH
            # Imprimindo valores
            Label(tab_ph, text='Volume of acid: {} mL'.format(Ac_vol*1000), anchor=W).place(x=100,y=170,width=450,height=20)
            Label(tab_ph, text='Volume of base: {} mL'.format(B_vol*1000), anchor=W).place(x=100,y=190,width=450,height=20)
            Label(tab_ph, text='Concentration of acid: {} mol/L'.format(Ac_con), anchor=W).place(x=100,y=210,width=450,height=20)
            Label(tab_ph, text='Concentration of acid: {} mol/L'.format(B_con), anchor=W).place(x=100,y=230,width=450,height=20)
            # Resultado
            Label(tab_ph, text = 'pH = {:.1f}'.format(pH), anchor=W, foreground='#00a').place(x=100,y=250,width=450,height=20)
            Label(tab_ph, text = 'pOH = {:.1f}'.format(pOH), anchor=W, foreground='#00a').place(x=100,y=270,width=450,height=20)
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

        Label(tab_ph, text="Enter the acid concentration (mol/L): ", anchor=W).place(x=10,y=70, width=300, height=20) # Acid concentration
        input_Ac_con = Entry(tab_ph)
        input_Ac_con.place(x=10,y=90,width=50,height=20)

        Label(tab_ph, text="Enter the Base concentration (mol/L)", anchor=W).place(x=300,y=70, width=300, height=20) # Basic concentration
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
            H_con = max(1e-14, H_con)
            print(H_con)

            if B_vol == Ac_vol:
                pH = 7
                pOH = 7
            elif B_vol > Ac_vol:
                OH_con = (B_con * B_vol - Ac_con * Ac_vol)/(Ac_vol + B_vol)
                pOH = -log10(OH_con)
                pH = 14 - pOH
            else:
                pH = -log10(H_con)
                pOH = 14 - pH
                # Resultado
            Label(tab_ph, text = 'pH = {:.1f}'.format(pH), anchor=W, foreground='#00a').place(x=100,y=300,width=450,height=20)
            Label(tab_ph, text = 'pOH = {:.1f}'.format(pOH), anchor=W, foreground='#00a').place(x=100,y=320,width=450,height=20)

            # Imprimindo valores
            Label(tab_ph, text='Volume of acid: {} ml'.format(Ac_vol*1000), anchor=W).place(x=100,y=200,width=450,height=20)
            Label(tab_ph, text='Volume of base: {} ml'.format(B_vol*1000), anchor=W).place(x=100,y=220,width=450,height=20)
            Label(tab_ph, text='Concentration of acid: {} mol/L'.format(Ac_con), anchor=W).place(x=100,y=240,width=450,height=20)
            Label(tab_ph, text='Concentration of acid: {} mol/L'.format(B_con), anchor=W).place(x=100,y=260,width=450,height=20)
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

        Label(tab_ph, text="Enter the acid concentration (mol/L): ", anchor=W).place(x=10,y=70, width=300, height=20) # Acid concentration
        input_Ac_con = Entry(tab_ph)
        input_Ac_con.place(x=10,y=90,width=50,height=20)

        Label(tab_ph, text="Enter the Base concentration (mol/L)", anchor=W).place(x=300,y=70, width=300, height=20) # Basic concentration
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

            # Calcular número de moles final
            final_acid = max(0, init_acid - init_base)
            final_base = max(0, init_base - init_acid)

            # Volume final
            final_volume = Ac_vol + B_vol

            # Concentrações finais de ácido e base
            final_Ac_con = final_acid / final_volume
            final_B_con = final_base / final_volume

            # Concentração de H+
            H_con = sqrt(kb * final_B_con)
            H_con = max(1e-14,H_con)

            # Calcular pH e pOH
            if Ac_vol == B_vol:
                pH = 7
                pOH = 7
            elif Ac_vol > B_vol:
                H_con = (Ac_con * Ac_vol - B_con * B_vol)/(B_vol + Ac_vol)
                pH = -log10(H_con)
                pOH = 14 - pH

            else:
                pOH = -log10(H_con)
                pH = 14 - pOH
                # Resultado
            Label(tab_ph, text = 'pH = {:.1f}'.format(pH), anchor=W, foreground='#00a').place(x=100,y=300,width=450,height=20)
            Label(tab_ph, text = 'pOH = {:.1f}'.format(pOH), anchor=W, foreground='#00a').place(x=100,y=320,width=450,height=20)

            # Imprimindo valores
            Label(tab_ph, text='Volume of acid: {} mL'.format(Ac_vol*1000), anchor=W).place(x=100,y=200,width=450,height=20)
            Label(tab_ph, text='Volume of base: {} mL'.format(B_vol*1000), anchor=W).place(x=100,y=220,width=450,height=20)
            Label(tab_ph, text='Concentration of acid: {} mol/L'.format(Ac_con), anchor=W).place(x=100,y=240,width=450,height=20)
            Label(tab_ph, text='Concentration of acid: {} mol/L'.format(B_con), anchor=W).place(x=100,y=260,width=450,height=20)
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

        Label(tab_ph, text="Enter the acid concentration (mol/L): ", anchor=W).place(x=10,y=70, width=300, height=20) # Acid concentration
        input_Ac_con = Entry(tab_ph)
        input_Ac_con.place(x=10,y=90,width=50,height=20)

        Label(tab_ph, text="Enter the Base concentration (mol/L)", anchor=W).place(x=300,y=70, width=300, height=20) # Basic concentration
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

            pH = -log10(H)
            pOH = -log(OH)

            # Resultado
            Label(tab_ph, text = 'pH = {:.1f}'.format(round(pH), 2), anchor=W, foreground='#00a').place(x=100,y=350,width=450,height=20)
            Label(tab_ph, text = 'pOH = {:.1f}'.format(round(pOH), 2), anchor=W, foreground='#00a').place(x=100,y=370,width=450,height=20)

            # Imprimindo valores
            Label(tab_ph, text='Volume of acid: {} mL'.format(Ac_vol*1000), anchor=W).place(x=100,y=230,width=450,height=20)
            Label(tab_ph, text='Volume of base: {} mL'.format(B_vol*1000), anchor=W).place(x=100,y=250,width=450,height=20)
            Label(tab_ph, text='Concentration of acid: {} mol/L'.format(Ac_con), anchor=W).place(x=100,y=270,width=450,height=20)
            Label(tab_ph, text='Concentration of acid: {} mol/L'.format(B_con), anchor=W).place(x=100,y=290,width=450,height=20)
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
    def tcurve_sa():
        Label(tab_tcurve, text="Enter the acid volume (mL): ", anchor=W).place(x=10,y=30, width=300, height=20) # Acid volume
        input_Ac_vol = Entry(tab_tcurve)
        input_Ac_vol.place(x=10,y=50,width=50,height=20)

        Label(tab_tcurve, text="Enter the acid concentration (N): ", anchor=W).place(x=10,y=70, width=300, height=20) # Acid concentration
        input_Ac_con = Entry(tab_tcurve)
        input_Ac_con.place(x=10,y=90,width=50,height=20)

        Label(tab_tcurve, text="Enter the Base concentration (N)", anchor=W).place(x=300,y=70, width=300, height=20) # Base concentration
        input_B_con = Entry(tab_tcurve)
        input_B_con.place(x=300,y=90,width=50,height=20)
                

        def generate_tcurve_sa():
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
                    n_Acid = C_Acid * V_acid - C_base * V
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
                plt.plot(V_Base_add, pH, label = 'Titration curve', color='green')
                plt.xlabel('Base volume added (mL)')
                plt.ylabel('pH')
                plt.title('Titration curve')
                plt.legend()
                plt.grid(True)
                plt.show()
            
            # Gráfico dentro de janela
            fig = plt.figure(figsize=(8,8))
            plt.plot(V_Base_add, pH, label = 'Titration curve', color='green')
            plt.xlabel('Base volume added (mL)')
            plt.ylabel('pH')
            plt.title('Titration curve')
            plt.legend()
            plt.grid(True)
                
            graph = FigureCanvasTkAgg(fig, master=tab_tcurve)
            graph.draw()
            graph.get_tk_widget().place(x=10,y=250, width=600, height=250)
            # Botão para mostrar gráfico mais detalhado
            showmore = Button(tab_tcurve, text="Show more", command=show_graph)
            showmore.place(x=300,y=210,width=100, height=20)
        # Botão para calcular
        calculate = Button(tab_tcurve, text="Calculate", command=generate_tcurve_sa)
        calculate.place(x=100,y=130,width=300, height=20)
    def tcurve_sb():
        Label(tab_tcurve, text="Enter the base volume (mL): ", anchor=W).place(x=10,y=30, width=300, height=20) # Base volume
        input_Ac_vol = Entry(tab_tcurve)
        input_Ac_vol.place(x=10,y=50,width=50,height=20)

        Label(tab_tcurve, text="Enter the acid concentration (N): ", anchor=W).place(x=10,y=70, width=300, height=20) # Acid concentration
        input_Ac_con = Entry(tab_tcurve)
        input_Ac_con.place(x=10,y=90,width=50,height=20)

        Label(tab_tcurve, text="Enter the Base concentration (N)", anchor=W).place(x=300,y=70, width=300, height=20) # Base concentration
        input_B_con = Entry(tab_tcurve)
        input_B_con.place(x=300,y=90,width=50,height=20)
        def generate_tcurve_sb():
            # Variáveis de entrada
            try:
                # Entrada
                V_Base = float(input_Ac_vol.get())
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

            # Volume do ácido necessário para a neutralização
            V_Acid = (C_base * V_Base)/C_Acid
            # Criação de uma lista de volumes da base a serem adicionados
            V_Acid_add = np.linspace(0, 2*V_Acid, 500)

            # Cálculo de pH para cada volume adicionado
            pH = []
            for V in V_Acid_add:
                if V < V_Acid:
                    n_Base = C_base * V_Base - C_Acid * V
                    V_total = V_Base + V
                    if n_Base > 0:
                        pOH = -np.log10(n_Base/V_total)
                        pH.append(14 - pOH)
                    else:
                        pH.append(14)
                elif V == V_Acid:
                    pH.append(7) # Ponto de equivalência
                else:
                    n_Base = C_Acid * V - C_base * V_Base
                    V_total = V_Base + V
                    pOH = -np.log10(n_Base/V_total)
                    pH.append(pOH)

            # Imprimindo valores inseridos
            Label(tab_tcurve, text='Concentration of acid: {}'.format(C_Acid), anchor=W).place(x=100,y=170,width=450,height=20)
            Label(tab_tcurve, text='Concentration of base: {}'.format(C_base), anchor=W).place(x=100,y=190,width=450,height=20)
            Label(tab_tcurve, text='Volume of acid: {}mL'.format(V_Base), anchor=W).place(x=100,y=210,width=450,height=20)

            # Gerando gráfico
            def show_graph():
                plt.figure(figsize=(8,6))
                plt.plot(V_Acid_add, pH, label = 'Titration curve', color='blue')
                plt.xlabel('Base volume added (mL)')
                plt.ylabel('pH')
                plt.title('Titration curve')
                plt.legend()
                plt.grid(True)
                plt.show()
            
            # Gráfico dentro de janela
            fig = plt.figure(figsize=(8,8))
            plt.plot(V_Acid_add, pH, label = 'Titration curve', color='blue')
            plt.xlabel('Base volume added (mL)')
            plt.ylabel('pH')
            plt.title('Titration curve')
            plt.legend()
            plt.grid(True)
                
            graph = FigureCanvasTkAgg(fig, master=tab_tcurve)
            graph.draw()
            graph.get_tk_widget().place(x=10,y=250, width=600, height=250)
            # Botão para mostrar gráfico mais detalhado
            showmore = Button(tab_tcurve, text="Show more", command=show_graph)
            showmore.place(x=300,y=210,width=100, height=20)
        # Botão para calcular
        calculate = Button(tab_tcurve, text="Calculate", command=generate_tcurve_sb)
        calculate.place(x=100,y=130,width=300, height=20)
    def tcurve_wasb():
        # Titulação de ácido fraco
        Label(tab_tcurve, text="Enter the initial volume (mL): ", anchor=W).place(x=10,y=30, width=300, height=20) # Acid volume
        input_in_vol = Entry(tab_tcurve)
        input_in_vol.place(x=10,y=50,width=50,height=20)

        Label(tab_tcurve, text="Enter the acid constant dossolution (mL): ", anchor=W).place(x=300,y=30, width=300, height=20) # Constante de dissolução do ácido fraco
        Label(tab_tcurve, text=" * 10^- ", anchor=W).place(x=350,y=50,width=50,height=20)
        input_Ka_significant_digits = Entry(tab_tcurve)
        input_Ka_significant_digits.place(x=300,y=50,width=50,height=20)
        input_Ka_exponent = Entry(tab_tcurve)
        input_Ka_exponent.place(x=400,y=50,width=50,height=20)

        Label(tab_tcurve, text="Enter the acid concentration (N): ", anchor=W).place(x=10,y=70, width=300, height=20) # Acid concentration
        input_Ac_con = Entry(tab_tcurve)
        input_Ac_con.place(x=10,y=90,width=50,height=20)

        Label(tab_tcurve, text="Enter the Base concentration (N)", anchor=W).place(x=300,y=70, width=300, height=20) # Base concentration
        input_B_con = Entry(tab_tcurve)
        input_B_con.place(x=300,y=90,width=50,height=20)

        Label(tab_tcurve, text="Number of acid valence: ", anchor=W).place(x=10,y=110, width=300, height=20) # Acid concentration
        input_Ac_val = Entry(tab_tcurve)
        input_Ac_val.place(x=10,y=130,width=50,height=20)
                

        def generate_tcurve_wasb():
            # Variáveis de entrada
            try:
                Vo = float(input_in_vol.get())
            except ValueError:
                error_non_numeric()

            try:
                Ka_ex = float(input_Ka_exponent.get())
            except ValueError:
                error_non_numeric()
            try:
                Ka_sd =float(input_Ka_significant_digits.get())
            except ValueError:
                error_non_numeric()

            try:
                Ca = float(input_Ac_con.get())
            except ValueError:
                error_non_numeric()

            try:
                Cb = float(input_B_con.get())
            except ValueError:
                error_non_numeric()

            try:
                Ac_val = float(input_Ac_val.get())
            except ValueError:
                error_non_numeric()

            # Valor de Ka e pKa
            Ka = Ka_sd * 10 ** -Ka_ex
            pKa = -log10(Ka)
            # pH = 1/2 * pKa - 1/2 * log(Ca)

            # Expressão logarítima para valores do gráfico
            V_Base = (Ca * Vo)/Cb
            V_Base_add = np.linspace(0, 2*V_Base, 500)
            # Constantes de titulação
            pH = []
            for V in V_Base_add:
                if (V == 0):
                    V_total = Vo
                    pH.append(1/2 * pKa - log(Ca))
                elif (V < Vo):
                    V_total = Vo + V
                    H = -log(Ca * Ka) * 1/2
                    Cs = Ac_val/(H/(V_total))
                    pH.append(pKa + log(Ca/Cs))
                elif (V == Vo): # Ponto de equivalência
                    pH.append(7)
                else:
                    V_exc = (V - Vo)
                    V_total = Vo + V_exc
                    OH = Cb * V_exc/V_total
                    pOH = -log(OH)
                    pH.append(14 - pOH)
                print(pH)

            # Gerando gráfico
            def show_graph():
                plt.figure(figsize=(8,6))
                plt.plot(V_Base_add, pH, label = 'Titration curve', color='green')
                plt.xlabel('Base volume added (mL)')
                plt.ylabel('pH')
                plt.title('Titration curve')
                plt.legend()
                plt.grid(True)
                plt.show()
            
            # Gráfico dentro de janela
            fig = plt.figure(figsize=(8,8))
            plt.plot(V_Base_add, pH, label = 'Titration curve', color='green')
            plt.xlabel('Base volume added (mL)')
            plt.ylabel('pH')
            plt.title('Titration curve')
            plt.legend()
            plt.grid(True)
                
            graph = FigureCanvasTkAgg(fig, master=tab_tcurve)
            graph.draw()
            graph.get_tk_widget().place(x=10,y=250, width=600, height=250)
            # Botão para mostrar gráfico mais detalhado
            showmore = Button(tab_tcurve, text="Show more", command=show_graph)
            showmore.place(x=300,y=210,width=100, height=20)
        # Botão para calcular
        calculate = Button(tab_tcurve, text="Calculate", command=generate_tcurve_wasb)
        calculate.place(x=100,y=150,width=300, height=20)
    def tcurve_wbsa():
        # Titulação de base fraca
        Label(tab_tcurve, text="Enter the initial volume (mL): ", anchor=W).place(x=10,y=30, width=300, height=20) # Acid volume
        input_in_vol = Entry(tab_tcurve)
        input_in_vol.place(x=10,y=50,width=50,height=20)

        Label(tab_tcurve, text="Enter the base constant dossolution (mL): ", anchor=W).place(x=300,y=30, width=300, height=20) # Constante de dissolução do ácido fraco
        Label(tab_tcurve, text=" * 10^- ", anchor=W).place(x=350,y=50,width=50,height=20)
        input_Kb_significant_digits = Entry(tab_tcurve)
        input_Kb_significant_digits.place(x=300,y=50,width=50,height=20)
        input_Kb_exponent = Entry(tab_tcurve)
        input_Kb_exponent.place(x=400,y=50,width=50,height=20)

        Label(tab_tcurve, text="Enter the acid concentration (N): ", anchor=W).place(x=10,y=70, width=300, height=20) # Acid concentration
        input_Ac_con = Entry(tab_tcurve)
        input_Ac_con.place(x=10,y=90,width=50,height=20)

        Label(tab_tcurve, text="Enter the Base concentration (N)", anchor=W).place(x=300,y=70, width=300, height=20) # Base concentration
        input_B_con = Entry(tab_tcurve)
        input_B_con.place(x=300,y=90,width=50,height=20)

        Label(tab_tcurve, text="Number of acid valence: ", anchor=W).place(x=10,y=110, width=300, height=20) # Acid concentration
        input_Ac_val = Entry(tab_tcurve)
        input_Ac_val.place(x=10,y=130,width=50,height=20)
                

        def generate_tcurve_wasb():
            # Variáveis de entrada
            try:
                Vo = float(input_in_vol.get())
            except ValueError:
                error_non_numeric()

            try:
                Kb_ex = float(input_Kb_exponent.get())
            except ValueError:
                error_non_numeric()
            try:
                Kb_sd =float(input_Kb_significant_digits.get())
            except ValueError:
                error_non_numeric()

            try:
                Ca = float(input_Ac_con.get())
            except ValueError:
                error_non_numeric()

            try:
                Cb = float(input_B_con.get())
            except ValueError:
                error_non_numeric()

            try:
                Ac_val = float(input_Ac_val.get())
            except ValueError:
                error_non_numeric()

            # Valor de Ka e pKa
            Kb = Kb_sd * 10 ** -Kb_ex
            pKb = -log10(Kb)
            # pH = 1/2 * pKa - 1/2 * log(Ca)

            # Expressão logarítima para valores do gráfico
            V_Acid = (Ca * Vo)/Cb
            V_Acid_add = np.linspace(0, 2*V_Acid, 500)
            # Constantes de titulação
            pH = []
            for V in V_Acid_add:
                if (V == 0):
                    V_total = Vo
                    pOH = 1/2 * pKb - log(Cb)
                    pH.append(14 - pOH)
                elif (V < Vo):
                    V_total = Vo + V
                    OH = -log(Ca * Kb) * 1/2
                    Cs = Ac_val/(OH/(V_total))
                    pOH = pKb + log(Cb/Cs)
                    pH.append(14 - pOH)
                elif (V == Vo): # Ponto de equivalência
                    pOH = (1/2) * pKb - (1/2) * log(Cs)
                    pH.append(7 - pOH)
                else:
                    V_exc = (V - Vo)
                    V_total = Vo + V_exc
                    H = Cb * V_exc/V_total
                    pH.append(-log(H))
                print(pH)

            # Gerando gráfico
            def show_graph():
                plt.figure(figsize=(8,6))
                plt.plot(V_Acid_add, pH, label = 'Titration curve', color='blue')
                plt.xlabel('Base volume added (mL)')
                plt.ylabel('pH')
                plt.title('Titration curve')
                plt.legend()
                plt.grid(True)
                plt.show()
            
            # Gráfico dentro de janela
            fig = plt.figure(figsize=(8,8))
            plt.plot(V_Acid_add, pH, label = 'Titration curve', color='blue')
            plt.xlabel('Base volume added (mL)')
            plt.ylabel('pH')
            plt.title('Titration curve')
            plt.legend()
            plt.grid(True)
                
            graph = FigureCanvasTkAgg(fig, master=tab_tcurve)
            graph.draw()
            graph.get_tk_widget().place(x=10,y=250, width=600, height=250)
            # Botão para mostrar gráfico mais detalhado
            showmore = Button(tab_tcurve, text="Show more", command=show_graph)
            showmore.place(x=300,y=210,width=100, height=20)
        # Botão para calcular
        calculate = Button(tab_tcurve, text="Calculate", command=generate_tcurve_wasb)
        calculate.place(x=100,y=150,width=300, height=20)

    
    # Opções
    Options_frame = Frame(tab_tcurve)
    Options_frame.pack()
    Options_list = [
        "titration of strong acid",
        "titration of strong base",
        "titration of weak acid to strong base",
        "titration of weak base to strong acid",
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
        if SelOption.get() == "titration of strong acid":
            tcurve_sa()
        if SelOption.get() == "titration of strong base":
            tcurve_sb()
        elif SelOption.get() == "titration of weak acid to strong base":
            tcurve_wasb()
        elif SelOption.get() == "titration of weak base to strong acid":
            tcurve_wbsa()

    SelOption.trace("w", option_changed)
    SelOption.set(Options_list[0])

def agcurve():
    def error_non_numeric():
        Label(tab_ph, text = "ERROR: Non numeric value", anchor=W, foreground='#a00').place(x=100,y=170,width=450,height=20)
    Label(tab_agcurve, text="Enter the ananlyte volume (mL): ", anchor=W).place(x=10,y=30, width=300, height=20) # Base volume
    input_V_Analyte = Entry(tab_agcurve)
    input_V_Analyte.place(x=10,y=50,width=50,height=20)

    Label(tab_agcurve, text="Enter the analityte concentration (mols/mL): ", anchor=W).place(x=10,y=70, width=300, height=20) # Acid concentration
    input_C_Analyte = Entry(tab_agcurve)
    input_C_Analyte.place(x=10,y=90,width=50,height=20)

    Label(tab_agcurve, text="Enter the maximum volume of titrant used (mL)", anchor=W).place(x=300,y=30, width=300, height=20) # Base concentration
    input_Titrant_Vol = Entry(tab_agcurve)
    input_Titrant_Vol.place(x=300,y=50,width=50,height=20)

    Label(tab_agcurve, text="Enter concentration of titrant (mol/L)", anchor=W).place(x=300,y=70, width=300, height=20) # Base concentration
    input_Titrant_Con = Entry(tab_agcurve)
    input_Titrant_Con.place(x=300,y=90,width=50,height=20)
    def agcalc():
        try:
            # Entrada
            V_Analyte = float(input_V_Analyte.get()) / 1000
        except ValueError:
            # Erro
            error_non_numeric()

        try:
            # Entrada
            C_Analyte = float(input_C_Analyte.get())
        except ValueError:
            error_non_numeric()

        try:
            # Entrada
            Vmax_Titrant = float(input_Titrant_Vol.get()) / 1000
        except ValueError:
            error_non_numeric()

        try:
            # Entrada
            C_Titrant = float(input_Titrant_Con.get())
        except ValueError:
            error_non_numeric()

        # Imprimindo valores inseridos
        Label(tab_agcurve, text='Volume of analyte: {} L'.format(V_Analyte), anchor=W).place(x=100,y=170,width=450,height=20)
        Label(tab_agcurve, text='Concentration of analyte: {} mols/L'.format(C_Analyte), anchor=W).place(x=100,y=190,width=450,height=20)
        Label(tab_agcurve, text='Maximum volume of titrant: {} L'.format(Vmax_Titrant), anchor=W).place(x=100,y=210,width=450,height=20)
        Label(tab_agcurve, text="Concentration of titrant: {} mols/L".format(C_Titrant), anchor=W).place(x=100,y=230,width=450,height=20)

        # Calcular o pAg e gerar gráfico
        def calc_pAg(concentration, volume):
            return -np.log10(concentration * volume)
        V_Titrant = np.linspace(0.001,Vmax_Titrant,100)
        pAg = [calc_pAg(C_Titrant, volume) for volume in V_Titrant]
                
        def show_graph():
            plt.figure(figsize=(8,6))
            plt.plot(V_Titrant, pAg, label = 'Titration curve', color='orange')
            plt.xlabel('Volume of titrant (L)')
            plt.ylabel('pAg')
            plt.title('Argetometric Titration curve')
            plt.legend()
            plt.grid(True)
            plt.show()
                
        #Gráfico dentro de janela
        fig = plt.figure(figsize=(8,8))
        plt.plot(V_Titrant, pAg, label = 'Titration curve', color='orange')
        plt.xlabel('Volume of titrant (L)')
        plt.ylabel('pAg')
        plt.title('Argetometric Titration curve')
        plt.legend()
        plt.grid(True)
                    
        graph = FigureCanvasTkAgg(fig, master=tab_agcurve)
        graph.draw()
        graph.get_tk_widget().place(x=10,y=270, width=600, height=250)
        # Botão para mostrar gráfico mais detalhado
        showmore = Button(tab_agcurve, text="Show more", command=show_graph)
        showmore.place(x=500,y=210,width=100, height=20)
    # Botão para calcular
    calculate = Button(tab_agcurve, text="Calculate", command=agcalc)
    calculate.place(x=100,y=130,width=300, height=20)

def calc_fa():
    def error_non_numeric():
        Label(tab_ph, text = "ERROR: Non numeric value", anchor=W, foreground='#a00').place(x=100,y=170,width=450,height=20)
    Label(tab_fa, text="Enter the PM value (g/mol): ", anchor=W).pack()# Base volume
    input_PM = Entry(tab_fa)
    input_PM.pack()

    Label(tab_fa, text="Enter the M value (mol/L)", anchor=W).pack() # Base concentration
    input_M = Entry(tab_fa)
    input_M.pack()

    def fa():
        # Recebendo valores
        try:
            PM = float(input_PM.get()) / 1000 # Peso molecular
            print("PM = {}".format(PM))
        except ValueError:
            # Erro
            error_non_numeric()

        try:
            M = float(input_M.get()) / 1000 # Molaridade
            print("M = {}".format(M))
        except ValueError:
            # Erro
            error_non_numeric()

        # Calculando o valor de FA
        Fa = (PM * M)/1000 # Fator analítico
        print("PM = {}".format(PM))
        print("M = {}".format(M))
        print("FA = {}".format(Fa))
        # Label(tab_ph, text='Ka: {}'.format(ka), anchor=W).place(x=100,y=280,width=450,height=20)
        values = Label(tab_fa, text="PM = {}\n M = {}".format(PM,M).format(Fa), anchor=W)
        resp = Label(tab_fa, text="FA = {}".format(Fa), anchor=W, foreground='#00a')
        values.pack()
        resp.pack()
    # Botão
    calculate = Button(tab_fa, text="Calculate", command=fa)
    calculate.pack()

# Apagar esta função quando finalizar
def Nulo():
    print("")

######################################### Unit Converter ##############################################################
##### Volume #######
def volume_window():
    volc_win = Tk()
    volc_win.title("Convert volume")
    volc_win.geometry('260x280')
    def error_non_numeric():
        Label(volc_win, text = "ERROR: Non numeric value", anchor=W, foreground='#a00').place(x=100,y=170,width=450,height=20)
    def volume_ml():
        Label(volc_win, text="Enter volume in milliters (mL): ", anchor=W).pack()# mL volume
        input_mL = Entry(volc_win)
        input_mL.pack()

        def calc_volume():
            # Recebendo valores
            try:
                mL = float(input_mL.get())
                print("mL volume = {}".format(mL))
            except ValueError:
                # Erro
                error_non_numeric()
            # mL to L
            L = mL / 1000
            print(L)
            resp = Label(volc_win, text = "The volume in Liters is {}L".format(L), anchor=W, foreground='#00a')
            resp.pack()
        calculate = Button(volc_win, text="Calculate", command=calc_volume)
        calculate.pack()
    def volume_L():
        Label(volc_win, text="Enter volume in Liters (L): ", anchor=W).pack()# L volume
        input_L = Entry(volc_win)
        input_L.pack()

        def calc_volume():
            # Recebendo valores
            try:
                L = float(input_L.get())
                print("L volume = {}".format(L))
            except ValueError:
                # Erro
                error_non_numeric()
            # mL to L
            mL = L * 1000
            print(L)
            resp = Label(volc_win, text = "The volume in Liters is {}L".format(mL), anchor=W, foreground='#00a')
            resp.pack()
        calculate = Button(volc_win, text="Calculate", command=calc_volume)
        calculate.pack()
    # Tipo de conversão
    Options_frame = Frame(volc_win)
    Options_frame.pack()
    Options_list = [
        "mL to L",
        "L to mL"
    ]
    SelOption = StringVar()
    Options = OptionMenu(Options_frame,SelOption,*Options_list)
    Options.pack()

    def clear_volc_win():
        for widget in volc_win.winfo_children():
            if widget != Options_frame:
                widget.destroy()
    def option_changed(*args):
        clear_volc_win()
        if SelOption.get() == "mL to L":
            volume_ml()
        elif SelOption.get() == "L to mL":
            volume_L()

    SelOption.trace("w", option_changed)
    SelOption.set(Options_list[0])
##### Molaridade #######
def molarity_window():
    mol_win = Tk()
    mol_win.title("Volume unit")
    mol_win.geometry('260x280')
    def error_non_numeric():
        Label(mol_win, text = "ERROR: Non numeric value", anchor=W, foreground='#a00').place(x=100,y=170,width=450,height=20)
    def molarity():
        Label(mol_win, text="Enter number of mols: ", anchor=W).pack()# L volume
        input_Mol = Entry(mol_win)
        input_Mol.pack()
        Label(mol_win, text="Enter volume (L): ", anchor=W).pack()# L volume
        input_Vol = Entry(mol_win)
        input_Vol.pack()
        def calc_molarity():
            # Recebendo valores
            try:
                Vol = float(input_Vol.get())
            except ValueError:
            # Erro
                error_non_numeric()
            try:
                Mol = float(input_Mol.get())
            except ValueError:
            # Erro
                error_non_numeric()

            # Calcular molaridade
            M = Mol/Vol
            values = Label(mol_win, text = "n° of mols = {} \n Volume = {}L".format(Vol,Mol), anchor=W)
            resp = Label(mol_win, text = "M = {}mols/L".format(M), anchor=W, foreground='#00a')
            values.pack()
            resp.pack()
        calculate = Button(mol_win, text="Calculate", command=calc_molarity)
        calculate.pack()
    molarity()
######################################### About Page ##################################################################
def about():
    about = Tk()
    about.title(Versioner['name'])
    about.geometry('400x300')
    about.resizable(False,False)
    # Elementos da página
    name1 = Label(about, text=Versioner['name'],font={"bold",16})
    version = Label(about, text="Version {} {}".format(Versioner['version'],Versioner['status']))
    author = Label(about, text="(c) 2024 João Marcelo Coelho Pacheco, all rights reserved")

    name1.pack()
    version.pack()
    author.pack()

    def web_doc():
        web.open("https://github.com/JoaoM199/integrative-project")

    doc_page = Button(about, text="Documentation", command=web_doc)
    doc_page.pack(anchor="s")
    about.mainloop()

######################################### Main Window #################################################################
app = Tk()
app.title("{} {} {}".format(Versioner['name'],Versioner['version'],Versioner['status']))
app.geometry('700x600')

# Add tabs
tabs = ttk.Notebook(app)
tabs.pack()

tab_desc = Frame(tabs, width=500, height=300)
tab_desc.pack()
descritive()
tabs.add(tab_desc, text="Descriptive measures")

tab_ph = Frame(tabs, width=600, height=600)
tab_ph.pack(fill='both', expand=1)
phc()
tabs.add(tab_ph, text="pH & pOH")

tab_tcurve = Frame(tabs, width=700, height=900)
tab_tcurve.pack(fill="both",expand=1)
tcurve()
tabs.add(tab_tcurve, text="Titration curve")

tab_agcurve = Frame(tabs, width=600, height=600)
tab_agcurve.pack(fill='both',expand=1)
agcurve()
tabs.add(tab_agcurve, text="Argetometric Titration curve")

tab_fa = Frame(tabs, width=500, height=500)
tab_fa.pack(fill='both',expand=1)
calc_fa()
tabs.add(tab_fa, text="Analitical Factor")

# Menubar
menubar = Menu(app)
mfile = Menu(menubar, tearoff=0)
'''
mfile.add_command(label='Save as', command=Nulo)
mfile.add_command(label='print', command=Nulo)
mfile.add_command(label='print', command=Nulo)
mfile.add_command(label='clear', command=Nulo)
mfile.add_separator()
'''
mfile.add_command(label='exit', command=app.quit)
menubar.add_cascade(label="File",menu=mfile)

tools = Menu(menubar, tearoff=0)
tools.add_command(label='convert volume', command=volume_window)
tools.add_command(label="molarity", command=molarity_window)
menubar.add_cascade(label='Tools', menu=tools)

'''
settings = Menu(menubar, tearoff=0)
settings.add_command(label='Preferences', command=Nulo)
menubar.add_cascade(label='settings', menu=settings)
'''

help = Menu(menubar, tearoff=0)
help.add_command(label='about', command=about)
menubar.add_cascade(label='help', menu=help)

app.config(menu=menubar)
app.mainloop()