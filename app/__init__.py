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
from .functions.phc_curves import tcurve_strong_acid, tcurve_strong_base, tcurve_weak_acid, tcurve_weak_base
from .functions.argentometric import agcurve
from .functions.analytical import conv_volume_L, conv_volume_mL, analitical_factor

app = Flask(__name__)

# cores para debug
YELLOW = "\033[33m"
RESET = "\033[0m"

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
    return render_template('phcalc.html')

@app.route('/phcalc/acid_base1', methods=['GET', 'POST'])
def acid_base1():
    acid_vol = None 
    acid_con = None 
    base_vol = None 
    base_con = None
    pH = None
    pOH = None

    if request.method == 'POST':
        acid_vol = request.form.get('acid_vol')
        acid_con = request.form.get('acid_con') 
        base_vol = request.form.get('base_vol') 
        base_con = request.form.get('base_con')
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
    return render_template('acid_base1.html', pH=pH, pOH=pOH)

@app.route('/phcalc/acid_base2', methods=['GET', 'POST'])
def acid_base2():
    acid_vol = None 
    acid_con = None 
    base_vol = None 
    base_con = None
    pH = None
    pOH = None
    input_ka_significant_digits = None 
    input_ka_exponent = None 
    if request.method == 'POST':
        acid_vol = request.form.get('acid_vol')
        acid_con = request.form.get('acid_con') 
        base_vol = request.form.get('base_vol') 
        base_con = request.form.get('base_con')
        input_ka_significant_digits = request.form.get('input_ka_significant_digits')
        input_ka_exponent = request.form.get('input_ka_exponent')
        if acid_vol and acid_con and base_vol and base_con:
            try:
                # Converter os valores inseridos para float
                acid_vol = float(acid_vol)
                acid_con = float(acid_con)
                base_vol = float(base_vol)
                base_con = float(base_con)
                input_ka_significant_digits = float(input_ka_significant_digits)
                input_ka_exponent = float(input_ka_exponent)
                # Executando cálculos
                pH, pOH = phc_weak_acid(acid_vol, acid_con, base_vol, base_con, input_ka_significant_digits, input_ka_exponent)
            except ValueError:
                pH = pOH = None
    return render_template('acid_base2.html', pH=pH, pOH=pOH)

@app.route('/phcalc/acid_base3', methods=['GET', 'POST'])
def acid_base3():
    acid_vol = None 
    acid_con = None 
    base_vol = None 
    base_con = None
    pH = None
    pOH = None
    input_kb_significant_digits = None 
    input_kb_exponent = None 
    if request.method == 'POST':
        acid_vol = request.form.get('acid_vol')
        acid_con = request.form.get('acid_con') 
        base_vol = request.form.get('base_vol') 
        base_con = request.form.get('base_con')
        input_kb_significant_digits = request.form.get('input_kb_significant_digits')
        input_kb_exponent = request.form.get('input_kb_exponent')
        if acid_vol and acid_con and base_vol and base_con:
            try:
                # Converter os valores inseridos para float
                acid_vol = float(acid_vol)
                acid_con = float(acid_con)
                base_vol = float(base_vol)
                base_con = float(base_con)
                input_kb_significant_digits = float(input_kb_significant_digits)
                input_kb_exponent = float(input_kb_exponent)
                # Executando cálculos
                pH, pOH = phc_weak_base(acid_vol, acid_con, base_vol, base_con, input_kb_significant_digits, input_kb_exponent)
            except ValueError:
                pH = pOH = None
    return render_template('acid_base3.html', pH=pH, pOH=pOH)

@app.route('/phcalc/acid_base4', methods=['GET', 'POST'])
def acid_base4():
    acid_vol = None 
    acid_con = None 
    base_vol = None 
    base_con = None
    pH = None
    pOH = None
    input_ka_significant_digits = None 
    input_ka_exponent = None 
    input_kb_significant_digits = None 
    input_kb_exponent = None 
    if request.method == 'POST':
        acid_vol = request.form.get('acid_vol')
        acid_con = request.form.get('acid_con') 
        base_vol = request.form.get('base_vol') 
        base_con = request.form.get('base_con')
        input_ka_significant_digits = request.form.get('input_ka_significant_digits')
        input_ka_exponent = request.form.get('input_ka_exponent')
        input_kb_significant_digits = request.form.get('input_kb_significant_digits')
        input_kb_exponent = request.form.get('input_kb_exponent')
        if acid_vol and acid_con and base_vol and base_con:
            try:
                # Converter os valores inseridos para float
                acid_vol = float(acid_vol)
                acid_con = float(acid_con)
                base_vol = float(base_vol)
                base_con = float(base_con)
                input_ka_significant_digits = float(input_ka_significant_digits)
                input_ka_exponent = float(input_ka_exponent)
                input_kb_significant_digits = float(input_kb_significant_digits)
                input_kb_exponent = float(input_kb_exponent)
                # Executando cálculos
                pH, pOH = phc_weak_acid_base(acid_vol, acid_con, base_vol, base_con, input_ka_significant_digits, input_ka_exponent, input_kb_significant_digits, input_kb_exponent)
            except ValueError:
                pH = pOH = None
    return render_template('acid_base4.html', pH=pH, pOH=pOH)

@app.route('/phcurve')
def phcurve():
    return render_template('phcurve.html')

