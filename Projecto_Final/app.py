"""Programa Principal del proyecto modular del BCCR"""

import  matplotlib.pyplot as plt
import pandas as pd

from procesamiento_datos import (calcular_variacion_periodos, calcular_menor_variacion_periodos , mostrar_primeras_entradas,
                                comparar_productos, calcular_menor_variacion_precio)

from lectura_datos import leer_archivos_csv
from limpieza_datos import limpiar_datos



    
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
        elif opcion == "2":
            calcular_mayor_variacion_precio(datos)        
        elif opcion == "3":
            calcular_menor_variacion_precio(datos)
        elif opcion == "4":
            comparar_productos(datos)
            
        elif opcion == "5":
            """Graficar el historial de precios de un producto a lo largo del tiempo"""
            plt.figure(figsize=(12, 8))
            producto = input("Ingrese el Codigo del producto: ").strip()
            df = datos.copy()
            df = df[df["CODIGO"] == int(producto)]
            plt.plot(df["MES"], df["PRECIO"], label="PRECIO", color="blue", marker="o")
            plt.title("Historial de Precios del Producto")
            plt.xlabel("Mes")
            plt.ylabel("Precio en Colones")
            plt.tight_layout() 
            plt.legend()
            plt.show()
            
            
        elif opcion == "6":
            print("\nAnalisis Finalizado")
            input("Presione Enter para Salir...")
            break
        else:
            print("\nERROR Opcion invalida. Escriba un numero del 1 al 6.")
            
        input("Presione enter para continuar..")

if __name__ == "__main__":
    ejecutar()
    
    