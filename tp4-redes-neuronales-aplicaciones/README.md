## Trabajo Práctico 4 - Redes Neuronales - Aplicaciones

### Problema 1 - Identificación de imágenes de señales de tránsito

#### Enunciado

El objetivo de este trabajo es implementar un agente que identifique señales de tránsito en imágenes.

#### Requerimientos

- Python 3.11 o superior
- Instalar las dependencias del proyecto:
  ```bash
  python3 -m pip install -r requirements.txt
  ```
- Descomprimir el dataset de señales de tránsito en el directorio "gtsrb" o "gtsrb-small" (dependiendo de la versión del dataset que se quiera utilizar).

#### Resolución del problema

Para resolver el problema 1 se implementó un modelo de red neuronal convolucional con la libreria 'TensorFlow' para identificar señales de tránsito en imágenes. El modelo se entrena con un dataset de señales de tránsito que contiene 43 clases de señales de tránsito y casi 30 mil imágenes. El dataset se divide en dos conjuntos: uno de entrenamiento y otro de prueba. El conjunto de entrenamiento se utiliza para entrenar el modelo y el conjunto de prueba se utiliza para evaluar el modelo.

El modelo consta de los siguientes layers:
``` python
model = Sequential([
        Conv2D(32, (3, 3), activation='relu', input_shape=(IMG_WIDTH, IMG_HEIGHT, 3)),
        MaxPooling2D((2, 2)),
        Conv2D(64, (3, 3), activation='relu'),
        MaxPooling2D((2, 2)),
        Flatten(),
        Dense(128, activation='relu'),
        Dense(2 if IS_SMALL else NUM_CATEGORIES, activation='softmax')
    ])
```

- Sequential: Es un modelo de red neuronal secuencial.
- Conv2D: Es un layer de convolución 2D que aplica una operación de convolución a la entrada. En este caso, se utiliza para extraer características de las imágenes.
- MaxPooling2D: Es un layer de pooling 2D que reduce la dimensionalidad de las imágenes.
- Flatten: Es un layer que aplana la entrada. En este caso, se utiliza para convertir la salida del layer de convolución en un vector.
- Dense: Es un layer de neuronas completamente conectadas. En este caso, se utiliza para clasificar las imágenes.

Otras configuraciones del modelo:

- Activation: Es un layer de activación. En este caso, se utiliza para aplicar la función de activación 'relu' a la salida de los layers de convolución y el layer de neuronas completamente conectadas.
- InputShape: Es un layer de entrada. En este caso, se utiliza para especificar el tamaño de las imágenes de entrada.

El modelo se entrena con los siguientes parámetros:

- Optimizer: Es un optimizador. En este caso, se utiliza el optimizador 'adam'.
- Loss: Es una función de pérdida. En este caso, se utiliza la función de pérdida 'categorical_crossentropy'.
- Metrics: Es una métrica. En este caso, se utiliza la métrica 'accuracy'.

Hay dos versiones del modelo: una versión pequeña y una versión grande. La versión pequeña se utiliza para entrenar el modelo con un dataset pequeño y la versión grande se utiliza para entrenar el modelo con un dataset grande.

#### Ejecución del programa

Para ejecutar el programa, se debe ejecutar el siguiente comando:
```bash
python traffic.py data_directory
```

Donde 'data_directory' es el directorio que contiene el dataset de señales de tránsito. Puede ser "gtsrb-small" o "gtsrb".

#### Resultados

Resultados de la versión pequeña del modelo:

![small.png](assets%2Fsmall.png)

Resultados de la versión grande del modelo:

![large.png](assets%2Flarge.png)

#### Conclusiones

- A partir de la implementación del modelo de red neuronal convolucional, se puede concluir que el modelo es un modelo complejo y difícil de implementar. Sin embargo, el modelo es muy preciso y eficiente para identificar señales de tránsito en imágenes.