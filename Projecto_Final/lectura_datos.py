import pandas as pd
import glob

# Busca todos los archivos Excel
archivos = glob.glob("datos/*.csv")

# Lista donde se almacenarán los DataFrames
lista_df = []

# Leer cada archivo
for archivo in archivos:
    df = pd.read_csv(archivo)
    lista_df.append(df)

# Unir todos los DataFrames
df_final = pd.concat(lista_df, ignore_index=True)

print(df_final)