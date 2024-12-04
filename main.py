import numpy as np
import pandas as pd  # pt cerinta 2

# Cerinta 1

# Citim matricea din fișierul text într-un numpy.ndarray
file_path = 'matrice_2.txt'  # Asigură-te că fișierul este în același folder cu scriptul
matrix = np.loadtxt(file_path, dtype=int)

# Afișăm conținutul matricei
print("Cerinta 1")
print("Conținutul matricei citite din fișier:")
print(matrix)
print("")


# Cerinta 2

# Generăm un vector de 50 de valori aleatorii în intervalul [-10, 10]
random_vector = np.random.uniform(-10, 10, 50)

# Creăm un pandas.Series cu etichete de forma R_1, R_2, ...
labels = [f"R_{i+1}" for i in range(50)]
series = pd.Series(random_vector, index=labels)

# Afișăm seria
print("Cerinta 2")
print("Seria generată este:")
print(series)
print("")

# Cerinta 3

# Generăm matricea numpy aleatoare (10, 7) în intervalul [-10, 10]
matrix = np.random.uniform(-10, 10, size=(10, 7))

# Creăm un pandas.DataFrame din matrice
row_labels = [f"R{i+1}" for i in range(10)]  # Etichete de rând: R1, R2, ..., R10
column_labels = [f"V{j+1}" for j in range(7)]  # Etichete de coloană: V1, V2, ..., V7
dataframe = pd.DataFrame(matrix, index=row_labels, columns=column_labels)

# Afișăm DataFrame-ul
print("Cerinta 3")
print("DataFrame generat din matricea numpy:")
print(dataframe)
print("")


# Cerinta 4
# Inițializăm matricea inițială (4x5) cu toate elementele 9
matrix = np.full((4, 5), 9)

# Modificăm matricea pentru a obține rezultatul cerut
matrix[:, 1:4] = 0  # Setăm coloanele 2, 3, 4 la 0
matrix[-1, :] = 5  # Setăm ultima linie la 5
matrix[:, [0, -1]] = 5  # Setăm marginile (prima și ultima coloană) la 5

# Afișăm matricea rezultată
print("Cerinta 4")
print("Matricea rezultată:")
print(matrix.astype(float))
print("")


# Cerinta 5
# Creăm dicționarul cu chei de forma Stud_1, ..., Stud_7 și liste de 5 note aleatorii
studenti = {f"Stud_{i+1}": np.random.randint(1, 11, 5).tolist() for i in range(7)}

# Convertim dicționarul într-un pandas.DataFrame
df_studenti = pd.DataFrame(studenti)

# Afișăm DataFrame-ul
print("Cerinta 5")
print("DataFrame cu notele studenților:")
print(df_studenti)
print("")

# Cerinta 6
# Pas 1: Crearea fișierelor CSV (pentru demonstrație)
# Seria 1
seria_1 = [1, 2, 3, 4, 5]
seria_1_path = "Seria_1.csv"
pd.DataFrame({"Values": seria_1}).to_csv(seria_1_path, index=False)

# Seria 2
seria_2 = [10, 20, 30, 40, 50]
seria_2_path = "Seria_2.csv"
pd.DataFrame({"Values": seria_2}).to_csv(seria_2_path, index=False)

# Pas 2: Citirea fișierelor CSV în pandas.Series
series_1 = pd.read_csv(seria_1_path)["Values"]
series_2 = pd.read_csv(seria_2_path)["Values"]

# Pas 3: Crearea dicționarului
dict_series = {
    "C_1": series_1,
    "C_2": series_2
}

# Pas 4: Crearea DataFrame-ului din dicționar
df_series = pd.DataFrame(dict_series)

# Afișarea DataFrame-ului
print("Cerinta 6")
print("DataFrame creat din cele două serii:")
print(df_series)
print("")

# Cerinta 7
# Pas 1: Crearea fișierului KO.csv (pentru demonstrație)
data = {
    "Open": [50, 52, 54, 53, 55],
    "Close": [51, 53, 56, 52, 54],
    "High": [52, 54, 57, 55, 56],
    "Low": [49, 51, 53, 51, 53]
}
ko_path = "KO.csv"
pd.DataFrame(data).to_csv(ko_path, index=False)

# Pas 2: Citirea fișierului KO.csv
df = pd.read_csv(ko_path)

# Pas 3: Calcularea raportului de volatilitate (RV)
df["RV"] = (df["Close"] - df["Open"]) / (df["High"] - df["Low"])

# Pas 4: Salvarea DataFrame-ului modificat în KO_RV.csv
rv_path = "KO_RV.csv"
df.to_csv(rv_path, index=False)

# Afișarea DataFrame-ului rezultat
print("Cerinta 7")
print("DataFrame cu coloana RV adăugată:")
print(df)
print("")

# Cerinta 8
# Pas 1: Creăm dicționarul pentru ani și studenți
ani_studiu = {
    f"An_{an}": {f"Stud_{stud}": np.random.randint(1, 11) for stud in range(1, 9)}
    for an in range(1, 4)
}

# Pas 2: Transformăm dicționarul într-un pandas.DataFrame
df_ani_studiu = pd.DataFrame(ani_studiu)

# Pas 3: Afișăm DataFrame-ul
print("Cerinta 8")
print("DataFrame creat din dicționarul de ani și studenți:")
print(df_ani_studiu)
print("")

# Cerinta 9
# Dimensiunea matricei
n = 7

# Inițializăm matricea cu valori de 4
matrix = np.full((n, n), 4.0)

# Setăm valorile diagonalei principale la 11
np.fill_diagonal(matrix, 11)

# Setăm valorile interioare la 0 unde este necesar
for i in range(1, n - 1):
    for j in range(1, n - 1):
        if i != j:  # Excludem diagonala principală
            matrix[i, j] = 0

# Setăm elementul central la 99
matrix[n // 2, n // 2] = 99

# Afișăm matricea rezultată
print("Cerinta 9")
print("Matricea generată corect este:")
print(matrix)