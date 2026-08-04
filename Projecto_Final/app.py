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
    
    