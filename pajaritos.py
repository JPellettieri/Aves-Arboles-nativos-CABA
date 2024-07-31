import pandas as pd
import seaborn as sns

df = pd.read_csv('./aves.csv', sep='\t', lineterminator='\n', encoding='latin-1')

# Imprimir dimensiones de df
print(df.shape)
print(df.head())
#print(df.columns)

#Imprimir tabla de Aves 
#print(df['especie'])

# Imprimir especies
#especies = df['especie'].unique()
#print(especies)

# Selecciona solo las columnas de interés
df_filtrado = df[['order', 'family', 'genus', 'species', 'decimalLatitude',	'decimalLongitude']]

# Muestra las primeras 5 filas del DataFrame filtrado
# print(df_filtrado.head())

# Exporta el DataFrame filtrado a un nuevo archivo CSV
#df_filtrado.to_csv('aves_filtradas.csv', index=False)

import matplotlib.pyplot as plt

### HISTOGRAMA DE ESPECIES ###
# Obtiene el conteo de cada especie
conteo_especies = df_filtrado['species'].value_counts()
# Crea el histograma
conteo_especies.plot(kind='bar')
# Establece las etiquetas de los ejes
# plt.xlabel('Especies')
# plt.ylabel('Abundancia')
# plt.title('Histograma de Especies')
# Muestra el histograma
# plt.show()

### HISTOGRAMA DE FAMILIAS ###
# Obtiene el conteo de cada familia
conteo_especies = df_filtrado['family'].value_counts()
# Crea el histograma
conteo_especies.plot(kind='bar')
# Establece las etiquetas de los ejes
# plt.xlabel('Familia')
#plt.ylabel('Abundancia')
#plt.title('Histograma de Familias')
# Muestra el histograma
# plt.show()
### Tabla de abundancia de familias###
abundancia_familias = df_filtrado['family'].value_counts()
# Convierte la serie en un DataFrame para una mejor visualización
df_abundancia_familias = abundancia_familias.reset_index()

# Renombra las columnas
df_abundancia_familias.columns = ['Familia', 'Abundancia']

# Muestra la tabla
#print(df_abundancia_familias)
# Muestra las filas desde la 20 hasta la 40
# print(df_abundancia_familias.iloc[20:50])

# Filtra las familias que tienen más de 50 observaciones
df_abundancia_familias_filtradas = df_abundancia_familias[df_abundancia_familias['Abundancia'] > 50]

# Muestra la tabla filtrada
#print(df_abundancia_familias_filtradas)

import matplotlib.pyplot as plt

# Crea un scatter plot con las coordenadas de las aves
plt.figure(figsize=(10, 10))
for especie in df_filtrado['species'].unique():
    df_especie = df_filtrado[df_filtrado['species'] == especie]
    plt.scatter(df_especie['decimalLongitude'], df_especie['decimalLatitude'], label=especie)

plt.xlabel('Longitud')
plt.ylabel('Latitud')
plt.title('Distribución espacial de las especies de aves')
plt.legend()
# plt.show()


import matplotlib.pyplot as plt
import numpy as np

# Crea un scatter plot con las coordenadas de las aves
# plt.figure(figsize=(10, 10))
for especie in df_filtrado['species'].unique():
    df_especie = df_filtrado[df_filtrado['species'] == especie]
    plt.scatter(df_especie['decimalLongitude'], df_especie['decimalLatitude'], label=especie)

# Crea una grilla
# plt.grid(True, which="both", linestyle='--', linewidth=0.5)
#plt.xticks(np.arange(df_filtrado['decimalLongitude'].min(), df_filtrado['decimalLongitude'].max(), 0.01))
#plt.yticks(np.arange(df_filtrado['decimalLatitude'].min(), df_filtrado['decimalLatitude'].max(), 0.01))

#plt.xlabel('Longitud')
#plt.ylabel('Latitud')
#plt.title('Distribución espacial de las especies de aves')
#plt.legend()
#plt.show()

# Crea una copia de df_filtrado para evitar SettingWithCopyWarning
df_filtrado = df_filtrado.copy()

# Crea nuevas columnas para las coordenadas del sector
df_filtrado['sector_latitud'] = (df_filtrado['decimalLatitude'] / 0.01).round().astype(int)
df_filtrado['sector_longitud'] = (df_filtrado['decimalLongitude'] / 0.01).round().astype(int)

# Agrupa por sector y calcula la abundancia y el número de especies únicas en cada sector
df_sectores = df_filtrado.groupby(['sector_latitud', 'sector_longitud']).agg(
    Abundancia=('family', 'count'),
    Especies=('species', 'nunique')
)

# Muestra la tabla
print(df_sectores)

import matplotlib.pyplot as plt
import numpy as np

# Crea un scatter plot con las coordenadas de los sectores
plt.figure(figsize=(10, 10))

# Usa el número de especies como color de los puntos
plt.scatter(df_sectores.reset_index()['sector_longitud'] * 0.01, df_sectores.reset_index()['sector_latitud'] * 0.01, 
            c=df_sectores['Especies'], cmap='Greens')

# Crea una grilla
plt.grid(True, which="both", linestyle='--', linewidth=0.5)
plt.xticks(np.arange(df_filtrado['decimalLongitude'].min(), df_filtrado['decimalLongitude'].max(), 0.01))
plt.yticks(np.arange(df_filtrado['decimalLatitude'].min(), df_filtrado['decimalLatitude'].max(), 0.01))

plt.xlabel('Longitud')
plt.ylabel('Latitud')
plt.title('Distribución espacial de las especies de aves')
plt.colorbar(label='Número de especies')
plt.show()