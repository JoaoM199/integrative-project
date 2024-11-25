def conv_volume_L(L_value):
    return L_value * 1000
def conv_volume_mL(ML_value):
    return ML_value/1000
def analitical_factor(PM_value, M_value):
    # PM_value -> Peso molecular
    # M_value -> Molaridade
    return (PM_value * M_value)/1000