"""Programa Principal del proyecto modular del BCCR"""

import  matplotlib.pyplot as plt
import pandas as pd

from lectura_datos import leer_archivos_csv()
from limpieza_datos import limpiar_datos, filtrar_diferencial_alto, filtrar_por_tipo_entidad,filtrar_por_entidad



def mostrar_primeras_entradas(datos):
    """Muestra una vita de las columnas principales"""
    
    columnas = ["CODIGO","PRODUCTOS","TIPO","CALIDAD/TAMAÑO","UNIDADVENTA","PRECIO","IVA","SEMANA","MES","AÑO"]
    print(datos[columnas].head().to_string(index=False))

def ejecutar():
    datos_crudos = leer_archivos_csv()
    datos = limpiar_datos(datos_crudos)
    print("Datos cargados exitosamente")
    while True:
        print("\nPROYECTO DE ANALISIS PRECIOS CNP")
        print("1. Mostrar primeras entidades Limpias")
        print("2. Mostrar entidades con diferencial superior al promedio")
        print("3. Promedio por tipo entidad")
        print("4. Mostrar lista de entidades")
        print("5. Graficar")
        print("6. Salir")
        
        opcion = input("Ingrese la opcion del Menu: ").lower().strip()
        if opcion == "1":
            mostrar_primeras_entradas(datos)
        elif opcion == "2":
            pass
        
        elif opcion == "3":
            pass
        elif opcion == "4":
            pass
            
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
    
    