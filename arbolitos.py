import pandas as pd
import matplotlib.pyplot as plt

# Asegúrate de reemplazar 'ruta/a/tu/archivo.csv' con la ruta correcta a tu archivo
df = pd.read_csv('./arbolado-publico-lineal-2017-2018.csv')

# Imprime todas las especies únicas en el dataset
especies_unicas = df['nombre_cientifico'].unique()
especies_unicas.sort()
#print(especies_unicas)

# Imprime la cantidad de apariciones de cada especie
conteo_especies = df['nombre_cientifico'].value_counts()
#print(conteo_especies)

# # Crea una figura y un conjunto de subtramas
# fig, ax = plt.subplots()

# # Crea un gráfico de barras con el conteo de especies
# conteo_especies.plot(kind='bar', ax=ax)

# # Establece las etiquetas de los ejes
# ax.set_xlabel('Especies')
# ax.set_ylabel('Cantidad')

# # Muestra el gráfico
# plt.show()

# Filtra el conteo de especies para incluir solo las especies con más de 500 apariciones
especies_filtradas = conteo_especies[conteo_especies >= 500]

# Convierte especies_unicas a un objeto Series de pandas
especies_unicas = pd.Series(especies_unicas)

# Actualiza especies_unicas para incluir solo las especies filtradas
especies_unicas = especies_unicas[especies_unicas.isin(especies_filtradas.index)]

# Ordena las especies únicas
especies_unicas.sort_values(inplace=True)

print(len(especies_unicas))
