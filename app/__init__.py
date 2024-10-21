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
    n = None
    sd = None
    rsd = None
    t_value = None
    dof = None
    critical_value = None
    error_margin = None
    u = None
    confidence_interval = None
    
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
                mean = np.mean(values)
                deviation_values= np.abs(values - mean).tolist()
                result = np.mean(deviation_values)
                print(f"mean: {mean}")
                print(f"deviation_values: {deviation_values}")
                print(f"result: {result}")
            elif calculation_type == "sd":
                mean = np.mean(values)
                # standard deviation
                sd = np.std(values)
                # relative standard deviation
                rsd = (sd/mean) * 100
                print(f"mean: {mean}")
                print(f"sd: {sd}")
                print(f"rsd: {sd}")
            elif calculation_type == "confidence":
                t_value = float(request.form.get('trust'))
                mean = np.mean(values)
                sd = np.std(values, ddof=1)
                n = len(values)
                dof = n - 1

                critical_value = stats.t.ppf((1 + t_value / 100) / 2.0, dof)
                error_margin = critical_value * (sd/np.sqrt(n))
                confidence_interval  = (mean - error_margin, mean + error_margin)
                u = float(confidence_interval[0]), float(confidence_interval[1])

                print(f"critical_value: {critical_value}")
                print(f"error_margin: {error_margin}")
                print(f"u: {u}")

    return render_template('descriptive.html', 
                           calculation_type=calculation_type, 
                           result=result, values=values, 
                           deviation_values=deviation_values, 
                           sd=sd, 
                           rsd=rsd, 
                           mean=mean, 
                           t_value=t_value, 
                           critical_value=critical_value, 
                           error_margin=error_margin, 
                           u=u)
@app.route('/phcalc', methods=['GET', 'POST'])
def phcalc():
        # iniciando variáveis para evitar erros
    calculation_type = None
    acid_vol_str = None
    base_vol_str = None
    acid_con_str = None
    base_con_str = None
    acid_vol = None
    base_vol = None
    acid_con = None
    base_con = None
    n_Ac = None
    n_B = None
    pH = None
    pOH = None
    
    if request.method == 'POST':
        calculation_type = request.form.get('calculation_type')

        # verificando se as entradas existem
        acid_vol_str = request.form.get('acid_vol')
        base_vol_str = request.form.get('base_vol')
        acid_con_str = request.form.get('acid_con')
        base_con_str = request.form.get('base_con')
        


        print(f"calculation_type: {calculation_type}")
        if calculation_type == 'phc_strong':
            if acid_vol_str and base_vol_str and acid_con_str and base_con_str:
                try:
                    # passando valores para as variáveis
                    acid_vol = float(acid_vol_str)
                    base_vol = float(base_vol_str)
                    acid_con = float(acid_con_str)
                    base_con = float(base_con_str)
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


@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == "__main__":
    app.run(debug=True)