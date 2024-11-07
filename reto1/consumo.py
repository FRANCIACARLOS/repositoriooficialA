# se importa la libreria de pandas
import pandas as pd 
data = {
    "Nombre": ["Manzana", "Quinoa", "Salmón", "Yogur Griego", "Espinaca", "Frijoles Negros", "Aguacate", "Huevos", "Zanahoria", "Avena"],
    "Categoría": ["Fruta", "Grano", "Proteína", "Lácteos", "Vegetal", "Legumbres", "Fruta", "Proteína", "Vegetal", "Grano"],
    "Calorías": [95, 222, 206, 150, 23, 114, 160, 78, 41, 150],
    "Proteína (g)": [0.5, 8.1, 22, 15, 2.9, 7.6, 2, 6, 0.9, 5],
    "Grasas Totales (g)": [0.3, 3.6, 12, 5, 0.4, 0.5, 15, 5, 0.2, 3],
    "Carbohidratos (g)": [25, 39, 0, 10, 3.6, 20.4, 9, 0.6, 9.6, 27],
    "Apto Veg": ["Sí", "Sí", "No", "No", "Sí", "Sí", "Sí", "No", "Sí", "Sí"],
    "Tiempo Prep (min)": [5, 15, 20, 0, 10, 60, 5, 5, 5, 5],
    "Popularidad (1-5)": [4.5, 4.2, 4.8, 4.7, 4.3, 4.0, 4.6, 4.3, 4.4, 4.5],
    "Sin Gluten": ["Sí", "Sí", "Sí", "No", "Sí", "Sí", "Sí", "Sí", "Sí", "Sí"],
    "Orgánico": ["Sí", "Sí", "No", "Sí", "Sí", "No", "Sí", "No", "Sí", "Sí"]
}
# Crear un DataFrame
df = pd.DataFrame(data)
# Guardar el DataFrame en un archivo CSV
df.to_csv("comida_saludable.csv", index=False)
print("El archivo 'comida_saludable.csv' ha sido creado.")