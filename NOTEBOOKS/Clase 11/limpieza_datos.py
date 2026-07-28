"""Funciones para limpiar y filtrar los datos cambiarios."""

import pandas as pd


def limpiar_datos(datos):
    """Prepara la tabla del BCCR y calcula la columna Diferencial."""
    datos_limpios = datos.copy()

    datos_limpios.columns = datos_limpios.iloc[0]
    datos_limpios = datos_limpios.iloc[1:].reset_index(drop=True)
    datos_limpios["Tipo de Entidad"] = (
        datos_limpios["Tipo de Entidad"].ffill()
    )
    datos_limpios = datos_limpios.dropna(
        subset=["Entidad Autorizada"]
    ).copy()

    columnas_numericas = ["Compra", "Venta"]

    if "Diferencial Cambiario" in datos_limpios.columns:
        columnas_numericas.append("Diferencial Cambiario")

    for columna in columnas_numericas:
        datos_limpios[columna] = pd.to_numeric(
            datos_limpios[columna],
            errors="coerce",
        )

    datos_limpios = datos_limpios.dropna(
        subset=["Compra", "Venta"]
    ).copy()
    datos_limpios["Diferencial"] = (
        datos_limpios["Venta"] - datos_limpios["Compra"]
    )

    return datos_limpios