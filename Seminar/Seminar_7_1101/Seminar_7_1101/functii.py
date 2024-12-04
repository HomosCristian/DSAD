import pandas as pd
import numpy as np


def index_disimilaritate(df, coloane):
    X = df[coloane].values
    # print(X, X.shape)
    sume_pe_linii = np.sum(a=X, axis=1) #facem sume pe linii
    print(sume_pe_linii, sume_pe_linii.shape)
    R = np.transpose(sume_pe_linii - X.T)
    print(R, R.shape)
    Tx = np.sum(a=X, axis=0) #facem sume pe coloane
    Tr = np.sum(a=R, axis=0)
    # print(Tx + Tr)
    Tx[Tx==0] = 1 #inlocuire elemente 0 cu 1 pentru impartire
    Tr[Tr==0] = 1

    px = X/Tx
    pr = R/Tr
    print(px, px.shape)
    print(pr, pr.shape)

    rezultat = 1/2 * np.abs(px-pr)
    print(rezultat, rezultat.shape)
    return np.sum(a=rezultat, axis = 1) #suma pe linii la nivel de unitate administrativ teritoriala


def entropie_Shannon_Weaver(df, coloane):
    X = df[coloane].values
    # print(X, X.shape)
    SL = np.sum(a=X, axis=1) #facem sume pe linii
    print(SL, SL.shape)
    p = np.transpose(X.T / SL)
    print(p, p.shape)
    # inlocuire elemente 0 cu 1 pentru evitare impartire la zero
    p[p == 0] = 1
    rezultat = -1 * p * np.log2(p)
    print(rezultat.shape)
    return np.sum(a=rezultat, axis=1)  # sume pe lini
    # calculam entropia la nivelul fiecarei
    # unitati administrativ-teritoriale

