import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
import pandas as pd


# Portal cu bibliotecile grafice in Python:
# https://python-graph-gallery.com/

# reprezentare grafica a unei matrici de corelatie
def corelograma(R2, titlu='Corelograma', dec=2, valMin=-1, valMax=1):
    plt.figure(num=titlu, figsize=(12, 8))
    plt.title(label=titlu, fontsize=12,
              verticalalignment='bottom')
    sb.heatmap(data=np.round(R2, decimals=dec), vmin=valMin, vmax=valMax,
               # cmap='Blues')
               cmap='bwr', annot=True)


def cerculCorelatiilor(R2, k1=0, k2=1, dec=2,
            titlu='Cercul corelatiilor'):
    plt.figure(num=titlu, figsize=(6, 6))
    plt.title(label=titlu, fontsize=12,
              verticalalignment='bottom')
    # desenarea unui cerc de raza 1
    theta = [t for t in np.arange(0, np.pi*2, 0.01)]
    # print(theta)
    x = [np.cos(t) for t in theta]
    y = [np.sin(t) for t in theta]
    plt.plot(x, y)
    plt.axhline(y=0, c='g')
    plt.axvline(x=0, c='g')

    if isinstance(R2, np.ndarray):
        plt.xlabel(xlabel='Variabila ' + str(k1+1),
                   fontsize=10,
                   verticalalignment='top', color='g')
        plt.ylabel(ylabel='Variabila ' + str(k2 + 1),
                   fontsize=10,
                   verticalalignment='bottom', color='g')
        plt.scatter(x=R2[:, k1], y=R2[:, k2], c='b')
        for i in range(R2.shape[0]):
            # plt.text(x=R2[i, k1], y=R2[i, k2], s='text')
            plt.text(x=R2[i, k1], y=R2[i, k2], s='(' +
                 str(np.round(R2[i, k1], decimals=dec)) +
                ', ' + str(np.round(R2[i, k2], decimals=dec)) + ')')

    elif isinstance(R2, pd.DataFrame):
        plt.xlabel(xlabel='Variabila ' + R2.columns.values[k1],
                   fontsize=10,
                   verticalalignment='top', color='g')
        plt.ylabel(ylabel='Variabila ' + R2.columns.values[k2],
                   fontsize=10,
                   verticalalignment='bottom', color='g')
        plt.scatter(x=R2.iloc[:, k1], y=R2.iloc[:, k2], c='r')
        for i in range(R2.index.values.shape[0]):
            plt.text(x=R2.iloc[i, k1], y=R2.iloc[i, k2],
            s=R2.index.values[i])

    else:
        raise Exception('Tip parametru incorect!')


def variantaExplicata(alfa,
        titlu='Varianta explicata de componentele principale'):
    plt.figure(num=titlu, figsize=(9, 6))
    plt.title(label=titlu, fontsize=12,
              verticalalignment='bottom')
    plt.xlabel(xlabel='Componente pricipale',
               fontsize=10,
               verticalalignment='top', color='g')
    plt.ylabel(ylabel='Valori proprii - varianta',
               fontsize=10,
               verticalalignment='bottom', color='g')
    valoriX = ['C'+str(i+1) for i in range(len(alfa))]
    # plt.plot(valoriX, alfa, 'o-', c='b')
    plt.plot(valoriX, alfa, linestyle='-', marker='o', c='b')
    # plt.plot(valoriX, alfa, 'X-', c='b')
    plt.axhline(y=1, c='r')

def afisare():
    plt.show()