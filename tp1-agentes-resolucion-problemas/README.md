## Trabajo Práctico 1 - Agentes y Resolución de Problemas

### Problema: Grados de Separación

#### Enunciado

El objetivo de este trabajo es implementar un agente que resuelva el problema de los grados de separación entre actores de cine. El problema consiste en encontrar la menor cantidad de películas que conectan a dos actores. Para ello se cuenta con una base de datos de películas y actores, y se puede utilizar la información de la página web [IMDB](https://www.imdb.com/).

> Ejemplo: El camino más corto entre Jennifer Lawrence y Tom Hanks es 2: Jennifer Lawrence está conectada con Kevin
Bacon porque ambos protagonizan X-Men: First Class, y Kevin Bacon está conectado con
Tom Hanks porque ambos protagonizan Apollo 13

#### Resolución del problema

Para resolver el problema se implementó un agente que utiliza tres tipos de algoritmos de búsqueda:

- Búsqueda en profundidad (DFS)

> Este algoritmo comienza desde un nodo inicial y explora todos los nodos vecinos de forma recursiva, hasta que encuentra el nodo objetivo o no quedan más nodos por explorar. Si no encuentra el nodo objetivo, retrocede y explora otro camino.

- Búsqueda en amplitud (BFS)

> Este algoritmo comienza desde un nodo inicial y explora todos los nodos vecinos, luego explora los nodos vecinos de los nodos vecinos, y así sucesivamente, hasta que encuentra el nodo objetivo o no quedan más nodos por explorar.

- Búsqueda en profundidad iterativa (IDS)

> Este algoritmo comienza desde un nodo inicial y explora todos los nodos vecinos de forma recursiva, hasta que encuentra el nodo objetivo o no quedan más nodos por explorar. Si no encuentra el nodo objetivo, aumenta la profundidad máxima y vuelve a comenzar.

__Para cualquiera de las implementaciones, si se encuentra el nodo objetivo, se devuelve el camino que lleva al nodo objetivo__

El agente recibe como parámetros el nombre de los actores. El agente utiliza la base de datos de películas y actores para obtener la información necesaria para resolver el problema.

#### Ejecución

:warning: _Para ejecutar el agente se debe tener instalado Python 3.8 o superior._

Para ejecutar el agente se debe ejecutar el siguiente comando:

```bash
python3 degrees.py large|small
```

Donde `large` o `small` es el tamaño de la base de datos que se desea utilizar. 

#### Ejemplos

Ingrese el nombre del actor 1: Dwanye Johnson
Ingrese el nombre del actor 2: Clint Eastwood

El resultado es el siguiente:

![IDS.png](assets%2FIDS.png)

#### Conclusiones

Se puede observar que el algoritmo IDS es el que encuentra el camino más rápido, ya que no explora todos los nodos como lo hace BFS, y no se queda en un camino como lo hace DFS. Sin embargo, el algoritmo IDS es más lento que BFS, ya que debe ejecutarse varias veces.

#### Aplicaciones en la vida real

Este problema se puede aplicar en la vida real para encontrar la menor cantidad de pasos que conectan a dos personas en una red social, como por ejemplo Facebook o LinkedIn.

#### Presentación

La presentación d PowerPoint se puede ver en el siguiente archivo: [IA - TP1 - Pacha.pdf](assets%2FIA%20-%20TP1%20-%20Pacha.pdf) 
