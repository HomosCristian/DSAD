import pandas as pd
import numpy as np
import functii as f

etnii_df = pd.read_csv(filepath_or_buffer="dataIN/Ethnicity.csv",
                       index_col=0)
print(etnii_df)

judete_df = pd.read_excel(io="dataIN/CoduriRomania.xlsx",
                          sheet_name="Localitati",
                          index_col=0)

print(judete_df)

regiuni_df = pd.read_excel(io="dataIN/CoduriRomania.xlsx",
                          sheet_name=1,
                          index_col=0)
print(regiuni_df)

macroregiuni_df = pd.read_excel(io="dataIN/CoduriRomania.xlsx",
                          sheet_name=2,
                          index_col=0)
print(macroregiuni_df)

judete_merge_df = etnii_df.merge(right=judete_df, left_index=True,
                                 right_index=True)

print(judete_merge_df)

etnii_list = list(etnii_df.columns.values[1:])
print(type(etnii_list), etnii_list)

judete_list = etnii_list + ['County']
print(judete_list)

judete_agregs = judete_merge_df[judete_list].groupby(by="County").sum()
print(judete_agregs)

judete_agregs.to_csv("dataOUT/etniiJudete.csv")

regiuni_list = etnii_list + ['Regiune']
print(regiuni_list)

regiuni_merge_df = judete_agregs.merge(right=regiuni_df, left_index=True,
                                 right_index=True)
print(regiuni_merge_df)

regiuni_agregs = regiuni_merge_df[regiuni_list].groupby(by="Regiune").sum()
print(regiuni_agregs)

indice_disimilaritate_localitati = f.index_disimilaritate(etnii_df, etnii_list)
print(indice_disimilaritate_localitati, indice_disimilaritate_localitati.shape)
id_df = pd.DataFrame(data=indice_disimilaritate_localitati,
                     columns=["indice_disimilaritate"],
                     index=etnii_df["City"].values)

print(id_df)


id_df.to_csv(path_or_buf="dataOUT/IndexDisimilaritateLocalitati.csv",
              index_label="Localitate")

indice_disimilaritate_judete = f.index_disimilaritate(judete_agregs,
                                                      etnii_list)

id_judete_df = pd.DataFrame(data=indice_disimilaritate_judete,
                     columns=["indice_disimilaritate"],
                     index=regiuni_df["NumeJudet"].values)

print(id_judete_df)

id_judete_df.to_csv(path_or_buf="dataOUT/IndexDisimilaritateJudete.csv",
                    index_label="Judet")

# apel entropie Shannon-Weaver la nivel de localitati
ESW_localitati = f.entropie_Shannon_Weaver(etnii_df, etnii_list)
ESW_localitati_df = pd.DataFrame(data=ESW_localitati,
                    columns=['Entropia Shannon-Weaver'],
                    index=etnii_df["City"].values)
print(ESW_localitati_df)
ESW_localitati_df.to_csv(path_or_buf='./dataOUT/ESW_localitati.csv',
                    index_label='Localitate')

# apel entropie Shannon-Weaver la nivel de judete
ESW_judete = f.entropie_Shannon_Weaver(judete_agregs, etnii_list)
ESW_judete_df = pd.DataFrame(data=ESW_judete,
                    columns=['Entropia Shannon-Weaver'],
                    index=regiuni_df["NumeJudet"].values)
print(ESW_judete_df)
ESW_judete_df.to_csv(path_or_buf='./dataOUT/ESW_judete.csv',
                    index_label='Judet')




