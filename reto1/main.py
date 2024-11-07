#consumo de alimentos saludables
# se importa la libreria de pandas
import pandas as pd
# se define la ruta del path 
path='calories.csv'
# se lee el archivo CSV
Data=pd.read_csv(path,encoding='latin1')
# se imprime la información
print(type(Data))
print(Data) 