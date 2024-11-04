import numpy as np
import scipy.stats as stats

def calc_critical_value(values, t_value):
    n = len(values)
    dof = n - 1
    critical_value = stats.t.ppf((1 + t_value / 100) / 2.0, dof)
    print(f"n = {n}")
    print(f"dof = {dof}")
    print(f"critical_value = {critical_value}")

    return critical_value

def calc_error_margin(values, critical_value):
    n = len(values)
    sd = np.std(values, ddof=1)
    error_margin = critical_value * (sd/np.sqrt(n))
    print(f"n = {n}")
    print(f"sd = {sd}")
    print(f"error_margin = {error_margin}")

    return error_margin

def calc_confidence_interval(values, error_margin):
    mean = np.mean(values)
    confidence_interval  = (mean - error_margin, mean + error_margin)
    print(f"mean = {mean}")
    print(f"confidence_interval = {confidence_interval}")

    return confidence_interval

def calc_u(confidence_interval):
    u = float(confidence_interval[0]), float(confidence_interval[1])
    print(f"confidence_interval = {confidence_interval}")
    print(f"u = {u}")

    return u


# Testando função
a = [1,2,2.1,2.2,2.3,2.7,2.5,2.9,3]
b = 95

critAB = calc_critical_value(a, b)
errAB = calc_error_margin(a, critAB)
confAB = calc_confidence_interval(a, errAB)
uAB = calc_u(confAB)