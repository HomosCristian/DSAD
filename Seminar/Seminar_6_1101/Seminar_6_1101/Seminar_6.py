import numpy as np
import pandas as pd

import grafice
import grafice as graf


# creati o matrice de (5, 4) de valori
# aleatoare in virgula mobila in intervalul [1, 10]
nda_1 = np.random.uniform(1, 10, size=(5, 4))
print(nda_1)

# creare pandas.Dataframe din numpy.ndarray
df_1 = pd.DataFrame(data=nda_1)
print(df_1, type(df_1))

# etichetati coloanele de forma 'C_1', ..., 'C_4'
# si liinile de forma 'L_1', ..., 'L_4'
df_2 = pd.DataFrame(data=nda_1,
            index=('L_'+str(i+1) for i in range(nda_1.shape[0])),
            columns=('C_'+str(j+1) for j in range(nda_1.shape[1])))
print(df_2)

# extrageti etichetele de linii
print(df_2.index, type(df_2.index))
print(list(df_2.index), type(list(df_2.index)))
# extrageti etichetele de coloane
print(df_2.columns, type(df_2.columns))

# extrageti valorile tabloul bidimensional
print(df_2.values, type(df_2.values))

# creare pandas.DataFrame din dictionar Python

# creati un dictionar cu chei de forma 'C1', ..., 'C5'
# si valori liste de cate 7 elemente in virgula mobila,
# generate aleatoriu in [1, 10]
dict_1 = {'C'+str(x+1):
    [y for y in np.random.uniform(1, 10, 7)]
          for x in range(5)}
for (c, v) in dict_1.items():
    print(c, ':', v)

df_3 = pd.DataFrame(data=dict_1)
print(df_3)

df_4 = pd.DataFrame(data=dict_1,
        index=['L'+str(i+1) for i in range(len(dict_1['C1']))])
print(df_4)

# accesare celule in pandas.DataFrame
print(df_4['C2'], type(df_4['C2']))
# print(df_4['C2', 'C3'], type(df_4['C2', 'C3']))  # incorect
print(df_4[['C2', 'C3']], type(df_4[['C2', 'C3']]))
# putem extrage o sublista de coloane din tablou
sublista = df_4.columns.values[2:]
print(sublista)
print(df_4[sublista])

# accesare valoare de la linia 1 coloana 3
print(df_4.iloc[0].iloc[2])
print(df_4.loc['L1'].loc['C3'])
print(df_4.iloc[0].loc['C3'])
# extragere sub-tablou
print(df_4.iloc[3:, :4])
print(df_4.loc['L4':, :'C5'])

# creati o matrice de (12, 10) de valori
# aleatoare in virgula mobila in intervalul [1, 10]
nda_2 = np.random.uniform(1, 10, size=(30, 20))
print(nda_2)

# calculati matricea de corelatie
cor = np.corrcoef(x=nda_2, rowvar=False)  # avem variabilele pe coloane
print(cor)

# graf.corelograma(cor, dec=1, titlu='Corelograma din numpy.ndarray')

# pandas.DataFrame pentru matricea de corelatie
cor_df = pd.DataFrame(data=cor,
            index=['L'+str(i+1) for i in range(cor.shape[0])],
            columns=['C' + str(j + 1) for j in range(cor.shape[1])])
# graf.corelograma(cor_df, titlu='Corelograma din pandas.DataFrame')

# apel cerc al corelatiilor pentru numpy.ndarray
# graf.cerculCorelatiilor(cor, dec=1,
#             titlu='Cercul corelatiilor din numpy.ndarray')
#
# graf.cerculCorelatiilor(cor_df,
#             titlu='Cercul corelatiilor din pandas.DataFrame')

# graf.cerculCorelatiilor('mama mea')

# creati un vector de 15 valori in virgula mobila in [0, 3)
vect_1 = np.random.uniform(0, 3, size=15)
print(vect_1, type(vect_1))
# sortare vector
vect_1 = np.sort(a=vect_1)
print(vect_1)
# facem reverse la vector pentru a-l obtine sortat descrescator
vect_1 = vect_1[::-1]
print(vect_1)

# apel grafic pentru varianta explicata
graf.variantaExplicata(vect_1)

graf.afisare()

