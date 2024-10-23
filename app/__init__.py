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

from flask import Flask, render_template, request, json
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import os

# Funções
from .functions.deviation import calculate_deviation, calculate_deviation_mean
from .functions.sd import calc_sd, calc_rsd
from .functions.confidence import calc_critical_value, calc_error_margin, calc_confidence_interval, calc_u
from .functions.phc_calc import phc_strong_acid_base, phc_weak_acid, phc_weak_base, phc_weak_acid_base

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

@app.route('/phcalc', methods=['GET', 'POST'])
def phcalc():
    calculation_type = None
    acid_vol = None 
    acid_con = None 
    base_vol = None 
    base_con = None
    input_ka_significant_digits = None 
    input_ka_exponent = None 
    input_kb_significant_digits = None 
    input_kb_exponent = None
    pH = None
    pOH = None

    if request.method == 'POST':
        calculation_type = request.form.get('calculation_type')
        acid_vol = request.form.get('acid_vol')
        acid_con = request.form.get('acid_con') 
        base_vol = request.form.get('base_vol') 
        base_con = request.form.get('base_con')
        input_ka_significant_digits = request.form.get('input_ka_significant_digits') 
        input_ka_exponent = request.form.get('input_ka_exponent')
        input_kb_significant_digits = request.form.get('input_kb_significant_digits')
        input_kb_exponent = request.form.get('input_kb_exponent')
        if calculation_type == "phc_strong_acid_base":
            if acid_vol and acid_con and base_vol and base_con:
                try:
                    # Converter os valores inseridos para float
                    acid_vol = float(acid_vol)
                    acid_con = float(acid_con)
                    base_vol = float(base_vol)
                    base_con = float(base_con)
                    # Executando cálculo
                    pH, pOH = phc_strong_acid_base(acid_vol, acid_con, base_vol, base_con)
                except ValueError:
                    pH = pOH = None
    return render_template('phcalc.html', calculation_type=calculation_type,
                           pH=pH, 
                           pOH=pOH)

@app.route('/constaints')
def constaints():
    # Carregar o arquivo json
    json_path = os.path.join(os.path.dirname(__file__), 'static', 'json', 'acid_base_constaints.json')
    with open (json_path, 'r', encoding='utf-8') as d:
        constaints = json.load(d)
    # carregar a página
    return render_template('constaints.html', constaints=constaints)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == "__main__":
    app.run(debug=True)