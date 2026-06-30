"""Practica Semana 07: analisis de emprendimientos costarricenses.

Complete los espacios marcados con TODO. El objetivo es generar un reporte por
sede usando listas, diccionarios, funciones, ciclos y condicionales.
"""

from sedes import sedes


def calcular_total(ventas):
    """_Recibo una lista, la sumo y retorno el total.

    Args:
        ventas (list): Lista con las ventas del emprendimiento

    Returns:
        float: Sumatoria total de Ventas
    """
    return sum(ventas)

def calcular_promedio(lista):
    """Retorna el promedio de ventas de una Lista"""
    return sum(lista) / len(lista)

def calcular_procentaje(total,ventas, formato = False):
    porcentaje = total / meta * 100
    if formato:
        return f"{total / meta * 100:.2f}%"
    
    return porcentaje

def calcular_clasificacion(total, meta):
    porcentaje = calcular_porcetaje(total, meta)
    if porcentaja_sede >= 100:
        mensaje_sede = "Meta alcanzada."
    elif porcentaja_sede >= 80:
        mensaje_sede = "Meta casi alcanzada, prestar atencion."
    else:
        "Meta no alcanzada URGE ATENCION"

reporte = []

"""
    print(sedes)
    print("Cantidad de sedes: ", len(sedes))
    print ("Tipo Variables sedes:", type(sedes[0]))
    print("Datos por sede: ", sedes[0].keys())
    print("Primera sede: ", sedes[0])
    print("Nombre Primera sede: ", sedes[0]["nombre"])
""" 
for sede in sedes:




    ventas = sede["ventas"]
    meta= sede["meta"]
    total_sede = calcular_total(ventas)
    promedio_sede = calcular_promedio(ventas)
    porcentaje_sede = calcular_procentaje(total_sede,meta, True)
    estado = calcular_clasificacion(total_sede,meta)


    print(porcentaja_sede, total_sede)




#print(imprimir_reporte(reporte))
#MAS ingresos
#Provincias


