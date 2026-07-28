"""Programa Principal del proyecto modular del BCCR"""

from lectura_datos import URL_BCCR, cargar_tabla_bccr
from limpieza_datos import limpiar_datos, filtrar_diferencial_alto, filtrar_por_tipo_entidad,filtrar_por_entidad, mostrar_primeras_entidades



def mostrar_primeras_entidades(datos):
    """Muestra una vita de las columnas principales"""
    
    columnas = ["ENTIDAD","COMPRA","VENTA","DIFERENCIAL"]
    print(datos[columnas].head().to_string(index=False))

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
            mostrar_primeras_entidades(datos)
        elif opcion == "2":
            resultado = filtrar_diferencial_alto(datos)
            resultado = resultado.sort_values(by="DIFERENCIAL", ascending=False)
            mostrar_primeras_entidades(resultado)
        
        elif opcion == "3":
            filtrado = filtrar_por_tipo_entidad(datos)
            print(filtrado.to_string())
        elif opcion == "4":
            entidades = filtrar_por_entidad(datos)
            print(entidades.to_string())
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
    
    