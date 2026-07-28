"""Programa Principal del proyecto modular del BCCR"""

from lectura_datos import URL_BCCR, cargar_tabla_bccr



def ejecutar():
    datos_crudos = cargar_tabla_bccr(URL_BCCR)
    print(datos_crudos)



if __name__ == "__main__":
    ejecutar()
    
    