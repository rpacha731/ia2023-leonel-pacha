## Trabajo Práctico 3 - Aprendizaje

Este trabajo consta de dos ejercicios:
- [Problema 1 - Compras](problema1-compras)
- [Problema 2 - NIM](problema2-nim)

### Problema 1 - Compras

#### Enunciado

El objetivo de este trabajo es implementar un agente que prediga si los clientes de compras en línea completarán una compra.

#### Requerimientos

- Python 3.11 o superior
- Instalar las dependencias del proyecto:
  ```bash
  python3 -m pip install -r requirements.txt
  ```

#### Resolución del problema

Para resolver el problema 1 se implementó un agente que utiliza un modelo de k-nearest neighbors (kNN) para predecir si un cliente completará una compra en línea o no. El modelo se entrena con un dataset de clientes de compras en línea que contiene 17 atributos y una etiqueta que indica si el cliente completó la compra o no. El dataset se divide en dos conjuntos: uno de entrenamiento y otro de prueba. El conjunto de entrenamiento se utiliza para entrenar el modelo y el conjunto de prueba se utiliza para evaluar el modelo.
Dependiendo del SIZE del test set, el modelo puede predecir correctamente entre el 80% y el 90% de los clientes que completarán una compra en línea.

Resultado: <br>

![result-shopping.png](assets%2Fresult-shopping.png)

### Problema 2 - NIM

#### Enunciado

El objetivo de este trabajo es implementar una IA que se enseñe a sí misma a jugar al NIM a través del aprendizaje por
refuerzo.

#### Requerimientos

- Python 3.11 o superior

#### Resolución del problema

Para resolver el problema 2 se implementó un agente que utiliza un modelo de Q-learning para aprender a jugar al NIM. El modelo se entrena jugando partidas contra sí mismo y actualizando la tabla Q con los resultados de cada partida. El agente aprende a jugar al NIM en aproximadamente 10000 partidas. Luego de entrenar al agente, se puede jugar contra él. El agente siempre gana. 😥

Resultado: <br>

![result-nim.png](assets%2Fresult-nim.png)

## Conclusiones de ambos problemas

### Problema 1 - Compras

- El modelo de kNN es un modelo simple y fácil de implementar. Sin embargo, el modelo no es muy preciso y no es muy eficiente para predecir grandes cantidades de datos.

### Problema 2 - NIM

- El aprendizaje por refuerzo es un método de aprendizaje que permite que un agente aprenda a jugar al NIM sin necesidad de que se le enseñe cómo jugar. El agente aprende a jugar al NIM jugando partidas contra sí mismo y actualizando la tabla Q con los resultados de cada partida.
