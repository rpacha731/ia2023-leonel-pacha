## Trabajo Práctico 4 Bis - Redes Neuronales - Aplicaciones

### Análisis de sentimientos con PySentimiento

#### Enunciado

Este trabajo se implementó para la presentación de NLP como tema final. Consta de dos implementaciones de análisis de sentimientos, una para análisis de reviews en formato csv y otra para el análisis de una review en particular mediante una interfaz web con Flask.

#### Instalación

Primero, crear el entorno virtual con el siguiente comando:

```bash
python -m venv venv
```

Luego, para instalar las dependencias necesarias, ejecutar el siguiente comando:

```bash
pip install -r requirements.txt
```

#### Uso

Para ejecutar el análisis de reviews en formato csv, ejecutar el siguiente comando:

```bash
python pysentimient.py
```

Notar que el archivo csv debe estar en una carpeta llamada "dataset" en el mismo directorio que el archivo pysentimiento.py. Y el nombre del archivo debe ser "reviews.csv".

Para ejecutar el análisis de una review en particular, ingresar al directorio "app_web" y ejecutar el siguiente comando:

```bash
python app.py
```

Esto levantará un servidor local en el puerto que muestra la consola. 

#### Resolución del problema

Para la resolución del problema se utilizó la librería PySentimiento, que es una librería de análisis de sentimientos en español. Esta librería utiliza un modelo de redes neuronales pre-entrenado para realizar el análisis de sentimientos.

Se utilizaron 4 modelos distintos para realizar el análisis de sentimientos. Los modelos utilizados fueron:

- **Modelo 1**: Modelo RoBERTuito Sentiment Analysis (RoBERTa) pre-entrenado para el análisis de sentimientos. El modelo da como resultado un valor entre 0 y 1, compuesto por la probabilidad de que el texto sea positivo, neutro o negativo. 
- **Modelo 2**: Modelo RoBERTutio Emotion Analysis (RoBERTa) pre-entrenado para el análisis de emociones. El modelo da como resultado un valor entre 0 y 1, compuesto por la probabilidad de que el texto sea alegre, triste, enojado, sorprendido, asustado, disgustado u otros.
- **Modelo 3**: Modelo RoBERTuito Hate Speech Analysis (RoBERTa) pre-entrenado para el análisis de hate speech. El modelo da como resultado un valor entre 0 y 1, compuesto por la probabilidad de que el texto sea hate_hateful, hate_targeted o hate_aggressive.
- **Modelo 4**: Modelo RoBERTuito Irony Detection (RoBERTa) pre-entrenado para la detección de ironía. El modelo da como resultado un valor entre 0 y 1, compuesto por la probabilidad de que el texto sea irónico o no.

Los 4 modelos se utilizan para las dos implementaciones. 

#### Resultados

Los resultados obtenidos para el análisis de reviews en formato csv fueron los siguientes:

Con el archivo de entrada [reviews](dataset%2Freviews.csv) se obtuvo el archivo [reviews_sentiment](dataset%2Freviews_sentiment.csv)

Los resultados obtenidos para el análisis de una review en particular fueron los siguientes:

Por ejemplo, para la review "Me encanta este producto, es muy bueno y lo recomiendo" se obtuvo el siguiente resultado:

![review-good.png](assets%2Freview-good.png)

Otro ejemplo, para la review "No me gusta este producto, es muy malo y no lo recomiendo" se obtuvo el siguiente resultado:

![review-bad.png](assets%2Freview-bad.png)

#### Conclusiones

- La implementación web se podría transformar en una API para utilizarlo como microservicio en un sistema más grande.
- El análisis de sentimientos tiene muchas aplicaciones en el mundo real, como por ejemplo, análisis de reviews de productos, análisis de comentarios en redes sociales, análisis de comentarios en foros, etc. Además, se puede implementar para la toma de decisiones en empresas acerca de sus productos o servicios.
- El análisis de sentimientos puede ser utilizado para el análisis de datos personales, por lo que se debe tener cuidado con la privacidad de los datos. Además, se debe tener en cuenta que el análisis de sentimientos no es 100% preciso, por lo que se debe tener cuidado con las decisiones que se toman en base a los resultados obtenidos. Como también se debe tener cuidado con los sesgos que pueda tener el modelo utilizado.

PARA MÁS INFORMACIÓN CONSULTAR EL [INFORME](IA%20-%20INFORME%20NLP.pdf) Y LA [PRESENTACIÓN](IA%20-%20PRESENTACION%20NLP.pdf).