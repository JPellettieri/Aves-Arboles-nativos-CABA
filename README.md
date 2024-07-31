# Aves-Arboles-nativos-CABA
Impacto de la composición florística de ambientes urbanos en los ensambles de aves, CABA, Argentina
Titulo:
"Impacto de la composición florística de ambientes urbanos en los ensambles de aves, CABA, Argentina”
Objetivo:
Estudiar las relaciones entre el arbolado urbano y los ensambles de aves presentes en CABA
Método:
Empleando base de datos de arboles de la ciudad de buenos aires y el avistaje de aves realizado con la aplicacion  "EOD – eBird Observation Dataset"
Fuente de datos de aves: https://www.gbif.org/es/dataset/search DOI10.15468/dl.zcdpuc 
Pasos de análisis de datos:
1.	Filtrado de datos, me quedo con las observaciones que se observaron mas de ... veces
2.	Clasificación entre nativo y exótico (según país nomas) tanto de aves como de arboles
3.	Dividir el territorio de la provincia de BsAs en grilla, No estoy segura que tamaño asignarle a la grilla considere recuadros de 10x10 cuadras
4.	Dar formato a datos para que quede: 
N° de recuadro – N° de especies de arboles presentes- N° de especies de aves presentes- Porcentaje de natividad de arboles- Porcentaje de natividad de aves
5.	¿Hay correlación? ¿Las regiones con mas especies de arboles nativos tienden a presentar mas proporción de aves nativas?
Preguntas de completitud:
¿Qué especies de aves son indicadores de lugares con pocos arboles nativos? ¿Cuáles de lugares con muchas exóticas? 
Para este análisis: 
1.	Determino que porcentaje es considerados esencialmente nativo, que porcentaje es considerado esencialmente exótico y dejo un intermedio de “mixto”. 
Posible: exótico menos de 30% nativas, Mixto entre 30% y 60%, Nativo más de 60%
2.	Evalúo anidamiento en cada una de las categorías. La especie que este presente en la mayoría de cada categoría y no se encuentre en las otras se la puede considerar posible indicadora.
Debería analizar abundancia relativa de cada especie? Análisis de composición?

Actividades:
1)	Exploración de datos:
•	Mapa de aves sin Nan (sacar las sin definir)
•	Mapa de arboles para ver a ojo qué onda
•	Histograma para ver que aves son las mas comunes y evaluar si hay q clasificarlas a mano entre nativas y exóticas. 
•	Histograma árboles y evaluar clasificación a mano
•	Clasificar en nativo y exótico
•	Porcentaje de natividad general de la región tanto de aves como de árboles.
•	Definir en función de eso que porcentaje se considera que una región es nativa o no?
•	Si hago curva de rarefacción entonces requiero mantener el dato de cuantos individuos hay de cada especies! Ojo al filtrar!
