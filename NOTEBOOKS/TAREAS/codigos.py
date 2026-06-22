# Datos de entrada (SUCIOS)
#nombre_input = "  juAN pEREz   "
#email_input = "  Juan.Perez@Empresa.COM "

# Escribe tu código aquí:
#nombre = nombre_input.strip().title()
#email = email_input.strip().lower()
#print(f"Usuario: {nombre} | Email: {email}")
# Resultado esperado: "Usuario: Juan Perez | Email: juan.perez@empresa.com"



ventas_semana = [145000, 118000, 162000, 137000, 128000]
META_SEMANAL = 700000
#

cantidad_dias = len(ventas_semana)
total_ventas = sum(ventas_semana)
promedio_ventas = total_ventas / cantidad_dias
venta_mayor = max(ventas_semana)
venta_menor = min(ventas_semana)
rango_ventas = venta_mayor - venta_menor
porcentaje_meta = (total_ventas / META_SEMANAL) * 100
meta_alcanzada = total_ventas >= META_SEMANAL


if meta_alcanzada:
    meta_supera = total_ventas - META_SEMANAL
else:
    meta_faltante = META_SEMANAL - total_ventas
    

import matplotlib.pyplot as plt

ventas_semana = [145000, 118000, 162000, 137000, 128000]
META_SEMANAL = 700000

dias = ["Lun", "Mar", "Mié", "Jue", "Vie"]


if meta_alcanzada:
    mensaje = f"Meta alcanzada. Superada por: {meta_supera:,.0f}"
else:
    mensaje = f"Meta NO alcanzada. Faltan: {meta_faltante:,.0f}"

plt.bar(dias, ventas_semana, label="Ventas")

plt.axhline(
    y=META_SEMANAL / len(ventas_semana),
    linestyle="--",
    label="Meta diaria promedio"
)

plt.title("Ventas vs Meta")
plt.xlabel("Días")
plt.ylabel("Ventas ($)")
plt.legend()

# Mostrar mensaje debajo del gráfico
plt.figtext(
    0.5,      # posición horizontal (centro)
    0.01,     # posición vertical (parte inferior)
    mensaje,
    ha="center",
    fontsize=10
)

plt.show()
