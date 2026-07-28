import pandas as pd
import glob
import os
import re
from datetime import datetime

# Diccionario de meses en español
meses = {
    1: "Enero",
    2: "Febrero",
    3: "Marzo",
    4: "Abril",
    5: "Mayo",
    6: "Junio",
    7: "Julio",
    8: "Agosto",
    9: "Septiembre",
    10: "Octubre",
    11: "Noviembre",
    12: "Diciembre"
}

# Ruta de los archivos CSV
archivos = glob.glob("C:\\Users\\Admin\\Documents\\GitHub\\2026C2-G01-FUNDAMENTOS DE PYTHON\\Projecto_Final\\datos\\*.csv")

# Lista donde se almacenarán los DataFrames
lista_df = []

# Leer todos los archivos
for archivo in archivos:

    print(f"Leyendo: {os.path.basename(archivo)}")

    df = pd.read_csv(
        archivo,
        sep=";",
        encoding="latin-1",
        skiprows=2
    )

    # Limpiar nombres de columnas
    df.columns = df.columns.str.strip()

    # Eliminar columnas vacías
    df = df.loc[:, ~df.columns.str.contains("^Unnamed")]

    # Obtener el nombre del archivo
    nombre_archivo = os.path.basename(archivo)

    # Extraer semana y año del nombre del archivo
    coincidencia = re.search(r"Semana_(\d+)-(\d+)", nombre_archivo)

    semana = int(coincidencia.group(1))
    anio = int(coincidencia.group(2))

    # Obtener el lunes correspondiente a esa semana
    fecha = datetime.fromisocalendar(anio, semana, 1)

    # Agregar nuevas columnas
    df["Semana"] = semana
    df["Mes"] = meses[fecha.month]
    df["Año"] = anio

    # Agregar el DataFrame a la lista
    lista_df.append(df)

# Unir todos los DataFrames
ventas = pd.concat(lista_df, ignore_index=True)

# Mostrar información
print("\nInformación del DataFrame")
print(ventas.info())

print("\nPrimeros registros")
print(ventas.head())

print("\nCantidad de registros:", len(ventas))