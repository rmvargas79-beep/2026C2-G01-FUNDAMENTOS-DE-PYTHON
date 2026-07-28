"""Programa Principal del proyecto modular del BCCR"""

from lectura_datos import URL_BCCR, cargar_tabla_bccr
from limpieza_datos import limpiar_datos


def ejecutar():
    datos_crudos = cargar_tabla_bccr(URL_BCCR)
    datos = limpiar_datos(datos_crudos)
    datos.info()
    print(datos_crudos.head())
    print(datos.head())
    datos.info()



if __name__ == "__main__":
    ejecutar()
    
    