@app.route('/phcurve/curve_acid_base1', methods=["GET", "POST"])
def curve_acid_base1():
    acid_vol = None
    acid_con = None
    base_con = None
    img_base64 = None
    if request.method == 'POST':
        acid_vol = request.form.get('acid_vol')
        acid_con = request.form.get('acid_con')
        base_con = request.form.get('base_con')
        if acid_vol and acid_con and base_con:
            try:
                acid_vol = float(acid_vol)
                acid_con = float(acid_con)
                base_con = float(base_con)
                # realizando cálculos
                img_base64 = tcurve_strong_acid(acid_vol, acid_con, base_con)
            except ValueError:
                img_base64 = None
    return render_template('curve_acid_base1.html', img_base64=img_base64)

@app.route('/phcurve/curve_acid_base2', methods=["GET", "POST"])
def curve_acid_base2():
    base_vol = None
    base_con = None
    acid_con = None
    img_base64 = None
    if request.method == 'POST':
        base_vol = request.form.get('base_vol')
        base_con = request.form.get('base_con')
        acid_con = request.form.get('acid_con')
        if base_vol and base_con and acid_con:
            try:
                base_vol = float(base_vol)
                base_con = float(base_con)
                acid_con = float(acid_con)
                # realizando cálculos
                img_base64 = tcurve_strong_base(base_vol, base_con, acid_con)
            except ValueError:
                img_base64 = None
    return render_template('curve_acid_base2.html', img_base64=img_base64)

@app.route('/phcurve/curve_acid_base3', methods=["GET", "POST"])
def curve_acid_base3():
    acid_vol = None
    acid_con = None
    base_con = None
    img_base64 = None
    acid_valence = None
    input_ka_significant_digits = None
    input_ka_exponent = None
    if request.method == 'POST':
        acid_vol = request.form.get('acid_vol')
        acid_con = request.form.get('acid_con')
        base_con = request.form.get('base_con')
        acid_valence = request.form.get('acid_valence')
        input_ka_significant_digits = request.form.get('input_ka_significant_digits')
        input_ka_exponent = request.form.get('input_ka_exponent')
        if acid_vol and acid_con and base_con:
            try:
                acid_vol = float(acid_vol)
                acid_con = float(acid_con)
                base_con = float(base_con)
                acid_valence = float(acid_valence)
                input_ka_significant_digits = float(input_ka_significant_digits)
                input_ka_exponent = float(input_ka_exponent)
                # realizando cálculos
                img_base64 = tcurve_weak_acid(acid_vol, acid_con, base_con, input_ka_significant_digits, input_ka_significant_digits, acid_valence)
            except ValueError as e:
                print(f"{YELLOW}Erro de valor: {e} {RESET}")
                img_base64 = None
    return render_template('curve_acid_base3.html', img_base64=img_base64)

@app.route('/phcurve/curve_acid_base4', methods=["GET", "POST"])
def curve_acid_base4():
    acid_vol = None
    acid_con = None
    base_con = None
    img_base64 = None
    base_valence = None
    input_kb_significant_digits = None
    input_kb_exponent = None
    if request.method == 'POST':
        acid_vol = request.form.get('base_vol')
        acid_con = request.form.get('base_con')
        base_con = request.form.get('acid_con')
        base_valence = request.form.get('base_valence')
        input_kb_significant_digits = request.form.get('input_kb_significant_digits')
        input_kb_exponent = request.form.get('input_kb_exponent')
        if acid_vol and acid_con and base_con:
            try:
                acid_vol = float(acid_vol)
                acid_con = float(acid_con)
                base_con = float(base_con)
                base_valence = float(base_valence)
                input_kb_significant_digits = float(input_kb_significant_digits)
                input_kb_exponent = float(input_kb_exponent)
                # realizando cálculos
                img_base64 = tcurve_weak_base(acid_vol, acid_con, base_con, input_kb_significant_digits, input_kb_significant_digits, base_valence)
            except ValueError:
                img_base64 = None
    return render_template('curve_acid_base4.html', img_base64=img_base64)

@app.route('/argentometric_curve', methods=['GET','POST'])
def argentometric():
    analyte_vol = None
    analyte_con = None
    titrant_max_vol = None
    titrant_con = None
    img_base64 = None
    if request.method == 'POST':
        analyte_vol = request.form.get('analyte_vol')
        analyte_con = request.form.get('analyte_con')
        titrant_max_vol = request.form.get('titrant_max_vol')
        titrant_con = request.form.get('titrant_con')
        if analyte_vol and analyte_con and titrant_max_vol and titrant_con:
            try:
                analyte_vol = float(analyte_vol) / 1000
                analyte_con = float(analyte_con)
                titrant_max_vol = float(titrant_max_vol) / 1000
                titrant_con = float(titrant_con)
                img_base64 = agcurve(analyte_vol, analyte_con, titrant_max_vol, titrant_con)
            except ValueError:
                img_base64 = None

    return render_template('argentometric.html', img_base64=img_base64)

@app.route('/analytical_factor', methods=['GET','POST'])
def analytical_factor():
    PM_value = None
    M_value = None
    FA = None
    if request.method == 'POST':
        PM_value = request.form.get('PM_value')
        M_value = request.form.get('M_value')
        if PM_value and M_value:
            try:
                PM_value = float(PM_value)
                M_value = float(M_value)
                FA = analitical_factor(PM_value, M_value)
            except ValueError:
                FA = None
    return render_template('analytical.html', FA=FA)

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