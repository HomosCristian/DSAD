import numpy as np
import matplotlib.pyplot as plt


# expresii Lambda in Python
# calculati media a 2 valori numerice
media = lambda a, b: (a + b) / 2
print(media(3, 5))

medie_vector = lambda vector: np.mean(vector)
print(medie_vector([1, 2, 3, 4, 5]))
print(np.mean([1, 2, 3, 4, 5]))

# generati cuburile primelor 10 numere naturale
cuburi = ((x+1)**3 for x in range(10))
# nu exista comprehension pentru tupluri in Python
# tuplurile sunt un tip imuabil
# generatorul este o functie speciala in Python
# care placand o valoare initiala permite
# obtinerea valorii urmatoare intr-o secventa la runtime
print(cuburi, type(cuburi))
for cub in cuburi:
    print(cub)

# populati cu valori intregi aleatoare de la 1 la 10
# o matrice de (5, 7)
# plecand de la vector de valori
vect_1 = np.random.randint(1, 10+1, 70)
print(vect_1, type(vect_1))

matrice_1 = np.ndarray(shape=(5, 7), buffer=vect_1,
          dtype=int, order='C')
# matrice_1 = np.ndarray(shape=(5, 7, 2), buffer=vect_1,
#           dtype=int, order='C')
# 'C' Continuous - populare matrice pe linii
# 'F' Fortran - popularea matricei pe coloane
# 'A' Any
print(matrice_1, type(matrice_1))

print('dimensiunea in octeti a unui element din vector:',
      vect_1.itemsize)
# sa se contruiasca mstrice ignorand primele 3 elemente din vector
matrice_2 = np.ndarray(shape=(5, 7), buffer=vect_1,
            offset=3*vect_1.itemsize, dtype=int, order="C")
print(matrice_2)

# dictionary comprehension
dict_1 = {x+1: x+1 for x in range(10)}
print(dict_1)

dict_2 = {x+1: (x+1)**3 for x in range(10)}
print(dict_2)

# sa se creeze un dictionar cu chei de forma
# 'Stud_1', ..., 'Stud_5'
# iar valorile sunt intregi aleator generati de la 1 la 10
A = ['Stud_'+str(x+1) for x in range(5)]
print(A)
B = [x for x in np.random.randint(1, 10+1, 10)]
print(B)
dict_3 = {k: v for (k, v) in zip(A, B)}
# zip(A, B, C) va crea tupluri de forma (a, b, c)
# unde a este in A
# b este B
# si c este in C
print(dict_3)

# sa se creeze un dictionar cu chei de forma
# 'Stud_1', ..., 'Stud_5'
# iar valorile sunt liste de cate 7 valori intregi aleatoare
# intre 1 si 10
dict_4 = {'Stud_'+str(x+1):
          [y for y in np.random.randint(1, 10+1, 7)]
          for x in range(5)}
print(dict_4)
for (k, v) in dict_4.items():
    print(k, ':', v)

# sa se extraga matricea corespunzatoare
# din valorile dictionarului

# reprezantare grafica a dictionarului cu cuburile
# primelor 10 numere naturale

# grafic linie cu valorile furnizate doar pentru axa Y
# valorile dictioanrului f(x) = y = x**3
plt.plot(dict_2.values())

# grafic in care furnizam explicit si valorile pentru axa X
# si pe cele pentru axa Y
plt.plot(dict_2.keys(), dict_2.values())

dict_5 = {'X'+str(x+1): (x+1)**2 for x in range(10)}
plt.plot(dict_5.keys(), dict_5.values())

plt.show()
