import  matplotlib.pyplot as plt
import pandas as pd

from lectura_datos import leer_archivos_csv
from limpieza_datos import limpiar_datos

def calcular_variacion_periodos(datos,columna_periodo,periodo1,periodo2,descripcion):
    """Calcula los 10 productos con mayor variación entre dos períodos."""

    datos_calculo = datos.copy()

    # Forzar que el precio sea un valor numerico
    datos_calculo["PRECIO"] = pd.to_numeric(datos_calculo["PRECIO"],errors="coerce")

    # Obtener la informacion del primer periodo 
    datos_periodo1 = datos_calculo[datos_calculo[columna_periodo] == periodo1].copy()
    # Obtener la informacion del primer periodo 
    datos_periodo2 = datos_calculo[datos_calculo[columna_periodo] == periodo2].copy()

    if datos_periodo1.empty:
        print(f"\nNo existen datos para {periodo1}.")
        return

    if datos_periodo2.empty:
        print(f"\nNo existen datos para {periodo2}.")
        return

    # Calcular el precio promedio por producto en cada período
    periodo1_resumen = (datos_periodo1.groupby(["CODIGO", "PRODUCTOS", "TIPO", "CALIDAD", "UNIDAD"],as_index=False)["PRECIO"].mean().rename(columns={"PRECIO": "PRECIO_PERIODO_1"}))

    periodo2_resumen = (datos_periodo2.groupby(["CODIGO", "PRODUCTOS", "TIPO", "CALIDAD", "UNIDAD"],as_index=False)["PRECIO"].mean().rename(columns={"PRECIO": "PRECIO_PERIODO_2"}))

    # Unir los dos períodos utilizando el código del producto
    comparacion = pd.merge(periodo1_resumen,periodo2_resumen,on=["CODIGO", "PRODUCTOS", "TIPO", "CALIDAD", "UNIDAD"],how="inner")

    if comparacion.empty:
        print(
            "\nNo existen productos en común entre los dos períodos."
        )
        return

    # Calcular la variación
    comparacion["VARIACION"] = (comparacion["PRECIO_PERIODO_2"] - comparacion["PRECIO_PERIODO_1"])
    comparacion["VARIACION"] = comparacion["VARIACION"].fillna(0)

    # Calcular el valor absoluto para ordenar
    comparacion["VARIACION_ABSOLUTA"] = (comparacion["VARIACION"].abs())

    # Calcular variación porcentual
    comparacion["VARIACION_PORCENTUAL"] = (comparacion["VARIACION"] / comparacion["PRECIO_PERIODO_1"] * 100)

    # Obtener los 10 productos con mayor cambio
    datos_finales = (comparacion.sort_values(by="VARIACION_ABSOLUTA",ascending=False).head(10))

    columnas_mostrar = ["CODIGO","PRODUCTOS","TIPO","CALIDAD","UNIDAD","PRECIO_PERIODO_1","PRECIO_PERIODO_2","VARIACION","VARIACION_PORCENTUAL"]

    print(
        f"\nLos 10 productos con mayor variación entre los "
        f"{descripcion} {periodo1} y {periodo2} son:\n"
    )

    print(datos_finales[columnas_mostrar].to_string(index=False,formatters={"PRECIO_PERIODO_1": "{:,.2f}".format,"PRECIO_PERIODO_2": "{:,.2f}".format,"VARIACION": "{:,.2f}".format,"VARIACION_PORCENTUAL": "{:,.2f}%".format}))


def calcular_menor_variacion_periodos(datos,columna_periodo,periodo1,periodo2,descripcion):
    """Calcula los productos con menor variación entre dos períodos."""

    datos_calculo = datos.copy()

    # Convertir precio a numérico
    datos_calculo["PRECIO"] = pd.to_numeric(datos_calculo["PRECIO"],errors="coerce")
    datos_calculo = datos_calculo.dropna(subset=["PRECIO"])

    # Filtrar períodos
    datos_periodo1 = datos_calculo[datos_calculo[columna_periodo] == periodo1].copy()

    datos_periodo2 = datos_calculo[datos_calculo[columna_periodo] == periodo2].copy()

    if datos_periodo1.empty:
        print(f"\nNo existen datos para {periodo1}.")
        return

    if datos_periodo2.empty:
        print(f"\nNo existen datos para {periodo2}.")
        return

    columnas_grupo = ["CODIGO","PRODUCTOS","TIPO","CALIDAD","UNIDAD"]

    periodo1_resumen = (datos_periodo1.groupby(columnas_grupo, as_index=False)["PRECIO"].mean().rename(columns={"PRECIO": "PRECIO_PERIODO_1"}))

    periodo2_resumen = (datos_periodo2.groupby(columnas_grupo, as_index=False)["PRECIO"].mean().rename(columns={"PRECIO": "PRECIO_PERIODO_2"}))

    comparacion = pd.merge(periodo1_resumen,periodo2_resumen,on=columnas_grupo,how="inner")

    comparacion["VARIACION"] = (comparacion["PRECIO_PERIODO_2"] - comparacion["PRECIO_PERIODO_1"])

    comparacion["VARIACION_ABSOLUTA"] = (comparacion["VARIACION"].abs())

    comparacion["VARIACION_PORCENTUAL"] = (comparacion["VARIACION"] / comparacion["PRECIO_PERIODO_1"] * 100).fillna(0)

    # Ordenar de menor a mayor variación
    datos_finales = comparacion.sort_values(by="VARIACION_ABSOLUTA",ascending=True)

    columnas = ["CODIGO","PRODUCTOS","TIPO","CALIDAD","UNIDAD","PRECIO_PERIODO_1","PRECIO_PERIODO_2","VARIACION","VARIACION_PORCENTUAL"]

    print(f"\nProductos con menor variación entre " f"{descripcion} {periodo1} y {periodo2}\n")

    print(datos_finales[columnas].to_string(index=False,formatters={"PRECIO_PERIODO_1": "{:,.2f}".format,"PRECIO_PERIODO_2": "{:,.2f}".format,"VARIACION": "{:,.2f}".format,"VARIACION_PORCENTUAL": "{:,.2f}%".format,}))