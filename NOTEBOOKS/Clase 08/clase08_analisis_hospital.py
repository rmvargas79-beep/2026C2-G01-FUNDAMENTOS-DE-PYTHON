"""Semana 08: analisis basico de pacientes desde JSON.

Complete los requerimientos indicados. El objetivo principal es practicar
ciclos: recorrer una lista de pacientes leida desde JSON y acumular indicadores
simples.
"""

import json

ARCHIVO_DATOS = "NOTEBOOKS\Clase 08\datos_clinica.json" #clinica_avanzada.json


def calcular_promedio(suma, cantidad):
    """Retorna el promedio de una suma entre una cantidad."""
    return suma / cantidad


def es_adulto_mayor(edad):
    """Retorna True si la edad corresponde a una persona adulta mayor."""
    
    if edad >= 60:
        return True
    else:
        return False


# REQUERIMIENTO 1:
# Construya aqui la lectura del JSON con el docente.
# Al terminar, la variable pacientes debe tener 15 registros.
with open(ARCHIVO_DATOS,"r", encoding="utf-8") as archivo:
    pacientes = json.load(archivo)

#print("Tipo de datos:", type(pacientes))
#print("Cantidad de Pacientes:", len(pacientes))
primer_paciente = pacientes[0]

# 2. Exploracion inicial
print("Cantidad de pacientes:", len(pacientes))

if len(pacientes) == 0:
    print("Primero construya con el docente la lectura del JSON.")
    print("Cuando cargue correctamente, debe mostrar 15 pacientes.")
else:
    # REQUERIMIENTO 2:
    # Explore el primer paciente y muestre sus llaves y valores.
    print("Primer Paciente:", primer_paciente)
    print("Campos del diccionario:", primer_paciente.keys())
    

    # Variables acumuladoras del analisis.  suma_edades, conteo_san_jose, 
    # conteo_mujeres, conteo_hombres y adultos_mayores.
    suma_edades = 0
    conteo_san_jose = 0
    conteo_mujeres = 0
    conteo_hombres = 0
    adultos_mayores = []
    lista_enfermedades = []
    conteo_enfermedades = {}

    # 4. Ciclo principal
    # Cada vuelta del ciclo representa un paciente del JSON.
    for paciente in pacientes:
        nombre = paciente["nombre"]
        edad = paciente["edad"]
        provincia = paciente["provincia"]
        genero = paciente["genero"]
        enfermedades = paciente["enfermedades"]

        # REQUERIMIENTO 3:
        # Complete aqui los acumuladores dentro del ciclo.

        # 3.1 Sume la edad del paciente en suma_edades
        suma_edades = paciente["edad"] + suma_edades
        # 3.2 Si la provincia es "San Jose", aumente conteo_san_jose
        if paciente["provincia"] == "San Jose":
            conteo_san_jose += 1
        
        # 3.3 Si genero es "F", aumente conteo_mujeres
        if paciente["genero"] == "F":
            conteo_mujeres += 1
        
        # 3.4 Si genero es "M", aumente conteo_hombres
        if paciente["genero"] == "M":
            conteo_hombres += 1
        # 3.5 Si es_adulto_mayor(edad) es True, agregue el nombre
        # a adultos_mayores
        if es_adulto_mayor(paciente["edad"]):
            adultos_mayores.append(paciente["nombre"])
        # RETO FINAL OPCIONAL:
        # Cada paciente tiene una lista en paciente["enfermedades"].
        # Guarde esa lista en una variable y sume su cantidad con len().
        for enfermedad in paciente["enfermedades"]:
            if enfermedad not in lista_enfermedades:
                lista_enfermedades.append(enfermedad)
            if enfermedad in conteo_enfermedades:
                conteo_enfermedades[enfermedad] +=1
            else:
                conteo_enfermedades[enfermedad] = 1
        


    # REQUERIMIENTO 4:
    # Calcule la edad_promedio usando calcular_promedio().
    edad_promedio = 0
    edad_promedio = calcular_promedio(suma_edades,len(pacientes))

    # Resultados
    print("\nRESUMEN BASICO")
    print("Edad promedio:", round(edad_promedio, 1))
    print("Pacientes de San Jose:", conteo_san_jose)
    print("Mujeres:", conteo_mujeres)
    print("Hombres:", conteo_hombres)
    print("Adultos mayores:", adultos_mayores)
    print("Cantidad de Enfermedades Unicas:", len(lista_enfermedades))

    # REQUERIMIENTO 5:
    # Escriba dos conclusiones basadas en los resultados.
    print("\nCONCLUSIONES")
    print("Conclusion 1: Para recorrer listas siempre es mejor mas facil y sencillo usar For")
    print("Conclusion 2: La sintaxis es super importante, despues de los errores se logica la sintaxis es muy comun")

    print("\nCONTEO Enfermedades")
    for enfermedad, cantidad in conteo_enfermedades.items():
        print(enfermedad, ":", cantidad)
    
    