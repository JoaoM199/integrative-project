import numpy as np
from scipy.optimize import fsolve
import matplotlib.pyplot as plt
import base64
import io

def agcurve(analyte_vol, analyte_con, titrant_max_vol=10.0, titrant_con=0.1):
    titrant_vol = np.linspace(0.1, titrant_max_vol, 100)
    print(f"titrant_max_vol={titrant_max_vol}")
    print(f"titrant_con={titrant_con}")
    pAg = []
    for vol in titrant_vol:
        total_vol = analyte_vol + vol

        moles_Ag_added = titrant_con * vol
        moles_analyte = analyte_con * analyte_vol

        if moles_Ag_added < moles_analyte:
            Ag_con = 1e-10
        else:
            excess_ag = moles_Ag_added - moles_analyte
            Ag_con = excess_ag / total_vol
        pAg_value = -np.log10(Ag_con)
        pAg.append(pAg_value)

    # plotando gráfico
    plt.figure(figsize=(8,6))
    plt.plot(titrant_vol, pAg, label = 'Titration curve', color='orange')
    plt.xlabel('Volume of tritant (mL)')
    plt.ylabel('pAg')
    plt.title('Argetometric Titration curve')
    plt.grid(True)
    # converter gráfico para base64
    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)
    img_base64 = base64.b64encode(buf.getvalue()).decode("utf-8")
    buf.close()

    return img_base64