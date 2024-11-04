import numpy as np

def calculate_deviation(values):
    mean = np.mean(values)
    deviation_values= np.abs(values - mean).tolist()


    print(f"mean = {mean}")
    print(f"deviation_values = {deviation_values}")

    return deviation_values

def calculate_deviation_mean(deviation_values):
    mean = np.mean(deviation_values)
    print(f"mean = {mean}")

    return mean