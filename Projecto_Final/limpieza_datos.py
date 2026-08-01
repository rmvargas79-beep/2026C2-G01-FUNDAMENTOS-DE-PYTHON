"""Funciones para limpiar y filtrar los datos cambiarios."""

import pandas as pd


def limpiar_datos(datos):
    """Prepara y Limpia los datos que se leen de los cvs y estan en el dataframe de pandas."""
    datos_limpios = datos.copy()

    datos_limpios["Código"] = datos_limpios["Código"].astype("Int64")
    columnas_numericas = ["Código", "Precio Venta", "Semana", "Año"]

    for columna in columnas_numericas:
        datos_limpios[columna] = pd.to_numeric(
            datos_limpios[columna],
            errors="coerce",
        )

    #Renombrar nombres Columnas
    datos_limpios.rename(columns = {
        'Código':'CODIGO',
        'Productos': 'PRODUCTOS',
        'Tipo': 'TIPO',
        'Calidad / Tamaño':'CALIDAD',
        'Unidad de Venta': 'UNIDAD',
        'IVA':'IVA',
        'Precio Venta':'PRECIO',
        'Semana':'SEMANA',
        'Mes':'MES',
        'Año':'AÑO'
    }, inplace=True)
    
    
    
    datos_limpios.drop(
    columns=["Precio venta", "Precio venra"],
    inplace=True,
    errors="ignore"
    )
    
    

    return datos_limpios
