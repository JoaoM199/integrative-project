'''
    Projeto Integrador Transdisciplinar em Ciência da Computação II
    Nome do projeto: AQCALC
    Aluno: João Marcelo Coelho Pacheco
    RGM: 23163054
    Tutores: Thyago Alves Sobreira, Leonardo Akira Teixeira Dantas Kamimura, Vagner da Silva
    Universidade: Cruzeiro do Sul Virtual

    Descrição
    Uma calculadora científica para cálculos epecíficos da Química Analítica. Trata-se de meu projeto final da minha graduação em Ciência da Computação. Inicialmente era um programa executável para PC windows e Linux (ou similares), tendo em vista que o uso de serviços online e smartphones, resolvi mudar o escopo desse projeto para um site/aplicativo para que mais profissionais e estudantes da área da Química, Engenharia, Farmácia entre outros possam usufruir do meu aplicativo.
'''

from flask import Flask, render_template, request
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import json

# Funções
from .functions.deviation import calculate_deviation, calculate_deviation_mean
from .functions.sd import calc_sd, calc_rsd
from .functions.confidence import calc_critical_value, calc_error_margin, calc_confidence_interval, calc_u

app = Flask(__name__)

# Definir rotas
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/descriptive', methods=['GET', 'POST'])
def descriptive():
    # iniciando variáveis para evitar erros
    calculation_type = None
    result = None
    values = None
    mean = None
    deviation_values= None
    sd = None
    rsd = None
    t_value = None
    critical_value = None
    error_margin = None
    u = None
    confidence_interval = None
    mean_deviation = None
    
    if request.method == 'POST':
        calculation_type = request.form.get('calculation_type')
        values_str = request.form.get('values')

        print(f"calculation_type: {calculation_type}")
        print(f"values_str: {values_str}")
        if values_str:
            values = [float(x) for x in request.form.get('values').split(',')]
            print(f"values { values }")
            if calculation_type == 'mean':
                result = np.mean(values)
                print(f"result:{result}")
            elif calculation_type == 'deviation':
                deviation_values = calculate_deviation(values)
                result = calculate_deviation_mean(deviation_values)
            elif calculation_type == "sd":
                sd = calc_sd(values)
                rsd = calc_rsd(values)
            elif calculation_type == "confidence":
                t_value = float(request.form.get('trust'))
                print(t_value)
                critical_value = calc_critical_value(values, t_value) 
                error_margin = calc_error_margin(values, critical_value)
                confidence_interval = calc_confidence_interval(values, error_margin)
                u = calc_u(confidence_interval)
                

    return render_template('descriptive.html', 
                           calculation_type=calculation_type, 
                           result=result, 
                           values=values, 
                           deviation_values=deviation_values, 
                           mean_deviation=mean_deviation,
                           sd=sd, 
                           rsd=rsd, 
                           mean=mean, 
                           t_value=t_value, 
                           critical_value=critical_value, 
                           error_margin=error_margin, 
                           confidence_interval=confidence_interval,
                           u=u)
