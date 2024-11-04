import numpy as np

def calc_sd(values):
    mean = np.mean(values)
    # standard deviation
    sd = np.std(values)

    print(f"mean = {mean}")
    print(f"sd = {sd}")

    return sd

def calc_rsd(values):
    mean = np.mean(values)
    # standard deviation
    sd = np.std(values)
    # relative standard deviation
    rsd = (sd/mean) * 100

    print(f"mean = {mean}")
    print(f"sd = {sd}")
    print(f"rsd = {rsd}")

    return rsd