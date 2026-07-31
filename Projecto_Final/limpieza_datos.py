"""Funciones para limpiar y filtrar los datos cambiarios."""

import pandas as pd


def limpiar_datos(datos):
    """Prepara la tabla del BCCR y calcula la columna Diferencial."""
    datos_limpios = datos.copy()

    #datos_limpios.columns = datos_limpios.iloc[0]
    #datos_limpios = datos_limpios.iloc[1:].reset_index(drop=True)
    #datos_limpios["Tipo de Entidad"] = (
    #    datos_limpios["Tipo de Entidad"].ffill()
    #)
    #datos_limpios = datos_limpios.dropna(
    #    subset=["Entidad Autorizada"]
    #).copy()

    columnas_numericas = ["Código", "Precio Venta", "Semana", "Año", "Precio venta", "Precio venra"]

    #if "Diferencial Cambiario" in datos_limpios.columns:
    #    columnas_numericas.append("Diferencial Cambiario")

    for columna in columnas_numericas:
        datos_limpios[columna] = pd.to_numeric(
            datos_limpios[columna],
            errors="coerce",
        )

    #datos_limpios = datos_limpios.dropna(
    #    subset=["Compra", "Venta"]
    #).copy()
    #datos_limpios["Diferencial"] = (
    #    datos_limpios["Venta"] - datos_limpios["Compra"]
    #)
    
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
    
    datos_limpios["CODIGO"] = datos_limpios["CODIGO"].astype(int)

    return datos_limpios
