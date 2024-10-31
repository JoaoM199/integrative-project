import numpy as np
from scipy.optimize import fsolve
import matplotlib.pyplot as plt
import base64
import io

def tcurve_strong_acid(acid_vol, acid_con, base_con):
    # Volume da base necessário para neutralização
    base_vol = (acid_con * acid_vol)/base_con
    # Criação de uma lista de volumes da base a serem adicionados
    base_vol_add = np.linspace(0, 2 * base_vol, 500)
    # calculando pH para cada volume adicionado
    pH = []
    for v in base_vol_add:
        if v < base_vol:
            acid_n = acid_con * acid_vol - base_con * v
            total_vol = acid_vol + v
            if acid_n > 0:
                pH.append(-np.log10(acid_n))
            else:
                pH.append(0)
        elif v == base_vol:
            pH.append(7)
        else:
            base_n = base_con * v - acid_con * acid_vol
            total_vol = acid_vol + v
            pOH = -np.log10(base_n/total_vol)
            pH.append(14 - pOH)

    # plotando gráfico
    plt.figure(figsize=(8,6))
    plt.plot(base_vol_add, pH, label = 'Titration curve', color='green')
    plt.xlabel('Base volume added (mL)')
    plt.ylabel('pH')
    plt.title('Titration curve')
    plt.grid(True)
    # converter gráfico para base64
    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)
    img_base64 = base64.b64encode(buf.getvalue()).decode("utf-8")
    buf.close()

    return img_base64
def tcurve_strong_base(base_vol, base_con, acid_con):
    # Volume da base necessário para neutralização
    acid_vol = (base_con * base_vol)/acid_con
    # Criação de uma lista de volumes da base a serem adicionados
    acid_vol_add = np.linspace(0, 2 * acid_vol, 500)
    # calculando pH para cada volume adicionado
    pH = []
    for v in acid_vol_add:
        if v < acid_vol:
            base_n = base_con * acid_vol - acid_con * v
            total_vol = acid_vol + v
            if base_n > 0:
                pH.append(-np.log10(base_n))
            else:
                pH.append(0)
        elif v == acid_vol:
            pH.append(7)
        else:
            acid_n = acid_con * v - base_con * base_vol
            total_vol = base_vol + v
            pOH = -np.log10(acid_n/total_vol)
            pH.append(14 - pOH)

    # plotando gráfico
    plt.figure(figsize=(8,6))
    plt.plot(acid_vol_add, pH, label = 'Titration curve', color='blue')
    plt.xlabel('Base volume added (mL)')
    plt.ylabel('pH')
    plt.title('Titration curve')
    plt.grid(True)
    # converter gráfico para base64
    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)
    img_base64 = base64.b64encode(buf.getvalue()).decode("utf-8")
    buf.close()

    return img_base64
def tcurve_weak_acid(acid_vol, acid_con, base_con, input_ka_significant_digits, input_ka_exponent, acid_valence):
    # ka e pka
    ka = input_ka_significant_digits * np.pow(10,input_ka_exponent)
    pKa = -np.log10(ka)
    # pH = 1/2 * pKa - 1/2 * log(Ca)

    # expressão logarítimica para os valores do gráfico
    base_vol_eq = (acid_con * acid_vol) / base_con
    base_vol_add = np.linspace(0, 2 * base_vol_eq, 500)
    # constante de titulação
    pH = []
    for v in base_vol_add:
        total_vol = acid_vol + v
        # Antes do ponto de equivalência
        if (v < base_vol_eq):
            acid_remaining = (acid_con * (acid_vol - v)) / total_vol
            salt_concentration = (base_con * v) / total_vol

            # Evitar valores menores que 0 e maiores que 14
            if acid_remaining > 0:
                pH_value = pKa + np.log10(salt_concentration / acid_remaining)
            else:
                pH_value = 0
            
            pH.append(max(0, min(14, pH_value)))
        
        # Ponto de equivalência
        elif v == base_vol_eq:
            pH.append(pKa)
        
        # Após o ponto de equivalência
        else:
            excess_base = (v - base_vol_eq) * base_con / total_vol
            if excess_base > 0:
                pOH = -np.log10(excess_base)
                pH_value = 14 - pOH
            else:
                pH_value = 14
            pH.append(max(0, min(14, pH_value)))
    
    # plotando gráfico
    plt.figure(figsize=(8,6))
    plt.plot(base_vol_add, pH, label = 'Titration curve', color='green')
    plt.xlabel('Base volume added (mL)')
    plt.ylabel('pH')
    plt.title('Titration curve')
    plt.grid(True)
    # converter gráfico para base64
    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)
    img_base64 = base64.b64encode(buf.getvalue()).decode("utf-8")
    buf.close()

    return img_base64
def tcurve_weak_base(base_vol, base_con, acid_con, input_kb_significant_digits, input_kb_exponent, base_valence):
    # kb e pKb
    kb = input_kb_significant_digits * np.pow(10, input_kb_exponent)
    pKb = -np.log10(kb)

        # expressão logarítimica para os valores do gráfico
    acid_vol_eq = (base_con * base_vol) / acid_con
    acid_vol_add = np.linspace(0, 2 * acid_vol_eq, 500)
    # constante de titulação
    pH = []
    for v in acid_vol_add:
        total_vol = base_vol + v
        # Antes do ponto de equivalência
        if (v < acid_vol_eq):
            base_remaining = (base_con * (base_vol - v)) / total_vol
            salt_concentration = (acid_con * v) / total_vol

            # Evitar valores menores que 0 e maiores que 14
            if base_remaining > 0:
                pOH = pKb + np.log10(salt_concentration / base_remaining)
                pH_value = 14 - pOH
            else:
                pH_value = 14
            
            pH.append(max(0, min(14, pH_value)))
        
        # Ponto de equivalência
        elif v == acid_vol_eq:
            pOH = 14 - pKb
            pH.append(pOH)
        
        # Após o ponto de equivalência
        else:
            excess_acid = (v - acid_vol_eq) * acid_con / total_vol
            if excess_acid > 0:
                pOH = -np.log10(excess_acid)
                pH_value = pOH
            else:
                pH_value = 0
            pH.append(max(0, min(14, pH_value)))

    # plotando gráfico
    plt.figure(figsize=(8,6))
    plt.plot(acid_vol_add, pH, label = 'Titration curve', color='blue')
    plt.xlabel('Base volume added (mL)')
    plt.ylabel('pH')
    plt.title('Titration curve')
    plt.grid(True)
    # converter gráfico para base64
    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)
    img_base64 = base64.b64encode(buf.getvalue()).decode("utf-8")
    buf.close()

    return img_base64
