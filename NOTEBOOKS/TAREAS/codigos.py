# Datos de entrada (SUCIOS)
nombre_input = "  juAN pEREz   "
email_input = "  Juan.Perez@Empresa.COM "

# Escribe tu código aquí:
nombre = nombre_input.strip().title()
email = email_input.strip().lower()
print(f"Usuario: {nombre} | Email: {email}")
# Resultado esperado: "Usuario: Juan Perez | Email: juan.perez@empresa.com"
