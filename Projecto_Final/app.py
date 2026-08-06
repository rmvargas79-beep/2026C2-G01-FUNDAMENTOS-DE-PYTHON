"""Programa Principal del proyecto modular del BCCR"""

import  matplotlib.pyplot as plt
import pandas as pd

from procesamiento_datos import (calcular_variacion_periodos, calcular_menor_variacion_periodos , mostrar_primeras_entradas,
                                comparar_productos, calcular_menor_variacion_precio, calcular_mayor_variacion_precio)

from lectura_datos import leer_archivos_csv
from limpieza_datos import limpiar_datos

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
            nombre= df[df["CODIGO"] == int(producto)]["PRODUCTOS"].iloc[0]
            plt.plot(df["MES"], df["PRECIO"], label="PRECIO", color="blue", marker="o")
            plt.title("Historial de Precios del Producto " + nombre)
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
    
    