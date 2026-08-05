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
    
    

def mostrar_primeras_entradas(datos):
    """Muestra una vita de las columnas principales"""
    
    columnas = ["CODIGO","PRODUCTOS","TIPO","CALIDAD"]
    datos_ordenados = datos.sort_values(by="PRODUCTOS")
    datos_ordenados = datos_ordenados.drop_duplicates(subset="CODIGO")
    
    # Ancho de cada columna
    ancho = {
        "CODIGO": 10,
        "PRODUCTOS": 40,
        "TIPO": 20,
        "CALIDAD": 20
    }

    # Encabezados
    encabezado = ""
    for col in columnas:
        encabezado += col.center(ancho[col])

    print(encabezado)
    print("-" * len(encabezado))

    # Filas
    for _, fila in datos_ordenados.iterrows():
        print(
            str(fila["CODIGO"]).center(ancho["CODIGO"]) +
            str(fila["PRODUCTOS"]).center(ancho["PRODUCTOS"]) +
            str(fila["TIPO"]).center(ancho["TIPO"]) +
            str(fila["CALIDAD"]).center(ancho["CALIDAD"])
        ) 
        
        
        


def comparar_productos(datos):
    
    columnas = ["CODIGO","PRODUCTOS","TIPO","CALIDAD","UNIDAD","PRECIO","MES","AÑO"]

    while True:
        print("\nComparar Dos Productos")
        print("1. Comparar Dos Productos Por Código")
        print("2. Comparar Productos Por Nombre")
        print("3. Salir")

        opcion = input("Ingrese la opción del menú: ").lower().strip()

        if opcion == "1":
            try:
                codigo1 = int(input("Ingrese el primer codigo: ").strip())
                codigo2 = int(input("Ingrese el segundo codigo: ").strip())
            except ValueError:
                print("\nDigite solo Numeros Enteros.")
                input("Presione enter para continuar...")
                continue

            producto1 = datos[datos["CODIGO"] == codigo1]
            producto2 = datos[datos["CODIGO"] == codigo2]

            if producto1.empty:
                print(f"\nNo se encontró el producto con código {codigo1}.")

            if producto2.empty:
                print(f"\nNo se encontró el producto con código {codigo2}.")

            if not producto1.empty and not producto2.empty:

            # Crear un DataFrame independiente para cada producto
            df1 = (
                datos[datos["CODIGO"] == codigo1]
                .copy()
                .sort_values(by=["AÑO", "SEMANA"])
            )

            df2 = (
                datos[datos["CODIGO"] == codigo2]
                .copy()
                .sort_values(by=["AÑO", "SEMANA"])
            )

            # Convertir los precios a valores numéricos
            df1["PRECIO"] = pd.to_numeric(
                df1["PRECIO"],
                errors="coerce"
            )

            df2["PRECIO"] = pd.to_numeric(
                df2["PRECIO"],
                errors="coerce"
            )

            # Eliminar registros sin semana o precio
            df1 = df1.dropna(subset=["SEMANA", "PRECIO"])
            df2 = df2.dropna(subset=["SEMANA", "PRECIO"])

            # Obtener los nombres de los productos
            nombre_producto1 = df1.iloc[0]["PRODUCTOS"]
            nombre_producto2 = df2.iloc[0]["PRODUCTOS"]

            # Crear la figura
            plt.figure(figsize=(12, 6))

            # Graficar el primer producto
            plt.plot(
                df1["SEMANA"],
                df1["PRECIO"],
                marker="o",
                linestyle="-",
                linewidth=2,
                label=f"{nombre_producto1} - Código {codigo1}"
            )

            # Graficar el segundo producto
            plt.plot(
                df2["SEMANA"],
                df2["PRECIO"],
                marker="s",
                linestyle="--",
                linewidth=2,
                label=f"{nombre_producto2} - Código {codigo2}"
            )

            # Personalizar el gráfico
            plt.title(
                "Comparación del historial de precios por producto",
                fontsize=14
            )
            plt.xlabel("Semana")
            plt.ylabel("Precio en colones")

            plt.grid(
                True,
                linestyle="--",
                alpha=0.5
            )

            plt.legend()
            plt.xticks(rotation=45)
            plt.tight_layout()

            # Mostrar el gráfico
            plt.show()
                

        elif opcion == "2":
            nombre1 = input("Ingrese el nombre del primer producto: ").strip()
            nombre2 = input("Ingrese el nombre del segundo producto: ").strip()
            producto1 = datos[datos["PRODUCTOS"].str.contains(nombre1,case=False,na=False)]
            producto2 = datos[datos["PRODUCTOS"].str.contains(nombre2,case=False,na=False)]

            if producto1.empty:
                print(
                    f"\nNo se encontró ningún producto con el nombre "
                    f"'{nombre1}'."
                )

            if producto2.empty:
                print(
                    f"\nNo se encontró ningún producto con el nombre "
                    f"'{nombre2}'."
                )

            if not producto1.empty and not producto2.empty:
                resultado = (datos[datos["PRODUCTOS"].str.contains(nombre1,case=False,na=False) | datos["PRODUCTOS"].str.contains(nombre2,case=False,na=False)][columnas].sort_values(by=["PRODUCTOS"]))
                print("\nComparación de productos por nombre:\n")
                print(resultado.to_string(index=False))

        elif opcion == "3":
                print("\nFin de la comparación de productos.")
                input("Presione Enter para salir...")
                break

        else:
            print("\nERROR: Opción inválida. Escriba un número del 1 al 3.")

        input("\nPresione Enter para continuar...")
