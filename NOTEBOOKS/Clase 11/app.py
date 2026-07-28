"""Programa Principal del proyecto modular del BCCR"""

from lectura_datos import URL_BCCR, cargar_tabla_bccr
from limpieza_datos import limpiar_datos


def ejecutar():
    datos_crudos = cargar_tabla_bccr(URL_BCCR)
    datos = limpiar_datos(datos_crudos)
    print("Datos cargados exitosamente de https://gee.bccr.fi.cr")
    while True:
        print("\nPROYECTO DE ANALISIS BCCR")
        print("1. Mostrar primeras entidades Limpias")
        print("2. Mostrar entidades con diferencial superior al promedio")
        print("3. Promedio por tipo entidad")
        print("4. Mostrar lista de entidades")
        print("5. Graficar")
        print("6. Salir")
        
        opcion = input("Ingrese la opcion del Menu: ").lower().strip()
        if opcion == "1":
            datos.info()
            print(datos.head())
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
    
    