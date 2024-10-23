import numpy as np
from scipy.optimize import fsolve

def phc_strong_acid_base(acid_vol, acid_con, base_vol, base_con):
    print("Ácido forte e base forte:")
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
    
    print(f"pH = {pH}")
    print(f"pOH = {pOH}")

    return pH, pOH

def phc_weak_acid(acid_vol, acid_con, base_vol, base_con, input_ka_significant_digits, input_ka_exponent):
    print("Ácido fraco e base forte:")
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
    # volume final
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

    print(f"pH = {pH}")
    print(f"pOH = {pOH}")

    return pH, pOH

def phc_weak_base(acid_vol, acid_con, base_vol, base_con, input_kb_significant_digits, input_kb_exponent):
    print("Ácido forte e base fraca:")
    # calcular a constante da base
    kb = input_kb_significant_digits * np.pow(10,input_kb_exponent)
    # converter volumes para litros
    acid_vol = acid_vol/1000
    base_vol = base_vol/1000
    # calcular número de moles inicial
    init_acid = acid_con * acid_vol
    init_base = base_con * base_vol
    # Calcular número de moles final
    final_acid = max(0, init_acid - init_base)
    final_base = max(0, init_base - init_acid)
    # volume final
    final_volume = acid_vol + base_vol
    # concentrações finais de H+
    final_acid_con = final_acid / final_volume
    final_base_con = final_base / final_volume
    # concentração de H+
    H_con = np.sqrt(kb * final_base_con)
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

    print(f"pH = {pH}")
    print(f"pOH = {pOH}")

    return pH, pOH

def phc_weak_acid_base(acid_vol, acid_con, base_vol, base_con, input_ka_significant_digits, input_ka_exponent, input_kb_significant_digits, input_kb_exponent):
    # calcular a constante do ácido
    ka = input_ka_significant_digits * np.pow(10,input_ka_exponent)
    # calcular a constante da base
    kb = input_kb_significant_digits * np.pow(10,input_kb_exponent)
    # converter volumes para litros
    acid_vol = acid_vol/1000
    base_vol = base_vol/1000
    # calcular número de moles iniciais
    init_acid = acid_con * acid_vol
    init_base = base_con * base_vol
    # calcular número de moles final
    final_acid = max(0, init_acid - init_base)
    final_base = max(0, init_base - init_acid)
    # volume final
    final_volume = acid_vol + base_vol
    # concentrações finais de ácido e base
    final_acid_concentration = final_acid / final_volume
    final_base_concentration = final_base / final_volume

    # Realizando equações do equilíbrio
    def eq(vars):
        H, OH = vars
        eq1 = ka - H * (final_acid_concentration + H)/(final_base_concentration + OH)
        eq2 = kb - OH * (final_base_concentration + OH)/(final_acid_concentration + H)
        return [eq1, eq2]
    H, OH = fsolve(eq, (1e-7, 1e-7), xtol=1e-8, maxfev=2000)
    pH = -np.log10(H)
    pOH = -np.log(OH)

    print(f"pH = {pH}")
    print(f"pOH = {pOH}")

    return pH, pOH

# testando funções
phc_strong_acid_base(20, 0.1, 15, 0.3)
phc_weak_acid(20, 0.1, 15, 0.3, 1.3, 7)
phc_weak_base(20, 0.1, 15, 0.3, 1.3, 7)
phc_weak_acid_base(20, 0.1, 15, 0.3, 1.3, 7, 1.5, 9)