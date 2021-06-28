from sklearn import datasets
import pandas as pd
import matplotlib.pyplot as plt

print("CARGANDO EL ARCHIVO......")
print("------------------------------------------------------------------------------------------------")
data = pd.read_csv('netflix_titles.csv')
print(data)
print()
print("------------------------------------------------------------------------------------------------")


print("Visualizar los primeros 10 registros del conjunto de datos")
print("------------------------------------------------------------------------------------------------")
print(data.head(10))
print()
print("------------------------------------------------------------------------------------------------")

print("Visualizar los últimos 15 registros del conjunto de datos")
print("------------------------------------------------------------------------------------------------")
print(data.tail(15))
print()
print("------------------------------------------------------------------------------------------------")


print("Generar los estadísticos básicos")
print("------------------------------------------------------------------------------------------------")
print(data.describe())
print()
print("------------------------------------------------------------------------------------------------")

print("Verificando si hay valores vacios")
print("------------------------------------------------------------------------------------------------")
print(data.isnull())
print()
print("------------------------------------------------------------------------------------------------")

print("Completar todos los datos vacíos (na) con ceros (0)")
print("------------------------------------------------------------------------------------------------")
datallena = data.fillna(0)
print(datallena)
print()
print("------------------------------------------------------------------------------------------------")


print("Realizar un gráfico de tipo 'scatter' utilizando para el eje X la variable 'release_year'y para el eje Y la variable'type_id'.")
print("------------------------------------------------------------------------------------------------")
graficar = datallena.plot(x='show_id', y='release_year', kind='scatter', color="red")
plt.show()
print()
print()
print("------------------------------------------------------------------------------------------------")




