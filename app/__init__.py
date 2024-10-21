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


@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == "__main__":
    app.run(debug=True)