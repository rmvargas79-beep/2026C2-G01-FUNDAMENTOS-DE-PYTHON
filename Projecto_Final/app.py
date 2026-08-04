"""Programa Principal del proyecto modular del BCCR"""

import  matplotlib.pyplot as plt
import pandas as pd

from lectura_datos import leer_archivos_csv
from limpieza_datos import limpiar_datos



def mostrar_primeras_entradas(datos):
    """Muestra una vita de las columnas principales"""
    
    columnas = ["CODIGO","PRODUCTOS","TIPO","CALIDAD"]
    datos_ordenados = datos.sort_values(by="PRODUCTOS")
    datos_ordenados = datos_ordenados.drop_duplicates(subset="CODIGO")
    #print(datos_ordenados[columnas].to_string(index=False))
    
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
                resultado = (datos[datos["CODIGO"].isin([codigo1, codigo2])][columnas].sort_values(by=["CODIGO"]))
                print("\nComparación de productos por código:\n")
                print(resultado.to_string(index=False))

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


    
def calcular_mayor_variacion_precio(datos):
    """Muestra los 10 productos con mayor variación de precio."""

    while True:
        print("\nMostrar los 10 productos con mayor variación de precio")
        print("1. Comparar dos semanas")
        print("2. Comparar dos meses")
        print("3. Comparar dos años")
        print("4. Salir")

        opcion = input("Ingrese la opción del menú: ").strip()

        if opcion == "1":
            
            semana1 = int(input("Digite el número de la primera semana: ").strip())
            semana2 = int(input("Digite el número de la segunda semana: ").strip())
            

            calcular_variacion_periodos(
                datos=datos,
                columna_periodo="SEMANA",
                periodo1=semana1,
                periodo2=semana2,
                descripcion="semanas"
            )

        elif opcion == "2":
            mes1 = input(
                "Digite el nombre del primer mes: "
            ).strip().capitalize()

            mes2 = input(
                "Digite el nombre del segundo mes: "
            ).strip().capitalize()

            calcular_variacion_periodos(datos=datos,columna_periodo="MES",periodo1=mes1,periodo2=mes2,descripcion="meses")
            
        elif opcion == "3":
            anio1 = int(input("Digite el primer año: ").strip())
            anio2 = int(input("Digite el segundo año: ").strip())
            
            calcular_variacion_periodos(datos=datos,columna_periodo="AÑO",periodo1=anio1,periodo2=anio2,descripcion="años")

        elif opcion == "4":
            print("\nFin del análisis de variación de precios.")
            input("Presione Enter para salir...")
            break

        else:
            print("\nERROR: Opción inválida. Escriba un número del 1 al 4.")

        input("\nPresione Enter para continuar...")    
    

def calcular_variacion_periodos(datos,columna_periodo,periodo1,periodo2,descripcion):
    """Calcula los 10 productos con mayor variación entre dos períodos."""

    datos_calculo = datos.copy()

    # Asegurar que PRECIO sea numérico
    datos_calculo["PRECIO"] = pd.to_numeric(datos_calculo["PRECIO"],errors="coerce")

    # Eliminar registros sin código o precio
    #datos_calculo = datos_calculo.dropna(subset=["CODIGO", "PRECIO"])

    # Filtrar el primer período
    datos_periodo1 = datos_calculo[datos_calculo[columna_periodo] == periodo1].copy()

    # Filtrar el segundo período
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

    print(
        datos_finales[columnas_mostrar].to_string(
            index=False,
            formatters={
                "PRECIO_PERIODO_1": "{:,.2f}".format,
                "PRECIO_PERIODO_2": "{:,.2f}".format,
                "VARIACION": "{:,.2f}".format,
                "VARIACION_PORCENTUAL": "{:,.2f}%".format
            }
        )
    )


def ejecutar():
    datos_crudos = leer_archivos_csv()
    datos = datos_crudos.copy()
    datos = limpiar_datos(datos_crudos)
    print("Datos cargados exitosamente")
    while True:
        print("\nPROYECTO DE ANALISIS PRECIOS CNP")
        print("1. Mostrar Lista de Productos")
        print("2. Mostrar Diez Productos con Mayor variacion de Precio")
        print("3. Mostrar Diez Productos con Menor variacion de Precio")
        print("4. Comparar Dos Productos")
        print("5. Mostrar Historial de un Producto")
        print("6. Salir")
        
        opcion = input("Ingrese la opcion del Menu: ").lower().strip()
        if opcion == "1":
            mostrar_primeras_entradas(datos)
            #print(len(datos))
            #datos.info()
            #print(datos.head())
        elif opcion == "2":
            pass
        
        elif opcion == "3":
            pass
        elif opcion == "4":
            comparar_productos(datos)
            
        elif opcion == "5":
            pass
        elif opcion == "6":
            print("\nAnalisis Finalizado")
            input("Presione Enter para Salir...")
            break
        else:
            print("\nERROR Opcion invalida. Escriba un numero del 1 al 6.")
            
        input("Presione enter para continuar..")
    #datos.info()
    #print(datos_crudos.head())
    #print(datos.head())
    #atos.info()



if __name__ == "__main__":
    ejecutar()
    
    