import numpy as np
import Functii as fun


# list comprehension
# creare lista cu valori de la 1 la 100
list_1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
list_2 = list_1.copy() # shallow copy
list_2 = [x for x in list_1]  # deep copy
print(list_2)
list_3 = [x for x in range(0, 100, 1)]
# (inceput, sfarsit, pas)
# interval deschis la dreapta
# pasul implicit este 1
# valoarea implicita de inceput este 0
list_3 = [(x+1) for x in range(100)]
print(list_3)

# sa se creeze o lista de 100 de valori aleatoare
# in intervalul [-5, 5)
vect_1 = np.random.rand(10)
print(type(vect_1), vect_1)
list_4 = [x for x in fun.randomAB(-5, 5, 100)]
print(list_4)

# cum sunt pasati parametri la functii in Python?
a, b = 7, 11
print(a, b)
# a, b = b, a  # interschimb pythonian
fun.interschimb(a, b)
print(a, b)

# In Python parametri la functii sunt
# pasati ca referinte la obiecte
list_5 = [7, 11, 1, 2, 3]
print(list_5)
fun.interschimbList(list_5)
print(list_5)

# list comprehension cu conditii
list_6 = [-13, 8, -7, -3, 1, 2, 4, 7]
# obtineti prin comprehension o lista
# cu valori negative si impare
list_7 = [x for x in list_6
          if x<0 if x%2==1]
print(list_7)

# comprehension cu mai multe variabile
A = list_6
B = [-4, -2, 1, 2, 6]
list_8 = [(x+y) for x in A for y in B]
# produs cartezian intre multimile A si B
print(list_8)
print(len(list_8))

# comprehension cu mai multe variabile si conditii
list_9 = [(x**y) for x in A for y in B
          if x<0 if x%2==1 if y>0 if y%2==0]
print(list_9)

# lucru cu fisier text ca o lista de string-uri
fisier_text = open(file='Functii.py', mode='r')
print(type(fisier_text), fisier_text)
with fisier_text as f:
    for linie in f:
        # print(linie)  # print() insereaza un <NL><CR>
        print(linie[:-1])

# dictionare
# colectii asociative de valori eterogene
# cheile sunt de tip imutabil
dict_1 = {'luni': 3.14,
          'marti': 'mama',
          'miercuri': [1, 2, 3]}
print(type(dict_1), dict_1)
# extrage lista de chei
print(type(dict_1.keys()), dict_1.keys())
print(type(list(dict_1.keys())), list(dict_1.keys()))
# orice colectie secventiala de obiecte poate fi asimilata
# unei liste Python si convertita catre o lista Python

# extragere lista de valori
print(type(dict_1.values()), dict_1.values())

# extragere lista de perechi (cheie, valoare)
print(type(dict_1.items()), dict_1.items())
# parcurgere lista (k, v)
for (k, v) in dict_1.items():
    print(k, ": ", v)