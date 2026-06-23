"""Reto integrador: control de ingreso al Anfiteatro del CENAC.

Nombre del estudiante: Ronald Mauricio Vargas Villegas
Fecha: 22/06/2026

Contexto:
El Anfiteatro del Centro Nacional de la Cultura (CENAC), en Costa Rica, tiene
capacidad máxima para 700 personas.
Fuente: https://si.cultura.cr/infraestructura/anfiteatro-del-centro-nacional-de-cultura

Objetivo:
Registre los grupos que desean entrar y evite que la ocupación supere 700.

Reglas:
- Cada entrada es un grupo completo. No se permite entrada parcial.
- Escriba "fin" para terminar.
- Acepte solo enteros mayores que cero.
- Si ocupación actual + grupo <= 700, acepte el grupo.
- Si ocupación actual + grupo > 700, rechace el grupo.

Requisitos:
- Use listas para grupos aceptados y rechazados.
- Use while, for, condicionales y try-except.
- No use menú, while True, funciones propias, CSV, listas anidadas ni
  comprensiones de listas.

Después de cada grupo válido, muestre:
- Mensaje de aceptación o rechazo.
- Ocupación actual.
- Espacios disponibles.

Al finalizar, muestre:
- Grupos aceptados, grupos rechazados y personas admitidas.
- Capacidad máxima, espacios disponibles y porcentaje de ocupación.
- Grupo aceptado más pequeño y más grande, si existe alguno.
- Estado final:
  menos de 560 = disponibilidad normal,
  560 a 699 = ocupación preventiva,
  700 = capacidad completa.

Salida esperada:
Entradas: 650, 60, 50, fin

Grupo aceptado: ingresan 650 personas.
Ocupación actual: 650
Espacios disponibles: 50

Grupo rechazado: no hay espacio para 60 personas.
Ocupación actual: 650
Espacios disponibles: 50

Grupo aceptado: ingresan 50 personas.
Ocupación actual: 700
Espacios disponibles: 0

REPORTE FINAL
Grupos aceptados: 2
Grupos rechazados: 1
Personas admitidas: 700
Capacidad máxima: 700
Espacios disponibles: 0
Porcentaje de ocupación: 100.00%
Grupo aceptado más pequeño: 50
Grupo aceptado más grande: 650
Estado final: capacidad completa.

Otros casos para probar:
- Entradas 100, 200, 150, fin -> 450 personas, estado normal.
- Entrada 701, fin -> grupo rechazado, 0 personas admitidas.
- Entrada fin -> reporte sin grupos aceptados.
- Texto, 0 o negativos -> entrada inválida y el programa continúa.
"""


# Desarrolle su solución a partir de esta línea.
porcentaje_ocupacion = 0.0
cantidad_grupo = 0
grupos_aceptados = [] #Lista de los grupos aceptados
grupos_rechazados = [] #Lista de los grupos rechazados
grupo_aceptado = 0
grupo_rechazado = 0
personas_admitidas = 0
CAPACIDAD_MAXIMA = 700
campos_disponibles = 700
continuar = True # condicion para terminar
estado_final = "Disponibilidad Normal"

while continuar:

    eleccion = input("Digite la cantidad de personas o 'fin' para terminar: ").strip().lower()
    
    if eleccion == "fin":
        porcentaje_ocupacion = (personas_admitidas / CAPACIDAD_MAXIMA) * 100
        if campos_disponibles == 0:
            estado_final = "Capacidad Completa"
        elif campos_disponibles >= 560 and campos_disponibles < 699:
            estado_final = "Ocupación Preventiva"
        
        print("\n📈 REPORTE FINAL")
        print(f"Grupos aceptados: {grupo_aceptado}")
        print(f"Grupos rechazados: {grupo_rechazado}")
        print(f"Personas admitidas: {personas_admitidas}")
        print(f"Capacidad máxima: {CAPACIDAD_MAXIMA}")
        print(f"Espacios disponibles: {campos_disponibles}")
        print(f"Porcentaje de ocupación: {porcentaje_ocupacion:.2f}%")
        print(f"El Grupo mas pequeño aceptado es : {min(grupos_aceptados)}")
        print(f"El Grupo mas grande aceptado es : {max(grupos_aceptados)}")        
        print(f"Estado final: {estado_final}")
        continuar = False

    else:
        cantidad_grupo = int(eleccion)

        if cantidad_grupo <= 0:
            print(f"El grupo debe ser mayor a cero. ✖️")
            
        if personas_admitidas + cantidad_grupo <= CAPACIDAD_MAXIMA:
            grupo_aceptado += 1
            personas_admitidas += cantidad_grupo
            grupos_aceptados.append(cantidad_grupo)
            campos_disponibles = (CAPACIDAD_MAXIMA - personas_admitidas)
            print("Bienvenidos a la actividad por favor pasen adelante.")
            print(f"Ocupación actual es de: {personas_admitidas} personas.")
            print(f"La cantidad de campos disponibles es de: {campos_disponibles}.")

        else:
            print(f"Lo sentimos no tenemos mas lugares")
            print(f"La cantidad de campos disponibles es de: {campos_disponibles}.")
            grupos_rechazados.append(cantidad_grupo)
            grupo_rechazado += 1
    
    