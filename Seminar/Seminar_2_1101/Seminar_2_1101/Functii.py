import numpy as np


def randomAB(a, b, n): # asumam ca a, b, n sunt intregi
    return a + np.random.rand(n) * (b - a)
    # operatorii '+' si '*' sunt supraincarcati pentru
    # adunare scalar la stanga unui vector, respectiv
    # inmultirea unui vector cu un scalar la dreapta

def interschimb(a, b):  # asumam ca a si b sunt de tip numeric
    aux = a
    a = b
    b = aux
    print('interschimb in functie:', a, b)

def interschimbList(l): # asumam ca l este o lista Python
    # intershimbam primele 2 elemente ale listei
    aux = l[0]
    l[0] = l[1]
    l[1] = aux
