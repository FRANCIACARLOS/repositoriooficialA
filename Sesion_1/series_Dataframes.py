#importamos la biblioteca pandas y la llamamos "pd"
import pandas as pd

# creamos una serie de pandas que es como una lista de etiquetas 
# Los valores son nombres de jugadores de PSG
# El indice especifica los numeros de caisetas de esos jugadores
psg_players = pd.Series (
    ["Navas","Mbappe", "Neymar", "Messi"],  #Lista de nombres de jugadores
    index=[ 1, 7, 10, 30]
)
#Eliminammos el indice, por lo que pandas asigna un indice núerico autómatico 
#empezando desde 0
psg_players = pd.Series (
    ["Navas","Mbappe", "Neymar", "Messi"],  #Lista de nombres de jugadores
)
#imprime la serie para ver su contenido
print(psg_players) 


#importamos la biblioteca pandas y la llamamos "pd"
import pandas as pd
#creamos una serie de pandas usando una lista 
psg_dict={1: "Navas",7: "Mbappe",10: "Neymar",30: "Messi"}
#creamos una serie de pandas usando el diccionario
psg_players_dict= pd.Series(psg_dict)
#imprime la serie creada a partir del diccionario
print(psg_players_dict) 
#imprime la serie creada a partir del diccionario
print(psg_players_dict[7]) 
#imprime la serie creada a partir del diccionario
print(psg_players_dict) 
#imprimimos el valor en la posición (indice) 7 de la serie creada a partir del diccionario
print(psg_players_dict[7]) 
print(psg_players_dict[0:3]) 
#Diccionario con datos de jugadores
dict={"jugador":["Navas", "Mbappe", "Neymar", "Messi"],
      "Altura": [183.0, 170.0, 170.0, 165.0],
      "Goles": [2, 200, 150, 200]}
# Crear un Dataframe con el diccionario y indices personalizados
df = pd.DataFrame(dict, index=[1, 7, 10, 30])
#Imprimir el Dataframe
print(df)
