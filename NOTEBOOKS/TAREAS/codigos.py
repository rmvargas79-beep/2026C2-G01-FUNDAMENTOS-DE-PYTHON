"""
try:
    cuenta = float(input("Por Favor Digite el Monto de la Cuenta: ")) #Pedimo el monto de la Cuenta
    propina = float(input("Por Favor Digite el Monto que desea dejar de Propina ✌️: ")) #Monto que desea dejar de propina
    

    

## Proceso
    if cuenta <= 0:  #Verifico que la Cuenta no sea 0 o menos
        print("La Cuenta debe ser mayor a cero.")
    elif propina < 0: # Verifico que la propina no sea Negativa, el usuario puede descidir no dejar propina
        print("La propina no puede ser negativa.")
    else:
        total = cuenta + (cuenta * propina / 100) #A la cuenta le sumo el valor de la propina para el total 
        ## Salida esperada
        print(f"El total de tu cuenta es: {total:.2f}.\n El Subtotal sería: {cuenta:.2f} y el monto de la propina: {(cuenta * propina / 100):.2f}")
    
except ValueError:
    print("Por favor los montos digitados deben ser de numeros.")
    
"""

#El Usuario necesita identificar si el numero es par o impar. Se le solicitara un numero al usuario y el sistema devera devolver si es par o impar.
try:
    numero = int(input("Por Favor Digite el numero a evaluar: ")) #Pedimos el numero a evaluar

## Proceso
    resto = numero % 2 # Asigo el resto de la division entre dos a la variable resto 0 si es par 1 si es impar
    print(resto)
    if resto:  #Verifico si resto es 1 o Verdadero
        print(f"El numero: {numero}, es un numero impar.")
    else: 
        print(f"El numero: {numero}, es un numero par.")
    
except ValueError:
    print("Por favor digitar solamente numeros enteros.")