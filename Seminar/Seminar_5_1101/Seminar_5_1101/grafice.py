import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb


# reprezentare grafica a unei matrici de corelatie
def corelograma(R2, titlu='Corelograma', dec=2, valMin=-1, valMax=1):
    plt.figure(num=titlu, figsize=(12, 8))
    plt.title(label=titlu, fontsize=12,
              verticalalignment='bottom')
    sb.heatmap(data=np.round(R2, decimals=dec), vmin=valMin, vmax=valMax,
               # cmap='Blues')
               cmap='bwr', annot=True)

def afisare():
    plt.show()