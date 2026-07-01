"""Practica Semana 07: analisis de emprendimientos costarricenses.

Complete los espacios marcados con TODO. El objetivo es generar un reporte por
sede usando listas, diccionarios, funciones, ciclos y condicionales.
"""

from sedes import sedes

reporte = []
lista_impresion = []
venta_mas_alta = 0

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

def calcular_porcentaje(total,ventas, formato = False):
    porcentaje = total / meta * 100
    if formato:
        return f"{total / meta * 100:.2f}%"
    
    return porcentaje

def calcular_clasificacion(total, meta):
    porcentaje = calcular_porcentaje(total, meta)
    if porcentaje >= 100:
        mensaje_sede = "Meta alcanzada."
    elif porcentaje >= 80:
        mensaje_sede = "Meta casi alcanzada, prestar atencion."
    else:
        mensaje_sede = "Meta no alcanzada URGE ATENCION"

    return mensaje_sede

def calcular_provincias(sedes):
    
    provincias = []
    for sede in sedes:
        prov = sede["provincia"] 
        if prov not in provincias:
            provincias.append(prov)     
        
    return provincias


def imprimir_reporte(lista_impresion):
    
    """Imprime el reporte final de ventas por sede."""
    print("REPORTE FINAL")
    print("-" * 50)

    for fila in lista_impresion:
        print(f"Sede: {fila['nombre']}")
        print(f"Provincia: {fila['provincia']}")
        print(f"Tipo: {fila['tipo']}")
        print(f"Total semanal: ₡{fila['total']:,.0f}")
        print(f"Promedio diario: ₡{fila['promedio']:,.0f}")
        print(f"Cumplimiento: {fila['porcentaje']}%")
        print(f"Estado: {fila['estado']}")
        print("-" * 50)

    
    
    return reporte

def calcular_ingresos(sedes):
    sedes_mas_altas = []
    venta = 0
    
    for sede in sedes:
        
        if venta < sum(sede["ventas"]):
            venta= sum(sede["ventas"])
            sedes_mas_altas = [sede["nombre"]]
            sedes_mas_altas.append(sum(sede["ventas"]))
        elif venta == sum(sede["ventas"]):
            sedes_mas_altas.append(sede["nombre"])
            sedes_mas_altas.append(sum(sede["ventas"]))

    return sedes_mas_altas




for sede in sedes:




    ventas = sede["ventas"]
    meta= sede["meta"]
    total_sede = calcular_total(ventas)
    promedio_sede = calcular_promedio(ventas)
    porcentaje= calcular_porcentaje(total_sede,meta,True)
    estado = calcular_clasificacion(total_sede,meta)

    if venta_mas_alta <= total_sede:
        venta_mas_alta = total_sede
        #agregar una lista de la sede
    
    lista_impresion.append(
        {
            "nombre": sede["nombre"],
            "provincia": sede["provincia"],
            "tipo": sede["tipo"],
            "total": total_sede,
            "promedio": promedio_sede,
            "porcentaje": porcentaje,
            "estado": estado,
        }
    )
    print(imprimir_reporte(lista_impresion))
    #print(porcentaje, total_sede)


print("Cantidad de sedes:", len(lista_impresion))
provincias = calcular_provincias(sedes)
print(f"Las Provincias Evaluadas son : {provincias}")
ventas_mayores = calcular_ingresos(sedes)
print(f"Las Sedes con Mayores ventas son:")
print(ventas_mayores)
#print(len(ventas_mayores))




#print(imprimir_reporte(reporte))
#MAS ingresos
#Provincias


