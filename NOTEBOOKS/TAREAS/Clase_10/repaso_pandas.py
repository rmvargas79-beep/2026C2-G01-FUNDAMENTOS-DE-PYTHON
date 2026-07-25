#Repaso Tutoria 25/07/2026
#pip install pandas

import pandas as pd

pts = 42
datos = {
    "estudiante": ["Pamela", "Ronald", "Maria", "Luis"],
    "puntos": [40, 36, 25, 20],
    "edad":[20, 25, 19, 30]
        
}

estudiantes = pd.DataFrame(datos)
print(estudiantes.shape)
print(estudiantes)


estudiantes["nota"] = (estudiantes["puntos"] * 100) / pts

estudiantes["Estado"] = estudiantes["nota"].apply( lambda nota: "Aprobado" if nota >= 70 else "Reprobado")


print(estudiantes)