'''
@app.route('/phcalc', methods=['GET', 'POST'])
def phcalc():
    # iniciando variáveis para evitar erros
    calculation_type = None
    acid_vol_str = None
    base_vol_str = None
    acid_con_str = None
    base_con_str = None
    input_ka_significant_digits_str = None
    input_ka_exponent_str = None
    acid_vol = None
    base_vol = None
    acid_con = None
    base_con = None
    input_ka_significant_digits = None
    input_ka_exponent = None
    n_Ac = None
    n_B = None
    pH = None
    pOH = None
    ka = None
    init_acid = None
    init_base = None
    final_acid = None
    final_base = None
    final_volume = None
    final_acid_con = None
    final_base_con = None
    H_con = None
    OH_con = None
    
    if request.method == 'POST':
        calculation_type = request.form.get('calculation_type')

        # verificando se as entradas existem
        acid_vol_str = request.form.get('acid_vol')
        base_vol_str = request.form.get('base_vol')
        acid_con_str = request.form.get('acid_con')
        base_con_str = request.form.get('base_con')
        input_ka_significant_digits_str = request.form.get('input_ka_significant_digits')
        input_ka_exponent_str = request.form.get('input_ka_exponent')

        print(f"calculation_type: {calculation_type}")
        if calculation_type == 'phc_strong':
            if acid_vol_str and base_vol_str and acid_con_str and base_con_str and input_ka_significant_digits_str and input_ka_exponent_str:
                try:
                    # passando valores para as variáveis
                    acid_vol = float(acid_vol_str)
                    base_vol = float(base_vol_str)
                    acid_con = float(acid_con_str)
                    base_con = float(base_con_str)
                    input_ka_significant_digits = float(input_ka_significant_digits_str)
                    input_ka_exponent = float(input_ka_exponent_str)
                except ValueError:
                    print("Erro na conversão dos valores para float")
                    return render_template('phcalc.html', calculation_type=calculation_type, pH=pH, pOH=pOH)
            
            if calculation_type == 'phc_strong' and acid_vol and base_vol and acid_con and base_con:
                # Converter para litros
                acid_vol = acid_vol/1000
                base_vol = base_vol/1000
                # Quantidade de substância
                n_Ac = acid_vol * acid_con
                n_B = base_vol * base_con
                # calcular substância em excesso
                if n_Ac > n_B:
                    qn = n_Ac - n_B
                else:
                    qn = n_B - n_Ac
                # concentração da espécie em excesso
                n_con = qn/(acid_vol + base_vol)
                # calcular pH e pOH
                if n_Ac > n_B:
                    pH = -np.log10(n_con)
                else:
                    pOH = -np.log10(n_con)
                # calcular pH a partir do pOH ou vice-versa
                if n_Ac > n_B:
                    pOH = 14 - pH
                else:
                    pH = 14 - pOH
                # volumes em equilíbrio
                if n_Ac == n_B:
                    pH = 7
                    pOH = 7
                else:
                    pH = pH
                    pOH = pOH
                if n_Ac < n_B:
                    pH = pH + qn
                    pOH = 14 - pH

            return render_template('phcalc.html', 
                               calculation_type=calculation_type, 
                               pH=pH, 
                               pOH=pOH)
        
        if calculation_type == "phc_weak_acid":
            if acid_vol_str and base_vol_str and acid_con_str and base_con_str and input_ka_significant_digits_str and input_ka_exponent_str:
                try:
                    # passando valores para as variáveis
                    acid_vol = float(acid_vol_str)
                    base_vol = float(base_vol_str)
                    acid_con = float(acid_con_str)
                    base_con = float(base_con_str)
                    input_ka_significant_digits = float(input_ka_significant_digits_str)
                    input_ka_exponent = float(input_ka_exponent_str)
                except ValueError:
                    print("Erro na conversão dos valores para float")
                    return render_template('phcalc.html', calculation_type=calculation_type, pH=pH, pOH=pOH)
            
            if calculation_type == "phc_weak_acid" and acid_vol and base_vol and acid_con and base_con and input_ka_exponent and input_ka_exponent:
                # calcular a constante do ácido
                ka = input_ka_significant_digits * np.pow(10,input_ka_exponent)
                # converter volumes para litros
                acid_vol = acid_vol/1000
                base_vol = base_vol/1000
                # calcular número de moles inicial
                init_acid = acid_con * acid_vol
                init_base = base_con * base_vol
                # Calcular número de moles final
                final_acid = max(0, init_acid - init_base)
                final_base = max(0, init_base - init_acid)
                # volume finaç
                final_volume = acid_vol + base_vol
                # concentrações finais de H+
                final_acid_con = final_acid / final_volume
                final_base_con = final_base / final_volume
                # concentração de H+
                H_con = np.sqrt(ka * final_acid_con)
                H_con = max(1e-14, H_con)

                if base_vol == acid_vol:
                    pH = 7
                    pOH = 7
                elif base_vol > acid_vol:
                    OH_con = (base_con * base_vol - acid_con * acid_vol)/(acid_vol + base_vol)
                    pOH = -np.log10(OH_con)
                    pH = 14 - pOH
                else:
                    pH = -np.log10(H_con)
                    pOH = 14 - pH
                return render_template('phcalc.html', 
                               calculation_type=calculation_type, 
                               pH=pH, 
                               pOH=pOH)
'''
@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == "__main__":
    app.run(debug=True)