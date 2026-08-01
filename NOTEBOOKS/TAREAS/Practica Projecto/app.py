from carga_datos import cargar_datos


def ejecutar():
    df = cargar_datos()
    if df.empty:
        print("No se pudieron cargar los datos.")
    else:
        print("\nPrimeros cinco registros del dataset:")
        print(df.head())

if __name__ == "__main__":
    ejecutar()